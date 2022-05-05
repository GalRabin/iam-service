from flask import Blueprint, request

from iam.bl.app.command.user.add_user import add_user_command

app_user = Blueprint("app_user", __name__)


@app_user.route("/v1/user", methods=["POST"])
def add_user_ctrl():
    add_user_command(**request.json)
    return "1"


@app_user.route("/v1/user/<int:user_id>", methods=["GET"])
def get_user_ctrl(user_id: int):
    pass


@app_user.route("/v1/user/<int:user_id>", methods=["PUT"])
def put_user_ctrl(user_id: int):
    pass


@app_user.route("/v1/user/<int:user_id>", methods=["DELETE"])
def delete_user_ctrl(user_id: int):
    pass
