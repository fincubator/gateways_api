import sqlalchemy as sa

from src.migrations import metadata

from config import sql_conn_url


# Not-async engine for migrations
sa.engine = sa.create_engine(sql_conn_url, echo=True)

asset = sa.Table(
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
