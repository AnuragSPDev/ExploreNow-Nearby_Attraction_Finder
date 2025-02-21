import logging
from sqladmin import ModelView
from models import Places, Categories, Attractions

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class PlacesAdmin(ModelView, model=Places):
    column_list = [Places.name, Places.latitude, Places.longitude]
    column_details_list = [Places.name, Places.latitude, Places.longitude, 'formatted_attractions']
    form_excluded_columns = ["created_at"]
    
    name = "Place"
    name_plural = "Places"


class CategoriesAdmin(ModelView, model=Categories):
    column_list = [Categories.name]
    column_details_list = ['name', 'formatted_attractions']
    name = "Category"
    name_plural = "Categories"


class AttractionsAdmin(ModelView, model=Attractions):
    column_list = [Attractions.name, Attractions.latitude, Attractions.longitude]
    column_details_list = ['name', 'description', 'latitude', 'longitude', 'formatted_place', 'formatted_category']
    name = "Attraction"
    name_plural = "Attractions"

def add_views(admin):
    admin.add_view(PlacesAdmin)
    logger.info("PlacesAdmin view added")
    admin.add_view(CategoriesAdmin)
    logger.info("CategoriesAdmin view added")
    admin.add_view(AttractionsAdmin)
    logger.info("AttractionsAdmin view added")
