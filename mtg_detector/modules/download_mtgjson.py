import requests
import logging,datetime

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        logging.info(f'{datetime.datetime.now()} {filename} downloaded successfully')
    else:
        logging.info(f'{datetime.datetime.now()} Failed to download {filename}')


def read_sets_list():
    """
    c'è un json con tutti i nomi dei set, questa funzione li legge e torna la lista
    """
    


    return



