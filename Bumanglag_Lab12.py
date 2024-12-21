# Menu function
def display_menu():
    # Menu items and prices
    menu = {
        1: {"name": "Burger", "price": 150},
        2: {"name": "Pizza", "price": 250},
        3: {"name": "Pasta", "price": 200},
        4: {"name": "Salad", "price": 120},
        5: {"name": "Fries", "price": 80}
    }
    
    # Menu header
    print("\n=== MENU ===")
    print("Item No. | Item Name | Price")
    print("-" * 30)
    
    # Display items
    for item_no, details in menu.items():
        print(f"{item_no:^8} | {details['name']:<9} | ₱{details['price']}")
    return menu

# Order function
def get_order(menu):
    # Get user input
    choice = int(input("\nEnter item number to order: "))
    
    # Input validation
    while choice not in menu:
        print("Invalid item number. Please try again.")
        choice = int(input("Enter item number to order: "))
    
    return menu[choice]

# Payment function
def process_payment(total_cost):
    # Get payment
    payment = float(input(f"\nTotal amount to pay: ₱{total_cost}\nEnter your payment: ₱"))
    
    # Payment validation
    while payment < total_cost:
        print("Insufficient payment. Please enter a valid amount.")
        payment = float(input("Enter your payment: ₱"))
    
    # Calculate change
    change = payment - total_cost
    print(f"\nChange: ₱{change:.2f}")
    return True

# Main program
def main():
    # Welcome message
    print("Welcome to the Food Ordering System!")
    
    # Show menu
    menu = display_menu()
    
    # Get order
    order = get_order(menu)
    
    # Order summary
    print(f"\nOrder Summary:")
    print(f"Item: {order['name']}")
    print(f"Price: ₱{order['price']}")
    
    # Process payment
    process_payment(order['price'])
    
    # Exit message
    print("\nThank you for your order!")

# Start program
if __name__ == "__main__":
    main()