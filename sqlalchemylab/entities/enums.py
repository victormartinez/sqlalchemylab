import enum


class Status(str, enum.Enum):
    REQUESTED = "REQUESTED"
    ACCEPTED = "ACCEPTED"
    REFUSED = "REFUSED"
