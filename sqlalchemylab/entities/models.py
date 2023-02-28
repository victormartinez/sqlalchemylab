import uuid

from sqlalchemy import VARCHAR, Boolean, Column, DateTime, Enum, Integer, String
from sqlalchemy.dialects import postgresql

from sqlalchemylab.db import BaseModel, functions
from sqlalchemylab.entities.enums import Status


class Reservation(BaseModel):
    __tablename__ = "reservations"

    id = Column(
        postgresql.UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4
    )
    requester_identification = Column(VARCHAR(length=20), nullable=False)
    location_preference = Column(String, nullable=True)
    num_chairs = Column(Integer, nullable=False, default=1)
    status = Column(
        Enum(Status), nullable=False, default=Status.REQUESTED
    )  # type: ignore
    data = Column(postgresql.JSONB, nullable=True, default=None)
    meta = Column(postgresql.JSON, nullable=True, default=None)
    booking_datetime = Column(DateTime(timezone=True), nullable=False)
    is_canceled = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=functions.utcnow())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=functions.utcnow(),
        onupdate=functions.utcnow(),
    )
