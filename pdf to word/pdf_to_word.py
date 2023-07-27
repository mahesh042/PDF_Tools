import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox 
from pdf2docx import Converter
import tkinter.ttk as ttk

# Declare variable 
progress_bar = None 

root = tk.Tk()

def update_progress(progress):
    progress_bar['value'] += progress
    root.update_idletasks()

def convert_to_word(file_path, output_file):
    global progress_bar
  
    try:
        progress_bar['value'] = 0
        update_progress(20)  

        cv = Converter(file_path)
        cv.convert(output_file, start=0, end=None)
        cv.close()

        update_progress(100)  
        messagebox.showinfo("Conversion Successful", f"{file_path} converted to Word as {output_file}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# GUI code

def convert_to_word_gui():
    global progress_bar

    root.title("PDF to Word Converter")  
    root.geometry("700x500")

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, file_path)

    def convert_file():
        file_path = input_entry.get()
        output_file = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word File", "*.docx")])
        if file_path and output_file:
            convert_to_word(file_path, output_file)
 
    input_label = ttk.Label(root, text="Select PDF File:")
    input_label.pack(pady=10)

    input_entry = ttk.Entry(root, width=50)
    input_entry.pack(pady=5)

    browse_button = ttk.Button(root, text="Browse", command=browse_file) 
    browse_button.pack(pady=5)

    # Create progressbar  
    progress_bar = ttk.Progressbar(root, length=500, mode='determinate')
    progress_bar.pack(pady=20)

    convert_button = ttk.Button(root, text="Convert to Word", command=convert_file)
    convert_button.pack(pady=10)

    root.mainloop()

if __name__ == '__main__':
    convert_to_word_gui()
