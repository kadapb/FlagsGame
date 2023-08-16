import sqlite3
from PIL import Image

# siai funkcijai reikia nurodyt parametra (musu database failo varda)
# ji sukuria 'tilta' tarp programos ir musu nurodytos Databazes
# ir taip leidzia iskviesti/irasyti/naudotis/keisti jos duomenimis.
def connect_database(database_name):
    conn = sqlite3.connect('veliavosDB/'+database_name)
    return conn


# siai funkcijai reikia nurodyti musu sukurta 'tilta'
def fetch_countries_and_flags(conn):
    cursor = conn.cursor()                          #   sukuriam rodykle
    query = "SELECT Country, Flag FROM Veliavos"    #   nurodom ka norim daryti su duomenu baze, siuo atveju - pasirenkam Country ir Flag stulpelius is lenteles "Veliavos"
    cursor.execute(query)                           #   sia komanda aktyvuojam musu duomenu uzklausa
    data = cursor.fetchall()                        #   visa istraukta informacija priskiriam kintamajam 'data' ir jis grazinam.
    return data

# duomenu bazeje nuotraukas saugome BLOB formatu, kad matytume nuotraukas, reikia jas konvertuoti naudojant PIL bibliotekos 'Image.open()' funkcija.
def convert_blob_to_image(blob_data):
    image = Image.open(blob_data)
    return image

