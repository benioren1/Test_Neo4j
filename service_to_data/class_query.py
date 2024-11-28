class Queries:
    def __init__(self, driver):
        self.driver = driver

    def get_bluetooth_connections(self):
        with self.driver.session() as session:
            # Cypher query to find devices connected via Bluetooth and calculate the total duration
            result = session.run("""
                MATCH p=(:Device)-[r:CONNECTED {method: 'Bluetooth'}]->(:Device)
                WITH p, SUM(r.duration_seconds) AS total_duration
                RETURN [node IN NODES(p) | node.id] AS devices, total_duration
            """)
            connections = []
            for record in result:
                connections.append({
                    'devices': record['devices'],
                    'total_duration': record['total_duration']
                })
            return connections
