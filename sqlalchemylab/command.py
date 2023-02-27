from datetime import datetime, timedelta

from sqlalchemylab.db.conn import Session
from sqlalchemylab.entities import models


def execute() -> None:
    tomorrow = datetime.utcnow() + timedelta(days=1)
    obj = models.Reservation(
        requester_identification="08998778901",
        num_chairs=10,
        booking_datetime=tomorrow
    )
    with Session() as session:
        session.add(obj)
        session.commit()
