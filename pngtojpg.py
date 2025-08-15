import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

#Convert opration
def convert_image():
    png_path = filedialog.askopenfilename(
        title="Select PNG File",
        filetypes=[("PNG Files", "*.png")]
    )
    if png_path:
        try:
            img = Image.open(png_path).convert("RGB")
            save_path = filedialog.asksaveasfilename(
                defaultextension=".jpg",
                filetypes=[("JPEG Files", "*.jpg")],
                title="Save as JPG"
            )
            if save_path:
                img.save(save_path, "JPEG")
                messagebox.showinfo("Success", "Conversion Successful!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

# Main Window
root = tk.Tk()
root.title("PNG to JPG Converter")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#1E1E2E")

# Title Label
title_label = tk.Label(root, text="Enter a png file to convert into jpg file", font=("Helvetica", 12, "bold"), bg="#1E1E2E", fg="#E0E0E0")
title_label.pack(pady=20)

# Convert Button
convert_btn = tk.Button(
    root, 
    text="Select PNG File",
    command=convert_image,
    font=("Helvetica", 12, "bold"),
    bg="#00A8E8",
    fg="white",
    relief="flat",
    activebackground="#0072FF",
    activeforeground="white",
    padx=20,
    pady=10
)
convert_btn.pack(pady=20)

# Footer
footer_label = tk.Label(root, text="Made by Rishi", font=("Helvetica", 9), bg="#1E1E2E", fg="#AAAAAA")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
