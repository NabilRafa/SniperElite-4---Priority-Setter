import tkinter as tk
from tkinter import messagebox
import psutil
import threading
import time

class PrioritySetterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Priority Setter - By Nabil Rafa \\ @nabilr.a95")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        self.monitoring = False
        self.monitor_thread = None
        self.current_pid = None
        
        # UI Elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="Process Priority Setter", 
            font=("Arial", 16, "bold"),
            pady=10
        )
        title_label.pack()
        
        # PID Input Frame
        input_frame = tk.Frame(self.root, pady=10)
        input_frame.pack()
        
        pid_label = tk.Label(input_frame, text="Process ID (PID):", font=("Arial", 10))
        pid_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        self.pid_entry = tk.Entry(input_frame, width=20, font=("Arial", 10))
        self.pid_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Start/Stop Button
        self.toggle_button = tk.Button(
            self.root,
            text="Start Monitoring",
            command=self.toggle_monitoring,
            font=("Arial", 11, "bold"),
            bg="#4CAF50",
            fg="white",
            width=20,
            height=2,
            cursor="hand2"
        )
        self.toggle_button.pack(pady=10)
        
        # Status Frame
        status_frame = tk.Frame(self.root, pady=10)
        status_frame.pack()
        
        status_title = tk.Label(status_frame, text="Status:", font=("Arial", 10, "bold"))
        status_title.pack()
        
        self.status_label = tk.Label(
            status_frame, 
            text="Not Active", 
            font=("Arial", 9),
            fg="gray"
        )
        self.status_label.pack()
        
        # Info Frame
        info_frame = tk.Frame(self.root, pady=10)
        info_frame.pack()
        
        self.info_label = tk.Label(
            info_frame,
            text="",
            font=("Arial", 8),
            fg="blue"
        )
        self.info_label.pack()
        
    def toggle_monitoring(self):
        if not self.monitoring:
            self.start_monitoring()
        else:
            self.stop_monitoring()
    
    def start_monitoring(self):
        pid_text = self.pid_entry.get().strip()
        
        if not pid_text:
            messagebox.showerror("Error", "Enter PID First!")
            return
        
        try:
            pid = int(pid_text)
        except ValueError:
            messagebox.showerror("Error", "PID must be number!")
            return
        
        # Check if process exists
        if not psutil.pid_exists(pid):
            messagebox.showerror("Error", f"Process with PID {pid} not found!")
            return
        
        try:
            process = psutil.Process(pid)
            process_name = process.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
            messagebox.showerror("Error", f"Could not access procces: {e}")
            return
        
        self.current_pid = pid
        self.monitoring = True
        
        # Update UI
        self.toggle_button.config(text="Stop Monitoring", bg="#f44336")
        self.pid_entry.config(state="disabled")
        self.status_label.config(text="Monitoring active", fg="green")
        self.info_label.config(text=f"Process: {process_name} (PID: {pid})")
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(target=self.monitor_priority, daemon=True)
        self.monitor_thread.start()
    
    def stop_monitoring(self):
        self.monitoring = False
        
        # Update UI
        self.toggle_button.config(text="Start Monitoring", bg="#4CAF50")
        self.pid_entry.config(state="normal")
        self.status_label.config(text="Monitoring Stopped", fg="orange")
        self.info_label.config(text="")
    
    def monitor_priority(self):
        while self.monitoring:
            try:
                if not psutil.pid_exists(self.current_pid):
                    self.root.after(0, lambda: self.on_process_terminated())
                    break
                
                process = psutil.Process(self.current_pid)
                
                # Get current priority
                current_priority = process.nice()
                
                # Windows priority classes:
                # psutil.HIGH_PRIORITY_CLASS = high priority
                target_priority = psutil.HIGH_PRIORITY_CLASS
                
                if current_priority != target_priority:
                    # Set to high priority
                    process.nice(target_priority)
                    self.root.after(0, lambda: self.update_status("Priority set to HIGH", "orange"))
                else:
                    self.root.after(0, lambda: self.update_status("Priority already HIGH ✓", "green"))
                
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                self.root.after(0, lambda: self.on_error(str(e)))
                break
            
            # Wait 1 second before next check
            time.sleep(1)
    
    def update_status(self, message, color):
        if self.monitoring:
            self.status_label.config(text=message, fg=color)
    
    def on_process_terminated(self):
        self.monitoring = False
        self.toggle_button.config(text="Start Monitoring", bg="#4CAF50")
        self.pid_entry.config(state="normal")
        self.status_label.config(text="Process stopped", fg="red")
        messagebox.showwarning("Process Terminated", "Monitored Process has been stopped!")
    
    def on_error(self, error_msg):
        self.monitoring = False
        self.toggle_button.config(text="Start Monitoring", bg="#4CAF50")
        self.pid_entry.config(state="normal")
        self.status_label.config(text="Error accurred", fg="red")
        messagebox.showerror("Error", f"Error while monitoring: {error_msg}")

def main():
    root = tk.Tk()
    app = PrioritySetterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
