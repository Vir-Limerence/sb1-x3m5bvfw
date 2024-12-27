from database.mongo_client import get_collection
from datetime import datetime

class Topology:
    @staticmethod
    def save_topology(topology_data: dict) -> str:
        topologies = get_collection('topologies')
        topology_data['timestamp'] = datetime.utcnow()
        result = topologies.insert_one(topology_data)
        return str(result.inserted_id)