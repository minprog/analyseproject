# Pandas

Leer gegevens op te slaan en te manipuleren met behulp van de **pandas**-bibliotheek van Python. 

## Notebooks

Deze opdracht heeft de vorm van een Jupyter "notebook". Dit is een aparte programmeeromgeving waarin experimenteren centraal staat. Je kunt code schrijven, snel uittesten, verbeteren en nogmaals uitvoeren zonder tussenstappen. Het systeem wordt daarom veel gebruikt in de verkennende fase van data-verwerkingsprojecten. Het programmeren gebeurt in je webbrowser.

🧑‍💻 Als je niet bij het college was, of je wil nog even rusten kijken hoe het werkt, dan kun je [hier een filmpje vinden met uitleg over Notebooks](https://www.youtube.com/watch?v=HW29067qVWk) om goed te kunnen starten.

## Downloaden

Alle [oefeningen en de benodigde achtergrondinformatie staan in een zipfile](pandas.zip) (download). Je kunt deze op een handige plek opslaan. Dan ga je naar de terminal en `cd` naar die directory.

Daar ga je eerst Jupyter installeren:

    pip3 install jupyter pandas

(Of eventueel `pip` in plaats van `pip3`.)

Als het installeren van een Python-package niet werkt op die manier op jouw computer dan weet je misschien zelf hoe je het moet installeren, óf je vraagt nog even hulp.

## Starten

Als Jupyter is geinstalleerd kun je Jupyter Notebook starten met dit commando:

    jupyter-notebook

Dit zou een nieuw tabblad in je webbrowser moeten openen, waarin je ook alle bestanden uit de huidige directory ziet staan. Klik op het notebookbestand met de naam `pandas.ipynb`. Hierdoor wordt een nieuw tabblad geopend met de inhoud van het notitieboek. Volg daar de instructies voor het gebruik van notebooks.

## uvx

Als de installatie mislukt kun je naar de laptophelpdesk om het te fixen. In noodgevallen mag je `uvx` gebruiken. Installeer dan eerst `uv` van de volgende pagina:

<https://github.com/astral-sh/uv>

En geef dan op de command line het commando:

    uvx --with pandas --with jupyter --from jupyter-core jupyter notebook pandas.ipynb
