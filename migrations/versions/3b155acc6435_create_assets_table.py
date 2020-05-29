"""create assets table

Revision ID: 3b155acc6435
Revises: 
Create Date: 2020-05-22 14:31:51.769077

"""
import sys
# Fix import for docker
sys.path.append('/app')

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3b155acc6435'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'assets',
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


def downgrade():
    op.drop_table('assets')
