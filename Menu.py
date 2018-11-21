import os

while True:
    print("""Menu:
    
1 - Nowa gra
2 - Wyjdź\n
""")

    inp = int(input("Podaj cyfrę odpowiednią opcji: "))

    if inp == 1:
        os.system('python Start.py')
        # import Start
    elif inp == 2:
        print("Exit")
        break
    else:
      print("\nNie ma takiej opcji!\n")