#Make by Amirali Zandi
import  qrcode
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

def generate_qr():
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    
    data = qr_text.get()
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    img = Image.open("qrcode.png")
    img = img.resize((300, 300), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.config(image=img)
    panel.image = img
    messagebox.showinfo("QR Code Generated", "QR Code saved as 'qrcode.png'")

root = tk.Tk()
root.title("QR Code Generator")
root.configure(background="black")
root.geometry("600x700")

qr_label = tk.Label(root, text="Enter text to generate QR Code:")
qr_label.configure(bg="darkred", fg="white")
qr_label.pack(pady=30)
qr_label.configure(width=30, height=3)


qr_text = tk.Entry(root, width=35, font=("Arial", 15))
qr_text.configure(bg="gray", fg="white")
qr_text.pack(pady=40)

generate_btn = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_btn.configure(bg="darkred", fg="white")
generate_btn.pack(pady=50)
generate_btn.configure(width=15, height=2)

panel = tk.Label(root)
panel.pack(pady=10)
#
root.mainloop()
