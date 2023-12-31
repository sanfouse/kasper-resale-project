"""empty message

Revision ID: a55c662c8878
Revises: f2724565bcd1
Create Date: 2023-11-07 16:14:26.310032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a55c662c8878'
down_revision = 'f2724565bcd1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('adverts_users')
    op.add_column('adverts', sa.Column('user', sa.BigInteger(), nullable=True))
    op.create_foreign_key('fk_adverts_users_id_user', 'adverts', 'users', ['user'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_adverts_users_id_user', 'adverts', type_='foreignkey')
    op.drop_column('adverts', 'user')
    op.create_table('adverts_users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('advert', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['advert'], ['adverts.id'], name='fk_adverts_users_adverts_advert_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user'], ['users.id'], name='fk_adverts_users_users_user_id', onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='adverts_users_pkey')
    )
    # ### end Alembic commands ###
