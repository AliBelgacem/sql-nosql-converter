import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
from converter import sql_to_nosql, nosql_to_sql

class ConverterGUI:
    def __init__(self, root):
        root.title("SQL to NoSQL Converter")
        root.geometry("800x600")

        tab_control = ttk.Notebook(root)
        self.sql_to_nosql_tab = ttk.Frame(tab_control)
        self.nosql_to_sql_tab = ttk.Frame(tab_control)

        tab_control.add(self.sql_to_nosql_tab, text="SQL to NoSQL")
        tab_control.add(self.nosql_to_sql_tab, text="NoSQL to SQL")
        tab_control.pack(expand=1, fill="both")

        self.build_sql_to_nosql_tab()
        self.build_nosql_to_sql_tab()

    # ------------------------
    # SQL to NoSQL TAB
    # ------------------------
    def build_sql_to_nosql_tab(self):

        load_SQL_btn = ttk.Button(self.sql_to_nosql_tab, text="Load SQL from file", command=self.load_sql)
        load_SQL_btn.pack(pady=5)

        ttk.Label(self.sql_to_nosql_tab, text="Enter SQL:", font=("Arial", 12)).pack(pady=5)

        self.sql_input = scrolledtext.ScrolledText(self.sql_to_nosql_tab, height=10)
        self.sql_input.pack(fill="both", padx=10, pady=5)

        convert_btn = ttk.Button(self.sql_to_nosql_tab, text="Convert to NoSQL", command=self.convert_sql)
        convert_btn.pack(pady=5)

        ttk.Label(self.sql_to_nosql_tab, text="Output (JSON):", font=("Arial", 12)).pack(pady=5)

        self.nosql_output = scrolledtext.ScrolledText(self.sql_to_nosql_tab, height=10)
        self.nosql_output.pack(fill="both", padx=10, pady=5)

        save_NoSQL_btn = ttk.Button(self.sql_to_nosql_tab, text="Save to JSON file", command=lambda:self.save_to_file(self.nosql_output, "json"))
        save_NoSQL_btn.pack(pady=5)

    def convert_sql(self):
        sql_text = self.sql_input.get("1.0", tk.END).strip()
        if not sql_text:
            messagebox.showwarning("Warning", "SQL input is empty")
            return
        try:
            result = sql_to_nosql(sql_text)
            self.nosql_output.delete("1.0", tk.END)
            self.nosql_output.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed:\n{e}")

    def load_sql(self):
        path = filedialog.askopenfilename(filetypes=[("SQL Files", "*.sql")])
        if not path:
            return

        with open(path, "r", encoding="utf-8") as f:
            sql_text = f.read()
        self.sql_input.delete("1.0", tk.END)
        self.sql_input.insert(tk.END, sql_text)
        
    def save_to_file(self, text_area, mode):
        result = text_area.get("1.0", tk.END).strip()
        if not result:
            messagebox.showwarning("Warning", "Nothing to save!")
            return

        if mode == "sql":
            filetypes = [("SQL Files", "*.sql"), ("All Files", "*.*")]
            default_ext = ".sql"
        else:
            filetypes = [("JSON Files", "*.json"), ("All Files", "*.*")]
            default_ext = ".json"

        path = filedialog.asksaveasfilename(
            title="Save File",
            filetypes=filetypes,
            defaultextension=default_ext
        )
        if not path:
            return

        with open(path, "w", encoding="utf-8") as f:
            f.write(result)

        messagebox.showinfo("Saved", "File saved successfully!")

    # ------------------------
    # NoSQL to SQL TAB
    # ------------------------
    def build_nosql_to_sql_tab(self):

        load_NoSQL_btn = ttk.Button(self.nosql_to_sql_tab, text="Load JSON from file", command=self.load_nosql)
        load_NoSQL_btn.pack(pady=5)

        ttk.Label(self.nosql_to_sql_tab, text="Enter JSON:", font=("Arial", 12)).pack(pady=5)

        self.json_input = scrolledtext.ScrolledText(self.nosql_to_sql_tab, height=10)
        self.json_input.pack(fill="both", padx=10, pady=5)

        convert_btn = ttk.Button(self.nosql_to_sql_tab, text="Convert to SQL", command=self.convert_nosql)
        convert_btn.pack(pady=5)

        ttk.Label(self.nosql_to_sql_tab, text="Output (SQL):", font=("Arial", 12)).pack(pady=5)

        self.sql_output = scrolledtext.ScrolledText(self.nosql_to_sql_tab, height=10)
        self.sql_output.pack(fill="both", padx=10, pady=5)

        save_SQL_btn = ttk.Button(self.nosql_to_sql_tab, text="Save to SQL file", command=lambda:self.save_to_file(self.sql_output, "sql"))
        save_SQL_btn.pack(pady=5)

    def convert_nosql(self):
        json_text = self.json_input.get("1.0", tk.END).strip()
        if not json_text:
            messagebox.showwarning("Warning", "JSON input is empty")
            return
        try:
            result = nosql_to_sql(json_text)
            self.sql_output.delete("1.0", tk.END)
            self.sql_output.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed:\n{e}")

    def load_nosql(self):
        path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if not path:
            return

        with open(path, "r", encoding="utf-8") as f:
            json_text = f.read()

        self.json_input.delete("1.0", tk.END)
        self.json_input.insert(tk.END, json_text)

