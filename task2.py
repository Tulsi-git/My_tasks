from datetime import datetime
import csv


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

    def export_to_csv(self, filename=None):
        # If no filename is provided, create a dynamic filename
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"grocery_list.csv"
        
        # Open the file and write the data
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            
            # Write headers
            csv_writer.writerow(["Purchased ", "Pending Items"])
            
            # Determine the maximum length between purchased and pending lists
            max_length = max(len(self.purchased), len(self.pending))
            
            # Write items in two columns
            for i in range(max_length):
                purchased_item = self.purchased[i] if i < len(self.purchased) else ""
                pending_item = self.pending[i] if i < len(self.pending) else ""
                csv_writer.writerow([purchased_item, pending_item])
        
        print(f"Grocery list exported to {filename}")

grocery = Grocery()
grocery.add_items("Watch")
grocery.add_items("Mobile")
grocery.add_items("Laptop")
grocery.add_items("Shirt")

grocery.divide_items("Watch", purchased=True)
grocery.divide_items("Mobile", purchased=False)
grocery.divide_items("Laptop", purchased=True)  
grocery.divide_items("Shirt", purchased=False)

grocery.review_item()
grocery.export_to_csv()




