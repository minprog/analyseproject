# Stap 2. Beschrijving van je dataset

> Let op! Werk voor deze opdracht door met de Notebook die je bij de vorige milestone gemaakt hebt. Maak een nieuw kopje voor "Stap 2. Beschrijving van de dataset" en behandel de volgende onderdelen.

## Een indruk van de vijf belangrijkste variabelen

Hoe een dataset in elkaar zit, bepaalt welke [statistische toetsen](https://nl.wikipedia.org/wiki/Statistische_toets) je kunt uitvoeren. Sommige toetsen werken alleen goed als de data normaal verdeeld is. Als dat niet zo is, kun je sommige toetsen nog steeds uitvoeren, maar de uitkomsten zijn dan mogelijk minder betrouwbaar.

Centrummaten (mediaan, modus, gemiddelde) en spreidingsmaten (zoals standaardafwijking) helpen om een goed beeld te krijgen van je data. Grafieken zijn daarnaast belangrijk om de resultaten duidelijk te maken.

Een grondige analyse van je data helpt niet alleen bij betrouwbaardere resultaten, maar ook bij het plannen van je onderzoek. Je kunt beter inschatten aan welke variabelen je extra aandacht moet besteden en of je meer data nodig hebt.

**OPDRACHT A** Schrijf een tekst van minimaal 300 woorden waarin je de vijf belangrijkste variabelen van de dataset analyseert en voorbereidt voor verder onderzoek. Voor elke variabele beschrijf je het volgende:

- Beschrijf hoe de data eruitziet: wat valt op? zijn er bijzondere waarden (uitbijters)?

- Bepaal de centrummaten (mediaan, modus, gemiddelde) en de spreiding (standaardafwijking, variantie).

- Maak, als dat mogelijk is, een grafiek om de data te visualiseren (bijvoorbeeld histogrammen of boxplots).

Gebruik [Seaborn](https://seaborn.pydata.org/tutorial/introduction.html#a-high-level-api-for-statistical-graphics) om de grafiek te maken in je Notebook. Je mag natuurlijk hulp vragen en opzoeken hiervoor.

## Samenhang tussen variabelen

Na de analyse hierboven weet je veel over in ieder geval de belangrijkste variabelen, maar je weet weinig over de samenhang van de data, dat wil zeggen over de verbanden tussen twee of meer variabelen.

De simpelste verbanden kun je uitdrukken door middel van correlatie (een lineaire formule) of regressie (een polynomiaal).

Ook voor de samenhang van variabelen zijn visualisaties van belang: als twee variabelen samenhangen kan je vaak met een simpele scatterplot zien of de samenhang lineair is of van een hogere orde.

**OPDRACHT B** Schrijf een tekst van minimaal 300 woorden waarin je vijf combinaties van variabelen analyseert. Voor elke combinatie beschrijf je het volgende:

- Beschrijf waarom het logisch is om de gekozen twee variabelen te combineren.

- Maak een plot van de variabelen waaruit de samenhang zichtbaar wordt.

- Beschrijf wat voor relatie je kunt zien in de plot (vraag hulp hierbij als nodig).

## Bias in de data

Een cijfermatige of een relationele analyse van een dataset zegt wat over hoe de dataset in elkaar zit. Iedereen kan dat reproduceren. Het zegt echter niets over de samenhang tussen de dataset en de onderzoeksvraag!

Stel: je kunt met jouw data aantonen dat vrouwen slimmer zijn dan mannen. Mag je die conclusie dan trekken op basis van de dataset die je hebt gevonden of zit er (mogelijk) een bias in. Welke bias zou dat kunnen zijn?

Een [ethische analyse](https://www.datacompetent.eu/pages/blog?p=data-ethiek-het-kompas-voor-verantwoord-gebruik-van-data) is geen objectieve weergave van de data, maar moet ook niet volledig subjectief zijn: het is jouw professionele inschatting over de relatie tussen data en onderzoek. Hoe meer ervaring je hebt, hoe beter je dit kunt inschatten.

**OPDRACHT C** Schrijf een tekst van minimaal 200 woorden waarin je drie mogelijke vooroordelen uitlegt die in de data zouden kunnen zitten. Je kunt concluderen dat deze bias wél in je dataset zit, maar het kan ook zijn dat je een bias hebt gevonden die voor jouw dataset niet van toepassing lijkt te zijn. Laat zien hoe je dit weet.
