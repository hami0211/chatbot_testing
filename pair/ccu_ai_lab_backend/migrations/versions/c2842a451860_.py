"""empty message

Revision ID: c2842a451860
Revises: 9a711410f882
Create Date: 2021-01-18 02:04:05.537417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2842a451860'
down_revision = '9a711410f882'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('COPI_project_ibfk_1', 'COPI_project', type_='foreignkey')
    op.create_foreign_key(None, 'COPI_project', 'specific_periods', ['specific_period_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'COPI_project', type_='foreignkey')
    op.create_foreign_key('COPI_project_ibfk_1', 'COPI_project', 'specific_periods', ['specific_period_id'], ['id'])
    # ### end Alembic commands ###
