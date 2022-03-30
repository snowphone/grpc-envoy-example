import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Repository(Base):
	__tablename__ = 'key_value_repo'

	key = sa.Column(sa.String, primary_key=True)
	value = sa.Column(sa.String, nullable=False)

conn = sa.create_engine("sqlite://")

