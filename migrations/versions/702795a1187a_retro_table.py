"""retro table

Revision ID: 702795a1187a
Revises: 
Create Date: 2020-06-12 19:28:27.655295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '702795a1187a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('retro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.String(length=40), nullable=True),
    sa.Column('channel', sa.String(length=40), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('nature', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_retro_channel'), 'retro', ['channel'], unique=False)
    op.create_index(op.f('ix_retro_timestamp'), 'retro', ['timestamp'], unique=False)
    op.create_index(op.f('ix_retro_userid'), 'retro', ['userid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_retro_userid'), table_name='retro')
    op.drop_index(op.f('ix_retro_timestamp'), table_name='retro')
    op.drop_index(op.f('ix_retro_channel'), table_name='retro')
    op.drop_table('retro')
    # ### end Alembic commands ###
