from flask import Blueprint


app_group = Blueprint("app_group", __name__)


@app_group.route("/v1/group", methods=["POST"])
def add_group_ctrl():
    pass


@app_group.route("/v1/group/<int:group_id>", methods=["GET"])
def get_group_ctrl(group_id: int):
    pass


@app_group.route("/v1/group/<int:group_id>", methods=["PUT"])
def put_group_ctrl(group_id: int):
    pass


@app_group.route("/v1/group/<int:group_id>", methods=["DELETE"])
def delete_group_ctrl(group_id: int):
    pass
