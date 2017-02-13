# Inledning

## Produktion och paketering
Ingredienser tillhandahålls från ett sekundärt system som garanterar att lagret alltid står till förfogande (2.3). Ingredienslagret är därmed obunden från produktionsmängden.

Varje typ av kaka tillverkas i stora mängden och fryses ner i påsar à 15 kakor per påse; à 10 påsar per låda; à 36 lådor per pall; där varje pall innehåller samma typ av kakor och där pallen plastas in med streckkod (_**är streckkoden unik?**_) (2.3).

Processen att tillverka kakorna och ladda dem på pall tar 10 minuter (2.3).

## Förvaring
Färdiglastad pall transporteras till djupfrysförvaringslokal där pallen scannas vid ankomst (2.4).

## Beställning
Orderbeställning sker telefonledes. Alla som lägger order måste vara registrerade i databasen som kund. En orderbeställning består av 10 pallar av Tango-kakor och 6 pallar av Berliners-kakor på torsdag nästa vecka. Leverans sker endast av helpallar. (2.5)

## Lastning
Pallar lastas in från djupfrysförvaringen till frysacklimatiserad lastbil där lastbilenens utrymme tar 60 pallar. Utgångsporten till kajen har scanner för att läsa av streckkoden. Lastningen till kajen måste ske i produktionsordning enligt datum. (2.6) **Med andra ord: gammalt ut först.** Laddningstiden för en pall är på ungefär 1 minut (2.6). När lastbilen är lastad, erhåller föraren kundernas namn, adress samt pallarnas nummer som är kopplad till kund (2.6).

En lastbil kan ha pallar som ska levereras till olika kunder. Antalet kunder kan utöka drastiskt inom snar framtid och verksamheten kommer utökas till att omfatta hela Skandinavien! (_**Varför skriver man det? Är det att man ska tänka ett steg längre och designa databasen för att stödja en sådan utökning?**_) (2.6).

Systemet ska utökas i framtiden till att koppla leveranssystemet till företagets egna faktureringssystem (2.6).

## Kvalitetskontroll
Företaget gör stickprov på sina produkter. Om en viss produkt inte uppnår kraven måste dessa kvalitetsstoppas. Pallar som har producerats under den givna tidspektra måste därför kunna säljstoppas och får inte levereras till kund.	

## Ur Appendix C: Produktion, förvaring och leverans
```
Produktion: Tillverkning –> Frysning –> Påspaketering –> Lådpaketering –> Lastning på pall –>
Förvarning: –> {scanning} –> Djupfrysförvaringslokal med streckkodläsare –>
Leverans: –> {scanning} -> Kajramp för pålastning –> Frysacklimatiserad lastbil –> Förare erhåller kunduppgifter
```
