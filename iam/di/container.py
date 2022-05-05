from dependency_injector import containers, providers
from sqlalchemy import create_engine

from iam.db.repository.group_repository_sql import UserRepositorySql


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=["config.yml"])
    engine = providers.Factory(create_engine, url=config.db.url)
    user_repository = providers.Factory(UserRepositorySql, engine=engine)
    group_repository = providers.Factory(UserRepositorySql, engine=engine)
