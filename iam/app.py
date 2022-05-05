from flask import Flask

from iam.controller.v1.group_controller import app_group
from iam.controller.v1.user_controller import app_user
from iam.di.container import Container

app = Flask(__name__)
container = Container()
app.container = container
app.register_blueprint(app_user)
app.register_blueprint(app_group)


if __name__ == "__main__":
    app.run()
