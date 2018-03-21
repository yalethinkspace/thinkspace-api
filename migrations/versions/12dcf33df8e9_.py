"""empty message

Revision ID: 12dcf33df8e9
Revises: 2926750f49a0
Create Date: 2018-03-20 15:14:21.657118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12dcf33df8e9'
down_revision = '2926750f49a0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('project', sa.Integer(), nullable=False))
    op.add_column('post', sa.Column('user', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'post', 'user', ['user'], ['id'])
    op.create_foreign_key(None, 'post', 'project', ['project'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'user')
    op.drop_column('post', 'project')
    # ### end Alembic commands ###
