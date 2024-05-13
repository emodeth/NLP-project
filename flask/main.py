from distutils.log import debug 
from fileinput import filename 
from flask import *  
from pypdf import PdfReader 


app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return Response("{'Status':'OK'}",status=200)
  
@app.route('/upload', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        reader = PdfReader(f) 
        page = reader.pages[0] 
  
        text = page.extract_text() 
        print(text) 

        return Response("{'Status':'Retrieved'}",status=202)
  
if __name__ == '__main__':   
    app.run(debug=True)