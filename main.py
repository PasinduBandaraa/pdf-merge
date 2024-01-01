import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger


def merge_pdfs():
    pdfs = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if pdfs:
        merger = PdfMerger()
        for pdf in pdfs:
            merger.append(pdf)
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_file:
            merger.write(output_file)
            merger.close()
            messagebox.showinfo("Success", "PDFs merged successfully!")
        else:
            messagebox.showwarning("Warning", "Please select an output file.")
    else:
        messagebox.showwarning("Warning", "Please select PDF files to merge.")


root = tk.Tk()
root.title("PDF Merging Tool")

# Create a frame for better organization
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=30)

# Add an icon
icon = tk.PhotoImage(file="pdf_icon.png")  # Replace "pdf_icon.png" with your icon file
root.iconphoto(True, icon)

# Create and style widgets
title_label = tk.Label(main_frame, text="PDF Merger", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

merge_button = tk.Button(main_frame, text="Merge PDFs", command=merge_pdfs, width=15, height=2, bg="#4CAF50",
                         fg="white", font=("Arial", 12, "bold"))
merge_button.pack(pady=20)

info_label = tk.Label(main_frame, text="Select PDF files to merge", font=("Arial", 10))
info_label.pack()

root.mainloop()




