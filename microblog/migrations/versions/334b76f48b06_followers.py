"""followers

Revision ID: 334b76f48b06
Revises: dd2baa37705b
Create Date: 2020-03-15 11:59:42.238011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '334b76f48b06'
down_revision = 'dd2baa37705b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
