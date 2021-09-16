# kajot-gzipper
Jednoduchá python3 utilitka pro Kajot. Zagzipuje všechny soubory v dané složce do jednotlivých souborů.

## Použití
    gzipper.py [-h] [--list] [--ndel] [--outdir outdir] zipdir

    poziční argumenty:
      zipdir           Složka, kterou bude skript gzipovat (Výchozí je root).

    volitelné argumenty:
      -h, --help        Ukáže tuhle zprávu anglicky.
      --list, -l        Vypíše zagzipované soubory (Výchozí ne).
      --ndel, -nd       Nesmaže původní soubory (Výchozí ano).
      --outdir outdir, -o outdir
                        Specifikuje výstupní složku (Výchozí je stejná jako zipdir).


## Cron

Podle požadavků by měl cron job vypadat nějak takhle:

      0 0 1 * * (which python3) /prikladova/cesta/k/gzipper.py var/log/
      
Provede se tedy ne přesně každých 30 dní, ale na začátku každého měsíce. Zagzipuje všechny soubory ve /var/log/ na místě (originály se smažou, gzipy budou ve var/log/). Pokud se nestane chyba, nedá žádný výpis.
