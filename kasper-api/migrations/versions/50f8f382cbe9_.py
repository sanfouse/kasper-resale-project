"""empty message

Revision ID: 50f8f382cbe9
Revises: a55c662c8878
Create Date: 2023-11-08 13:16:36.087027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f8f382cbe9'
down_revision = 'a55c662c8878'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('dormitorys_adverts')
    op.add_column('adverts', sa.Column('dormitory', sa.BigInteger(), nullable=True))
    op.create_foreign_key('fk_adverts_dormitories_id_dormitory', 'adverts', 'dormitories', ['dormitory'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_adverts_dormitories_id_dormitory', 'adverts', type_='foreignkey')
    op.drop_column('adverts', 'dormitory')
    op.create_table('dormitorys_adverts',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('advert', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('dormitory', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['advert'], ['adverts.id'], name='fk_dormitorys_adverts_adverts_advert_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['dormitory'], ['dormitories.id'], name='fk_dormitorys_adverts_dormitories_dormitory_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='dormitorys_adverts_pkey')
    )
    op.drop_table('categories')
    # ### end Alembic commands ###