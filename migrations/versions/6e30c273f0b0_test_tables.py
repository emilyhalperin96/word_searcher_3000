"""test tables

Revision ID: 6e30c273f0b0
Revises: 3f862c3e17a7
Create Date: 2023-03-07 13:37:08.252825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e30c273f0b0'
down_revision = '3f862c3e17a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('themes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('themes', sa.String(), nullable=True),
    sa.Column('words_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['words_id'], ['easy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('themes')
    # ### end Alembic commands ###
