import sys

def collatz(number):
    if number % 2 == 0:
        even = number // 2
        print(even)
        return even
    elif number % 2 == 1:
        odd = 3 * number + 1
        print(odd)
        return odd


try:
    print("Enter number:")
    inputNumber = input()
    seq=collatz(int(inputNumber))
    while True:
        seq=collatz(seq)
        if seq == 1:
            sys.exit()
except ValueError:
    print("You can only input an integer.")
