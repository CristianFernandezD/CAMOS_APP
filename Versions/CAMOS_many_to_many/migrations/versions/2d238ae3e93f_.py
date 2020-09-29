"""empty message

Revision ID: 2d238ae3e93f
Revises: 5442f4ab2038
Create Date: 2020-09-29 11:09:55.185000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d238ae3e93f'
down_revision = '5442f4ab2038'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_fish_timestamp', table_name='fish')
    op.drop_table('fish')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fish',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_fish_timestamp', 'fish', ['timestamp'], unique=False)
    # ### end Alembic commands ###
