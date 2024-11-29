from tkinter import *
from PIL import ImageTk, Image  # pip install pillow

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x1000+0+0")

        # Load and resize the header image
        img1 = Image.open(r"D:\hotel_managemnet\images\img1.jpg")
        img1 = img1.resize((1550, 200), Image.Resampling.LANCZOS)  # Resize with smooth scaling
        self.photoimg1 = ImageTk.PhotoImage(img1)

        # Add header image to Label
        header_img = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        header_img.place(x=0, y=0, width=1550, height=200)  # Ensure height matches the resized image

        # Load and resize the logo image
        logo = Image.open(r"D:\hotel_managemnet\images\logo.jpg")
        logo = logo.resize((250, 200), Image.Resampling.LANCZOS)  # Resize with smooth scaling
        self.photoimg2 = ImageTk.PhotoImage(logo)

        # Add logo image to Label
        logo_img = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        logo_img.place(x=0, y=0, width=250, height=200)  # Ensure height matches the resized image

        # Title Label
        lbl_title = Label(
            self.root,
            text="HOTEL MANAGEMENT SYSTEM",
            font=("helvetica", 20, "bold"),
            bg="black",
            padx=6,
            fg="gold",
            bd=4,
            relief=RIDGE
        )
        lbl_title.place(x=0, y=200, width=1550, height=50)

        # ============== Main Frame ===============
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=250, width=1550, height=750)

        # ============== Menu Label ===============
        lbl_menu = Label(
            main_frame,
            text="Menu",
            font=("helvetica", 20, "bold"),
            bg="black",
            padx=6,
            fg="gold",
            bd=4,
            relief=RIDGE
        )
        lbl_menu.place(x=0, y=0, width=250, height=50)  # Place Menu Label in the main frame

        #================== Button frame ================
        btn_frame = Frame(main_frame,bd=4,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=35,width = 250,height = 190)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
