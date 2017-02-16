# Inledning

## Om företaget

### Produktion och paketering
Ingredienser tillhandahålls från ett sekundärt system som garanterar att lagret alltid står till förfogande (2.3). Ingredienslagret är därmed obunden från produktionsmängden.

Varje typ av kaka tillverkas i stora mängden och fryses ner i påsar à 15 kakor per påse; à 10 påsar per låda; à 36 lådor per pall; där varje pall innehåller samma typ av kakor och där pallen plastas in med en unik streckkod (2.3).

Processen att tillverka kakorna och ladda dem på pall tar 10 minuter (2.3).

### Förvaring
Färdiglastad pall transporteras till djupfrysförvaringslokal där pallen scannas vid ankomst (2.4).

### Beställning
Orderbeställning sker telefonledes. Alla som lägger order måste vara registrerade i databasen som kund. En orderbeställning består av 10 pallar av Tango-kakor och 6 pallar av Berliners-kakor på torsdag nästa vecka. Leverans sker endast av helpallar. (2.5)

### Lastning
Pallar lastas in från djupfrysförvaringen till frysacklimatiserad lastbil där lastbilenens utrymme tar 60 pallar. Utgångsporten till kajen har scanner för att läsa av streckkoden. Lastningen till kajen måste ske i produktionsordning enligt datum. (2.6) **Med andra ord: gammalt ut först.** Laddningstiden för en pall är på ungefär 1 minut (2.6). När lastbilen är lastad, erhåller föraren kundernas namn, adress samt pallarnas nummer som är kopplad till kund (2.6).

En lastbil kan ha pallar som ska levereras till olika kunder. Antalet kunder kan utöka drastiskt inom snar framtid och verksamheten kommer utökas till att omfatta hela Skandinavien! (_**Varför skriver man det? Är det att man ska tänka ett steg längre och designa databasen för att stödja en sådan utökning?**_) (2.6).

Systemet ska utökas i framtiden till att koppla leveranssystemet till företagets egna faktureringssystem (2.6).

### Kvalitetskontroll
Företaget gör stickprov på sina produkter. Om en viss produkt inte uppnår kraven måste dessa kvalitetsstoppas. Pallar som har producerats under den givna tidspektra måste därför kunna säljstoppas och får inte levereras till kund (2.7).

## Krav

### Produkt
En pall anses vara producerad när den blir inscannad vid ingången till djupfrysförvaringen (3.1).
Pallens unika nummer, produktnamn samt datum och tid då denna producerades (3.1).
Man måste alltid kunna se hur många pallar av en viss produkt som har blivit producerade ungen en given tid och datum (3.1).

### Material
När en pall produceras, måste materialdepån uppdateras (3.2).
Måste måste kunna se hur mycket det finns att tillgå av respektive ingrediens, samt se när och hurmycket av ingrediensen som har levererats (3.2).

### Recept
Ett interface krevs för att kunna se recepten samt uppdatera dem (3.3). Recepten ändras inte under production (3.3).

### Producerade pallar
Se rubrien "*Kvalitetskrav*". En order om att blockera en pall kommer alltid att ske innan pallen har levererats (3.4).
Man måste kunna spåra pallen genom dess unika nummer, för att få information om: dess innehåll, om pallen har levererats, och i sådant fall till vem (3.4).
Därtill behöver man även kunna ta fram vilken pall som innehåller en blockerad produkt (3.4).
Sedan behövs även kunna ta fram vilka pallar som har levererats till en specifik kund; dess leveransdatum och -tid (3.4).

### Beställning
En order behöver bli registrerad i databasen och man ska kunna ta fram ordrar som ska skickas en viss specifik tidperiod (3.5).

### Leverans
Innan produkten går från djupfrysförvaringen till den frysacklimatiserade lastbilen, ska en lastningsorder skapas (3.6). Den skapas när pallen skannas in vid kajmottagning och order erhålls av föraren efter slutförd pålastning (3.6).
Lastningsordern innehåller: kundinformation samt antalet pallar som ska levereras (3.6).
Lastningsordern som föraren får innehåller även fält för signering av kund och ordern måste sparas i databasen (3.6).
När en lastningsorder skrivs ut, ska den innehålla data om levererade pallar, kunduppgifter och leveransdatum (3.6).

## Förstudie
 * **Saknas:** Scanningsutrustning av streckkod.
    * **Lösning:** Mata in koden förhand i ett gränsnitt, där palltillverkningssimuleringer sker (4).
    * **Notering:** Denna funktion kommer tas bort i produkt (4).
 * **Olika programversioner:** Olika delar av företaget kommer använda olika delar av systemet och därför ska dessa grännsnit isoleras (4).
    * Ett program som hanterar allt som har med råmaterial och recept att göra (4).
    * Ett program som hanterar allt med produktion, kvalitetsspärr samt pallsökning. Här kommer man implementera även första punkten med palltillverkningssimuleringen (4).
    * Ett program som hanterar ordrar och leverans (4).
 * Vid visning för kund ska databasen innehålla en demo-information, så att man kan visa kunden programmets funktionalitet (4).

## Inläming
 * Första inläming sker av databasmodelen (5).
 * Andra inlämning sker av slutrapport och det utvecklade KST-programmet (5).

## Ur Appendix C: Produktion, förvaring och leverans
```
Produktion: Tillverkning –> Frysning –> Påspaketering –> Lådpaketering –> Lastning på pall –>
Förvarning: –> {scanning} –> Djupfrysförvaringslokal med streckkodläsare –>
Leverans: –> {scanning} -> Kajramp för pålastning –> Frysacklimatiserad lastbil –> Förare erhåller kunduppgifter
```
