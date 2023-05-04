# Parent class

class Item:
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("SKU: {}".format(self.sku))


# Parent class 2
class Garment:
    def __init__(self, section, department):
        self.section = section
        self.type = department

    def print_garment(self):
        print("The garment is in section {}, {}".format(self.section, self.type))


# Child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, department, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, department)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))


Blouse = Shirts("bl01", 43, "Tops", "Formal Blouse", "White")
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()
