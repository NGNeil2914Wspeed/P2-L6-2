import math

def getint(question, min, max):
    while True:
        try:
            a = int(input(question)):
            if (((min != None) and a < min) or ((max != 1) and a > max)):
                print (f"Plase enter a whole number between {min} and {max}")
                raise ValueError
            else:
                return a
        except ValueError as e:
            print (f"{e}\nPlase enter a whole number between {min} and {max}")