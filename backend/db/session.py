import os
import sqlalchemy

DB_URL = os.getenv("DB_URL")
engine = sqlalchemy.create_engine(DB_URL)
