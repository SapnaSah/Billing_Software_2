import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import os
import tempfile


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")  # Set the resolution
        self.root.title("Billing Software")

        # --- Top Images ---
        # Instead of hardcoding image paths, which might cause errors,
        # it's better to either ensure the images are in the same directory
        # or use a more robust way to handle file paths.  For this example,
        # I'll assume the images are in a subdirectory named "images".
        # If the images are not in a subdirectory, remove the "images/" part.
        try:
            img = Image.open("image/good.jpg")
            img = img.resize((400, 100), Image.Resampling.LANCZOS)
            self.photoimg = ImageTk.PhotoImage(img)
        except FileNotFoundError:
            print("Error: b1.jpg not found")
            self.photoimg = None  # Set to None to avoid errors later

        try:
            img_1 = Image.open("image/gro1.jpg")
            img_1 = img_1.resize((400, 100), Image.Resampling.LANCZOS)
            self.photoimg_1 = ImageTk.PhotoImage(img_1)
        except FileNotFoundError:
            print("Error: gro1.jpg not found")
            self.photoimg_1 = None

        try:
            img_2 = Image.open("image/b1.jpg")
            img_2 = img_2.resize((400, 100), Image.Resampling.LANCZOS)
            self.photoimg_2 = ImageTk.PhotoImage(img_2)
        except FileNotFoundError:
            print("Error: good.jpg not found.")
            self.photoimg_2 = None

        # Create labels for images, check if images were loaded.
        lbl_img = tk.Label(self.root, image=self.photoimg)
        lbl_img.place(x=0, y=0, width=400, height=100)
        lbl_img_1 = tk.Label(self.root, image=self.photoimg_1)
        lbl_img_1.place(x=400, y=0, width=400, height=100)
        lbl_img_2 = tk.Label(self.root, image=self.photoimg_2)
        lbl_img_2.place(x=800, y=0, width=400, height=100)

        # --- Title Label ---
        lbl_title = tk.Label(
            self.root,
            text="BILLING SOFTWARE USING PYTHON",
            font=("times new roman", 30, "bold"),  # Smaller font
            bg="white",
            fg="red",
        )
        lbl_title.place(x=0, y=100, width=1366, height=40)  # Adjusted height

        # --- Main Frame ---
        Main_Frame = tk.Frame(self.root, bd=5, relief=tk.GROOVE, bg="white")
        Main_Frame.place(x=0, y=140, width=1366, height=628)  # Adjusted y and height

        # --- Customer Frame ---
        Cust_Frame = tk.LabelFrame(
            Main_Frame,
            text="Customer",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="red",
        )
        Cust_Frame.place(x=10, y=10, width=300, height=150)  # Adjusted width and height.

        self.lbl_mob = tk.Label(
            Cust_Frame,
            text="Mobile No.",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="red",
        )
        self.lbl_mob.grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame, font=("times new roman", 12, "bold"), width=24)
        self.entry_mob.grid(row=0, column=1, padx=5, pady=2)

        self.lblCustName = tk.Label(
            Cust_Frame, font=("arial", 12, "bold"), bg="white", text="Customer Name", bd=4
        )
        self.lblCustName.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)

        self.txtCustName = ttk.Entry(Cust_Frame, font=("arial", 10, "bold"), width=24)
        self.txtCustName.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)

        self.lblEmail = tk.Label(
            Cust_Frame, font=("arial", 12, "bold"), bg="white", text="Email", bd=4
        )
        self.lblEmail.grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)

        self.txtEmail = ttk.Entry(Cust_Frame, font=("arial", 10, "bold"), width=24)
        self.txtEmail.grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)

        # --- Product Frame ---
        Product_Frame = tk.LabelFrame(
            Main_Frame,
            text="Product",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="red",
        )
        Product_Frame.place(x=320, y=10, width=680, height=150)  # Adjusted width

        # Category
        self.lblCategory = tk.Label(
            Product_Frame, font=("arial", 12, "bold"), bg="white", text="Category", bd=4
        )
        self.lblCategory.grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame, font=("arial", 10, "bold"), width=20)  # Shorter width
        self.Combo_Category.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)

        # Subcategory
        self.lblSubCategory = tk.Label(
            Product_Frame, font=("arial", 12, "bold"), bg="white", text="SubCategory", bd=4
        )
        self.lblSubCategory.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)

        self.ComboSubCategory = ttk.Combobox(
            Product_Frame, font=("arial", 10, "bold"), width=20, state="readonly"
        )  # Shorter width
        self.ComboSubCategory.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)

        # Product Name
        self.lblProduct = tk.Label(
            Product_Frame, font=("arial", 12, "bold"), bg="white", text="Product Name", bd=4
        )
        self.lblProduct.grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)

        self.ComboProduct = ttk.Combobox(Product_Frame, font=("arial", 10, "bold"), width=20)  # Shorter width.
        self.ComboProduct.grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)

        # Price
        self.lblPrice = tk.Label(
            Product_Frame, font=("arial", 12, "bold"), bg="white", text="Price", bd=4
        )
        self.lblPrice.grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        self.ComboPrice = ttk.Combobox(
            Product_Frame, font=("arial", 10, "bold"), width=20, state="readonly"
        )  # Shorter width
        self.ComboPrice.grid(row=0, column=3, sticky=tk.W, padx=5, pady=2)

        # Qty
        self.lblQty = tk.Label(
            Product_Frame, font=("arial", 12, "bold"), bg="white", text="Qty", bd=4
        )
        self.lblQty.grid(row=1, column=2, sticky=tk.W, padx=5, pady=2)

        self.ComboQty = ttk.Entry(Product_Frame, font=("arial", 10, "bold"), width=22)  # Shorter width
        self.ComboQty.grid(row=1, column=3, sticky=tk.W, padx=5, pady=2)

        # --- Middle Frame ---
        MiddleFrame = tk.Frame(Main_Frame, bd=10)
        MiddleFrame.place(x=10, y=170, width=1000, height=300)  # Adjusted y

        # image4
        try:
            img_2 = Image.open("image/download.jpeg")
            img_2 = img_2.resize((400, 280), Image.Resampling.LANCZOS)  # Adjusted size
            self.photoimg_2 = ImageTk.PhotoImage(img_2)
        except FileNotFoundError:
            print("Error: download.jpeg not found.")
            self.photoimg_2 = None

        lbl_img_2 = tk.Label(MiddleFrame, image=self.photoimg_2)
        lbl_img_2.place(x=0, y=0, width=400, height=280)

        # image5
        try:
            img_3 = Image.open("image/mall.jpg")
            img_3 = img_3.resize((400, 280), Image.Resampling.LANCZOS)  # Adjusted Size
            self.photoimg_3 = ImageTk.PhotoImage(img_3)
        except FileNotFoundError:
            print("Error: mall.jpg not found.")
            self.photoimg_3 = None

        lbl_img_3 = tk.Label(MiddleFrame, image=self.photoimg_3)
        lbl_img_3.place(x=410, y=0, width=400, height=280)  # Adjusted X

        # --- Right Frame (Bill Area) ---
        RightLabelFrame = tk.LabelFrame(
            Main_Frame,
            text="Bill Area",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="blue",
        )
        RightLabelFrame.place(x=1020, y=10, width=330, height=460)  # Adjusted

        scroll_y = tk.Scrollbar(RightLabelFrame, orient=tk.VERTICAL)
        self.textarea = tk.Text(
            RightLabelFrame,
            yscrollcommand=scroll_y.set,
            bg="white",
            fg="blue",
            font=("times new roman", 12),  # Smaller font
        )
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=tk.BOTH, expand=1)

        # --- Bottom Frame (Bill Counter) ---
        Bottom_Frame = tk.LabelFrame(
            Main_Frame,
            text="Bill Counter",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="blue",
        )
        Bottom_Frame.place(x=0, y=480, width=1010, height=140)  # Adjusted y and width.

        self.lblSubTotal = tk.Label(
            Bottom_Frame, font=("arial", 12, "bold"), bg="white", text="Sub Total", bd=4
        )
        self.lblSubTotal.grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.EntySubTotal = ttk.Entry(Bottom_Frame, font=("arial", 10, "bold"), width=20)
        self.EntySubTotal.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)

        self.lbl_tax = tk.Label(
            Bottom_Frame, font=("arial", 12, "bold"), bg="white", text="Gov Tax", bd=4
        )
        self.lbl_tax.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        self.txt_tax = ttk.Entry(Bottom_Frame, font=("arial", 10, "bold"), width=20)
        self.txt_tax.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)

        self.lblAmountTotal = tk.Label(
            Bottom_Frame, font=("arial", 12, "bold"), bg="white", text="Total", bd=4
        )
        self.lblAmountTotal.grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        self.txtAmountTotal = ttk.Entry(Bottom_Frame, font=("arial", 10, "bold"), width=20)
        self.txtAmountTotal.grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)

        # --- Button Frame ---
        btn_Frame = tk.Frame(Bottom_Frame, bd=2, bg="white")
        btn_Frame.place(x=250, y=0, width=750, height=120)  # Adjusted x and width.
        self.btnAdd = tk.Button(
            btn_Frame,
            text="Add",
            font=("arial", 12, "bold"),
            bg="blue",
            fg="white",
            width=10,
            command=self.add_item,
        )
        self.btnAdd.grid(row=0, column=0, padx=5, pady=5)
        self.btnGenerate = tk.Button(
            btn_Frame,
            text="Generate Bill",
            font=("arial", 12, "bold"),
            bg="green",
            fg="white",
            width=12,  # Shortened
            command=self.generate_bill,
        )
        self.btnGenerate.grid(row=0, column=1, padx=5, pady=5)
        self.btnClear = tk.Button(
            btn_Frame,
            text="Clear",
            font=("arial", 12, "bold"),
            bg="orange",
            fg="white",
            width=10,
            command=self.clear,
        )
        self.btnClear.grid(row=0, column=2, padx=5, pady=5)
        self.btnExit = tk.Button(
            btn_Frame,
            text="Exit",
            font=("arial", 12, "bold"),
            bg="red",
            fg="white",
            width=10,
            command=self.root.destroy,
        )
        self.btnExit.grid(row=0, column=3, padx=5, pady=5)
        self.btnSave = tk.Button(
            btn_Frame,
            text="Save Bill",
            font=("arial", 12, "bold"),
            bg="purple",
            fg="white",
            width=10,
            command=self.save_bill,
        )
        self.btnSave.grid(row=1, column=1, padx=5, pady=5)
        self.btnClearCart = tk.Button(
            btn_Frame,
            text="Clear Cart",
            font=("arial", 12, "bold"),
            bg="gray",
            fg="white",
            width=10,
            command=self.clear_cart,
        )
        self.btnClearCart.grid(row=1, column=2, padx=5, pady=5)
        self.btnPrint = tk.Button(
            btn_Frame,
            text="Print",
            font=("arial", 12, "bold"),
            bg="teal",
            fg="white",
            width=10,
            command=self.print_bill,
        )
        self.btnPrint.grid(row=1, column=0, padx=5, pady=5)

        self.btnSearch = tk.Button(
            btn_Frame,
            text="Search Bill",
            font=("arial", 12, "bold"),
            bg="brown",
            fg="white",
            width=10,
            command=self.search_bill,
        )
        self.btnSearch.grid(row=1, column=3, padx=5, pady=5)

        self.btnAbout = tk.Button(
            btn_Frame,
            text="About",
            font=("arial", 12, "bold"),
            bg="black",
            fg="white",
            width=10,
            command=self.about,
        )
        self.btnAbout.grid(row=1, column=4, padx=5, pady=5)

        # --- Data ---
        self.products = {
            "Grocery": {
                "Rice": {"Basmati": 60, "Sona Masoori": 50},
                "Oil": {"Sunflower": 120, "Mustard": 110},
                "Sugar": {"White Sugar": 40, "Brown Sugar": 45},
                "Salt": {"Table Salt": 20, "Rock Salt": 25},
                "Spices": {"Turmeric": 30, "Chili Powder": 35},
            },
            "Cosmetics": {
                "Face": {"Face Wash": 150, "Face Cream": 200},
                "Hair": {"Shampoo": 180, "Hair Oil": 90},
                "Body": {"Body Lotion": 250, "Sunscreen": 300},
                "Makeup": {"Lipstick": 500, "Foundation": 800},
                "Perfume": {"Eau de Toilette": 1000, "Eau de Parfum": 1500},
            },
            "Drinks": {
                "Soft Drink": {"Coke": 40, "Pepsi": 40},
                "Juice": {"Orange": 60, "Apple": 70},
                "Water": {"Mineral Water": 20, "Flavored Water": 25},
                "Energy Drink": {"Red Bull": 150, "Monster": 200},
                "Coffee": {"Instant Coffee": 250, "Ground Coffee": 300},
            },
            "Snacks": {
                "Chips": {"Lays": 20, "KurKure": 15},
                "Biscuits": {"Parle-G": 10, "Bourbon": 25},
                "Namkeen": {"Aloo Bhujia": 30, "Sev": 25},
                "Chocolates": {"Dairy Milk": 50, "Munch": 20},
                "Nuts": {"Cashew": 200, "Almonds": 250},
            },
            "Fruits": {
                "Apple": {"Red Apple": 100, "Green Apple": 80},
                "Banana": {"Yellow Banana": 30, "Raw Banana": 20},
                "Mango": {"Alphonso": 150, "Kesar": 120},
                "Grapes": {"Black Grapes": 60, "Green Grapes": 50},
            },
            "Vegetables": {
                "Potato": {"Aloo": 20, "Sweet Potato": 30},
                "Tomato": {"Red Tomato": 25, "Green Tomato": 20},
                "Onion": {"Red Onion": 15, "White Onion": 20},
                "Carrot": {"Red Carrot": 30, "Orange Carrot": 25},
                "Cabbage": {"Green Cabbage": 20, "Red Cabbage": 25},
            },
            "Dairy": {
                "Milk": {"Full Cream": 50, "Toned": 40},
                "Butter": {"Amul Butter": 200, "Britannia": 180},
                "Cheese": {"Amul Cheese": 250, "Britannia Cheese": 230},
                "Curd": {"Amul Curd": 60, "Mother Dairy": 55},
                "Paneer": {"Amul Paneer": 300, "Nandini Paneer": 280},
            },
            "Bakery": {
                "Bread": {"White Bread": 30, "Brown Bread": 35},
                "Cake": {"Chocolate Cake": 500, "Vanilla Cake": 400},
                "Pastry": {"Chocolate Pastry": 100, "Fruit Pastry": 120},
                "Cookies": {"Chocolate Chip": 150, "Oreo": 200},
            },
        }
        self.Combo_Category["values"] = list(self.products.keys())
        self.Combo_Category.bind("<<ComboboxSelected>>", self.update_subcategories)
        self.ComboSubCategory.bind("<<ComboboxSelected>>", self.update_products)
        self.ComboProduct.bind("<<ComboboxSelected>>", self.update_price)
        self.cart = []
        self.bill_number_prefix = "BILL"  # Class variable for bill prefix

    def update_subcategories(self, event=None):
        cat = self.Combo_Category.get()
        if cat:
            self.ComboSubCategory["values"] = list(self.products[cat].keys())
            self.ComboSubCategory.set("")
            self.ComboProduct.set("")
            self.ComboPrice.set("")

    def update_products(self, event=None):
        cat = self.Combo_Category.get()
        subcat = self.ComboSubCategory.get()
        if cat and subcat:
            self.ComboProduct["values"] = list(self.products[cat][subcat].keys())
            self.ComboProduct.set("")
            self.ComboPrice.set("")

    def update_price(self, event=None):
        cat = self.Combo_Category.get()
        subcat = self.ComboSubCategory.get()
        prod = self.ComboProduct.get()
        if cat and subcat and prod:
            price = self.products[cat][subcat][prod]
            self.ComboPrice.set(str(price))

    def add_item(self):
        cat = self.Combo_Category.get()
        subcat = self.ComboSubCategory.get()
        prod = self.ComboProduct.get()
        price = self.ComboPrice.get()
        qty = self.ComboQty.get()
        if not (cat and subcat and prod and price and qty):
            tk.messagebox.showwarning("Input Error", "Please fill all product fields.")
            return
        try:
            qty = int(qty)
            price = float(price)
            if qty <= 0:
                raise ValueError
        except ValueError:
            tk.messagebox.showerror("Input Error", "Quantity must be a positive integer.")
            return

        # Check for duplicate product in cart
        for item in self.cart:
            if item["category"] == cat and item["subcategory"] == subcat and item["product"] == prod:
                item["qty"] += qty
                item["total"] = item["qty"] * item["price"]
                self.update_bill_area()
                self.clear_product_fields()
                return

        self.cart.append(
            {
                "category": cat,
                "subcategory": subcat,
                "product": prod,
                "price": price,
                "qty": qty,
                "total": price * qty,
            }
        )
        self.update_bill_area()
        self.clear_product_fields()

    def update_bill_area(self):
        self.textarea.delete(1.0, tk.END)
        self.textarea.insert(tk.END, f"{'Product':20}{'Qty':>10}{'Price':>10}{'Total':>10}\n")
        self.textarea.insert(tk.END, "-" * 50 + "\n")
        subtotal = 0
        for item in self.cart:
            self.textarea.insert(
                tk.END, f"{item['product']:20}{item['qty']:>10}{item['price']:>10.2f}{item['total']:>10.2f}\n"
            )
            subtotal += item["total"]  # Corrected lineself.EntySubTotal.delete(0, tk.END)
        self.EntySubTotal.insert(0, f"{subtotal:.2f}")
        tax = subtotal * 0.05
        self.txt_tax.delete(0, tk.END)
        self.txt_tax.insert(0, f"{tax:.2f}")
        total = subtotal + tax
        self.txtAmountTotal.delete(0, tk.END)
        self.txtAmountTotal.insert(0, f"{total:.2f}")

    def clear_product_fields(self):
        self.Combo_Category.set("")
        self.ComboSubCategory.set("")
        self.ComboProduct.set("")
        self.ComboPrice.set("")
        self.ComboQty.delete(0, tk.END)

    def generate_bill(self):
        import datetime

        self.textarea.delete(1.0, tk.END)
        self.bill_no = f"{self.bill_number_prefix}{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"  # Use class variable
        self.textarea.insert(tk.END, f"\tBILLING SOFTWARE\n")
        self.textarea.insert(tk.END, f"Bill No: {self.bill_no}\n")
        self.textarea.insert(
            tk.END, f"Date: {datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
        )
        self.textarea.insert(tk.END, f"Customer Name: {self.txtCustName.get()}\n")
        self.textarea.insert(tk.END, f"Mobile No: {self.entry_mob.get()}\n")
        self.textarea.insert(tk.END, f"Email: {self.txtEmail.get()}\n")
        self.textarea.insert(tk.END, "-" * 50 + "\n")
        self.textarea.insert(tk.END, f"{'Product':20}{'Qty':>10}{'Price':>10}{'Total':>10}\n")
        self.textarea.insert(tk.END, "-" * 50 + "\n")
        subtotal = 0
        for item in self.cart:
            self.textarea.insert(
                tk.END, f"{item['product']:20}{item['qty']:>10}{item['price']:>10.2f}{item['total']:>10.2f}\n"
            )
            subtotal += item["total"]
        self.textarea.insert(tk.END, "-" * 50 + "\n")
        tax = subtotal * 0.05
        total = subtotal + tax
        self.textarea.insert(tk.END, f"Sub Total: {subtotal:.2f}\n")
        self.textarea.insert(tk.END, f"Gov Tax: {tax:.2f}\n")
        self.textarea.insert(tk.END, f"Total: {total:.2f}\n")
        self.current_bill_no = self.bill_no  # Store the bill number
        self.current_bill_text = self.textarea.get(1.0, tk.END)

    def clear(self):
        self.cart.clear()
        self.textarea.delete(1.0, tk.END)
        self.EntySubTotal.delete(0, tk.END)
        self.txt_tax.delete(0, tk.END)
        self.txtAmountTotal.delete(0, tk.END)
        self.clear_product_fields()
        self.txtCustName.delete(0, tk.END)
        self.entry_mob.delete(0, tk.END)
        self.txtEmail.delete(0, tk.END)

    def save_bill(self):
        if not hasattr(self, "current_bill_no") or not hasattr(self, "current_bill_text"):
            tk.messagebox.showwarning("No Bill", "Please generate a bill before saving.")
            return
        bills_dir = os.path.join(os.getcwd(), "bills")
        if not os.path.exists(bills_dir):
            os.makedirs(bills_dir)
        filename = os.path.join(bills_dir, f"{self.current_bill_no}.txt")
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(self.current_bill_text)
            tk.messagebox.showinfo("Saved", f"Bill saved as {filename}")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error saving bill: {e}")

    def clear_cart(self):
        self.cart.clear()
        self.update_bill_area()

    def print_bill(self):
        if not hasattr(self, 'current_bill_text'):
            tk.messagebox.showwarning("No Bill", "Please generate a bill before printing.")
            return

        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as tf:
                tf.write(self.current_bill_text)
            temp_path = tf.name
            os.startfile(temp_path, 'print')
        except Exception as e:
            tk.messagebox.showerror("Print Error", f"Could not print bill: {e}")

    def search_bill(self):
        bills_dir = os.path.join(os.getcwd(), "bills")
        if not os.path.exists(bills_dir):
            tk.messagebox.showinfo("No Bills", "No bills have been saved yet.")
            return
        bill_no = tk.simpledialog.askstring("Search Bill", "Enter Bill Number (e.g., BILL20250513123456):")
        if not bill_no:
            return
        filename = os.path.join(bills_dir, f"{bill_no}.txt")
        if not os.path.exists(filename):
            tk.messagebox.showerror("Not Found", f"Bill {bill_no} not found.")
            return
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                bill_text = f.read()
            self.textarea.delete(1.0, tk.END)
            self.textarea.insert(tk.END, bill_text)
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error reading bill: {e}")

    def about(self):
        tk.messagebox.showinfo("About", "Billing Software\nDeveloped in Python with Tkinter\n© 2025")


if __name__ == "__main__":
    root = tk.Tk()
    obj = Bill_App(root)
    root.mainloop()
