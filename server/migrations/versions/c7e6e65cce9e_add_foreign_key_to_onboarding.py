"""add foreign key to onboarding

Revision ID: c7e6e65cce9e
Revises: a841b724be26
Create Date: 2024-07-03 08:55:23.659621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7e6e65cce9e'
down_revision = 'a841b724be26'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('onboardings', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_onboardings_employee_id_employees'), 'onboardings', 'employees', ['employee_id'], ['id'])
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    op.drop_constraint(op.f('fk_onboardings_employee_id_employees'), 'onboardings', type_='foreignkey')
    op.drop_column('onboardings', 'employee_id')
    # ### end Alembic commands ###
