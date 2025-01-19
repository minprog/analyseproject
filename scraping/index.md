# Scraping

HTML is de taal waarin webpagina's zijn geschreven. In de basis gaat het om een tekstbestand. Met **tags** wordt de structuur expliciet aangegeven. Het volgende is een HTML-fragment (dus geen complete webpagina):

    <div class="infobox">
      <h2>Our address</h2>
      <p>
        Dalsteindreef 3002<br>
        1112 XC Diemen
      </p>
    </div>

Dit kan zomaar op een webpagina staan. Elke webbrowser heeft standaardregels ingebouwd om HTML "netjes" weer te geven. Een `<h2>` markeert een kopje van de 2e categorie. Een `<p>` is een paragraaf in de tekst, en een `<br>` markeert het einde van een regel.
HTML is dus bedoeld om _geautomatiseerd_ om te zetten in een visuele weergave, bedoeld voor mensen om te lezen. En niet alleen visueel, browsers zorgen ook voor een goede weergave voor mensen die tekst op een beeldscherm niet goed kunnen lezen, bijvoorbeeld met audio. Dit werk wordt allemaal overgenomen door de webbrowser, als de HTML maar op een logische manier ingedeeld is.

## Scraping

En nu komt het: omdat de informatie op de meeste websites op deze manier in HTML gecodeerd is, kun je ook geautomatiseerd informatie van websites afhalen. Zo kun je een database bouwen van informatie van bijvoorbeeld Wikipedia, de Tweede Kamer, of elke andere website waar veel informatie wordt gepubliceerd die interessant kan zijn om te analyseren.

Het uit HTML filteren van interessante informatie heet _scraping_.

Eén typisch voorbeeld is het scrapen van prijsinformatie van een verkoopwebsite, zodat deze kan weergegeven op een website die informatie van allerlei verkopers bij elkaar wil plaatsen. Winkels willen hun data enerzijds liever niet afstaan, maar tegelijk willen ze hun prijzen wel publiceren voor consumenten. Daarom is zulke informatie vaak wel te scrapen.

Je kunt scraping ook gebruiken voor bijvoorbeeld dataverzameling voor onderzoek. Als je wil onderzoeken hoe informatie wordt geformuleerd op een bepaalde website, of je hebt informatie nodig van, bijvoorbeeld, alle medewerkers van de UvA, dan kun je daar scraping voor inzetten.

## Selecteren met CSS

Nu is HTML van zichzelf goed gestructureerd, maar bouwers van websites houden meestal geen rekening met scraping, en zijn tevreden als de website er goed uitziet op mobiel. Nog sterker, vaak willen ze liever niet dat er gescrapet wordt. Ook is HTML ook weer niet zó gestructureerd. Een enkele HTML-pagina kan een heleboel `<h2>`-kopjes hebben, dus hoe weet je welke je moet hebben?

Hiervoor gebruiken we onder andere CSS, waarmee je op een compact manier regels kunt formuleren zoals:

- Geef me de inhoud van de tweede H2 van de webpagina
- Geef me de hele DIV die als class "infobox" heeft
- Geef me de inhoud van elke P op de pagina
- Geef me de inhoud van elke LI uit de tweede UL

In deze module leer je de basis-structuur van HTML (makkelijk) en de manier waarop je met CSS specifieke onderdelen van een pagina kunt selecteren (wat moeilijker).

## Oefenen

1. Bekijk de [short over HTML](https://cs50.harvard.edu/x/2024/shorts/html/) om te leren hoe de structuur van een HTML-document werkt en welke tags er zoal zijn en hoe ze gecombineerd kunnen worden.

1. En bekijk de [short over CSS](https://cs50.harvard.edu/x/2024/shorts/css/) om te leren hoe je met CSS specifieke delen van een HTML-document kunt selecteren.

1. Ga naar [deze website om extra te oefenen](https://flukeout.github.io/) om te oefenen. Zorg dat je de belangrijkste CSS-selectors kent. Let op: in de balk aan de rechterkant staat uitleg!

    - Tip: in de oefening worden speciale HTML-elementen gebruikt zoals `<bento>`. Deze bestaan normaal niet, maar de CSS werkt exact op dezelfde manier als bijvoorbeeld bij `<h1>`.

1. Ga dan naar de [MDN-pagina over selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors/Selectors_Tasks) om nog meer te oefenen. Klik bij de opdrachten op "Play" om naar een editor te gaat waar je live de opdracht kunt uittesten.
