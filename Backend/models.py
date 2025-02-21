from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import Base

class Places(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    created_at = Column(DateTime, default=func.now())
    attractions = relationship('Attractions', back_populates='place')

    @property
    def formatted_attractions(self):
        return ", ".join([attraction.name for attraction in self.attractions]) if self.attractions else "No attractions"

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    attractions = relationship('Attractions', back_populates='category')

    @property
    def formatted_attractions(self):
        return ", ".join([attraction.name for attraction in self.attractions]) if self.attractions else "No attractions"
    

class Attractions(Base):
    __tablename__ = 'attractions'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete="SET NULL"))
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)
    place_id = Column(Integer, ForeignKey('places.id', ondelete="CASCADE"))

    place = relationship('Places', back_populates='attractions')
    category = relationship('Categories', back_populates='attractions')

    @property
    def formatted_place(self):
        return self.place.name if self.place else 'No place'
    
    @property
    def formatted_category(self):
        return self.category.name if self.category else 'No category'
    