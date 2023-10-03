"""empty message

<<<<<<<< HEAD:migrations/versions/1086e9afc184_.py
<<<<<<<< HEAD:migrations/versions/1086e9afc184_.py
Revision ID: 1086e9afc184
Revises: 
Create Date: 2023-09-30 02:20:53.613398
========
Revision ID: 6ab733b7af49
Revises: 
Create Date: 2023-09-29 18:37:23.601224
>>>>>>>> main:migrations/versions/6ab733b7af49_.py
========
Revision ID: 98ec02fdc7f3
Revises: 
Create Date: 2023-10-02 22:52:10.597045
>>>>>>>> main:migrations/versions/98ec02fdc7f3_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/1086e9afc184_.py

revision = '1086e9afc184'

========
revision = '98ec02fdc7f3'
>>>>>>>> main:migrations/versions/98ec02fdc7f3_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('login_method', sa.String(length=80), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('street_address', sa.String(length=120), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('country', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Integer(), nullable=False),
    sa.Column('currency', sa.String(length=80), nullable=False),
    sa.Column('payment_method', sa.String(length=80), nullable=False),
    sa.Column('payment_amount', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=80), nullable=False),
    sa.Column('state', sa.String(length=80), nullable=False),
    sa.Column('country', sa.String(length=80), nullable=False),
    sa.Column('postal_code', sa.Integer(), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reset_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('token', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['email'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reset_tokens')
    op.drop_table('payments')
    op.drop_table('user')
    # ### end Alembic commands ###
