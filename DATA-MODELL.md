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