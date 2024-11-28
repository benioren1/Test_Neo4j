from flask import Blueprint, jsonify, request
from data_base.db import neo4j_driver
from service_to_data.class_query import Queries
bp_query = Blueprint('query', __name__)



@bp_query.route("/api/connections/bluetooth", methods=["GET"])
def get_bluetooth_connections():
    query = Queries(neo4j_driver)
    connections = query.get_bluetooth_connections()
    return jsonify(connections)


@bp_query.route("/api/device_connections/count", methods=["GET"])
def device_connections_count():

    device_id = request.args.get("device_id")

    if not device_id:
        return jsonify({"error": "device_id is required"}), 400

    query = Queries(neo4j_driver)

    count = query.count_connected_devices(device_id)

    return jsonify({"device_id": device_id, "connected_devices_count": count}), 200

@bp_query.route("/api/direct_connection", methods=["GET"])
def is_direct_connection():
    device_id_1 = request.args.get("device_id_1")
    device_id_2 = request.args.get("device_id_2")
    if not device_id_1 or not device_id_2:
        return jsonify({"error": "device_id_1 and device_id_2 are required"}), 400
    query = Queries(neo4j_driver)
    direct_connection = query.is_direct_connection(device_id_1, device_id_2)
    return jsonify({"device_id_1": device_id_1, "device_id_2": device_id_2, "direct_connection": direct_connection}), 200


@bp_query.route("/api/devices/connected", methods=["GET"])
def get_last_device_connection1():
    device_id = request.args.get("device_id")

    if not device_id or not device_id.strip():
        return jsonify({"error": "device_id is required"}), 400

    query = Queries(neo4j_driver)
    last_connection = query.get_last_device_connection(device_id)
    return jsonify({"device_id": device_id, "last_connection": last_connection}), 200

