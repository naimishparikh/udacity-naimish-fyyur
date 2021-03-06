"""empty message

Revision ID: 705dd821ab83
Revises: 2cd3c398e86f
Create Date: 2021-08-05 18:02:10.344366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '705dd821ab83'
down_revision = '2cd3c398e86f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'website')
    # ### end Alembic commands ###
