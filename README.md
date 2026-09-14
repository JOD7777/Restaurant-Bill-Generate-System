# 🍽️ Restaurant Bill Generator System

A simple, user-friendly **Restaurant Bill Generator System built with Python**.
This project allows restaurant staff to display a menu, take customer orders, calculate the subtotal, apply automatic discounts, calculate GST, and generate a professional formatted bill directly in the terminal.

---

## 📌 Project Overview

The **Restaurant Bill Generator System** is a command-line application designed to simplify restaurant billing operations.

The system provides:

* 📋 Restaurant menu display
* 🛒 Multiple-item ordering
* 🔢 Quantity management
* 💰 Automatic subtotal calculation
* 🏷️ Automatic discount calculation
* 🧾 GST calculation
* 👤 Customer information
* 🪑 Table number management
* 🕐 Automatic date and time
* 🆔 Automatic bill number generation
* 🖥️ Professional terminal bill format

This project is suitable for **Python beginners, students, and academic projects**.

---

## ✨ Features

### 📋 Menu Management

Displays available food items with their prices.

### 🛒 Order Management

Customers can select multiple food items and specify quantities.

### 💰 Automatic Billing

The system automatically calculates:

```text
Subtotal
Discount
GST
Grand Total
```

### 🏷️ Discount System

The application automatically applies discounts based on the subtotal:

|        Subtotal | Discount |
| --------------: | -------: |
|    Below ₹1,000 |       0% |
| ₹1,000 – ₹1,999 |       5% |
|  ₹2,000 or more |      10% |

### 🧾 GST Calculation

A **5% GST** is automatically calculated after applying the discount.

### 🆔 Bill Number

Each bill receives an automatically generated bill number using the current date and time.

### 🕐 Date & Time

The current date and time are automatically displayed on the generated bill.

---

## 🛠️ Technologies Used

* **Python 3**
* Python `datetime` module
* Terminal / Command Line Interface

No external Python packages are required.

---

## 📂 Project Structure

```text
Restaurant-Bill-Generator/
│
├── restaurant_bill.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Restaurant-Bill-Generator.git
```

### 2. Navigate to the Project

```bash
cd Restaurant-Bill-Generator
```

### 3. Check Python Installation

```bash
python3 --version
```

The project requires **Python 3.x**.

---

## ▶️ Run the Program

Run:

```bash
python3 restaurant_bill.py
```

On Windows, you can also use:

```bash
python restaurant_bill.py
```

---

## 🖥️ Example Usage

```text
*****************************************************************
                 WELCOME TO TASTY BITES RESTAURANT
*****************************************************************

Enter Customer Name: Supriyo
Enter Table Number: 5

=======================================================
                 TASTY BITES RESTAURANT
=======================================================
ID   ITEM                                  PRICE
-------------------------------------------------------
1    Burger                              ₹120.00
2    Pizza                               ₹250.00
3    Fried Rice                          ₹180.00
4    Chicken Biryani                     ₹220.00
5    Momos                               ₹100.00
6    French Fries                         ₹80.00
7    Cold Drink                           ₹50.00
8    Coffee                               ₹70.00
9    Ice Cream                            ₹90.00
-------------------------------------------------------

Enter Item ID (0 to finish): 2
Enter Quantity: 2

✓ Added 2 x Pizza = ₹500.00

Enter Item ID (0 to finish): 4
Enter Quantity: 1

✓ Added 1 x Chicken Biryani = ₹220.00

Enter Item ID (0 to finish): 0

Generating bill...
```

### Generated Bill

```text
=================================================================
                    TASTY BITES RESTAURANT
                    123 Main Street, Kolkata
=================================================================

Bill No.     : 20260915024710
Date & Time  : 15-09-2026 02:47 AM
Customer     : Supriyo
Table No.    : 5

-----------------------------------------------------------------
ITEM                          QTY          PRICE            TOTAL
-----------------------------------------------------------------
Pizza                           2        ₹250.00          ₹500.00
Chicken Biryani                1        ₹220.00          ₹220.00
-----------------------------------------------------------------

Subtotal                                           ₹720.00
Discount                                             ₹0.00
GST (5.0%)                                         ₹36.00

=================================================================
GRAND TOTAL                                        ₹756.00
=================================================================

                    Thank you for visiting!
                    Please visit again ❤️
=================================================================
```

---

## 🧮 Billing Formula

The application uses the following calculation:

### Subtotal

```text
Subtotal = Item Price × Quantity
```

for every ordered item.

### Discount

```text
Discount Amount = Subtotal × Discount Rate / 100
```

### Taxable Amount

```text
Taxable Amount = Subtotal - Discount
```

### GST

```text
GST = Taxable Amount × 5 / 100
```

### Grand Total

```text
Grand Total = Taxable Amount + GST
```

---

## 🔮 Future Improvements

The project can be expanded with:

* [ ] Graphical User Interface (GUI)
* [ ] SQLite/MySQL database
* [ ] Admin login system
* [ ] Customer database
* [ ] Food inventory management
* [ ] Printable invoices
* [ ] PDF bill generation
* [ ] Email bill functionality
* [ ] QR-code payment integration
* [ ] Multiple restaurant branches
* [ ] Daily/monthly sales reports
* [ ] Employee management
* [ ] Online ordering system
* [ ] Payment method selection
* [ ] Sales analytics dashboard

---

## 🎯 Learning Objectives

This project demonstrates practical use of:

* Python dictionaries
* Lists
* Functions
* Loops
* Conditional statements
* Exception handling
* User input
* Arithmetic operations
* String formatting
* Date and time handling
* Basic software/project structure

---

## 🤝 Contributing

Contributions are welcome!

### Steps

1. Fork this repository.
2. Create a new branch.

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes.

```bash
git commit -m "Add new feature"
```

5. Push your branch.

```bash
git push origin feature/new-feature
```

6. Open a Pull Request.

---

## ⚠️ Disclaimer

This project is created for **educational and demonstration purposes**.

The GST rate, restaurant information, menu prices, and discount rules included in the example are configurable and should be modified according to the actual restaurant's requirements and applicable local regulations.

---

## 👨‍💻 Author

**Supriyo Malik**

Cybersecurity & Advanced Networking Student

GitHub:
https://github.com/JOD7777

---

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for details.

---

⭐ If you find this project useful, consider giving the repository a **star**!
