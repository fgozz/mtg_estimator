from flask import Flask
from flask_restful import Api
from flasgger import Swagger

# endpoint lists
from resources.evaluate import Evaluator
from resources.detect import Detector

# per test upload image 
from flask import render_template


import logging, datetime






# Avvio applicazione
app = Flask(__name__)

swagger = Swagger(app)

api = Api(app, prefix="/estimator")

# Init endpoints
api.add_resource(Evaluator, '/evaluate')
api.add_resource(Detector, '/detect')





# test image upload
import sys
sys.path.append('..')

@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    logging.basicConfig(filename="log/flask_app.log", level=logging.INFO)
    logging.info(f'{datetime.datetime.now} --- Avvio applicazione ----')
    # avvio app
    app.run(port=5005, host='0.0.0.0', debug=True)











