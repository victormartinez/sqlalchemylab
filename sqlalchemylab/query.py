from sqlalchemy import select

from sqlalchemylab.db.conn import Session, engine
from sqlalchemylab.entities import models


def execute():
    session = Session(future=True)
    query = select(models.Reservation)
    result = session.execute(query).first()
    print(result)
