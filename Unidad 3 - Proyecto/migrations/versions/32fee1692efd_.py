"""empty message

Revision ID: 32fee1692efd
Revises: 2f20606eece9
Create Date: 2023-11-23 10:05:16.057782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32fee1692efd'
down_revision = '2f20606eece9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.String(length=250), nullable=True),
    sa.Column('precio_kg', sa.Float(), nullable=True),
    sa.Column('peso_kg', sa.Float(), nullable=True),
    sa.Column('marca', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('telefono', sa.String(length=20), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venta',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=True),
    sa.Column('nombre_cliente', sa.String(length=250), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('precio_total', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id_producto'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venta')
    op.drop_table('proveedor')
    op.drop_table('producto')
    # ### end Alembic commands ###
