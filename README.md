
# Rraspberry Pi 3g connector

Prosty programik do automatycznego łączenia i wznawiania połączenia z siecią 3g


### Modem
Huawei  E1750

### Skrypt do ręcznego łączenia z siecią 3g 
[Sakis3g](http://www.sakis3g.com/)

## Umiejscowienie programu na dysku
Najlepiej ściągnąć całe repozytorium do folderu "Rpi3gConnector", a ten folder wrzucić do "/home/pi"
```
	/home/pi/Rpi3gConnector
```
Inne ustawienie folderów uniemożliwi poprawne działanie

## Kilka słów o programie

Program napisany w Python`ie. Program sprawdza czy jest aktywne połączenie pingując stronę www. Jeśli odpowiedz jest pozytywna, program przechodzi w stan uśpienia na pewnie czas. Po upływie czasu program znowu odpytuje serwer czy jest on dla niego dostępny. Jeśli w tym czasie połączenie zostało zerwane, program podejmuję próbę ponownego połączenia, jeśli się uda, przechodzi w stan uśpienia, jeśli nie, próbuje ponownie się połączyć i tak w kółko. 

## Uruchomienie
Program można uruchomić ręcznie poprzez wydanie polecenia (w katalogu programu)

```sh
    sudo python connect3g.py
```

## Dodanie programu do automatycznego uruchomienia
Program może uruchamiać się automatycznie ze startem systemy, i działać aż do jego wyłączenia (odbywa się to w tle)


> ** Wystarczy wykonać te kroki:**
> - Skopiować zawartość folderu ```CopyToinit.d``` do katalogu /etc/init.d

    Polecenie: cp CopyToinit.d/connect3g /etc/init.d

> - Dodać skrypt do update-rc
    
    Polecenie: sudo update-rc.d connect3g defaults

> - W celu usunięcia skryptu z automatycznego uruchamiania
    
    Polecenie: sudo update-rc.d connect3g remove
Tutaj uwaga na ścieżkie wskazującą w pliku connect3g na plik connect3g.py
Domyślnie jest taka ścieżka: "/home/pi/Rpi3gConnector"
I w tym pliku skrypt szuka pliku "connect3g.py"



### Testy
Program został przetestowany organoleptycznie w taki sposób:
>- Udane połącznienie
>- Wyjęcie karty sim
>- Odłączenie modemu
>- Włożenie karty sim
>- Podłączenie modemu do Rpi
>- Udane ponownie połączenie po upływnie pewnej wartośći stałego czasu


### Znane problemy
Niestety kiedy Rpi jest połączone po 3g przez modem, wyjęcie modemu powoduje zawieszenie się systemu. Problem zaobserwowany z moim programem jak i bez niego. Póki co obejścia nie ma. Liczę na to, że swobodne rozłączenie z siecią 3g przebiega "łagodniej"
