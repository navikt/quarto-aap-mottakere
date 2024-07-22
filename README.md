# quarto-aap-mottakere
Datafortelling i Quarto for offentlig statistikk på mottakere av arbeidsavklaringspenger (AAP)

## Idé

Hente data fra BQ og replikere det som ligger på [nav.no om AAP-statistikk](https://www.nav.no/no/nav-og-samfunn/statistikk/aap-nedsatt-arbeidsevne-og-uforetrygd-statistikk/arbeidsavklaringspenger), bare gjøre det bedre.

Forbedringsliste:

- automatisk oppdatert hver måned
- dropdown for å velge periode, som defaulter til siste 12mnd eller i år
- først bare tabeller med last-ned-knapp, deretter legge til grafer

## Data

Data skal være fra tabeller med offentlig statistikk. Hvis vi legger det rett på BQ kan det aksesseres uten innlogging, verken i BQ eller Oracle. Dataflyten blir da:

1. lage dataene i skjema med dbt (feks **dvh_aap**)
2. overføre aggregat til **dvh_arb_stonad** 
    - kan droppe hvis vi ikke trenger å endre kolonnenavn
    - fint for å samle aggregatene, men strengt tatt ikke helt nødvendig
3. overføre data fra **dvh_arb_stonad** til BQ, som åpne data
    - eventuelt rett fra feks **dvh_aap** til BQ, men da er det ikke samlet på ett sted før BQ
4. lage Quarto