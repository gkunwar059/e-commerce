"""empty message

Revision ID: 2147aa44e139
Revises: 98fbd938372c
Create Date: 2025-02-12 08:26:13.182871

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2147aa44e139'
down_revision: Union[str, None] = '98fbd938372c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'quantity')
    op.add_column('productorder', sa.Column('quantity', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('productorder', 'quantity')
    op.add_column('order', sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
