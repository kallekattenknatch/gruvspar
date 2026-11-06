# Gruvspår

Oberoende kunskapsbank om gruvdriftens miljöspår, historiska och aktuella mätdata, föroreningar och dokumenterade miljö- och hälsofrågor.

## Status
Pilotversion 1.9. Webbplatsen utvecklas och uppgifterna kompletteras löpande. Kontrollera alltid källhänvisningar och datastatus innan informationen används som beslutsunderlag.

## Publiceringsprinciper
- Publicera dokumenterade miljöspår, inte prospekteringsmål eller mineralresursinformation.
- Ange källa, provmatris, datum, enhet och metod när uppgifterna finns.
- Skilj mellan mätvärde, riktvärde, riskbedömning och konstaterad skada.
- Saknade data är inte noll och är inte bevis för frånvaro av risk.
- Svampprov får aldrig beskrivas som jord- eller sandprov.
- Inga annonser, betalväggar eller köpta redaktionella placeringar.

## Lokal förhandsvisning
Öppna `index.html` eller kör:
```bash
python -m http.server 8000
```
Besök sedan http://localhost:8000.

## GitHub Pages
Aktivera Pages i repository-inställningarna när webbplatsens innehåll och länkar är färdiggranskade: Settings → Pages → Deploy from a branch → main → /(root).

## Swish
Föreslaget nummer: 073-631 51 81. Mottagaridentitet och kontoinnehav ska verifieras innan betalningslänk eller QR-kod aktiveras. Visa alltid mottagarnamnet tydligt och låt givaren kontrollera det i Swish-appen.


## Ekonomisk redovisning och datatäckning
- Platsprofilerna skiljer mellan faktisk producerad malm, gråberg, metallkoncentrat, ackumulerat malmvärde och gruvspecifikt rörelseresultat.
- Malmvärde publiceras inte som totalsumma förrän metallmängder, halter/utbyte och historiska priser kan kopplas till rätt gruva och år.
- Rörelseresultat summeras endast för verifierade år och gruvspecifika redovisningsenheter. Resultat för flera gruvor tillsammans fördelas inte.
- Saneringsredovisningen skiljer mellan budget, beviljade bidrag, utbetalda medel, entreprenörsersättning och slutlig projektkostnad.
- Varje profil ska visa kunskapsluckor. Ett tomt register är inte bevis för att påverkan, undersökningar eller åtgärder saknas.
- SGU:s Bergverksstatistik 2025 används för gruvspecifika produktionsuppgifter där sådana redovisas. Nationella eller gemensamma anläggningsflöden fördelas inte mellan gruvor utan underlag.

## Integritet och redaktionellt ansvar
Utkast till stadgar, integritetspolicy och redaktionell policy måste granskas och antas av ansvarig organisation innan de presenteras som gällande dokument.

## Nationellt källregister och karta
- `data/sources/nationellt.json` samlar nationella myndighetskällor och vägvisare till miljörapporter.
- `data/sites/` innehåller separata platsregister.
- `data/sources/` innehåller källor per plats.
- Den interaktiva kartan visar ett urval dokumenterade gruvor och gruvrelaterade miljöobjekt. Urvalet är inte en komplett nationell inventering.
- Kartmarkörer är orienterande platspositioner och ska inte tolkas som gränser för förorenade områden.
- Naturvårdsverkets nationella förteckning över utvinningsavfallsanläggningar är en startpunkt för fortsatt inventering, inte bevis för att varje objekt är förorenat.

## Nationellt källregister och karta
- `data/sources/nationellt.json` samlar nationella myndighetskällor och vägvisare till miljörapporter.
- `data/sites/` innehåller separata platsregister.
- `data/sources/` innehåller källor per plats.
- Den interaktiva kartan visar ett urval dokumenterade gruvor och gruvrelaterade miljöobjekt. Urvalet är inte en komplett nationell inventering.
- Kartmarkörer är orienterande platspositioner och ska inte tolkas som gränser för förorenade områden.
- Naturvårdsverkets nationella förteckning över utvinningsavfallsanläggningar är en startpunkt för fortsatt inventering, inte bevis för att varje objekt är förorenat.
