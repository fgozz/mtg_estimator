
import os

def list_files_in_folder(folder_path = "C:\\Users\\Utente\\Desktop\\mtg_detector\\data\\sets_data\\AllSetFiles"):
    files = os.listdir(folder_path)
    return files


def get_card_names():

    card_names = []

    files = list_files_in_folder()

    for set in files:
        # leggi tutti i json ed estrai 
        pass




    return card_names



