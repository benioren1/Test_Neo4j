from flask import Blueprint, jsonify
from data_base.db import neo4j_driver
from service_to_data.class_query import Queries
bp_query = Blueprint('query', __name__)



@bp_query.route("/api/connections/bluetooth", methods=["GET"])
def get_bluetooth_connections():
    query = Queries(neo4j_driver)
    connections = query.get_bluetooth_connections()
    return jsonify(connections)