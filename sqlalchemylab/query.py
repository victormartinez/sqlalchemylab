from sqlalchemy import select

from sqlalchemylab.db.conn import Session
from sqlalchemylab.entities import models


def execute() -> None:
    session = Session(future=True)
    query = select(models.Reservation)
    result = session.execute(query).first()
    print(result)
