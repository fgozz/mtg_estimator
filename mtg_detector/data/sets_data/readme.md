all'inizio pensavo di prenderli uno alla volta ma ho visto che c'è una cartella con tutti i json da scaricare

https://mtgjson.com/api/v5/AllSetFiles.zip



# all_set_list.json

non serve più? 

posso popolarlo leggendo i nomi dei file dello zip in caso.





# per trovare i nomi

eng

['data']['cards'][0]['name']

NB: lista di carte! [0] prende la prima

foreign

['data']['cards'][0]['foreignData'][0]


NB: lista di carte e lingue straniere, prendi la prima!



# link a cardmarket

['data']['cards'][0]["purchaseUrls"]["cardmarket"]

