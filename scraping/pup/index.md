# Werken met Pup

## Installatie

Voor Windows:

- [Installeer Git for Windows](https://gitforwindows.org)
- Maak een nieuwe map voor de scraping-opdrachten
- [Download de Pup-tool](https://github.com/ericchiang/pup/releases/download/v0.4.0/pup_v0.4.0_windows_amd64.zip) en zet `pup.exe` in die map
- Ga naar de Verkenner/Explorer, klik rechts op die map en open in Git Bash

Voor Mac:

- Ga naar de Terminal
- Probeer `brew install pup`
- Als je daarna `pup -h` tikt en je krijgt wat uitleg te zien en version 0.4.0, dan zit je goed.
- Maak een nieuwe map voor de scraping-opdrachten
- Open de Terminal in die map door de map naar het Terminal-icon in de dock te slepen

## Uitzoekwerk

Lees de [README](https://github.com/EricChiang/pup) van de tool `pup`. Met deze tool kun je informatie "scrapen" uit HTML-pagina's. HTML-pagina's bevatten bijvoorbeeld interessante informatie zoals de prijs van een product, of beurskoersen, of het laatste bedrijfsnieuws. Door te "scrapen" filteren we deze relevante informatie uit HTML-pagina's. Deze informatie kun je laten zien in je terminal, maar je kunt dit ook gebruiken voor bijvoorbeeld dataverzameling voor onderzoek.

Scraping met `pup` gaat op basis van de selectors die ook in CSS gebruikt worden. Hiermee kun je aangeven welk deel van de HTML je wilt hebben. Op de gelinkte GitHub-pagina van `pup` staat ook een lijstje van de ondersteunde CSS-selectors in deze tool.

## Gebruik van pup

Zorg dat je een html-bestand in de map hebt staan om mee te testen. Download bijvoorbeeld [War and Peace](https://www.pythonscraping.com/pages/warandpeace.html) (rechtsklik en download).

Geef dan het volgende commando om `pup` te testen.

- **Windows**

        cat warandpeace.html | ./pup -c 'h1 text{}'

- **Mac**

        cat warandpeace.html | pup -c 'h1 text{}'

Dit zou de inhoud van de eerste `h1`-tag moeten geven, en dat is "War and Peace".

## Opdrachten

Dit zijn uitzoekopdrachten. Bestudeer eerst zelf de webpagina in je browser, bekijk dan de html en vorm een idee van wat de oplossing kan zijn. Dan uitproberen tot het werkt.

Geef als oplossing de complete pup-commando's onder elkaar in één tekstbestand (platte tekst, geen doc of pdf). Zet onder elk commando de output die het geeft (maximaal 10 regels hiervan).

1.  Zoek uit hoe je alle `span`s met de class `green` kunt scrapen van de pagina <https://www.pythonscraping.com/pages/warandpeace.html>.

1.  Zoek uit hoe je <u>alleen de tekst</u> van bovenstaande `span`s kunt scrapen.

1.  Zoek uit met welk commando je alle URL's (links) naar het laatste nieuws van de NOS kunt scrapen. Gebruik hiervoor de pagina <https://nos.nl/nieuws/laatste> (download html [hier](nos.html)).

    - Tip: ga naar de [Inspector](https://developer.chrome.com/docs/devtools/open) in je webbrowser om te achterhalen waar in de HTML de informatie te vinden is.

1.  Zoek uit hoe je alle headlines kunt scrapen, dus de koppen van het nieuws.

1.  Zoek uit hoe je een korte omschrijving van het weer kunt printen vanuit de website van Weeronline (download html [hier](weer.html)).

1.  Zoek uit hoe je alle `tr` elementen uit de tabel op <https://pythonscraping.com/pages/page3.html> kunt scrapen, maar met uitzondering van het eerste `tr`-element (deze bevat de tabelkopjes en die hebben we niet nodig). In de README van Pup staan de selectors die je kunt gebruiken. Volg de link naar MDN om uit te zoeken hoe ze werken.
