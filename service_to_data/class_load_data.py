class PhoneTrackerRepository:
    def __init__(self, driver):
        self.driver = driver

    def create_graph(self, data):
        if isinstance(data, list):
            data = data[0]
        devices = data["devices"]
        interaction = data["interaction"]
        with self.driver.session() as session:
            for device in devices:
                session.run("""
                    MERGE (d:Device {id: $id})
                    SET d.name = $name,
                        d.brand = $brand,
                        d.model = $model,
                        d.os = $os,
                        d.latitude = $latitude,
                        d.longitude = $longitude,
                        d.altitude_meters = $altitude_meters,
                        d.accuracy_meters = $accuracy_meters
                """, id=device['id'],name=device['name'], brand=device['brand'], model=device['model'], os=device['os'],
                            latitude=device['location']['latitude'], longitude=device['location']['longitude'],
                            altitude_meters=device['location']['altitude_meters'],
                            accuracy_meters=device['location']['accuracy_meters'])
            session.run("""
                MATCH (from:Device {id: $from_id}), (to:Device {id: $to_id})
                CREATE (from)-[r:INTERACTED_WITH]->(to)
                SET r.method = $method,
                    r.bluetooth_version = $bluetooth_version,
                    r.signal_strength_dbm = $signal_strength_dbm,
                    r.distance_meters = $distance_meters,
                    r.duration_seconds = $duration_seconds,
                    r.timestamp = $timestamp
            """, from_id=interaction['from_device'], to_id=interaction['to_device'],
                        method=interaction['method'], bluetooth_version=interaction['bluetooth_version'],
                        signal_strength_dbm=interaction['signal_strength_dbm'],
                        distance_meters=interaction['distance_meters'],
                        duration_seconds=interaction['duration_seconds'], timestamp=interaction['timestamp'])

        return {"status": "success", "message": "Data added to Neo4j"}

