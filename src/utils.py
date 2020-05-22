import datetime
import decimal


def alchemy_encoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)


def all_to_string(obj):
    """All JSON types to strings as in original API."""
    # TODO
    return obj
