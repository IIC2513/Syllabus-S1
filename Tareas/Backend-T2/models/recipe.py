from sqlalchemy import Column, Integer, String, ARRAY
from config.database import Base

class Recipes(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    ingredients = Column(ARRAY(String), index=True)
    steps = Column(ARRAY(String), index=True)
    image = Column(String, index=True)
    categories = Column(ARRAY(String), index=True)
    evaluation = Column(Integer, index=True)
    preparation_time_in_minutes = Column(Integer, index=True)
