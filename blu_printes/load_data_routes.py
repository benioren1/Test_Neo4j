import json

from flask import Blueprint, request

bp_load = Blueprint("load",__name__)


@bp_load.route("/api/phone_tracker", methods=["POST"])
def create_phone_tracker():
    # TODO: Implement phone tracker loading
    data=request.get_json()
    print(json.dumps(data))
    query = # Debugging purpose)
    return {"message": "Phone tracker loaded successfully"} ,200
