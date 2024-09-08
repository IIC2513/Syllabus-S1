from sqlalchemy import create_engine
from models.recipe import Base
from config.database import SessionLocal
import json
import os

engine = create_engine(os.getenv("DATABASE_URL"))

async def seed_db():
    session = SessionLocal()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session.commit()
    session.close()

def seed_table(target, connection, **kw):
    tablename = str(target)
    with open('./seed/seed.json', 'r') as file:
        data = json.load(file)
    if tablename in data and len(data[tablename]) > 0:
        connection.execute(target.insert(), data[tablename])