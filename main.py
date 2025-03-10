from flask import Flask, request, render_template
from google.cloud import storage

app = Flask(__name__)

# Configure the GCS bucket name
GCS_BUCKET_NAME = 'bktsalesdata'

# Initialize the Google Cloud Storage client
storage_client = storage.Client()

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            # Upload large files using a resumable upload
            bucket = storage_client.bucket(GCS_BUCKET_NAME)
            blob = bucket.blob(file.filename)

            # Use a resumable upload
            blob.upload_from_file(file, content_type=file.content_type, 
                                  if_generation_match=None, 
                                  timeout=600)  # Increase timeout for large files
            
            return f'File {file.filename} uploaded successfully to {GCS_BUCKET_NAME}.'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
