import os
from werkzeug.utils import secure_filename
from flask import current_app
from typing import Dict
from werkzeug.datastructures import FileStorage

def save_uploaded_files(files: Dict[str, FileStorage]) -> Dict[str, str]:
    """Save uploaded files and return a dictionary of their paths."""
    saved_files = {}
    upload_folder = current_app.config['UPLOAD_FOLDER']
    
    os.makedirs(upload_folder, exist_ok=True)
    
    for key, file in files.items():
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            saved_files[key] = filepath
            
    return saved_files