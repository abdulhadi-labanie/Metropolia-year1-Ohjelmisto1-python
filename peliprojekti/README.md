# ECO-Airline Manager

## Tekijä
Abdulhadi Labanie

## Kuvaus pelistä
Tämä on tekstipohjainen peli, joka on tehty Pythonilla. Pelissä pelaaja toimii lentoyhtiön johtajana. Pelin tarkoituksena on valita hyvät lentoreitit ja ostaa oikeita lentokoneita, jotta yhtiö tekee voittoa ja säästää ympäristöä.

## Kestävän kehityksen teema
Peli liittyy kestävään kehitykseen ja ilmastotekoihin. Pelissä lasketaan CO2-päästöt ja lentokoneen tehokkuus. Pelaajan täytyy yrittää vähentää päästöjä reittivalinnoilla. 
Esimerkki: Jos käytät isoa lentokonetta lyhyellä reitillä, CO2-arvosana on huono. Oikea kone oikealle reitille antaa paremman arvosanan.

## Pelin rakenne ja logiikka
Pelin kulku on jaettu kolmeen pääosaan: pelaajan tiedot, uusi ura ja pelin logiikka. Voit nähdä pelin rakenteen alla olevasta kaaviosta:

![ECO-Airline Manager Map](<img/ECO-Airline Manager.png>)

## Vuokaavion (Flowchart) linkki https://canva.link/d0pgrpm9ju2hnk7

## Arkkitehtuuri ja tietorakenne
Pelin tiedot tallennetaan paikallisesti JSON-tiedostoon. Jokaisella pelaajalla on oma tiedosto (esimerkiksi `abdulhadi.json`). 

Tietorakenne on jaettu selkeisiin osiin:
1. Käyttäjä (Manager): Pelaajan nimi ja ikä.
2. Ura (Career): Yrityksen nimi, budjetti ja kotikenttä (esim. Helsinki).
3. Vuodet (Years): Tilastot tallennetaan vuosittain (esim. vuosi 2026).
4. Lentokoneet (Planes): Jokaisen koneen tekniset tiedot ja tulokset (lennot, matkustajat, voitto ja CO2-päästöt).

Tämä rakenne (OOP - Olio-ohjelmointi) pitää pelin tiedot hyvässä järjestyksessä ja helpottaa tallentamista.

## Mitä on tehty tähän mennessä
- Käyttäjän nimen ja iän kysyminen (pelaajan täytyy olla vähintään 12-vuotias).
- Päävalikko, joka toimii while-silmukassa.
- Syötteiden tarkistus ja virheiden käsittely (try-except).
- Luokkien (OOP) luominen: Manager, Career ja Plane.
- Pelin tilan tallentaminen ja lukeminen JSON-tiedostosta.
- CO2-laskuri ja voiton laskeminen.

## Miten peli käynnistetään
(
git clone
`git clone https://github.com/abdulhadi-labanie/Metropolia-year1-Ohjelmisto1-python.git`

Sitten RUN `main.py`

Jos haluat lisätä pelitilastosi:
1. kloonata pelin
2. pelata
3. Luoda PR:n ja hyväksyn JSON-tiedostosi. 
)
