# database delle carte da 

https://mtgjson.com/downloads/all-files/


## file server 

https://mtgjson.com/api/v5/


# Estratti i nomi di tutte le carte dai json

NB: Occorrerà controllare se una delle stringhe estratte dal tesseract è davvero una carta!


### Organizzazione:

Struttura cartella: divisa per set e ogni set diviso per lingua!

```
data\sets_data
    - set1/
    - set2/
        - set1_eng.json
    - ...
    - setN/
```

```
src/
    - i json scaricati da mtgjson con tutti i dati
```




