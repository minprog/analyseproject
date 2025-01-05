# Pandas

Leer gegevens op te slaan en te manipuleren met behulp van de **pandas**-bibliotheek van Python. 

## Notebooks

Deze opdracht heeft de vorm van een Jupyter "notebook". Dit is een aparte programmeeromgeving waarin experimenteren centraal staat. Je kunt code schrijven, snel uittesten, verbeteren en nogmaals uitvoeren zonder tussenstappen. Het systeem wordt daarom veel gebruikt in de verkennende fase van data-verwerkingsprojecten. Het programmeren gebeurt in je webbrowser.

🧑‍💻 Als je niet bij het college was, of je wil nog even rusten kijken hoe het werkt, dan kun je [hier een filmpje vinden met uitleg over Notebooks](https://www.youtube.com/watch?v=HW29067qVWk) om goed te kunnen starten.

## Downloaden

Alle [oefeningen en de benodigde achtergrondinformatie staan in een zipfile](pandas.zip) (download). Je kunt deze op een handige plek opslaan. Dan ga je naar de terminal en `cd` naar die directory.

## Installeren

Je zou al "Anaconda" op je computer moeten hebben omdat dit tijdens de introductie is geïnstalleerd. [Zie deze chatGPT share voor instructies om jupyter notebook op te starten en/of te installeren als je Anaconda hebt.](https://chatgpt.com/share/677ac682-5d6c-8003-a7a5-61d961dcba14) Als je geen Anaconda lijkt te hebben, chat dan verder door uit te leggen wat je op je scherm krijgt en wat je probeert - ChatGPT zal je verder helpen. Maar schroom niet om de docenten erbij te halen tijdens college :-)

## Starten

Als Jupyter is geinstalleerd kun je Jupyter Notebook starten met dit commando:

    jupyter-notebook

Dit zou een nieuw tabblad in je webbrowser moeten openen, waarin je ook alle bestanden uit de huidige directory ziet staan. Klik op het notebookbestand met de naam `pandas.ipynb`. Hierdoor wordt een nieuw tabblad geopend met de inhoud van het notitieboek. Volg daar de instructies voor het gebruik van notebooks.

## uvx

Als de installatie mislukt kun je naar de laptophelpdesk om het te fixen. In noodgevallen mag je `uvx` gebruiken. Installeer dan eerst `uv` van de volgende pagina:

<https://github.com/astral-sh/uv>

En geef dan op de command line het commando:

    uvx --with pandas --with jupyter --from jupyter-core jupyter notebook pandas.ipynb
