
import sys


def function1():
    print("Please enter 3 numbers:\n")
    a = input("Please enter your first(1st) digit: \n")
    while not a.isdigit():
        print("\nPlease supply a valid digit")
        a = input("Please enter your first(1st) digit: \n")

    b = input("\nPlease enter your second(2nd) digit: \n")
    while not b.isdigit():
        print("\nPlease supply a valid digit")
        b = input("Please enter your second(2nd) digit: \n")

    c = input("\nPlease enter your third(3rd) digit: \n")
    while not c.isdigit():
        print("Please supply a valid digit")
        c = input("Please enter your third(3rd) digit: \n")
    aa = int(a)
    bb = int(b)
    cc = int(c)
    while aa == bb and aa == cc and bb == cc:
        print(
            f"\nThe three(3) digits you have supplied are all equals to {a}.\nPlease do not supply three equal digits. Thanks.\n")
        function1()
    function2(aa, bb, cc)


def function2(aa, bb, cc):

    largest = max(aa, bb, cc)

    if largest == aa:
        print(f"\nthe first(1st) digit which is {aa} is the largest number.\n")
    elif largest == bb:
        print(
            f"\nthe second(2nd) digit which is {bb} is the largest number.\n")
    else:
        print(f"\nthe third(3rd) digit which is {cc} is the largest number.\n")

    function3()


def function3():
    d = input(
        "Restart \"What is the largest number program?\"\nPlease type \"Y\" to restart and \"N\" to quit:\n")
    if d.lower() == "y":
        function1()
    elif d.lower() == "n":
        sys.exit()
    else:
        print("Please supply either \"Y\" or \"N\" only. Thanks.")
        function3()


function1()
