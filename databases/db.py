import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


login = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASS"]
host = os.environ["MYSQL_HOST"]
db = os.environ["MYSQL_DB"]

engine = create_engine(
    f"mysql+pymysql://{login}:{password}@{host}/{db}?charset=utf8mb4"
)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)
