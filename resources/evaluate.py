from flask import request
# per gestire le immagini  
from flask import send_file, jsonify
# per gestione dell'endpoint e parsing delle richieste
from flask_restful import Resource, reqparse


# librerie necessarie per mtg_evaluator




class Evaluator(Resource):
    parser = reqparse.RequestParser()
    #parser.add_argument('check', required=False, help="descrizione di cosa fa questo campo del body")

    def get(self):
        image_path = "img/TODO.png"

        evaluation_data = {
            "valutazione": "100 euro"
        }
        
        image_data = send_file(image_path, mimetype='image/png')

        response_data = {
            'image': image_data,
            'text': evaluation_data
        }

        return jsonify(response_data)


    def post(self):
        return "bravo!"
