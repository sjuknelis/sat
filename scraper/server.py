from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from urllib.parse import unquote
import json

from process import process_content

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/upload')
def upload():
    json_string = request.args.get('data')

    process_content(json.loads(unquote(json_string)))

    return jsonify({"ok": True})

if __name__ == '__main__':
    app.run(debug=True, port=8000)
