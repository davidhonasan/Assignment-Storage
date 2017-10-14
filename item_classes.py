class Items:
    others = []

    def __init__(self, name="", category="", price=""):
        self.name = name
        self.category = category
        self.price = price

    def print_list(self):
        print("\n######## ITEM LIST ########")
        print("Fragile Items:")
        for i in Fragile.fragile_items:
            print(str(i.name), "\tRp.", str(i.price), "\tCondition:", str(i.condition))
        print("\nLuxury Items:")
        for i in Luxury.luxury_items:
            print(str(i.name), "\tRp.", str(i.price), "\tTax:", str(i.tax()))
        print("\nOther Items:")
        for i in Items.others:
            print(str(i.name), "\tRp.", str(i.price), "\tCategory:", str(i.category))

    def dispose(self):
        self.print_list()
        print("\n######## DISPOSE ########")
        x = input("What category you want the item to be disposed?[fragile/luxury/other]")
        y = input("What item you want to dispose?[write number index from 1]")
        if y.isdigit() is False:
            print("[ERROR!] Wrong command!")
            from OOP_Jude.vero_assignment.storage import main
            main()
        if x == "fragile":
            del Fragile.fragile_items[int(y) - 1]
        elif x == "luxury":
            del Luxury.luxury_items[int(y) - 1]
        elif x == "other":
            del self.others[int(y) - 1]
        else:
            print("[ERROR!] Wrong command!")
            from OOP_Jude.vero_assignment.storage import main
            main()

    def add_items(self):
        print("\n######## ADD ITEM ########")
        x = input("Name:")
        y = input("Category:[fragile/luxury/other]")
        z = input("Price:")
        if y.lower() == "fragile":
            w = input("Condition: [broken/unbroken]")
            Fragile.fragile_items.append(Fragile(x, y, z, w.upper()))
        elif y.lower() == "luxury":
            Luxury.luxury_items.append(Luxury(x, y, z))
        else:
            Items.others.append(Items(x, y, z))


class Fragile(Items):
    fragile_items = []

    def __init__(self, name="", category="", price="", condition=""):
        super().__init__(name, category, price)
        self.condition = condition

    def return_fragile(self):
        print("\n######## RETURNING FRAGILE ITEMS ########")
        returned_items = 0
        for i in self.fragile_items:
            if i.condition == "BROKEN":
                i.condition = "RETURNED"
                returned_items += 1
                print("You returned", i.name)
        if returned_items == 0:
            print("You returned nothing.")

class Luxury (Items):
    luxury_items = []

    def tax(self):
        tax = 25/100 * int(self.price)
        return tax

    def tax_total(self):
        tax_total = 0
        for i in self.luxury_items:
            tax_total += i.tax()
        return tax_total

    def print_tax_total(self):
        print("\n######## LUXURY TAX TOTAL ########")
        print("Tax total of all luxury items are", self.tax_total())