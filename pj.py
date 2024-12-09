import tkinter as tk
from tkinter import messagebox
import heapq
import random  
class TaskPlanner:
    def __init__(self, root):  
        self.root = root
        self.root.title("Daily Task Planner")
        self.tasks = []
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Task Name:").grid(row=0, column=0, padx=5, pady=5)
        self.task_name_entry = tk.Entry(self.root, width=30)
        self.task_name_entry.grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Duration (hours):").grid(row=1, column=0, padx=5, pady=5)
        self.task_duration_entry = tk.Entry(self.root, width=30)
        self.task_duration_entry.grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.root, text="Priority (1-10):").grid(row=2, column=0, padx=5, pady=5)
        self.task_priority_entry = tk.Entry(self.root, width=30)
        self.task_priority_entry.grid(row=2, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Generate Schedule", command=self.generate_schedule).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Tasks:").grid(row=5, column=0, columnspan=2)
        self.task_list = tk.Listbox(self.root, width=50, height=10)
        self.task_list.grid(row=6, column=0, columnspan=2, pady=10)
        tk.Label(self.root, text="Optimized Schedule:").grid(row=7, column=0, columnspan=2)
        self.schedule_text = tk.Text(self.root, width=50, height=10)
        self.schedule_text.grid(row=8, column=0, columnspan=2, pady=10)

    def add_task(self):
        name = self.task_name_entry.get().strip()
        try:
            duration = float(self.task_duration_entry.get())
            priority = int(self.task_priority_entry.get())            
            if name and duration > 0 and 1 <= priority <= 10:
                urgency = random.uniform(0.5, 1.5)  
                dynamic_priority = self.calculate_dynamic_priority(priority, duration, urgency)
                self.tasks.append((dynamic_priority, duration, name))
                self.task_list.insert(tk.END, f"{name} - {duration} hrs - Dynamic Priority: {dynamic_priority:.2f}")
                self.clear_entries()
            else:
                messagebox.showerror("Invalid Input", "Please enter valid task details.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for duration and priority.")

    def calculate_dynamic_priority(self, base_priority, duration, urgency):
        """
        AI-inspired function to calculate dynamic priority.
        The longer the task, the lower the priority, with some urgency factor.
        """
        priority_score = base_priority * (1 / duration) * urgency
        return max(1, min(priority_score, 10))  
    def clear_entries(self):
        self.task_name_entry.delete(0, tk.END)
        self.task_duration_entry.delete(0, tk.END)
        self.task_priority_entry.delete(0, tk.END)
    def generate_schedule(self):
        if not self.tasks:
            messagebox.showwarning("No Tasks", "Please add tasks before generating a schedule.")
            return
        total_hours = 24  
        available_time = total_hours
        self.tasks.sort(reverse=True, key=lambda task: task[0])
        schedule = []
        while self.tasks and available_time > 0:
            dynamic_priority, duration, name = self.tasks.pop(0)
            duration_to_schedule = min(duration, available_time)
            available_time -= duration_to_schedule
            schedule.append((name, duration_to_schedule))
        self.schedule_text.delete(1.0, tk.END)
        if schedule:
            self.schedule_text.insert(tk.END, "Scheduled Tasks (Descending Dynamic Priority):\n")
            for task in schedule:
                self.schedule_text.insert(tk.END, f"{task[0]} - {task[1]} hrs\n")
        else:
            self.schedule_text.insert(tk.END, "No tasks could be scheduled within the available time.")
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskPlanner(root)
    root.mainloop()
