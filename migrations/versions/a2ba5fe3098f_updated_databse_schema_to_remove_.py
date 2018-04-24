"""Updated databse schema to remove category relationship conflicts

Revision ID: a2ba5fe3098f
Revises: 2fd9a2f377d7
Create Date: 2018-04-24 16:50:16.110037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2ba5fe3098f'
down_revision = '2fd9a2f377d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('events_creator_id_fkey', 'events', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('events_creator_id_fkey', 'events', 'users', ['creator_id'], ['id'])
    # ### end Alembic commands ###
