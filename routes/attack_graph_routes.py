from flask import Blueprint, request, jsonify
from services.attack_graph_service import AttackGraphService
from utils.file_utils import save_uploaded_files
from utils.request_utils import validate_files

attack_graph_bp = Blueprint('attack_graph', __name__)
attack_graph_service = AttackGraphService()

@attack_graph_bp.route('/generate-attack-graph', methods=['POST'])
def generate_attack_graph():
    files = save_uploaded_files(request.files) if 'topologyFile' in request.files else {}
    data = request.form.to_dict()
    result = attack_graph_service.generate_graph(data, files)
    return jsonify(result)

@attack_graph_bp.route('/min-cut', methods=['POST'])
@validate_files(['attackGraphFile', 'vulnerabilityTableFile'])
def analyze_min_cut():
    files = save_uploaded_files(request.files)
    result = attack_graph_service.analyze_min_cut(files)
    return jsonify(result)

@attack_graph_bp.route('/node-partition', methods=['POST'])
@validate_files(['attackGraphFile'])
def partition_nodes():
    files = save_uploaded_files(request.files)
    data = request.form.to_dict()
    result = attack_graph_service.partition_nodes(data, files)
    return jsonify(result)