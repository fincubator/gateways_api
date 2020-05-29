"""create coins table

Revision ID: 098cb17abfbd
Revises: 3b155acc6435
Create Date: 2020-05-28 19:59:10.507974

"""
import sys
# Fix import for docker
sys.path.append('/app')

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = '098cb17abfbd'
down_revision = '3b155acc6435'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'coins',
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column("name", sa.String, unique=True),
    sa.Column("description", sa.String),
    sa.Column('backing_coin', sa.String),
    sa.Column('symbol', sa.String),

    sa.Column("deposit_allowed", sa.Boolean),
    sa.Column('withdrawal_allowed', sa.Boolean),

    sa.Column('memo_support', sa.Boolean),
    sa.Column('memo_version', sa.Integer),

    sa.Column('precision', sa.Integer),

    sa.Column("issuer", sa.String),
    sa.Column("issuer_id", sa.String),

    sa.Column("gateway_wallet", sa.String),
    sa.Column("wallet_type", sa.String),

    sa.Column('min_amount', sa.Integer),
    sa.Column('withdraw_fee', sa.Integer),
    sa.Column("deposit_fee", sa.Integer),

    sa.Column("confirmations", sa.Integer)
    )


def downgrade():
    op.drop_table('coins')
