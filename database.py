import os # import the os module 
from dotenv import load_dotenv # import the load_dotenv function from the dotenv module
from urllib.parse import quote

from sqlalchemy import create_engine , MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



load_dotenv() # load environment variable from the .env file

DATABASE_URL = os.getenv("DATABASE_URL") # Get the database_url environment variable

# DATABASE_URL=os.getenv("DATABASE_URL") # get the database_url environment variable

engine = create_engine(DATABASE_URL)  # create a sqlalchemy engine

metadata = MetaData() # CREATE A SQLALCHEMY METADATA OBJECT 

Sessionlocal = sessionmaker(autocommit=False , autoflush=False, bind=engine) # Create a sqlalchemy sessionmaker object

Base = declarative_base()  # create a sqlalchemy declarative base object