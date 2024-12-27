from database.mongo_client import get_collection
from datetime import datetime

class ScanResult:
    @staticmethod
    def save_result(scan_data: dict) -> str:
        scans = get_collection('scan_results')
        scan_data['timestamp'] = datetime.utcnow()
        result = scans.insert_one(scan_data)
        return str(result.inserted_id)
    
    @staticmethod
    def get_result(scan_id: str) -> dict:
        scans = get_collection('scan_results')
        return scans.find_one({'_id': scan_id})