from fastapi import FastAPI, HTTPException, Depends, Header, Query
from pydantic import BaseModel, Field
from typing import List, Optional, Annotated
import models.recipe as models
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session
from sqlalchemy import func, event
from contextlib import asynccontextmanager
from apscheduler.schedulers.background import BackgroundScheduler
from fastapi.middleware.cors import CORSMiddleware
from seed.seed import seed_db, seed_table

async def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(seed_db, 'interval', hours=1)
    scheduler.start()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await seed_db()
    await start_scheduler()
    yield

event.listen(models.Recipes.__table__, 'after_create', seed_table)

app = FastAPI(lifespan=lifespan)
models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def verify_token(authorization: Optional[str] = Header(None)):
    if authorization is None or not authorization.startswith("Bearer panconqueso"):
        raise HTTPException(status_code=401, detail="Missing or invalid authorization header")

class RecipeCreate(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image: str
    categories: List[str]
    evaluation: int
    preparation_time_in_minutes: int

class Recipe(BaseModel):
    id: int
    title: str
    description: str
    ingredients: list = []
    steps: list = []
    image: str
    categories: list = []
    evaluation: int
    preparation_time_in_minutes: int

class RecipeUpdate(BaseModel):
    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    ingredients: Optional[List[str]] = Field(default=None)
    steps: Optional[List[str]] = Field(default=None)
    image: Optional[str] = Field(default=None)
    categories: Optional[List[str]] = Field(default=None)
    evaluation: Optional[int] = Field(default=None)
    preparation_time_in_minutes: Optional[int] = Field(default=None)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
token_dependency = Annotated[str, Depends(verify_token)]

@app.get("/recipes/", response_model=List[Recipe])
async def get_recipes(
    db: db_dependency, 
    token: token_dependency,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
):
    offset = (page - 1) * page_size
    recipes = db.query(models.Recipes).offset(offset).limit(page_size).all()
    return recipes

@app.get("/recipes/{recipe_id}", response_model=Recipe)
async def get_recipe(recipe_id: int, db: db_dependency, token: token_dependency):
    recipe = db.query(models.Recipes).filter(models.Recipes.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.get("/recipes/ingredients/", response_model=List[Recipe])
async def get_recipes_by_ingredients(
    db: db_dependency,
    token: token_dependency,
    ingredients: List[str] = Query(..., alias="ingredients"),
):
    ingredient_list = [f"%{ingredient}%" for ingredient in ingredients]
    recipes = db.query(models.Recipes).filter(
        func.array_to_string(models.Recipes.ingredients, ',').ilike(func.concat(*ingredient_list))
    ).all()
    return recipes

@app.post("/recipes/", response_model=Recipe)
async def create_recipe(recipe: RecipeCreate, db: db_dependency, token: token_dependency):
    db_recipe = models.Recipes(
        title=recipe.title, 
        description=recipe.description, 
        ingredients=recipe.ingredients, 
        steps=recipe.steps, 
        image=recipe.image, 
        categories=recipe.categories, 
        evaluation=recipe.evaluation, 
        preparation_time_in_minutes=recipe.preparation_time_in_minutes
    )
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@app.patch("/recipes/{recipe_id}", response_model=Recipe)
async def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db), token: str = Depends(verify_token)):
    db_recipe = db.query(models.Recipes).filter(models.Recipes.id == recipe_id).first()
    if db_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    recipe_data = recipe.dict(exclude_unset=True)
    for key, value in recipe_data.items():
        setattr(db_recipe, key, value)

    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@app.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: int, db: db_dependency, token: token_dependency):
    recipe = db.query(models.Recipes).filter(models.Recipes.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}
