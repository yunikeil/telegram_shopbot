"""Initial tables

Revision ID: 1f048fde258b
Revises: 
Create Date: 2024-07-27 18:23:10.511268

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f048fde258b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catalog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('file_unique_tg_id', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_catalog_description'), 'catalog', ['description'], unique=False)
    op.create_index(op.f('ix_catalog_name'), 'catalog', ['name'], unique=False)
    op.create_table('user',
    sa.Column('tg_id', sa.BigInteger(), nullable=False),
    sa.Column('role', sa.Enum('user', 'admin', name='user_roles'), nullable=False),
    sa.Column('balance', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('tg_id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('catalog_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['catalog_id'], ['catalog.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tg_id', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('file_unique_tg_id', sa.String(), nullable=True),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['tg_id'], ['user.tg_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_purchase_description'), 'purchase', ['description'], unique=False)
    op.create_index(op.f('ix_purchase_name'), 'purchase', ['name'], unique=False)
    op.create_table('shopping_cart',
    sa.Column('catalog_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['catalog_id'], ['catalog.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.tg_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('catalog_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopping_cart')
    op.drop_index(op.f('ix_purchase_name'), table_name='purchase')
    op.drop_index(op.f('ix_purchase_description'), table_name='purchase')
    op.drop_table('purchase')
    op.drop_table('product')
    op.drop_table('user')
    op.drop_index(op.f('ix_catalog_name'), table_name='catalog')
    op.drop_index(op.f('ix_catalog_description'), table_name='catalog')
    op.drop_table('catalog')
    # ### end Alembic commands ###
