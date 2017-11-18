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

# ćwiczonko zero
# Sprawdź używając konstrukcji if/else jakie wartości logiczne posiadają następujące wartości:
# True, False, 1, 100, -999, 0
# Przykładowo: dla wartości 1, program ma wyświetlić '1 = prawda' lub '1 = fałsz', tak samo dla pozostałych wartości.

"""

if(True):
    print("True = prawda")
else:
    print("True = fałsz")

if(False):
    print("False = prawda")
else:
    print("False = fałsz")

if(1):
    print("1 = prawda")
else:
    print("1 = fałsz")

if(100):
    print("100 = prawda")
else:
    print("100 = fałsz")

if(-999):
    print("-999 = prawda")
else:
    print("-999 = fałsz")

if(0):
    print("0 = prawda")
else:
    print("0 = fałsz")

"""

#
# @Extra tasks
# 1. Sprawdź używając python'a czy dwa jest większę od czternastu.

"""
if(2>14):
    print("prawda")
else:
    print("fałsz")
"""
# 2. Sprawdź czy dla komputera dwanaście to to samo co dwa razy sześć.

"""
if( 12 == 2*6):
    print("prawda")
else:
    print("fałsz")
"""

# 3. Powiedz co wypisze poniższy program, ale nie sprawdzaj czy miałaś rację ;)
# x = 12
# if(12 > x):
#     print("prawda to")
# else:
#     print("nieprawda :o")
#
#=> peeewnie " nieprawda :o"

# 4. Korzystając tylko z pythona i konsoli sprawdź jaka jest kolejność wykonywania działań logicznych kiedy nie ma nawiasów.
# Tzn. czy pierwszeństwo ma 'and' czy 'or'
# Np. w zwykłej algebrze: 2 + 5 * 3 = 2 + (5 * 3) = 2 + 15
# A jak to będzie w algebrze bool'a?
#> pierwszeństwo ma and
"""
if(2 or 5 and 3 == 2 + 15):
    print("prawda")
else:
    print("fałsz")
"""
#algebra bool'a 
#   0+0=0           0*0=0
#   0+1=1           0*1=0
#   1+0=1           1*0=0
#   1+1=1           1*1=1

"""
if(False or True and True == False or True):
    print("prawda")
else:
    print("fałsz")
"""

# 5. Obok warunków wypisz jakie według Ciebie mają one wartości?
# Wszystkie pomoce dozwolone, oprócz użycia do tego python'a i konsoli.
# 12 > 5 #=>    True
# True or False #=>    True
# 1 > 3 and 3 > 11 #=>    False
# x*2 >= x #=>  
# x >= 0 or x < 0 #=>  false
# False == False #=>     False
# False and False #=>    False
# (12 > 3 and 11 > 4 and 8 >= 8) or 9 < -1 #=>     False
    
# W poniższych przykładach skracaj powoli warunek w takiej kolejności jak to zrobi komputer
#   np.: True and False or True #=> False or True #=> True
# True and True or False #=> True or False #=> True
# True or False and True #=> True or False #=> True
# True and (True or False) #=> True and True #=> True
# (True and True or False) or (True or False and True) #=> (True or False) or (True or False) #=> True or True #=> True
# True and (False or True) or (False or True and (False or True)) #=> True and True or (False or True and True) #=> True or (False or True) #=> True or True #=> True

#ćwiczonko pierwsze
#Sprawdź na przykładzie, jaką wartość logiczną ma suma logiczna, dla wszystkich możliwych przypadków.
#Wynik działania programu ma wyglądać następująco:
# Suma logiczna - alternatywa - or
# False or False = fałsz
# ...pozostałe przypadki
"""
if(False or False == False):
    print("prawda")
else:
    print("error")

if(False or True == True):
    print("prawda")
else:
    print("error")

if(True or False == True):
    print("prawda")
else:
    print("error")

if(True or True == True):
    print("prawda")
else:
    print("error")
"""


#ćwiczonko drugie
#Sprawdź na przykładzie, jaką wartość logiczną ma iloczyn logiczny, dla wszystkich możliwych przypadków
#Wynik działania programu ma wyglądać następująco:
# Iloczyn logiczny - koniunkcja - and
# False and False = fałsz
# ...pozostałe przypadki
"""
if((False and True) == False):
    print("prawda")
else:
    print("error")

if((True and False) == False):
    print("prawda")
else:
    print("error")

if((True and True) == True):
    print("prawda")
else:
    print("error")
"""
#ćwiczonko trzecie
#Wprowadź liczbę i sprawdź czy jest podzielna przez dwa

"""
print("x?=", end=" ")
x=int(input())

y=0

if(x % 2 == y):
    print(x, "podzielne przez 2 ")
else:
    print(x, "niepodzielne przez 2")
   
"""

#ćwiczonko czwarte
#Wprowadź liczbę i sprawdź jej podzielność przez drugą wprowadzoną liczbę
#Wprowadź liczbę której podzielność chcesz sprawdzić i liczbę przez którą ma być podzielna

print("x?=", end="")
x=int(input())
print("y?=", end="")
y=int(input())

i=0

if(x % y == i):
    print(i)
else:
    print("error")
    

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


#ćwiczonko dziesiąte a.
#Komputer rozumie tylko zera i jedynki.
#Więc dla komputera wszystko jest liczbą.
#Np. dziesiętna liczba 5, to dla komputera 0011 - to akurat łatwe
#Ale np. literka 'a' ? jaka to będzie liczba? nie będzie to wcale jakaś losowa kombinacja zer i jedynek
#Znaki zakodowane są w tak zwanym kodzie ASCII, każdy znak ma tam swój odpowiednik liczbowy.
# Aby zamienić dowolny znak na liczbę należy użyć funkcji ord(), np:
# ord("a") #=> 97
# Aby z liczby stworzyć znak należy uzyć funkcji chr(), np:
# chr(97) #=> "a"
# Twoje zadanie polega na tym aby sprawdzić jaka liczba w kodzie ASCII odpowiada literce 'h' oraz 'H'
# A potem sprawdzić jaka literka odpowiada liczbie 99 i 100 w kodzie ACII

#ćwiczonko dziesiąte b.
#Zastanów się co wypisze na ekran poniższa instrukcja:
# print( chr(ord("a")+1) )

#ćwiczonko dzisiąte c.
#Wypisz na ekran swoje imię(z wielkiej litery) korzystając z instrukcji print,
# ale nie używając do tego liter. (użyj funkcji chr(), możesz wspomóc się tablicą kodów ASCII)

#ćwiczonko dziesiąte d.
#Napisz program, który spyta Cię jaka liczba w kodzie ASCII odpowiada znakowi "?",
# a następnie wypisze sprawdzi i powie Ci czy dobrze odpowiedziałaś.
#Zrób to na dwa sposoby, w pierwszym użuj funkcji ord() a w drugim funkcji chr()


#ćwiczonko jedenaste
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
