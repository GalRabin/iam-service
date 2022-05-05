from sqlalchemy.engine import Engine

from iam.bl.repository.user_repository_interface import UserRepository


class UserRepositorySql(UserRepository):
    def __init__(self, engine: Engine):
        self._engine = engine

    def save(self):
        pass

    def update(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass
