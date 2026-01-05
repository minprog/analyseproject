# Pandas

Leer gegevens op te slaan en te manipuleren met behulp van de **pandas**-bibliotheek van Python. 

## Notebooks

Deze opdracht heeft de vorm van een Jupyter "notebook". Dit is een aparte programmeeromgeving waarin experimenteren centraal staat. Je kunt code schrijven, snel uittesten, verbeteren en nogmaals uitvoeren zonder tussenstappen. Het systeem wordt daarom veel gebruikt in de verkennende fase van data-verwerkingsprojecten. Het programmeren gebeurt in je webbrowser.

🧑‍💻 Als je niet bij het college was, of je wil nog even rusten kijken hoe het werkt, dan kun je [hier een filmpje vinden met uitleg over Notebooks](https://www.youtube.com/watch?v=HW29067qVWk) om goed te kunnen starten.

## Downloaden

Alle [oefeningen en de benodigde achtergrondinformatie staan in een zipfile](pandas.zip) (download). Je kunt deze op een handige plek opslaan. Dan ga je naar de terminal en `cd` naar die directory.

## Installeren

Je hebt al Python geïnstalleerd. Zorg dat dit nu echt soepel werkt en dat je in de terminal/command prompt ook Jupyter Notebook kunt opstarten.

Start deze ChatGPT share om te checken (gebruik a.u.b. deze en niet gewoon ChatGPT: we hebben 'm gevoerd met relevante informatie zodat het minder snel misloopt):

<https://chatgpt.com/g/g-muT6gPRxL-python-kickstarter>

Als je Python gewoon werkt, installeer dan met `pip` deze packages:

- jupyter
- seaborn
- pandas

Je kunt die ChatGPT ook vragen om hulp hierbij.

## Starten

Als Jupyter is geinstalleerd kun je Jupyter Notebook starten met dit commando:

    jupyter-notebook

Dit zou een nieuw tabblad in je webbrowser moeten openen, waarin je ook alle bestanden uit de huidige directory ziet staan. Klik op het notebookbestand met de naam `pandas.ipynb`. Hierdoor wordt een nieuw tabblad geopend met de inhoud van het notitieboek. Volg daar de instructies voor het gebruik van notebooks.

## uvx

Als de installatie mislukt kun je naar de laptophelpdesk om het te fixen. In noodgevallen mag je `uvx` gebruiken. Installeer dan eerst `uv` van de volgende pagina:

<https://github.com/astral-sh/uv>

En geef dan op de command line het commando:

    uvx --with pandas --with jupyter --from jupyter-core jupyter notebook pandas.ipynb
