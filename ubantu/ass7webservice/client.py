# client.py
import requests
import tkinter as tk
from tkinter import messagebox

def call_web_service():
    try:
        response = requests.get('http://localhost:5000/greet')
        if response.status_code == 200:
            data = response.json()
            messagebox.showinfo("Server Response", data['message'])
        else:
            messagebox.showerror("Error", f"Failed to get response. Status Code: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create a simple GUI
root = tk.Tk()
root.title("Distributed Client")

root.geometry("400x200")
label = tk.Label(root, text="Distributed Client App", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Get Greeting from Server", command=call_web_service, font=("Arial", 12), bg="lightblue")
button.pack(pady=20)

root.mainloop()
# pip install flask requests
# python server.py
# python client.py
