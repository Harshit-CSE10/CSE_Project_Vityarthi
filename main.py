import sys
from src.inventory import add_product, update_stock, get_all_products
from src.alerts import check_low_stock
from src.utils import get_valid_number

def menu():
    print("\n=== Local Business Inventory Manager ===")
    print("1. Add New Product")
    print("2. View Inventory")
    print("3. Record Sale")
    print("4. Check Low Stock Alerts")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            pid = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            price = get_valid_number("Enter Price: ", float)
            qty = get_valid_number("Enter Quantity: ", int)
            success, msg = add_product(pid, name, price, qty)
            print(msg)

        elif choice == '2':
            products = get_all_products()
            if not products:
                print("Inventory is empty.")
            else:
                print(f"\n{'ID':<10} {'Name':<20} {'Price':<10} {'Qty':<10}")
                print("-" * 50)
                for p in products:
                    print(f"{p.product_id:<10} {p.name:<20} ${p.price:<10.2f} {p.quantity:<10}")

        elif choice == '3':
            pid = input("Enter Product ID to sell: ")
            qty = get_valid_number("Quantity sold: ", int)
            success, msg = update_stock(pid, qty)
            print(msg)

        elif choice == '4':
            alerts = check_low_stock()
            if not alerts:
                print("All stock levels are healthy.")
            else:
                for alert in alerts:
                    print(alert)

        elif choice == '5':
            print("Exiting application...")
            sys.exit()
        
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()