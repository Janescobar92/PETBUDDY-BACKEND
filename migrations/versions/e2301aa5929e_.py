"""empty message

Revision ID: e2301aa5929e
Revises: 
Create Date: 2021-01-17 12:06:01.572071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2301aa5929e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_type_id', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=200), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('biografy', sa.Text(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('animals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('animal_type', sa.Enum('perro', 'gato', 'conejo', 'roedores', 'aves'), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('personality', sa.Enum('amigable', 'dominante', 'nervioso', 'agresivo', 'jugueton'), nullable=False),
    sa.Column('gender', sa.Boolean(create_constraint=False), nullable=True),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('size', sa.Float(), nullable=False),
    sa.Column('diseases', sa.Text(), nullable=False),
    sa.Column('sterilized', sa.Boolean(create_constraint=False), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user_author', sa.Integer(), nullable=True),
    sa.Column('points', sa.Float(), nullable=True),
    sa.Column('text', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['id_user_author'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_service_type', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('id_user_offer', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('price_h', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['id_service_type'], ['service_type.id'], ),
    sa.ForeignKeyConstraint(['id_user_offer'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('operations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_who_hire', sa.Integer(), nullable=False),
    sa.Column('service_id_hired', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=250), nullable=False),
    sa.Column('hired_time', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['service_id_hired'], ['services.id'], ),
    sa.ForeignKeyConstraint(['user_id_who_hire'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operations')
    op.drop_table('services')
    op.drop_table('review')
    op.drop_table('animals')
    op.drop_table('user')
    op.drop_table('service_type')
    # ### end Alembic commands ###
