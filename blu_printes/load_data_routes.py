import json
from flask import Blueprint, request, jsonify
from service_to_data.class_load_data import PhoneTrackerRepository
from data_base.db import neo4j_driver
bp_load = Blueprint("load",__name__)



@bp_load.route("/api/phone_tracker", methods=["POST"])
def create_phone_tracker():
    data = request.get_json()
    print(json.dumps(data, indent=4))
    query = PhoneTrackerRepository(neo4j_driver)
    result = query.create_graph(data)
    return jsonify(result)
