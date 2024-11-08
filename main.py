import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
from tkinter import *

def upload_file_pdf():
    path_file  = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    e1.config(state="normal")
    e1.delete(0, tk.END)  # ลบข้อความเก่าก่อน
    e1.insert(0, path_file)  # ใส่ path ของไฟล์ PDF ที่เลือก
    e1.config(state="readonly")

def pdf_to_image():
    try:
        path_file = e1.get()  # ดึง path ของไฟล์จาก e1
        save_format = format_var.get()
        if not path_file.endswith(".pdf"): # เช็กว่า หลังสุด มันมี .pdf ไหม
            raise ValueError("Please select a PDF file")
        save_path = filedialog.asksaveasfilename( filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")]) #รับประเภทได้แค่ jpg , png
        images = convert_from_path(path_file, dpi=300)
        for i, image in enumerate(images):
            page_number = i + 1  
            image.save(f"{save_path}_{page_number}.{save_format.lower()}", save_format)  
        messagebox.showinfo("Success",f"file path = {save_path}")
    except Exception as e:
        messagebox.showinfo("Error", f"Error: {e}")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("PDF to Image Converter")
root.geometry("300x200")  # เพิ่มขนาดหน้าต่างให้ใหญ่ขึ้น
root.config(bg="#f0f0f0")  # ตั้งสีพื้นหลังของหน้าต่าง


label1 = tk.Label(root,text="PDF to Image")
label1.pack()

e1=tk.Entry(root)
e1.pack()

# Dropdown 
format_var = StringVar(value="JPEG") #ค่าเริ่มต้น เป็น JPG ก่อน
file_format_dropdown = OptionMenu(root, format_var, "JPEG", "PNG")
file_format_dropdown.config(font=("Arial", 12), width=10, relief="solid")
file_format_dropdown.pack(pady=10)


#  Frame 
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20) 


b1 = tk.Button(button_frame, text="Upload file", command=upload_file_pdf,background = "green", fg = "white")
b1.pack(side="left", padx=10)

b2 = tk.Button(button_frame, text="Convert PDF", command=pdf_to_image,background = "red", fg = "white")
b2.pack(side="left", padx=10)


root.mainloop()
