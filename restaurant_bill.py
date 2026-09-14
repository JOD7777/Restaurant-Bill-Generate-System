# ============================================================
#              RESTAURANT BILL GENERATOR SYSTEM
# ============================================================

from datetime import datetime

# -------------------- RESTAURANT DETAILS --------------------

RESTAURANT_NAME = "TASTY BITES RESTAURANT"
RESTAURANT_ADDRESS = "123 Main Street, Kolkata"
GST_RATE = 5.0

# ------------------------- MENU -----------------------------

menu = {
    1: {"name": "Burger", "price": 120},
    2: {"name": "Pizza", "price": 250},
    3: {"name": "Fried Rice", "price": 180},
    4: {"name": "Chicken Biryani", "price": 220},
    5: {"name": "Momos", "price": 100},
    6: {"name": "French Fries", "price": 80},
    7: {"name": "Cold Drink", "price": 50},
    8: {"name": "Coffee", "price": 70},
    9: {"name": "Ice Cream", "price": 90},
}

# --------------------- DISPLAY MENU -------------------------

def display_menu():
    print("\n" + "=" * 55)
    print(f"{RESTAURANT_NAME:^55}")
    print("=" * 55)
    print(f"{'ID':<5}{'ITEM':<30}{'PRICE':>15}")
    print("-" * 55)

    for item_id, item in menu.items():
        print(
            f"{item_id:<5}"
            f"{item['name']:<30}"
            f"₹{item['price']:>13.2f}"
        )

    print("-" * 55)


# --------------------- TAKE ORDER ----------------------------

def take_order():
    order = []

    while True:
        try:
            item_id = int(input("\nEnter Item ID (0 to finish): "))

            if item_id == 0:
                break

            if item_id not in menu:
                print("❌ Invalid Item ID. Please try again.")
                continue

            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("❌ Quantity must be greater than 0.")
                continue

            item = menu[item_id]

            order.append({
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity,
                "total": item["price"] * quantity
            })

            print(
                f"✓ Added {quantity} x {item['name']} "
                f"= ₹{item['price'] * quantity:.2f}"
            )

        except ValueError:
            print("❌ Please enter a valid number.")

    return order


# --------------------- CALCULATE BILL ------------------------

def calculate_bill(order):
    subtotal = sum(item["total"] for item in order)

    # Discount rules
    if subtotal >= 2000:
        discount_rate = 10
    elif subtotal >= 1000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount = subtotal * discount_rate / 100
    taxable_amount = subtotal - discount

    gst = taxable_amount * GST_RATE / 100

    grand_total = taxable_amount + gst

    return subtotal, discount_rate, discount, gst, grand_total


# ----------------------- PRINT BILL --------------------------

def print_bill(order, customer_name, table_number):

    subtotal, discount_rate, discount, gst, grand_total = calculate_bill(order)

    bill_number = datetime.now().strftime("%Y%m%d%H%M%S")
    date_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    print("\n")
    print("=" * 65)
    print(f"{RESTAURANT_NAME:^65}")
    print(f"{RESTAURANT_ADDRESS:^65}")
    print("=" * 65)

    print(f"Bill No.     : {bill_number}")
    print(f"Date & Time  : {date_time}")
    print(f"Customer     : {customer_name}")
    print(f"Table No.    : {table_number}")

    print("-" * 65)
    print(
        f"{'ITEM':<25}"
        f"{'QTY':>8}"
        f"{'PRICE':>15}"
        f"{'TOTAL':>17}"
    )
    print("-" * 65)

    for item in order:
        print(
            f"{item['name']:<25}"
            f"{item['quantity']:>8}"
            f"₹{item['price']:>13.2f}"
            f"₹{item['total']:>15.2f}"
        )

    print("-" * 65)

    print(f"{'Subtotal':<48} ₹{subtotal:>12.2f}")

    if discount_rate > 0:
        print(
            f"{'Discount (' + str(discount_rate) + '%)':<48} "
            f"-₹{discount:>11.2f}"
        )
    else:
        print(f"{'Discount':<48} ₹{0:>12.2f}")

    print(f"{'GST (' + str(GST_RATE) + '%)':<48} ₹{gst:>12.2f}")

    print("=" * 65)
    print(f"{'GRAND TOTAL':<48} ₹{grand_total:>12.2f}")
    print("=" * 65)

    print(f"{'Thank you for visiting!':^65}")
    print(f"{'Please visit again ❤️':^65}")
    print("=" * 65)


# ----------------------- MAIN PROGRAM -----------------------

def main():

    print("\n")
    print("*" * 65)
    print(f"{'WELCOME TO ' + RESTAURANT_NAME:^65}")
    print("*" * 65)

    customer_name = input("\nEnter Customer Name: ")

    table_number = input("Enter Table Number: ")

    display_menu()

    print("\n🛒 Start taking order...")
    order = take_order()

    if not order:
        print("\n❌ No items ordered.")
        print("Thank you for visiting!")
        return

    print("\nGenerating bill...")

    print_bill(
        order,
        customer_name,
        table_number
    )


# ---------------------- PROGRAM START -----------------------

if __name__ == "__main__":
    main()