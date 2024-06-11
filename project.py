#This is my first project.
from colorama import Fore, Style,init
def order():
    bill = 0
    print("***please order the item***")
    price= {'pasta': '100', 'choumean': '50', 'momo': '180', 'rice': '250', 'cold drink': '50'}

    while True:
        item = input("Enter the item or (type **done** if you finishe order) ").strip().lower()
        if item =='done':
            break
        elif  item in price:
            bill += int(price[item])
    print("Your bill is ",bill)

def menu():
    print("***Welcome to Manu***")
    menu_items = {'pasta':'RS100','choumean':'RS50','momo':'RS180','Rice':'RS250','cold drink':'RS50' }
    for item in menu_items:
        print("\n" ,item,"==>",menu_items[item])

    ord = input("\n Which item so you want to order")
    order()


def main():
    print("***welcome to DJ MAAX RESTRURENT***\n")
    start = input("press 1 for see manu")
    if start == '1':
        menu()






if __name__=="__main__":
    main()