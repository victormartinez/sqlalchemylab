import settings
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(settings.DB_URI, **settings.DB_ENGINE_OPTIONS)
Session = sessionmaker(bind=engine, future=True)
