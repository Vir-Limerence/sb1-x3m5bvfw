from database.mongo_client import get_collection
from datetime import datetime

class AttackGraph:
    @staticmethod
    def save_graph(graph_data: dict) -> str:
        graphs = get_collection('attack_graphs')
        graph_data['timestamp'] = datetime.utcnow()
        result = graphs.insert_one(graph_data)
        return str(result.inserted_id)