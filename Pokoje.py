from pathlib import Path

from os import listdir
from os.path import isfile, join



# path = '/Users/Janko/PycharmProjects/TextAdventureGame/Przygody/pokoj1.txt'

Przygody = Path("Przygody/")

onlyfiles = [f for f in listdir(Path("Przygody/")) if isfile(join(Path("Przygody/"), f))]

pokoj = Przygody / "pokoj1.txt"

# f = open(pokoj)
#
# print(f.read())
#
# f.close()

print(onlyfiles)

pokoj1 = Przygody / onlyfiles[0]
pokoj2 = Przygody / onlyfiles[1]

f = open(pokoj1)
f2 = open(pokoj2)

print(f.read() + "\n")
print(f2.read())