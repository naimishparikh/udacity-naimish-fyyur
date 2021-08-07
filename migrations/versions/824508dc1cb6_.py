"""empty message

Revision ID: 824508dc1cb6
Revises: 705dd821ab83
Create Date: 2021-08-06 22:44:29.553764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '824508dc1cb6'
down_revision = '705dd821ab83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'website_link')
    op.drop_column('artist', 'website_link')
    # ### end Alembic commands ###
