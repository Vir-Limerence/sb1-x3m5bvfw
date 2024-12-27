from flask import Blueprint, request, jsonify
from services.topology_service import TopologyService
from utils.file_utils import save_uploaded_files
from utils.request_utils import validate_files, validate_json

topology_bp = Blueprint('topology', __name__)
topology_service = TopologyService()

@topology_bp.route('/generate-topology', methods=['POST'])
@validate_files(['topologyFile', 'expansionInfoFile'])
def generate_topology():
    files = save_uploaded_files(request.files)
    data = request.form.to_dict()
    result = topology_service.generate_topology(data, files)
    return jsonify(result)

@topology_bp.route('/verify-consistency', methods=['POST'])
@validate_json(['nodeReachVerification', 'pathReachVerification', 'integrityAnalysis'])
def verify_consistency():
    data = request.get_json()
    result = topology_service.verify_consistency(data)
    return jsonify(result)

@topology_bp.route('/scenario-division', methods=['POST'])
@validate_files(['topologyFile'])
def divide_scenarios():
    files = save_uploaded_files(request.files)
    data = request.form.to_dict()
    result = topology_service.divide_scenarios(data, files)
    return jsonify(result)