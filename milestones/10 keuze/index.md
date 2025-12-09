# Milestone 1: dataset, vraagstelling, kwaliteit

In verscheidene masters (onder andere Data Science) wordt gevraagd onderzoek te doen aan de hand van bestaande datasets. Ook in de praktijk van het bedrijfsleven zijn grote datasets van groot belang:

- Albert Heijn gebruikt de middels de bonuskaart verzamelde verkoopgegevens om hun voorraadbeheer te optimaliseren, agrarische bedrijven minimaliseren hun stikstofuitstoot met behulp van sensordata uit hun stallen en applicaties die gebruik maken van Large Language models en die getraind zijn op grote datasets (zoals ChatGPT) zijn niet meer weg te denken uit onze samenleving.

- Zelfrijdende auto's zouden niet mogelijk zonder de analyse van grote hoeveelheden data, een wereld zonder Google Maps is niet meer voor te stellen en de weersverwachting ontleent haar betrouwbaarheid aan grote hoeveelheden (historische) klimaatdata.

- Zelfs de (semi-)overheid maakt graag gebruik van grote datasets voor 'crowd control' bij grote evenementen, het motiveren en bijsturen van overheidsbeleid en het maken van een flexibele stedenbouwkundige planning. In brievenbussen en ondergrondse vuilcontainers zitten bijvoorbeeld sensoren die bijhouden of ze vol zitten, in de weg zitten sensoren die meten hoeveel verkeer er gebruik van maakt en de kwaliteit van het rioolwater is zorgvuldig in kaart gebracht omdat daarmee uitbraken van ziektes zoals Corona kunnen worden gevolgd.

Dat dat niet altijd goed gaat is bekend door de toeslagenaffaire, maar ook door de vergaande smart cities in China, waar gezichtsherkenning wordt ingezet op manieren die in het "vrije Westen" ondenkbaar zouden zijn of door het feit dat veel medische modellen gebaseerd zijn op de lichamen van (blanke) mannen. Een goed begrip van de gebruikte dataset is daarom essentieel voor het beantwoorden van een onderzoeksvraag met die data.

Het in kaart brengen van een dataset wordt ook  wel Exploratory Data Analysis (EDA) genoemd. Een EDA omvat een cijfermatige analyse van de dataset (denk aan de distributie of de centrummaten), maar ook een ethische analyse (zit er bias in de data? hoe verhoudt de data zich tot je onderzoekspopulatie?) en een haalbaarheidsanalyse (is de dataset compleet genoeg? Wordt de dataset sterker als die wordt gecombineerd met andere datasets?). Tenslotte geef je in een EDA vast een voorlopig antwoord op je onderzoeksvraag (niet op basis van onderzoek, maar op basis van je eigen indruk van de data).

In dit project ga je de belangrijkste stappen van een EDA doorlopen.

## Keuze dataset

Het internet staat vol met datasets, vaak direct toegankelijk, soms via een zogenaamde Application Programming Interface. Dat laatste  betekent dat de betreffende data alleen via software opgevraagd kan worden; hiervoor moet je dus een stukje (Python-)code schrijven, maar vaak is de code kant-en-klaar op internet te vinden. Sommige datasets kun je gewoon zo downloaden.

Welke dataset je gebruikt wordt alleen beperkt door jouw verbeelding: levert een gerichte zoekactie (bijvoorbeeld naar datasets van het CBS, aandelenkoersen, sportuitslagen of Twitter/X-berichten) niets op, maak dan gebruik van gespecialiseerde zoekmachines zoals kaggle.com, research.google.com of dateno.io.

Let op: je zult gedurende dit vak met deze dataset werken en ruilen van dataset is niet toegestaan (tenzij om dringende redenen, dit ter beoordeling van de docent die je begeleidt). Kies dus zorgvuldig!

**Opdracht 1a** --- Omschrijf in minimaal 500 woorden waarom je deze dataset gekozen hebt, waar je die gevonden hebt en hoe de data in elkaar zit (zonder daarbij in te gaan op de inhoud van de data). Wat zijn de belangrijkste kolommen in de dataset? Hoe groot is de dataset (met andere woorden: hoeveel rijen zijn er)? Hoe compleet is de dataset (hoeveel missing values zijn er? En misschien wel de belangrijkste vraag: is bij het samenstellen van de dataset een sampling-methode gebruikt en zoja: welke?

Dit zijn heel veel vragen, die expres niet mooi geordend zijn. Jij moet dit netjes ordenen in je notebook, zodat je alle vragen overzichtelijk en in een logische structuur beantwoordt.

Als onderdeel van deze vraag moet je de dataset inladen in je Notebook met hulp van Pandas. Zorg dat er een cel is waar je de dataset inlaadt in een dataframe. Vraag aan het eind van de cel de "head" (eerste paar regels) van de dataset op zodat deze wordt getoond (`df.head()`).

## Onderzoeksvraag

Normaal bepaal je eerst je onderzoeksvraag en zoek je daar een geschikte dataset bij, maar vanwege de beperkte tijd doen we het in dit vak andersom. Zorg dat je onderzoeksvraag relevant is en niet te groot. De vraag moet natuurlijk opgelost kunnen worden met data-analyse, en niet een groot onderzoek waarbij je ook nog mensen moet interviewen, eindeloos papers lezen, enzovoort.

**Opdracht 1b** Geef in minimaal 250 woorden een onderzoeksvraag die met de gekozen dataset te beantwoorden is. Schets kort een onderzoek waarmee de onderzoeksvraag te beantwoorden is. Let op, je hoeft het betreffende onderzoek mogelijk niet volledig uit te voeren, maar de onderzoeksvraag moet wel met de dataset te beantwoorden zijn. Motiveer dat de betreffende onderzoeksvraag maatschappelijk en/of wetenschappelijk relevant is (en gewoon: wat jij interessant vindt en graag wil begrijpen).

## Kwaliteit

De kwaliteit van een dataset bepaalt voor een groot deel de validiteit van het onderzoek dat aan de hand van die dataset wordt gedaan, de zogenaamde Data Quality Assessment (DQA). Helaas is er geen standaard definitie van de kwaliteitseisen die aan data kunnen en mogen worden gesteld. In de op het college uitgedeelde hand-out worden enkele begrippen uitgelegd die vaak in verband met DQA worden genoemd.

**Opdracht 1c** Behandel in minstens 500 woorden minimaal vijf kwaliteitseisen die in de hand-out worden genoemd en beschrijf *hoe* de door jou gekozen dataset daar al dan niet aan voldoet.
