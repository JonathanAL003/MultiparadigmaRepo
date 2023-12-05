"""empty message

Revision ID: 88d9ed4334f5
Revises: 32fee1692efd
Create Date: 2023-11-30 10:28:26.684544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88d9ed4334f5'
down_revision = '32fee1692efd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rfc', sa.String(length=20)))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proveedor', schema=None) as batch_op:
        batch_op.drop_column('rfc')

    # ### end Alembic commands ###
