from distutils.log import debug 
from fileinput import filename 
from flask import *  
from pypdf import PdfReader 
from flask_cors import CORS

app = Flask(__name__)  
CORS(app, origins='http://localhost:3000')
  
@app.route('/')   
def main():   
    return Response("{'Status':'OK'}",status=200)
  
@app.route('/upload', methods = ['POST'])   
def upload_and_process():
    """Handles file upload and text extraction from the first page of a PDF."""

    if request.method == 'POST':
        f = request.files.get('file')

        if f is None or f.filename == '':
            return Response("{'Status': 'Error', 'Message': 'No file uploaded'}", status=400)
        try:
            reader = PdfReader(f)
            page = reader.pages[0]
            text = page.extract_text()
        
            return Response(f"{{'Status': 202, 'Text': '{text}'}}", status=202)


        except Exception as e:
            print(f"Error processing file: {e}")
            return Response("{'Status': 'Error', 'Message': 'Internal server error'}", status=500)

    else:
        return Response("{'Status': 'Error', 'Message': 'Method not allowed'}", status=405)
  
if __name__ == '__main__':   
    app.run(debug=True)