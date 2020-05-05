# Demo aplikacija

Aplikacija prikazuje podatke o vremenu (temperaturu, pritisak, vlaznost vazduha i jacinu vetra).
Skripta Show prikazuje te podatke, a skripte Temperature, Presure, Humidity, Wind umesto senzora na deset sekundi generisu nasumicne podatke i salju ih skripti za prikaz.
Skripta Inicijalizacija projekta kreira korisnika i loguje ga, tj dobija token za tog korisnika. Tim tokenom kreira stvari (aplikacije) i jedan kanal i povezuje ih. Ovde se koristi http protokol.
Razmena poruka ide preko mqtt protokola.

# Instalacija
Najpre instalirati mainflux kao sto je opisano u dokumentima (link na poslednjem slajdu prezentacije). Skripte pokrenuti preko Jupyter Nootebook-a.
