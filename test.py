import tkinter as tk
from PIL import Image, ImageTk  # Make sure Pillow is installed

class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")  # Set the resolution
        self.root.title("Billing Software")

        try:
            img_2 = Image.open("image//b1.jpg")
            img_2 = img_2.resize((400, 100), Image.Resampling.LANCZOS)
            self.photoimg_2 = ImageTk.PhotoImage(img_2)
        except FileNotFoundError:
            print("Error: image/b1.jpg not found.")
            self.photoimg_2 = None

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = Bill_App(root)
    root.mainloop()
