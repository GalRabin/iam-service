from sqlalchemy import Column, Integer, String

from iam.db.entity.base import Base


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)

    def __repr__(self):
        return f"Group(id={self.id!r}, name={self.name!r})"
