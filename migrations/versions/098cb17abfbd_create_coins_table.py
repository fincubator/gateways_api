"""create coins table

Revision ID: 098cb17abfbd
Revises: 3b155acc6435
Create Date: 2020-05-28 19:59:10.507974

"""
import sys
sys.path.append('/app')

import sqlalchemy as sa

from models import coins

# revision identifiers, used by Alembic.
revision = '098cb17abfbd'
down_revision = '3b155acc6435'
branch_labels = None
depends_on = None


def upgrade():
    coins.create(sa.engine)


def downgrade():
    pass
