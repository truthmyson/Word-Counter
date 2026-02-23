import os
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS
from count_words import count_words

app = Flask(__name__)
CORS(app)

# ---------------------------
# API endpoint for file upload (expects JSON)
# ---------------------------
@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Receive JSON content
    Expects JSON: { "filename": "example.txt", "content": "base64 encoded content" }
    """
    # get json data
    data = request.get_json()

    # Validate required fields
    if 'filename' not in data and 'content' not in data:
        return jsonify({
            'status': 'error',
            'message': 'Missing filename and or contentfield',
            'response_code': 400
            })
    

    filename = data['filename']
    encoded_content = data['content']
    file_ext = os.path.splitext(filename)[1].lower()
    

    try:
        # Decode base64 content
        
        file_content_bytes = base64.b64decode(encoded_content)
        # get response
        response = count_words(file_content_bytes,file_ext)

        # only for postman testing
        # # send get response for non encoded data
        # response = count_words(encoded_content.encode(errors='replace'), file_ext)
        
        response['data']['file_name'] = filename
        response['data']['response_error'] = 200 if response['status'] == 'success' else 400


        return jsonify(response)
        
    except base64.binascii.Error as e:
        return jsonify({
            'status': 'error',
            'message': f'Invalid base64 encoding: {e}',
            'response_code': 400
            })


# ---------------------------
# Run the application
# ---------------------------
if __name__ == '__main__':
    
    app.run(debug=True)