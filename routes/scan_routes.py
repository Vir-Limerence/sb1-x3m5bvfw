from flask import Blueprint, request, jsonify
from services.scan_service import ScanService
from utils.request_utils import validate_json

scan_bp = Blueprint('scan', __name__)
scan_service = ScanService()

@scan_bp.route('/scan', methods=['POST'])
@validate_json(['target', 'scanType', 'portRange'])
def scan_network():
    config = request.get_json()
    result = scan_service.perform_scan(config)
    return jsonify(result)