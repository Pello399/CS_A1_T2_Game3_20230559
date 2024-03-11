import math

def is_perfect_square(n):
    if(n < 0):return False
    root = int(math.sqrt(n))
    if(root * root == n): return True
    else: return False
def menu1(num):
    print("Player 1")
    turn = int(input("Please enter a square number: "))
    while (turn <= num and turn > 0):

        if(is_perfect_square(turn)):
           num -= turn
        else:
            print("Please enter a valid number.")
            return menu1(num)
        if(num < 0):
            return num
        else:
            print(f"{num} Coins left")
            return num
    else:
        print("Please enter a valid number.")
        return menu1(num)
def menu2(num):
    print("Player 2")
    turn = int(input("Please enter a square number: "))
    while(turn <= num and turn > 0):

        if (is_perfect_square(turn)):
            num -= turn
        else:
            print("Please enter a valid number.")
            return menu2(num)
        if (num < 0):
            return num
        else:
            print(f"{num} Coins left")
            return num
    else:
        print("Please enter a valid number.")
        return menu2(num)

def main():
    print("*Welcome to Subtract a Square*")
    num = int(input("Enter the total number of coins: "))
    print(f"You have {num} left.")
    while(True):
        res1 = menu1(num)
        if(res1 <= 0):
            print("Player 1 wins!")
            break
        res2 = menu2(res1)
        if(res2 <= 0):
            print("Player 2 wins!")
            break
        num = res2

main()

## FILE :  CS_A1_T2_Game3_20230559
## Purpose : subtract a square first to zero wins
## Author : Ahmed Hamed Nabih Shabana
## ID : 20230559