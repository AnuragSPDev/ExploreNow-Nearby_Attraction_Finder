import os
import requests
from fastapi import HTTPException
from models import Places, Attractions, Categories
from sqlalchemy.orm import Session
from sqlalchemy import func


# Geoapify API key
GEOAPIFY_API_KEY = os.getenv("GEOAPIFY_API_KEY")
GEOAPIFY_PLACES_URL = "https://api.geoapify.com/v2/places"
GEOAPIFY_GEOCODE_URL = "https://api.geoapify.com/v1/geocode/search"

class Helpers:

    @staticmethod
    def get_lat_lon_from_geoapify(place_name):
        params = {"text": place_name, "apiKey": GEOAPIFY_API_KEY}
        response = requests.get(GEOAPIFY_GEOCODE_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error fetching coordinates from Geoapify")
        results = response.json().get("features", [])
        if not results:
            raise HTTPException(status_code=404, detail="Location not found")
        return results[0]["geometry"]["coordinates"][1], results[0]["geometry"]["coordinates"][0]
    
    @staticmethod
    def fetch_attractions_from_geoapify(lat, lon):
        params = {
            "categories": "tourism.sights",
            "filter": f"circle:{lon},{lat},5000",
            "apiKey": GEOAPIFY_API_KEY
        }
        response = requests.get(GEOAPIFY_PLACES_URL, params=params)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error fetching data from Geoapify")
        return response.json().get("features", [])
    
    @staticmethod
    def save_place_and_attractions(db: Session, name: str, lat: float, lon: float, attractions: list):
        place = Places(name=func.lower(name), latitude=lat, longitude=lon)
        db.add(place)
        db.commit()
        db.refresh(place)
        for attraction in attractions:
            category_id = Helpers.get_or_create_category(db, attraction["category"]) if "category" in attraction else None
            new_attraction = Attractions(
                name=attraction["name"],
                category_id=category_id,
                latitude=attraction["latitude"],
                longitude=attraction["longitude"],
                place_id=place.id
            )
            db.add(new_attraction)
        db.commit()

    @staticmethod
    def get_or_create_category(db: Session, category_name: str):
        category = db.query(Categories).filter(Categories.name == category_name).first()
        if category:
            print(f'category found: {category}, {category.id}')
            return category.id
        new_category = Categories(name=category_name)
        db.add(new_category)
        db.commit()
        db.refresh(new_category)
        print(f'Caegory created: {new_category}, {new_category.id}')
        return new_category.id

    @staticmethod
    def fetch_cities_from_geoapify(state_name: str):
        api_key = "YOUR_GEOAPIFY_API_KEY"
        url = f"https://api.geoapify.com/v1/geocode/search?text={state_name}&type=city&apiKey={GEOAPIFY_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('features', [])
        else:
            return []
        