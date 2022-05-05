from dependency_injector.wiring import Provide

from iam.bl.repository.user_repository_interface import UserRepository
from iam.di.container import Container


def update_user_command(
    user_repository: UserRepository = Provide[Container.user_repository],
):
    pass
