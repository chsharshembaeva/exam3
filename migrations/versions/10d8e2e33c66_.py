"""empty message

Revision ID: 10d8e2e33c66
Revises: 
Create Date: 2022-07-19 20:56:40.897222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10d8e2e33c66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password_hash', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('employee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullname', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.Column('short_info', sa.String(length=200), nullable=False),
    sa.Column('experience', sa.Integer(), nullable=False),
    sa.Column('preferred_position', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employee')
    op.drop_table('user')
    # ### end Alembic commands ###
