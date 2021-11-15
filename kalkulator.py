
action = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

item_1 = float(input("Podaj składnik 1.: "))
item_2 = float(input("Podaj składnik 2.: "))


def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multipy(x, y):
    return x * y
def divide(x, y):
    return x / y

if action == "1":
    print("dodaję:", item_1, "i", item_2)
    print("wynik to:", add(item_1, item_2))

elif action == "2":
    print("odejmuję:", item_1, "i", item_2)
    print("wynik to:", substract(item_1, item_2))

elif action == "3":
    print("monożę:", item_1, "i", item_2)
    print("wynik to:", multipy(item_1, item_2))

elif action == "4":
    print("dzielę:",  item_1, "przez", item_2)
    print("wynik to: ", divide(item_1, item_2))
