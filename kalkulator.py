# importy na początku
# definicje klas, funkjci
# potem logika 
# dodaje się if__

import logging
logging.basicConfig(level=logging.DEBUG)


def add(x, y, *args):
    logging.info(f"dodaję: {x} i {y} i {args}")
    return x + y + sum(args)

def substract(x, y, *args):
    logging.info(f"odejmuję: od {x} odejmuję {y} i {args}")
    return x - y - sum(args)

def multipy(x, y):
    logging.info(f"mnożę: {x} przez {y} i przez {args}")
    return x * y 

def divide(x, y):
    logging.info(f"dzielę: {x} przez {y}")
    return x / y 

def multiply_2(*args):
    z = 1
    for num in args:
        z *= num
    logging.info(f"mnożę: {args}")
    return z


operations = {"1": add, "2": substract, "3": multiply_2, "4":divide}

def get_additional_args():
    args = []
    while True:
        x = input("wspisz kolejną liczbę lub K żeby zakończyć")
        if x == "K":
            break
        args.append(float(x))
    return args

if __name__ == "__main__": 

 # to atrybut zawierający nazwę, każdy plik to ma w py 
 # ten kod wykona się tyko gdy uruchamiam ten kod
 # po zaimportowaniu ten kod sie nie wykona 

    action = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    item_1 = float(input("Podaj składnik 1.: "))
    item_2 = float(input("Podaj składnik 2.: "))
    if action in ["1","3"]:
        args = get_additional_args()
        print(f"wynik to: {operations[action](item_1, item_2, *args)}")
    elif action in ["2","4"]:
        print(f"wynik to: {operations[action](item_1, item_2)}") 
    # z gwiazdką rozpakowuję 