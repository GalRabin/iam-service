from dependency_injector.wiring import Provide

from iam.bl.repository.user_repository_interface import UserRepository
from iam.di.container import Container


def add_user_command(
    username: str,
    password: str,
    fullname: str,
    email: str,
    user_repository: UserRepository = Provide[Container.user_repository],
    **kwargs
):
    pass
