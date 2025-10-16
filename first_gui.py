import tkinter as tk
from tkinter import messagebox
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Todo List Application")
        self.root.geometry("500x400")
        
        self.tasks = []
        self.data_file = "todo_data.json"
        
        self.load_data()
        self.create_widgets()
        self.update_task_list()
    
    def create_widgets(self):
        # Input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        self.task_entry = tk.Entry(input_frame, width=40, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", lambda event: self.add_task())
        
        add_button = tk.Button(input_frame, text="Add Task", 
                              command=self.add_task, bg="lightgreen")
        add_button.pack(side=tk.LEFT, padx=5)
        
        # Task list frame
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Listbox with scrollbar
        self.task_listbox = tk.Listbox(list_frame, font=("Arial", 12), 
                                      selectmode=tk.SINGLE)
        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
        
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)
        
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Buttons frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)
        
        complete_button = tk.Button(button_frame, text="Mark Complete", 
                                   command=self.mark_complete, bg="lightblue")
        complete_button.pack(side=tk.LEFT, padx=5)
        
        delete_button = tk.Button(button_frame, text="Delete Task", 
                                command=self.delete_task, bg="lightcoral")
        delete_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(button_frame, text="Clear All", 
                               command=self.clear_all, bg="orange")
        clear_button.pack(side=tk.LEFT, padx=5)
    
    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
            self.save_data()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = not self.tasks[selected_index]["completed"]
            self.update_task_list()
            self.save_data()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
            self.save_data()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task!")
    
    def clear_all(self):
        if messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.tasks.clear()
            self.update_task_list()
            self.save_data()
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            text = task["text"]
            if task["completed"]:
                text = f"✓ {text}"
            self.task_listbox.insert(tk.END, text)
    
    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    self.tasks = json.load(f)
            except:
                self.tasks = []
    
    def save_data(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()