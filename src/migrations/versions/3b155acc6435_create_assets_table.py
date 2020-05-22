"""create assets table

Revision ID: 3b155acc6435
Revises: 
Create Date: 2020-05-22 14:31:51.769077

"""
import sys
sys.path.append('..')

from alembic import op
import sqlalchemy as sa

from src.database.tables import *


# revision identifiers, used by Alembic.
revision = '3b155acc6435'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    asset.create(sa.engine)


def downgrade():
    pass
