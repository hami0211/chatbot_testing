"""empty message

Revision ID: 5d04560d9aea
Revises: 9431ad0969c1
Create Date: 2021-01-12 10:04:36.634655

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5d04560d9aea'
down_revision = '9431ad0969c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('specific_periods', sa.Column('link', sa.String(length=256), nullable=True))
    op.add_column('specific_periods', sa.Column('nation', sa.String(length=64), nullable=True))
    op.drop_column('specific_periods', 'project_link')
    op.drop_column('specific_periods', 'project_nation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('specific_periods', sa.Column('project_nation', mysql.VARCHAR(length=64), nullable=True))
    op.add_column('specific_periods', sa.Column('project_link', mysql.VARCHAR(length=256), nullable=True))
    op.drop_column('specific_periods', 'nation')
    op.drop_column('specific_periods', 'link')
    # ### end Alembic commands ###