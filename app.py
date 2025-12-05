from flask import Flask, send_from_directory, jsonify, request
import os
import json

app = Flask(__name__, static_folder='.')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/images/<path:filename>')
def serve_images(filename):
    return send_from_directory('images', filename)

@app.route('/api/pages', methods=['GET'])
def list_pages():
    files = [f for f in os.listdir('.') if f.endswith('.json') and f != 'prompts.json' and f != 'package.json' and f != 'tsconfig.json']
    # Filter out system files or config files if any. 
    # The user mentioned "my_prompts.json", "friend_prompts.json".
    # We should probably exclude 'prompts.json' if we are moving away from it, or keep it if it's just another page.
    # The user said "split the prompts.json file into 3 files", so prompts.json might be redundant now.
    # I'll exclude it to avoid confusion, or maybe the user wants to keep it as a backup.
    # Let's just list all .json files that look like pages.
    return jsonify(files)

@app.route('/api/pages/<path:filename>', methods=['GET'])
def get_page(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

@app.route('/api/pages', methods=['POST'])
def save_page():
    data = request.json
    filename = data.get('filename')
    content = data.get('content')
    
    # Allow empty content (empty dict/array), but not None
    if not filename or content is None:
        return jsonify({"error": "Missing filename or content"}), 400
    
    if not filename.endswith('.json'):
        filename += '.json'
        
    # Security check: prevent directory traversal
    if '..' in filename or '/' in filename or '\\' in filename:
         return jsonify({"error": "Invalid filename"}), 400

    try:
        with open(filename, 'w') as f:
            json.dump(content, f, indent=2)
        return jsonify({"message": "Saved successfully", "filename": filename})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
