import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine
import models
from helpers.helpers import Helpers
from sqlalchemy import func

# Geoapify API key
# GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")
# GEOAPIFY_PLACES_URL = "https://api.geoapify.com/v2/places"
# GEOAPIFY_GEOCODE_URL = "https://api.geoapify.com/v1/geocode/search"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PlaceSearch(BaseModel):
    name: str

class CategoriesModel(BaseModel):
    id: int
    name: str

class AttractionsModel(BaseModel):
    id: int | None = None
    name: str
    category_id: int | None
    category_name: str
    latitude: float
    longitude: float

class PlacesModel(BaseModel):
    id: int | None = None
    name: str
    latitude: float
    longitude: float
    attractions: list[AttractionsModel]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
models.Base.metadata.create_all(bind=engine)

@app.post('/places/search/', response_model=PlacesModel)
async def search_place(request: PlaceSearch, db: db_dependency):
    db_place = db.query(models.Places).filter(func.lower(models.Places.name)==func.lower(request.name)).first()
    if db_place:
        return prepare_response(db, request.name)
    
    latitude, longitude = Helpers.get_lat_lon_from_geoapify(request.name)
    attractions_data = Helpers.fetch_attractions_from_geoapify(lat=latitude, lon=longitude)

    attractions = [{
        "name": attr["properties"].get("name", "Unknown"),
        "category": attr["properties"].get("categories", ["Unknown"])[0],
        "category_name": attr["properties"].get("categories", ["Unknown"])[0],
        "latitude": attr["geometry"]["coordinates"][1],
        "longitude": attr["geometry"]["coordinates"][0]
    } for attr in attractions_data]
    Helpers.save_place_and_attractions(db, request.name, latitude, longitude, attractions)
    return prepare_response(db, request.name)

def prepare_response(db: Session, place_name):
    db_place = db.query(models.Places).filter(func.lower(models.Places.name) == func.lower(place_name)).first()
    attractions = db.query(models.Attractions).join(models.Categories).filter(models.Attractions.place_id == db_place.id).all()
    return PlacesModel(
        id=db_place.id,
        name=db_place.name,
        latitude=db_place.latitude,
        longitude=db_place.longitude,
        attractions=[AttractionsModel(
            id=attr.id,
            name=attr.name,
            category_id=attr.category_id,
            category_name=attr.category.name,
            latitude=attr.latitude,
            longitude=attr.longitude
        ) for attr in attractions]
    )
