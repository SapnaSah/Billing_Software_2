# Billing Software

A simple billing software application built with **Python** and **Tkinter** for a graphical user interface. It allows users to manage customer information, add products to a cart, generate bills, and save/print them.

## Screenshots

### Main Page
![Screenshot 2025-05-25 162703](https://github.com/user-attachments/assets/15c87e2e-af8a-43c3-a2cd-bdd249cef1d5)

### Sample Input
![Screenshot 2025-05-25 163026](https://github.com/user-attachments/assets/13b71ff9-3cd9-4037-a488-3322cbd06f21)

### Sample Bill
![Screenshot 2025-05-25 163055](https://github.com/user-attachments/assets/085392cd-8647-40c4-a308-47dc7341ee6e)

### Saved Bill_at Notepad
![Screenshot 2025-05-25 180144](https://github.com/user-attachments/assets/d1383c46-3d49-4bca-a770-ec68b43e7061)


## Features

- **User-Friendly Interface**: Built with Tkinter for easy navigation.
- **Customer Management**: Input and display customer mobile number, name, and email.
- **Product Selection**: 
    - Categories: Grocery, Cosmetics, Drinks, Snacks, Fruits, Vegetables, Dairy, Bakery.
    - Subcategories and products with automatic price fetching.
- **Dynamic Cart**: Add multiple items with specified quantities.
- **Bill Generation**:
    - Detailed bill: product names, quantities, prices, and totals.
    - Calculates sub-total, 5% government tax, and grand total.
    - Shows bill number, date, and customer details.
- **Bill Management**:
    - **Save Bill**: Save bills as `.txt` files in the `bills` directory.
    - **Print Bill**: Print directly (requires a configured printer).
    - **Search Bill**: Retrieve saved bills by bill number.
- **Cart & Fields Control**:
    - **Add**: Add selected product and quantity to the cart.
    - **Clear Cart**: Remove all items from the current cart.
    - **Clear All**: Reset all input fields and the bill area.
- **Exit**: Close the application.
- **About**: Displays software information.

---

## Getting Started

### Prerequisites

- **Python 3.x**: [Download here](https://www.python.org/downloads/)
- **Pillow Library** (for images):
    ```bash
    pip install Pillow
    ```

### Installation

1. **Clone or download the repository** and navigate to the project folder.
2. **Create an `image` directory** in the project folder.
3. **Add images** to the `image` folder:
    - `a1.jpg`
    - `a2.jpg`
    - `a3.jpeg`
    - `a4.jpg`
    - `a5.jpeg`
    - `b1.jpg` (used in test.py)
    *(Use placeholder images if you don’t have these, but keep the names the same.)*
4. The `bills` directory will be created automatically when you save your first bill.

---

## Running the Application

To run the main billing software:

```bash
python main.py
```

To test image loading (for development):

```bash
python test.py
```

---

## Usage

1. **Enter Customer Details** (Mobile, Name, Email).
2. **Select Product** (Category > SubCategory > Product Name > Quantity).
3. **Add to Cart** and repeat as needed.
4. **Generate Bill** when ready.
5. **Save**, **Print**, **Clear Cart**, **Clear All**, or **Search Bill** as needed.
6. **Exit** to close the application.

---

## Project Structure

```
.
├── main.py                  # Main billing software script
├── test.py                  # Test script for image loading
├── README.md
├── image/                   # Image directory (create manually)
│   ├── a1.jpg
│   ├── a2.jpg
│   ├── a3.jpeg
│   ├── a4.jpg
│   ├── a5.jpeg
│   └── b1.jpg
└── bills/                   # Bills directory (auto-created)
    └── BILLYYYYMMDDHHMMSS.txt
```

---

## License

[MIT](LICENSE) (or specify your license)

---

## Acknowledgements

- [Tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [Pillow Docs](https://pillow.readthedocs.io/en/stable/)
