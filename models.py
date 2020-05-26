import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from migrations import metadata

from config import sql_conn_url


Base = declarative_base()

# Not-async engine for migrations
sa.engine = sa.create_engine(sql_conn_url, echo=True)


# TODO remove to migrations
assets = sa.Table(
    'assets', metadata,
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column("ticker", sa.String, unique=True),
    sa.Column('name', sa.String, unique=True),
    sa.Column('unified_cryptoasset_id', sa.Integer),
    sa.Column("can_deposit", sa.Boolean),
    sa.Column('can_withdraw', sa.Boolean),
    sa.Column('min_withdraw', sa.Numeric),
    sa.Column('max_withdraw', sa.Numeric),
    sa.Column('maker_fee', sa.Numeric),
    sa.Column("taker_fee", sa.Numeric),
)


class Asset(Base):
    __tablename__ = "assets"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    ticker = sa.Column(sa.String, unique=True)
    name = sa.Column(sa.String, unique=True)
    unified_cryptoasset_id = sa.Column(sa.Integer)
    can_deposit = sa.Column(sa.Boolean)
    can_withdraw = sa.Column(sa.Boolean)
    min_withdraw = sa.Column(sa.Numeric)
    max_withdraw = sa.Column(sa.Numeric)
    maker_fee = sa.Column(sa.Numeric)
    taker_fee = sa.Column(sa.Numeric)
