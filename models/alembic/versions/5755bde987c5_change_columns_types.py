"""Change columns types

Revision ID: 5755bde987c5
Revises: e58c16a4487a
Create Date: 2022-07-21 12:43:55.445027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5755bde987c5'
down_revision = 'e58c16a4487a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('requests', 'status',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=20),
               existing_nullable=False)
    op.alter_column('requests', 'description',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('requests_history', 'status',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=20),
               existing_nullable=False)
    op.alter_column('roles', 'role_name',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=20),
               existing_nullable=False)
    op.alter_column('type_bonus', 'description',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=True)
    op.alter_column('users', 'full_name',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'full_name',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
    op.alter_column('type_bonus', 'description',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('roles', 'role_name',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    op.alter_column('requests_history', 'status',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    op.alter_column('requests', 'description',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('requests', 'status',
               existing_type=sa.String(length=20),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    # ### end Alembic commands ###