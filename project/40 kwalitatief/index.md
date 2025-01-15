# Analyse kwalitatief

Als je interviews hebt gedaan, of een face-to-face enquete, dan moet je de audio van elke deelnemer opnemen en deze uitwerken.

De eerste stap is om een nette representatie van de gesproken tekst te krijgen. Hierbij moet duidelijk zijn hoe het interview is verlopen: wie zei wat en wanneer.

Daarna ga je analyseren.

## Stap 1. Audio organiseren

Zorg dat je alle audiobestanden netjes op een rij hebt op één computer. Je kunt ze ook delen met elkaar via Dropbox of een andere dienst. Dan kan iedereen er makkelijk bij.

## Stap 2. Transcriberen (uitschrijven)

Je gaat nu alle interviews uitschrijven. We gaan dat eerst zoveel mogelijk met AI-tools doen.
Ga naar <https://huggingface.co/spaces/Xenova/whisper-speaker-diarization> voor een demo waarin met een AI-model een interview uitgeschreven kan worden.

Dit model is speciaal geschikt voor "diarization" ofwel het herkennen van de verschillende sprekers en dit bij het uitschrijven ook vermelden.

- Sleep een audiofile naar de pagina
- Klik "Load model"
- Kies als taal Dutch/Flemish (belangrijk!)
- En dan "Run model"

Dit kan een behoorlijke tijd duren. Zorg dat de computer aan blijft staan, anders pauzeert het verwerken ook! Aan het CPU-gebruik kun je zien dat het nog werkt. Na een tijdje krijg je een uitwerking (transcript) te zien. Het valt waarschijnlijk op dat er best wat fouten in zitten. We vermoeden dat de modellen nog niet voldoende getraind zijn met Nederlandse audio.

Klik nu "Download transcript" om een JSON-bestand te downloaden. Doe dit voor alle audio-bestanden en geef de transcripts logische namen.

Download nu een [Python-programmaatje om de JSON om te zetten naar een tekst-uitwerking](trans.py). Je ziet dat onderaan het programma staat dat de inputfile `transcript.json` moet heten en de output-file is dan `transcript.txt`. Pas dit steeds aan voordat je het programma runt!

Dit is dus best wel wat handwerk, en dat is wat erbij hoort voor dit soort onderzoek. Het zijn stappen die je maar één keer hoeft te doen per interview.

## Stap 3. Corrigeren

De uitgeschreven interview bevatten nog veel fouten. Deze moeten met de hand worden gecorrigeerd. Hiervoor moet je het audiobestand luisteren en fouten aanpassen in de tekst. Zorg dus dat je de audiofile makkelijk kunt pauzeren om even te tikken (bv. op Mac open je ze in Quicktime Player en dan kun je met de pauzeknop op je toetsenbord werken).

Verdeel dit werk over het team.

Hieronder vind je een fragment uit een voorbeeld-interview. Het is een onderzoek dat gaat over gebruik van media voor het volgen van politieke ontwikkelingen. Je ziet dat de tekst is opgedeeld in segmenten, waar steeds wordt gemarkeerd wie wat zegt (interviewer I of deelnemer D3). Het is een gesprek met "deelnemer 3".

    I: Dat is interessant. Gebruik je ook andere bronnen, zoals nieuwswebsites of
    televisie, om je op de hoogte te houden?

    D3: Niet echt. Ik kijk bijna geen tv en nieuwswebsites vind ik vaak te saai of te
    moeilijk. Als ik iets belangrijks wil weten, zoek ik het op via Instagram of TikTok, waar
    anderen het al hebben samengevat.

    I: Je noemde net dat je onderwerpen belangrijk vindt die direct impact hebben op je
    leven. Kun je daar een voorbeeld van geven?

    D3: Ja, bijvoorbeeld klimaatprotesten. Ik zag dat een tijdje geleden jongeren op straat
    kwamen om meer actie te eisen van de regering. Dat vond ik echt iets waar ik over wilde weten,
    omdat ik me zorgen maak over hoe de aarde eruitziet als ik ouder ben.

Zo moeten jullie uitwerkingen er ook uitzien.

## Stap 4. Coderen van uitspraken

Bij het coderen ga je stukken tekst selecteren die relevant zijn voor je vraag. In overleg met je begeleider zijn er **drie categorieën gekozen** die jullie moeten coderen (vraag je begeleider!!). In het voorbeeld hieronder zie je een uitgewerkt.

- voorbeeldcategorie: Redenen om medium wel/niet te gebruiken
    - D3: "nieuwswebsites vind ik vaak te saai of te moeilijk"

Opmerking: hier wordt vrij letterlijk een reden genoemd waarom websites niet worden gebruikt voor het volgen van nieuws. Dat stukje selecteren we als fragment voor deze categorie. D3 vermelden we erbij voor het terugzoeken.

- voorbeeldcategorie: Redenen om nieuws te volgen
    - D3: "Ja, bijvoorbeeld klimaatprotesten. Ik zag dat een tijdje geleden jongeren op straat
    kwamen om meer actie te eisen van de regering. Dat vond ik echt iets waar ik over wilde weten,
    omdat ik me zorgen maak over hoe de aarde eruitziet als ik ouder ben."

Opmerking: deze hele tekst is een voorbeeld van een reden om nieuws te volgen. De laatste zin van het fragment is het meest relevant, maar het stuk ervoor geeft belangrijke context en nemen we daarom mee voor het coderen.

## Stap 5. Thema's vinden

Als we alle uitspraken in alle data hebben gevonden die te maken hebben met de categorieën, ga je deze per stuk verwerken. Als voorbeeld nemen we de categorie "Redenen om medium wel/niet te gebruiken". We gaan op een kwalitatieve manier thema's zoeken, net als je hebt gedaan tijdens het eerste college.

Zorg dat niets hiervan zelf verzonnen is. Alle ideeën uit de structuur moeten herleidbaar zijn naar een of meer uitspraken van deelnemers.

Een voorbeelduitwerking kan de volgende zijn. Let op dat we hier **niet het medium noemen**. Dit is dus een lijst van algemene redenen.

- Redenen om medium **wel** te gebruiken:

    1.  Toegankelijkheid: Het medium is makkelijk te bereiken, bijvoorbeeld via apps die jongeren al dagelijks gebruiken.
    2.  Taalgebruik: Het gebruik van eenvoudige of informele taal maakt de inhoud begrijpelijker.
    3.  Visuele ondersteuning: Korte video’s, infographics, of memes maken het onderwerp aantrekkelijker en makkelijker te volgen.
    4.  Snelle updates: Platforms zoals sociale media bieden actuele informatie over politieke ontwikkelingen.
    5.  Persoonlijke relevantie: Het medium biedt inhoud die aansluit bij de interesses of zorgen van de gebruiker (bijvoorbeeld klimaatverandering).
    6.  Interactiviteit: Mogelijkheid om te reageren, stemmen, of mee te discussiëren over onderwerpen.
    7.  Sociale druk: Vrienden of influencers delen content, waardoor de gebruiker zich betrokken voelt.
    8.  Entertainment-waarde: Politiek gepresenteerd op een informele, humoristische manier die uitnodigt tot verder kijken of lezen.

- Redenen om medium **niet** te gebruiken:

    1.  Complexiteit: Te veel jargon of ingewikkelde termen maken het moeilijk om de inhoud te begrijpen.
    2.  Langdradigheid: Lange artikelen of video’s voelen tijdrovend en onaantrekkelijk aan.
    3.  Betrouwbaarheid: Gebrek aan vertrouwen in de bron of zorgen over nepnieuws.
    4.  Relevantie: Het medium richt zich niet op onderwerpen die belangrijk worden gevonden door de gebruiker.
    5.  Negativiteit: Te veel negativiteit of polarisatie schrikt af.
    6.  Gebrek aan visuele aantrekkelijkheid: Veel tekst zonder visuele ondersteuning kan saai of overweldigend overkomen.
    7.  Drukte: Overweldigende hoeveelheid informatie of notificaties maakt het moeilijk om gefocust te blijven.
    8.  Traditionele uitstraling: Het medium voelt ouderwets aan (bijvoorbeeld traditionele nieuwsuitzendingen op televisie).
    9.  Gebrek aan interactie: Geen mogelijkheid om zelf vragen te stellen of te reageren.
    10. Overload aan inhoud: Te veel onderwerpen tegelijk zonder duidelijke focus op wat relevant is.

Een andere uitwerking kan er zo uitzien (een deel). Hier zie je dat we het belangrijk vonden om het medium wel te noemen. Dit kan relevant zijn voor beantwoording van de onderzoeksvraag.

- Krant (Papieren of digitaal)
    - Redenen om wél te gebruiken:
        1. Gedetailleerde en uitgebreide achtergrondinformatie.
        2. Diepgang in analyses en opiniestukken.
        3. Mogelijkheid om offline te lezen zonder afleiding.

    - Redenen om níét te gebruiken:
        1. Langere leestijd wordt als tijdrovend ervaren.
        2. Formele en complexe schrijfstijl kan jongeren afschrikken.
        3. Minder interactie of visuele ondersteuning zoals video’s.

- Instagram

    - Redenen om wél te gebruiken:
        1. Politieke content wordt gepresenteerd via aantrekkelijke visuele posts.
        2. Stories en Reels bieden snelle updates in een creatieve vorm.
        3. Mogelijkheid om accounts te volgen die aansluiten bij persoonlijke interesses.

    - Redenen om níét te gebruiken:
        1. Moeilijk om diepgaande informatie te vinden via dit medium.
        2. Veel content is gefilterd of oppervlakkig.
        3. Politieke boodschappen kunnen worden overstemd door commerciële of lifestyle-content.
