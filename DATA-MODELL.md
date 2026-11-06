# Gruvspårs datamodell

Detta register är gemensamt för alla platser. Varje sakuppgift lagras som en separat post och länkas till en eller flera källor.

## Grundregler
- Ett prov är alltid kopplat till sitt faktiska provmaterial. Svampresultat får aldrig registreras som jord-, sand- eller vattenresultat.
- Resultat, jämförelsevärde och riskbedömning är tre olika saker.
- En jämförelse kräver att material, enhet, användning och relevant population framgår.
- Planerad, beslutad, påbörjad, slutförd och verifierad åtgärd är skilda statusar.
- Saknad uppgift betyder endast att uppgiften saknas i Gruvspårs register.
- Varje post ska ha källa och evidensstatus. Användaruppgifter märks som obekräftade tills originalunderlag har granskats.
- Inga mineralresurser, prospekteringsmål eller uppgifter som hjälper till att hitta nya fyndigheter lagras eller publiceras.

## Filstruktur
- `schemas/record.schema.json`: valideringsregler för registerposter.
- `data/sites/garpenberg.json`: Garpenbergs platsregister.
- `data/sources/garpenberg.json`: källförteckning för Garpenberg.

## Evidensstatus
- `primary_source_verified`: originalrapport, beslut eller primärkälla granskad.
- `secondary_source`: uppgiften bygger på en identifierad andrahandskälla.
- `user_provided_unverified`: uppgift lämnad av användare, originalunderlag ännu inte granskat.
- `editorial_assessment`: Gruvspårs egen tydligt märkt sammanställning eller tolkning.
- `unknown`: status kan inte fastställas.

## Provresultat
Registrera minst provmaterial, provdatum, provpunkt, ämne, resultat, enhet och källa när uppgifterna finns. Ange även provberedning, exempelvis om svamp var tvättad och om resultatet avser färsk eller torr vikt. Blanda aldrig jämförelsevärden med laboratorieresultat.

## Garpenberg
Garpenberg är första fördjupade fallstudien. Uppgifter från tidigare samtal ska inte publiceras som verifierade analysresultat innan rapporter och provuppgifter har granskats.

## Perspektiv och redaktionell hållning

Gruvspår granskar gruvdriftens miljöpåverkan och hur företag och myndigheter hanterar den. Naturens, människors och ekosystemens långsiktiga skydd är utgångspunkten för vilka frågor som ställs och följs upp.

Detta innebär inte att slutsatser får bestämmas i förväg. Sakuppgifter ska vara spårbara och bedömningar ska stå i proportion till underlaget. Gruvspår ska:
- redovisa dokumenterad påverkan, utsläpp, föroreningar och miljörisker utan att tona ned dem,
- granska verksamhetsutövares ansvar, åtaganden och faktiska åtgärder,
- granska myndigheters beslut, tillsyn och uppföljning,
- redovisa osäkerheter, motstridiga uppgifter och kunskapsluckor öppet,
- även redovisa verifierade miljöförbättringar och åtgärder som fungerat,
- skilja mellan fakta, källors påståenden, myndighetsbedömningar och Gruvspårs egna analyser.

Gruvspår är inte neutralt inför miljöförstöring. Däremot ska metoderna vara sakliga, öppna och konsekventa. Ingen aktör ska dömas på förhand och ingen dokumenterad påverkan ska döljas.

## Privata laboratorierapporter och andra icke-offentliga underlag

En rapport behöver inte vara sökbar på internet för att kunna ligga till grund för en redovisning. Om en rapport har lämnats direkt till Gruvspår ska källan registreras som privat tillhandahållen, inte som en offentlig webblänk.

- Originalrapporten ska inte läggas i det publika GitHub-repot eller på webbplatsen utan uttryckligt godkännande från den som har rätt att dela den.
- Offentliga poster får återge relevanta analysuppgifter när rapporten har granskats och publicering är lämplig.
- Källhänvisningen ska då ange exempelvis: "Laboratorierapport, privat tillhandahållen till Gruvspår, ej offentligt tillgänglig". Ange laboratorium, rapportdatum och rapport-ID endast när dessa uppgifter får publiceras.
- Markera om rapporten har granskats av Gruvspår. En uppgift som återberättats muntligt eller i text men där rapporten inte har granskats ska fortsatt märkas `user_provided_unverified`.
- Publicera inte namn, kontaktuppgifter, kundnummer, provbeställaruppgifter eller andra person- och sekretesskänsliga detaljer.
- Om rapporten inte får citeras eller återges ska den endast användas som privat bakgrund, i enlighet med villkoren för utlämnandet.

Avsaknad av offentlig länk är alltså inte samma sak som avsaknad av källa. Källans åtkomststatus och granskningsstatus ska redovisas var för sig.

## Avgränsning av journalistiskt beställda analyser

Analyser som utförts inom SR:s journalistiska undersökning på reporterns begäran ska inte registreras, återges, citeras eller användas som underlag i Gruvspår. De tillhör det separata journalistiska arbetet.

Detta undantag gäller endast dessa specifika analyser. Andra analyser från laboratorier, myndigheter, universitet, forskare, verksamhetsutövare eller andra identifierbara källor får ingå när källan, provmaterialet, metoden och eventuella begränsningar redovisas. En analys behöver inte vara publicerad på internet för att kunna registreras, men åtkomst- och granskningsstatus ska framgå.

