from sqlalchemy import Column, Integer, String

from iam.db.entity.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    fullname = Column(String)
    email = Column(String)

    def __repr__(self) -> str:
        return (
            f"User(id={self.id!r}, username={self.username!r}, "
            f"password={self.password!r}), fullname={self.fullname!r},"
            f" email={self.email!r}))"
        )
