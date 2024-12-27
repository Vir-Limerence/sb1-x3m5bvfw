from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.scan_routes import scan_bp
from routes.topology_routes import topology_bp
from routes.attack_graph_routes import attack_graph_bp
from config import Config

app = Flask(__name__)
CORS(app)
app.config.from_object(Config)

# Register blueprints with correct URL prefixes
app.register_blueprint(auth_bp)  # No prefix for login
app.register_blueprint(scan_bp)  # No prefix for scan
app.register_blueprint(topology_bp)  # No prefix for topology routes
app.register_blueprint(attack_graph_bp)  # No prefix for attack graph routes

@app.route('/health')
def health_check():
    return {'status': 'ok', 'message': 'Server is running'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)