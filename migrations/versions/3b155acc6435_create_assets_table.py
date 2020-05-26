"""create assets table

Revision ID: 3b155acc6435
Revises: 
Create Date: 2020-05-22 14:31:51.769077

"""
import sys
# Fix import for docker
sys.path.append('/app')

import sqlalchemy as sa
from models import assets

# revision identifiers, used by Alembic.
revision = '3b155acc6435'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    assets.create(sa.engine)


def downgrade():
    pass
