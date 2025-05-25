# Billing Software
A simple billing software application built with **Python** and **Tkinter** for a graphical user interface. It allows users to manage customer information, add products to a cart, generate bills, and save/print them.

## Screenshots

### Main Page
![Screenshot 2025-05-25 162703](https://github.com/user-attachments/assets/15c87e2e-af8a-43c3-a2cd-bdd249cef1d5)

### Product Entry
![Screenshot 2025-05-25 212855](https://github.com/user-attachments/assets/15de9b39-e80e-4911-9a7b-a7925cf077ee)


### Sample Input
![Screenshot 2025-05-25 213321](https://github.com/user-attachments/assets/0f780678-5ace-464b-a08c-101a4c47f88d)

### More Product Entry
![Screenshot 2025-05-25 213008](https://github.com/user-attachments/assets/b8b3cab5-c100-491f-8503-c512bc493113)

### Sample Bill
![Screenshot 2025-05-25 213029](https://github.com/user-attachments/assets/e5ed6736-0fe7-415a-9fe3-1493e2f4e99c)

### Saved Bill_at Notepad
![Screenshot 2025-05-25 214442](https://github.com/user-attachments/assets/439ccb4a-0c8b-46d2-90c9-a193bbc421f1)

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
