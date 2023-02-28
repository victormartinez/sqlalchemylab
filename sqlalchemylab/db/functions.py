from typing import Any

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression
from sqlalchemy.types import DateTime


class utcnow(expression.FunctionElement):
    type = DateTime()
    inherit_cache = True


@compiles(utcnow, "postgresql")  # type: ignore
def pg_utcnow(element: Any, compiler: Any, **kw: Any) -> str:
    """
    Function created based in official docs from SQLAlchemy.
    https://docs.sqlalchemy.org/en/14/core/compiler.html#further-examples
    """
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"
