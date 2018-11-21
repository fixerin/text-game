# def updateBroni(power, bron):
#     power = power - dictBronie[eq[0][1]]
#     eq[0][1] = bron
#     power = power + dictBronie[bron]
#     print(power)
#     return power, eq
#
# # def switch(arg):
# #     switcher
#
# dictBronie = {'Tępy Patyk': 1,
#               'Ostry Patyk': 2,
#               'Krótki Miecz': 3,
#               'Długi Miecz': 4,
#               'Świety Granat': 100,
#               'Nipojęty Topór': 5,
#               'Ognisty Boomerang': 7,
#               'Diaboliczna Gitara': 10,
#               'brak': 0}
#
# eq = [["broń", "brak"],["zbroja", "brak"],["hełm", "brak"]]
# power = 0
#
# print("Znalazłeś Tępy Patyk!")
# inp = input("Checesz go założyć?")
# if inp == "tak" or inp == "yes":
#     power, eq = updateBroni(power, "Tępy Patyk")
#
# print("Znalazłeś Długi Miecz!")
# inp = input("Checesz go założyć?")
# if inp == "tak" or inp == "yes":
#     power, eq = updateBroni(power, "Długi Miecz")
#
# print(power, eq)

from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('przygody.xml')

items = mydoc.getElementsByTagName('opis')


# one specific item's data
print('\nItem #2 data:')
print(items[1].firstChild.data)
print(items[1].childNodes[0].data)

# all items data
print('\nAll item data:')
for elem in items:
    print(elem.firstChild.data)