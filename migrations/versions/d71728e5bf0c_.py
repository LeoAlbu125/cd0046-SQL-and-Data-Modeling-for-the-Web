"""empty message

Revision ID: d71728e5bf0c
Revises: 65e6d35ae94d
Create Date: 2023-09-09 00:58:19.021787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd71728e5bf0c'
down_revision = '65e6d35ae94d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('web_link', sa.String(length=120), nullable=True))
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Venue', schema=None) as batch_op:
        batch_op.drop_column('genres')
        batch_op.drop_column('web_link')

    # ### end Alembic commands ###
