'''
if warunek:
   instrukcja
elif warunek:
   instrukcja
...
else:
   instrukcja

'''
'''
Warunki:
Operatory logiczne (porównanie):
<  - mniejszy
<= - mniejszy lub równy
>  - większy
>= - większy lub równy
== - równy
!= - różny
<> - 

Operatory logiczna:
~ - negacja (!)
and - iloczyn logiczny, koninkcja (&&)
or - suma logiczna, alternatywa (||)

Wartości logiczne:
True - prawda
False - fałsz, nieprawda

None - wartość nieokreślona, nieznana
'''

# ćwiczonko pierwsze
# Sprawdź używając konstrukcji if/else jakie wartości logiczne posiadają następujące wartości:
# True, False, 1, 100, -999, 0
# Przykładowo: dla wartości 1, program ma wyświetlić '1 = prawda' lub '1 = fałsz', tak samo dla pozostałych wartości.


#ćwiczonko drugie
#Sprawdź na przykładzie, jaką wartość logiczną ma suma logiczna, dla wszystkich możliwych przypadków.
#Wynik działania programu ma wyglądać następująco:
# Suma logiczna - alternatywa - or
# False or False = fałsz
# ...pozostałe przypadki


#ćwiczonko drugie
#Sprawdź na przykładzie, jaką wartość logiczną ma iloczyn logiczny, dla wszystkich możliwych przypadków
#Wynik działania programu ma wyglądać następująco:
# Iloczyn logiczny - koniunkcja - and
# False and False = fałsz
# ...pozostałe przypadki


#ćwiczonko trzecie
#Wprowadź liczbę i sprawdź czy jest podzielna przez dwa


#ćwiczonko czwarte
#Wprowadź liczbę i sprawdź jej podzielność przez drugą wprowadzoną liczbę
#Wprowadź liczbę której podzielność chcesz sprawdzić i liczbę przez którą ma być podzielna


#ćwiczonko piąte
#Wprowadź liczbę i sprawdź czy mieści się w zakresie <50,100>


#ćwiczonko szóste
#Wprowadź liczbę i sprawdź czy mieści się w zakresie (50,100)


#ćwiczonko siódme
#Wprowadź liczbę i sprawdź czy mieści się w zakresie <25,50)


#ćwiczonko ósme
#Napisz program, który pobiera wagę samochodu i wypisuje jaką minimalną kategorię musisz posiadać aby go prowadzić
#Zestawienie kategorii:
#B1 (0   ,  400>  kg
#B  (400 , 3500>  kg
#C1 (3500, 7500>  kg
#C  (7500,    +)  kg

#ćwiczonko dziewiąte
#Napisz program, który pobiera liczbę i wypisuje na ekran czy jest dodatnia, ujemna czy równa zero.


#ćwiczonko dziesiąte
#Napisz program, który pobierze od Ciebie dwa ulubione przedmioty szkolne i powie Ci kim zostaniesz w przyszłości.
#Trzeba skonstruować instrukcje warunkowe w taki sposób aby został wypisany tylko jeden zawód.

# Kryteria:
## Przedmioty: Biologia, Chemia, Fizyka, Matematyka, Informatyka, Historia, Polski, Kultura.
## Kim zostaniesz:
##- Polski: polonista
##- Kultura i Historia: przewodnik
##- (Historia lub Kultura) i Polski: historyk
##- Matematyka: matematyk
##- Fizyka i Matematyka: fizyk
##- Informatyka i Matematyka: informatyk
##- Biologia i (Informatyka lub Matematyka): inżynier biomedyczny
##- Biologia: przyrodnik
##- Chemia i Matematyka: chemik
##- Biologia i Chemia: biotechnolog
##- W pozostałych przypadkach: naukowiec

# ---------------------------------------------
# Przykładowe wyniki działania programu:
# 1:
# Powiedz, jakie są Twoje ulubione przedmioty?
# pierwszy: Matematyka
# drugi: Historia
# Twój zawód przyszłości to: matematyk
#  
# 2:
# Powiedz, jakie są Twoje ulubione przedmioty?
# pierwszy: Chemia
# drugi: Historia
# Twój zawód przyszłości to: naukowiec
