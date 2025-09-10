from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import base64
import io

app = Flask(__name__)
CORS(app) 

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/convert", methods=["POST"])
def convert():
    try:
        data = request.get_json()
        file_data = data.get('fileData')
        mode = data.get('mode')
        filename = data.get('filename', 'converted_file')

        if mode == "encode":
            file_bytes = base64.b64decode(file_data.split(',')[1])
            encoded = base64.b64encode(file_bytes).decode("utf-8")
            return jsonify({
                'success': True,
                'data': encoded,
                'filename': filename + '.txt'
            })

        elif mode == "decode":
            decoded = base64.b64decode(file_data)
            encoded_data = base64.b64encode(decoded).decode("utf-8")
            return jsonify({
                'success': True,
                'data': encoded_data,
                'filename': filename.replace('.txt', '') + '_decoded.mp4'
            })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
