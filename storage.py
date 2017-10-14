from OOP_Jude.vero_assignment.item_classes import *

items = Items()
fragile = Fragile()
luxury = Luxury()


def welcome():
    print("Welcome to the storage!")
    main()


def main():
    print("\n######## MAIN ########")
    x = input("Please choose what you want to do:\n"
              "[1]Add items\n"
              "[2]List of items\n"
              "[3]Dispose items\n"
              "[4]Return all broken fragile items\n"
              "[5]Show tax total of all luxury items\n"
              "[6]Exit\n"
              "Input:")
    if x == "1":
        items.add_items()
        main()
    elif x == "2":
        items.print_list()
        main()
    elif x == "3":
        items.dispose()
        main()
    elif x == "4":
        fragile.return_fragile()
        main()
    elif x == "5":
        luxury.print_tax_total()
        main()
    elif x == "6":
        print("\nThank you for using Storage! :)")
        exit()
    else:
        print("[ERROR!] Wrong command!")
        main()


# Play welcome
welcome() 