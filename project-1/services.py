import csv
import pandas as pd

class Product():
    def __init__(self, name, price, stok, ) -> None:
        self.name = name
        self.price = price
        self.stok = stok

    @staticmethod
    def create(barang):
        # Read the existing CSV file to determine the next ID
        df = pd.read_csv("products.csv")
        #  Mengecek Id agar Auto Increment
        if not df.empty:
            next_id = df["id"].max() + 1
        else:
            next_id = 1

        data_barang = {
            "id": next_id,
            "name": barang["name"],
            "price": barang["price"],
            "stock": barang["stock"]
        }
        # Baca file
        with open("products.csv", mode="a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data_barang.keys())

            # Check if the file is empty and write the header if needed
            if file.tell() == 0:
                writer.writeheader()

            # Write the new data to the CSV file
            writer.writerow(data_barang)

    @staticmethod
    def read():
        try:
            df = pd.read_csv("products.csv")
            pd.set_option('display.max_rows', None)
            if not df.empty:
                df = df.drop(columns=['Unnamed: 5'], errors='ignore')
                print(df)
            else:
                print("The 'products.csv' file is empty.")
        except FileNotFoundError:
            print("The 'products.csv' file does not exist.")

    @staticmethod
    def get_by_id(product_id):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv("products.csv")
            
            # Ensure the DataFrame is sorted by 'id'
            df = df.sort_values(by='id')
            
            # Binary search for the product by 'id'
            left, right = 0, len(df) - 1
            while left <= right:
                mid = (left + right) // 2
                mid_id = df.iloc[mid]['id']
                if mid_id == product_id:
                    result = df.iloc[mid].to_frame().T  # Convert the row to a DataFrame
                    print("Product found:")
                    print(result)
                    return result.to_dict(orient='records')[0]
                elif mid_id < product_id:
                    left = mid + 1
                else:
                    right = mid - 1
            return None  # Product with the given ID is not found
        except FileNotFoundError:
            print("The 'products.csv' file does not exist.")
            return None
        
    @staticmethod
    def delete(product_id):
        try:
            # Read the CSV file into a DataFrame
            df = pd.read_csv("products.csv")
            
            # Check if the product with the specified ID exists
            if product_id in df['id'].values:
                # Delete the row with the matching product ID
                df = df[df['id'] != product_id]
                
                # Save the updated DataFrame back to the CSV file
                df.to_csv("products.csv", index=False)
                
                print(f"Product with ID {product_id} deleted.")
            else:
                print(f"Product with ID {product_id} not found.")
        except FileNotFoundError:
            print("The 'products.csv' file does not exist.")

# Implement Queue
# Untuk Menambah Banyak Barang Sekaligus
class ProductCreationQueue:
    def __init__(self):
        self.queue = []

    # Add to queue
    def add_product(self, product_data):
        self.queue.append(product_data)

    # Process queue
    def process_queue(self):
        while self.queue:
            product_data = self.queue.pop(0)  # Dequeue the first product data
            # Create an instance of the Product class
            product = Product(product_data["name"], product_data["price"], product_data["stock"])
            # Call the create method with the product data
            product.create(product_data)