

#Program(ciąg instrukcji):

#start
#instrukcja 1
#instrukcja 2
#instrukcja 3
#instrukcja sterująca a:
    #instrukcja a1
    #instrukcja a2
#instrukcja 4
#instrukcja 5
#instrukcja sterująca b:
    #instrukcja b1
    #instrukcja b2
    #instrukcja b3
#instrukcja 6
#stop


"""
Mamy do dyspozycji komputer i język programowania, żeby komputer zrobił dla nas to co byśmy chcieli.


1. Napisanie programu:
Chcemy aby komputer(procesor) coś dla nas zrobił(obliczył):
a. musimy dokładnie wiedzieć co chcemy żeby zostało zrobione    (określenie problemu)
b. ustalamy co ma być zrobione w naszym języku                  (sporządzamy algorytm rozwiązujący krok po kroku nasz problem)
c. zapisujemy co ma być zrobione w języku programowania         (piszemy program na komputerze w języku Python, na podstawie sporządzonego algorytmu)

2. Uruchomienie i wykonanie programu:
Procesor nie rozumie języka programowania.
Dlatego musimy przetłumaczyć to co zapisaliśmy w języku programowania na język maszynowy, który jest zrozumiały dla procesora.
Do tego służy interpreter języka Python, który musimy zainstalować na komputerze.
Uruchamiamy interpreter języka podając mu jako argument plik naszego programu(np: python program.py)
    Cykl wykonania naszego programu:
        a. interpreter pobiera (pierwszą/kolejną) instrukcję z naszego programu
        b. interpreter tłumaczy instrukcje z języka Python na język maszynowy
        c. procesor wykonuje instrukcje którą dostanie w języku maszynowym
        d. powrót do punktu a.
    Interpreter pobiera kolejne instrukcje, aż do momentu kiedy się skończą.
    Instrukcje pobierane są po kolei, kolejność może być zmieniona poprzez użycie specjalnych instrukcji - sterujących.
    Dzięki instrukcjom sterującym możemy wybierać jaka instrukcja zostanie wykonana.


            My(wypisz na ekran napis "Super") -> język programowania(print("Super")) -> program

            Program -> interpreter -> język maszynowy(010101001010111010101001110101011)

            Język maszynowy -> procesor -> wynik(to co byśmy chcieli)


"""

### Instrukcje sterujące

## if (warunek) instrukcjaI
"""
a. sprawdź(oblicz) warunek
b. jeśli warunek prawdziwy(=true) wykonaj instrukcjaI
c. jeśli warunek fałszywy(=false) przejdź do następnej instrukcji programu
"""

#Ćwiczonko numer pierwsze: zapisz algorytm wykonania instrukcji if/else
"""
a. sprawdz warunek
b. jesli warunek jest prawdziwy wykonaj instrukcje
c. jesli warunek jest fałszywy wykonaj instrukcje else
"""


#Ćwiczonko numer drugie: zapisz algorytm wykoniania instrukcji if/elif/else
"""
a. sprawdz warunek dla instrukcji if
b. jesli warunek jest prawdziwy wykonaj instrukcje if
c. jesli warunek jest fałszywy przejdz do instrukcji elif
d. sprawdz warunek dla instrukcji elif
e. jeśli warunek jest prawdziwy wykonaj instrukcje elif
f. jeśli warunek jest fałszywy wykonaj instrukcje else
"""
## while (warunek) instrukcjaW
"""
a. sprawdź warunek
b. jeśli warunek prawdziwy wykonaj instrukcjaW i przejdź do punktu a.
c. jeśli warunek fałszywy przejdź do następnej instrukcji programu
"""

#Ćwiczonko numer trzecie: zapisz algorytm wykoniania instrukcji while/else
"""
a. sprawdz warunek dla instrukcjiW
b. jeśli warunek prawdziwy wykonaj instrukcjeW i przejdz do punktu a 
c. jeśli warunek fałszywy wykonaj instrukcje else
"""