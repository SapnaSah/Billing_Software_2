# Billing Software

This is a simple billing software application built using **Python** and the **Tkinter** library for the graphical user interface. It allows users to manage customer information, add products to a cart, generate bills, and save/print them.

---

## Features

* **User-Friendly Interface**: Built with Tkinter for an intuitive and easy-to-navigate experience.
* **Customer Management**: Input and display customer mobile number, name, and email.
* **Product Selection**:
    * Categorized products (Grocery, Cosmetics, Drinks, Snacks, Fruits, Vegetables, Dairy, Bakery).
    * Subcategories and individual products with their respective prices.
    * Automatic price fetching based on product selection.
* **Dynamic Cart**: Add multiple items with specified quantities.
* **Bill Generation**:
    * Generates a detailed bill with product names, quantities, prices, and totals.
    * Calculates sub-total, government tax (5%), and grand total.
    * Includes bill number, date, and customer details.
* **Bill Management**:
    * **Save Bill**: Save generated bills as text files (`.txt`) in a dedicated `bills` directory.
    * **Print Bill**: Print the generated bill directly (requires a default printer configured on the system).
    * **Search Bill**: Retrieve and display previously saved bills by their bill number.
* **Cart and Fields Control**:
    * **Add**: Adds selected product and quantity to the cart.
    * **Clear Cart**: Empties the current billing cart.
    * **Clear All**: Resets all input fields and the bill area.
* **Exit**: Close the application.
* **About**: Displays information about the software.

---

## Getting Started

### Prerequisites

* **Python 3.x**: Make sure you have Python installed on your system.
* **Pillow Library**: This is required for handling images. Install it using pip:
    ```bash
    pip install Pillow
    ```

### Installation

1.  **Clone the repository** (or download the source code):
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```
2.  **Create an `image` directory**: Inside the project directory, create a folder named `image`.
3.  **Add images**: Place the following image files into the `image` directory:
    * `good.jpg`
    * `gro1.jpg`
    * `b1.jpg`
    * `download.jpeg`
    * `mall.jpg`
    *(Note: Placeholder images are fine if you don't have these exact ones, but ensure they are named correctly.)*

### Running the Application

Execute the Python script:

```bash
python your_script_name.py# Billing_Software_2

Markdown

# Billing Software

This is a simple billing software application built using **Python** and the **Tkinter** library for the graphical user interface. It allows users to manage customer information, add products to a cart, generate bills, and save/print them.

---

## Features

* **User-Friendly Interface**: Built with Tkinter for an intuitive and easy-to-navigate experience.
* **Customer Management**: Input and display customer mobile number, name, and email.
* **Product Selection**:
    * Categorized products (Grocery, Cosmetics, Drinks, Snacks, Fruits, Vegetables, Dairy, Bakery).
    * Subcategories and individual products with their respective prices.
    * Automatic price fetching based on product selection.
* **Dynamic Cart**: Add multiple items with specified quantities.
* **Bill Generation**:
    * Generates a detailed bill with product names, quantities, prices, and totals.
    * Calculates sub-total, government tax (5%), and grand total.
    * Includes bill number, date, and customer details.
* **Bill Management**:
    * **Save Bill**: Save generated bills as text files (`.txt`) in a dedicated `bills` directory.
    * **Print Bill**: Print the generated bill directly (requires a default printer configured on the system).
    * **Search Bill**: Retrieve and display previously saved bills by their bill number.
* **Cart and Fields Control**:
    * **Add**: Adds selected product and quantity to the cart.
    * **Clear Cart**: Empties the current billing cart.
    * **Clear All**: Resets all input fields and the bill area.
* **Exit**: Close the application.
* **About**: Displays information about the software.

---

## Getting Started

### Prerequisites

* **Python 3.x**: Make sure you have Python installed on your system.
* **Pillow Library**: This is required for handling images. Install it using pip:
    ```bash
    pip install Pillow
    ```

### Installation

1.  **Clone the repository** (or download the source code):
    ```bash
    git clone <repository_url>
    cd <repository_folder>
    ```
2.  **Create an `image` directory**: Inside the project directory, create a folder named `image`.
3.  **Add images**: Place the following image files into the `image` directory:
    * `good.jpg`
    * `gro1.jpg`
    * `b1.jpg`
    * `download.jpeg`
    * `mall.jpg`
    *(Note: Placeholder images are fine if you don't have these exact ones, but ensure they are named correctly.)*

### Running the Application

Execute the Python script:

```bash
python your_script_name.py
(Replace your_script_name.py with the actual name of your Python file, e.g., bill_app.py)

Usage
Customer Details: Enter the customer's mobile number, name, and email in the "Customer" section.
Select Product:
Choose a Category from the dropdown.
Select a SubCategory.
Choose a Product Name.
The Price will automatically populate.
Enter the desired Qty (Quantity).
Add to Cart: Click the Add button to add the selected item to the cart. The bill area on the right will update.
Generate Bill: Once all items are added, click Generate Bill to finalize the bill with customer details, bill number, and totals.
Manage Bill:
Click Save Bill to save the current bill.
Click Print to print the bill.
Click Clear Cart to remove all items from the current cart without clearing customer details.
Click Clear to clear all fields and the bill area.
Click Search Bill to look up a past bill.
Exit: Click Exit to close the application.
Project Structure
.
├── your_script_name.py  # Main application script
└── image/              # Directory for images
    ├── good.jpg
    ├── gro1.jpg
    ├── b1.jpg
    ├── download.jpeg
    └── mall.jpg
└── bills/              # Directory where bills are saved (created automatically)
    └── BILLYYYYMMDDHHMMSS.txt
