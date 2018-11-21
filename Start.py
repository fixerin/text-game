from xml.dom import minidom

def czytajXML():
    mydoc = minidom.parse('przygody.xml')
    items = mydoc.getElementsByTagName('pokoj')

    pass

def opisPokoju():

    pass

def przerywnik():
    input("Wcisnij enter by kontynuować...\n")
    pass

def howMuchPowa(power):
    print("Twoja moc jest rowna " + str(power) + "\n")


def updateBroni(power, bron):
    power = power - dictBronie[eq[0][1]]
    eq[0][1] = bron
    power = power + dictBronie[bron]
    print(power)
    return power, eq

# NIEDOKOŃCZONE

def updatePozycji(pozycja):
    global a, x, y

    inp = input("""W którą stronę chcesz się udać?
E - Wschód
W - Zachód
N - Północ
S - Południe:\n""")


    while not (inp.lower() == "e" and x != 8) or (inp.lower() == "w" and x != 0) or (inp.lower() == "n" and y != 0) or (inp.lower() == "s" and y != 8):
        print("Nie możesz się tam udać...\n")
        inp = input("Do wyboru masz : E, W, N, S?\n")
        continue
    else:
        for i in range(9):
            for j in range(9):
                a[i][j] = str(i) + "x" + str(j)

        if inp == "e":
            x = x + 1
            pozycja = a[y][x] = "TY"

        elif inp == "w":
            x = x - 1
            pozycja = a[y][x] = "TY"

        elif inp == "n":
            y = y - 1
            pozycja = a[y][x] = "TY"

        elif inp == "s":
            y = y + 1
            pozycja = a[y][x] = "TY"

        else:
            print("Błąd...")



    #     print("Błąd :(")

    return pozycja

def pokazPozycje():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in a]))

def pokazEq(eq):
    print("\nTwój ekwipunek:")
    print(str(eq[0][0]) + " => " + str(eq[0][1]))
    print(str(eq[1][0]) + " => " + str(eq[1][1]))
    print(str(eq[2][0]) + " => " + str(eq[2][1]) + "\n")


dictBronie = {'Tępy Patyk': 1,
              'Ostry Patyk': 2,
              'Krótki Miecz': 3,
              'Długi Miecz': 4,
              'Świety Granat': 100,
              'Nipojęty Topór': 5,
              'Ognisty Boomerang': 7,
              'Diaboliczna Gitara': 10,
              'brak': 0}

power = 0

# Ekwipunek
eq = [["broń", "brak"],["zbroja", "brak"],["hełm", "brak"]]

# Współrzędne pozycji
x = 5
y = 5

print("\nWitaj przybyszu!")
print("Jak Cię zwą?")
name = input()


print("""
Tak więc, """ + name + """, znajdujesz się właśnie na początku swojej przygody, czyli w pokoju 0x0.
Pokoi jest w sumie 81. Nie musisz wchodzić do każdego. Twoim celem jest dotarcie do pokoju 8x8
Poglądowo jesteś tutaj:
""")

przerywnik()

m = 9
n = 9
a = [0] * n             #Tworzenie listy jednowymiarowej
for i in range(n):
    a[i] = [i] * m      #Tworzenie listy dwuwymiarowej

for i in range(n):
    for j in range(m):
        a[i][j] = str(i) + "x" + str(j)  # Wypelnienie listy kolejnymi nazwami pokoi

pozycja = a[y][x] = "TY"

pokazPozycje()
# print('\n'.join([''.join(['{:4}'.format(item) for item in row])
#       for row in a]))


print("\nJesteś świerzakiem, więc nie masz żadnej mocy. Jej poziom jest równy " + str(power))
print("""Możesz zawsze sprawdzić ilość mocy wpisując 'moc'. Pokaze Ci to jej aktualny poziom. 
""")

inp = input("Sam spróbuj:\n")
while inp.lower() != "moc":
    print("Coś poszło nie tak :(")
    inp = input("Spróbuj raz jeszcze:\n")
else:
    # print("Coś poszło nie tak")
    howMuchPowa(power)
    print("Słabiak XD\n")

print("Moc mozesz podnieść poprzez różne zdarzenia, albo ekwipunek, czyli: zbroje, hełm i miecz.\n"
      "Tak, biegasz boso...\n")
print("Twój ekwipunek: ")
# pokazEq(eq + "\n")
pokazEq(eq)

print("Możesz sprawdzić swój ekwipunek wpisując 'eq'.\n")
inp = input("Spróbuj sam:\n")
while inp.lower() != "eq":
    print("To nie to polecenie. Spróbuj raz jeszcze\n")
    inp = input()
else:
    pokazEq(eq)

print("""Ok, podstawy co do twojej postaci mamy za sobą. Czas na omówienie poruszania się.
Jesteś w lewym górnym kącie mapy.
Znajdujesz się w pustym pokoju z białymi ścianami. Widzisz przed sobą dwie pary drzwi:
- na południu drewniane
- na wschodzie grube metalowe.\n""")

pozycja = updatePozycji(pozycja)

# inp = input("""W którą stronę chcesz się udać?
# E - Wschód
# W - Zachód
# N - Północ
# S - Południe:\n""")
#
# while inp.lower() == "e" or inp.lower() == "w" or inp.lower() == "n" or inp.lower() == "s":
#     pozycja = updatePozycji(pozycja, inp)
#     break
# else:
#     print("Nie rozumiem polecenia\n")
#     inp = input("Do wyboru masz : E, W, N, S?\n")

# print(a)
# print(pozycja)
print("Jesteś teraz tutaj:\n")
pokazPozycje()





# print(eq)
