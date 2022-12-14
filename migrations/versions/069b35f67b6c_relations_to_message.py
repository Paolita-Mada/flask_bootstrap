"""relations to message

Revision ID: 069b35f67b6c
Revises: 0c21144e14ce
Create Date: 2022-12-07 22:05:31.908895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '069b35f67b6c'
down_revision = '0c21144e14ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
