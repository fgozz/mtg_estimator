
import csv
import time
import requests
import logging, datetime

from pprint import pprint



def read_card_list():

    card_list = []

    # Apre il file CSV in modalità di lettura
    with open('data/list_to_evaluate.csv', mode='r') as file:
        # Crea un oggetto lettore CSV
        csv_reader = csv.reader(file)

        # Legge ogni riga del file CSV
        for row in csv_reader:
            card_list.append(row)

    return card_list

def evaluate_card(card):
    set = card[1]
    id = card[2]

    # componi url
    url = f'https://api.scryfall.com/cards/{set}/{id}'

    # fai chiamata
    # Fai la richiesta GET
    response = requests.get(url)

    # Controlla lo stato della risposta
    if response.status_code == 200:
        # se la risposta è in formato JSON
        data = response.json()  
        logging.info(f'{datetime.datetime.now()} {data}')
    else:
        # Se c'è stato un errore nella richiesta, stampa lo status code
        logging.info(f'{datetime.datetime.now()} Errore: {response.status_code}')

    return data['prices']['eur']

def evaluate_card_list(card_list):

    evaluated_list = []

    stima_valutazione = len(card_list) * 1/2 

    logging.info(f'{datetime.datetime.now()} inizio valutazione {len(card_list)} carte. Stima valutazione: {stima_valutazione}s ')

    for card in card_list:
        time.sleep(0.4)

        try:
            value = evaluate_card(card)
        except:
            logging.info(f'{datetime.datetime.now()} valutazione di {card} fallita!')
            continue    
        card.append(value)

        evaluated_list.append(card)

    logging.info(f'{datetime.datetime.now()} valutate {len(evaluated_list)} carte')

    return evaluated_list

def write_evaluated_list(evaluated_list):

    logging.info(f'{datetime.datetime.now()} scrittura di {len(evaluated_list)} valutazioni su file')

    # Scrivi la lista di liste in un file CSV
    with open('data/list_evaluated.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(evaluated_list)

    return



def total_evaluation(evaluated_list):

    total_evaluation = 0

    for card in evaluated_list:
        total_evaluation = total_evaluation + float(card[3])

    return total_evaluation




if __name__ == "__main__":
    logging.basicConfig(filename="log/evaluate_mtg_list.log", level=logging.INFO)
    logging.info(f'{datetime.datetime.now()} ----- Script start -----')

    card_list = read_card_list()

    # valutazione carta singola
    #evaluation = evaluate_card(card_list[1])
    #logging.info(f'{datetime.datetime.now()} valore di {card_list[1][0]}: {evaluation}')

    valuated_list = evaluate_card_list(card_list)

    write_evaluated_list(valuated_list)

    total_evaluation = total_evaluation(valuated_list)

    print(f"VALUTAZIONE COMPLESSIVA: {total_evaluation}")

    logging.info(f'{datetime.datetime.now()} ----- Script end -----')
