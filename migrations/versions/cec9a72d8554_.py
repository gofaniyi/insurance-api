"""empty message

Revision ID: cec9a72d8554
Revises: f307b25a5513
Create Date: 2019-05-30 04:01:48.066114

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'cec9a72d8554'
down_revision = 'f307b25a5513'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('risks',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('data', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('risk_type_id', sa.Integer(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('risks_company_id_fkey')),
    sa.ForeignKeyConstraint(['risk_type_id'], ['risk_types.id'], name=op.f('risks_risk_type_id_fkey')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_risks'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('risks')
    # ### end Alembic commands ###