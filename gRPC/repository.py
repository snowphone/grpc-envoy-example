from typing import Optional, Tuple
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Entry(Base):
	__tablename__ = 'entries'

	key = sa.Column(sa.String, primary_key=True)
	value = sa.Column(sa.String, nullable=False)

	def __init__(self, key: str, value: str) -> None:
		self.key = key
		self.value = value

	def __repr__(self) -> str:
		return f"Entry(key={self.key}, value={self.value})"

url = "postgresql://user:password@database:5432/db"
testUrl = "sqlite://"


class Repository:
	def __init__(self, url: str) -> None:
		engine = sa.create_engine(url, echo=True)

		if not database_exists(url):
			create_database(url)

		Base.metadata.create_all(engine)

		Session = sessionmaker()
		Session.configure(bind=engine)

		self.sess = Session()
		self.sess.commit()
		return

	def add(self, key: str, value: str):
		if key in self:
			self.sess.query(Entry).filter(Entry.key == key).update({Entry.value: value})
		else:
			self.sess.add(Entry(key, value))
		self.sess.commit()
	
	def get(self, key: str) -> Optional[str]:
		entry: Optional[Entry] = self.sess.query(Entry).get(key)
		if entry is None:
			return None
		return str(entry.value)
	
	def __contains__(self, item: str) -> bool:
		return self.get(item) is not None
