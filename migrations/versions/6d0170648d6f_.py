"""empty message

Revision ID: 6d0170648d6f
Revises: 87b10e41bb0c
Create Date: 2022-08-15 10:57:40.024349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d0170648d6f'
down_revision = '87b10e41bb0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    # ### end Alembic commands ###