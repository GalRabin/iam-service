from dependency_injector.wiring import Provide

from iam.bl.repository.group_repository_interface import GroupRepository
from iam.di.container import Container


def add_group_command(
    group_repository: GroupRepository = Provide[Container.group_repository],
):
    pass
