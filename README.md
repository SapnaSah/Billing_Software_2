# Billing Software

A simple billing software application built with **Python** and **Tkinter** for a graphical user interface. It allows users to manage customer information, add products to a cart, generate bills, and save/print them.

---

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

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd Billing_Software_2
    ```
2. **Create an `image` directory** in the project folder.
3. **Add images** to the `image` folder:
    - `good.jpg`
    - `gro1.jpg`
    - `b1.jpg`
    - `download.jpeg`
    - `mall.jpg`
    *(Use placeholder images if you don’t have these, but keep the names the same.)*
4. The `bills` directory will be created automatically when you save your first bill.

---

## Running the Application

```bash
python your_script_name.py
```
*Replace `your_script_name.py` with the actual Python script’s name, e.g., `bill_app.py`.*

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
├── your_script_name.py      # Main script
├── image/                   # Image directory
│   ├── good.jpg
│   ├── gro1.jpg
│   ├── b1.jpg
│   ├── download.jpeg
│   └── mall.jpg
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
