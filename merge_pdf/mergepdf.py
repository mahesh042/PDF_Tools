import PyPDF2
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk

def merge_pdfs(_pdfs, output_file):
    mergeFile = PyPDF2.PdfMerger()

    for _pdf in _pdfs:
        pdf_reader = PyPDF2.PdfReader(_pdf, 'rb')
        num_pages = len(pdf_reader.pages)
        for page_num in range(0, num_pages):
            mergeFile.append(pdf_reader, pages=(page_num, page_num+1))

    mergeFile.write(output_file)
    mergeFile.close()

def merge_pdfs_gui():
    root = tk.Tk()

    def browse_files():
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        file_list.delete(0, tk.END)
        for file_path in file_paths:
            file_list.insert(tk.END, file_path)

    def merge_files():
        files = file_list.get(0, tk.END)
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF File", "*.pdf")])
        if output_file:
            merge_pdfs(files, output_file)
            tk.messagebox.showinfo("Merge Complete", "PDF files merged successfully!")

    def delete_file():
        selected_indices = file_list.curselection()
        if selected_indices:
            for index in selected_indices[::-1]:
                file_list.delete(index)
                
                
    root.title("PDF Merger")
    root.geometry("700x500")


    file_list = tk.Listbox(root, selectmode=tk.MULTIPLE)
    file_list.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    browse_button = ttk.Button(root, text="Add Files", command=browse_files)
    browse_button.pack(side=tk.TOP, padx=10, pady=10)

    delete_button = ttk.Button(root, text="Delete File", command=delete_file)
    delete_button.pack(pady=5)
    
    merge_button = ttk.Button(root, text="Click here to Merge the selected PDF Files", command=merge_files)
    merge_button.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

    root.mainloop()

if __name__ == '__main__':
    merge_pdfs_gui()
