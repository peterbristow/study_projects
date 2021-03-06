"""adding favourite colour column

Revision ID: 1567a97438f7
Revises: 2583771190de
Create Date: 2018-03-20 18:19:48.247423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1567a97438f7'
down_revision = '2583771190de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('favourite_colour', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'favourite_colour')
    # ### end Alembic commands ###
