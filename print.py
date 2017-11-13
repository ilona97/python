"""
print(wartość1, wartość2, wartość3, sep="separator", end="co na końcu")
print(value1, value2, value3, sep=" ", end="\n")
"""
# print("karol", "pulawski", end="")
# print("nastepny")

#znaki białe: spacje, tabulatory, przejścia do następnej lini - wszystko czego nie widać
#znaki specjalne: 
# \n - następna linia
# \t - tabulator
# \" \' 
# \f \v \b

#Ćwiczonka:

#1 wypisz "Super"
print("Super")


#2 wypisz "Kubuś Puchatek" dowolnym sposobem
print("Kubuś Puchatek")

#3 wypisz "Kubuś Puchatek" nie używając spacji w wartościach
print("Kubuś", "Puchatek")

#4 wypisz "Kubuś Puchatek, misio" nie używając spacji w wartościach
print("Kubuś", "Puchatek,", "misio")

#5 wypisz "Jeden, Dwa, Trzy, " nie używając znaków białych i interpunkcyjnych w wartościach
print("Jeden,", "Dwa,", "Trzy," )

#6 wypisz "Kropka." nie używając znaków interpunkcyjnych w wartościach
print("Kropka", end=".\n")

#7 wypisz "Jeden, Dwa, Trzy." nie używając znaków białych i interpunkcyjnych w wartościach
print("Jeden", "Dwa", "Trzy", sep=", ", end=".\n")


#8 wypisz  "Koniec
#           Kropka."
# nie używając znaków białych i interpunkcyjnych w wartościach
print("Koniec", "Kropka", sep="\n", end=".\n")


#9 wypisz "Jeden - misio
#          Dwa - misiaczki."
# nie używając znaków interpunkcyjnych w separatorach
print("Jeden - misio", "Dwa - misiaczki", sep="\n", end=".\n" )


#10 wypisz "Jeden - misio
#           Dwa - misiaczki
#           Kropka"
# nie używając słowa "Kropka" w wartościach
print("Jeden - misio", "Dwa - misiaczki\n", sep="\n", end="Kropka\n" )


#11 wypisz "Jeden - misio
#           Kropka."
# nie używając znaku przejścia do następnej linii w separatorach i wartościach
print("Jeden - misio", end="\nKropka.\n")


#12  wypisz "Wpadła gruszka do fartuszka
#            a za gruszką dwa jabłuszka,
#            a śliweczka wpaść nie chciała,
#            bo śliweczka niedojrzała!"
# nie używając słowa 'śliweczka' i wykrzyknika w wartościach
print("Wpadła gruszka do fartuszka\na za gruszka dwa jabłuszka,\na", "wpaść nie chciała,\nbo", "niedojrzała", sep=" śliweczka ", end="!\n")


#13 wypisz "Jadą, jadą misie, Śmieją im się pysie.
#           Przyjechały do lasu, narobiły hałasu,
#           Przyjechały do boru, narobiły rumoru."
# nie używając w wartościach litery 'u'
print("Jadą, jądą misie, Śmieją im się pysie.\nPrzyjechały do las", " narobiły hałas","\nPrzyjechały do bor"," narobił rumor", sep="u,", end="u.\n")
                                                                                                                      # ^litera 'u' użyta w wartości