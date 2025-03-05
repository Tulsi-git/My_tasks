class Grocery:
    def __init__(self):
        self.cart = []
        self.purchased = [ ]
        self.pending = []

    def add_items(self,item):
        self.cart.append(item)

    def divide_items(self,item,purchased=True):
        if item in self.cart:
            self.cart.remove(item)
            if purchased:
                self.purchased.append(item)
            else:
                self.pending.append(item)
        else:
            print("Error : item not found.")

    def review_item(self):
        print("Purchased items:")
        for item in self.purchased:
            print(f"{item}")
        print("pending items:")
        for item in self.pending:
            print(f"{item}")

grocery = Grocery()
grocery.add_items("Watch")
grocery.add_items("Mobile")

grocery.divide_items("Watch", purchased=True)
grocery.divide_items("Mobile", purchased=False)

grocery.review_item()




