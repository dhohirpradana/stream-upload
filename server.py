import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/upload", methods=["POST"])
def upload():
    try:
        # Ensure the directory exists for saving the uploaded file
        output_dir = "uploaded_files"
        os.makedirs(output_dir, exist_ok=True)

        # Extract file name from the Content-Disposition header if available
        file_name = request.headers.get("X-Filename")
        if not file_name:
            file_name = "uploaded_file"  # Fallback file name if none is provided

        output_file_path = os.path.join(output_dir, file_name)

        # Write the uploaded data to the file
        with open(output_file_path, "wb") as f:
            chunk_size = 4096
            while True:
                chunk = request.stream.read(chunk_size)
                if len(chunk) == 0:
                    break
                f.write(chunk)

        # Send a success response to the client
        return jsonify({"message": "File upload successful", "file_name": file_name, "path": output_file_path}), 200
    except Exception as e:
        # Send an error response to the client
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
