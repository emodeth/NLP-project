from distutils.log import debug 
from fileinput import filename 
from flask import *  
from pypdf import PdfReader 
from flask_cors import CORS
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
CORS(app, origins='http://localhost:3000')
  

class Upload(Resource):

    def post(self):
        f = request.files.get('file')

        if f is None or f.filename == '':
            return Response("{'Status': 'Error', 'Message': 'No file uploaded'}", status=400)
        try:
            reader = PdfReader(f)
            page = reader.pages[0]
            text = page.extract_text()

            data = {
                'Status': 202,
                'Text': text
            }
        
            return jsonify(data)


        except Exception as e:
            print(f"Error processing file: {e}")
            return Response("{'Status': 'Error', 'Message': 'Internal server error'}", status=500)

  
api.add_resource(Upload, '/upload')

  
if __name__ == '__main__':   
    app.run(debug=True)