import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(os.getenv('DATABASE_URL'), echo=False)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(engine)
