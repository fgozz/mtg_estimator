from flask import request
# per gestire le immagini  
from flask import send_file, jsonify
# per gestione dell'endpoint e parsing delle richieste
from flask_restful import Resource, reqparse

# librerie necessarie per mtg_detector
import pytesseract
import numpy as np
from PIL import Image

import logging, datetime

class Detector(Resource):
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

        filename = "img/download/test.png"

        # salva l'immagine
        image = request.files['image']
        image.save(filename)

        # carica l'immagine e usa l'OCR
        img = np.array(Image.open(filename))
        text = pytesseract.image_to_string(img)

        # confronta le stringhe con i nomi delle carte
        logging.info(f'{datetime.datetime.now} OCR Result: {text}')

        # ritorna il nome più simile
        #card_name = "Lightning Bolt"
        
        card_name = text

        return card_name
