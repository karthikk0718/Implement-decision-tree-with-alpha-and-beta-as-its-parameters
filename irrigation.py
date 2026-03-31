import tkinter as tk
import random

# Function to simulate sensor data
def get_sensor_data():
    moisture = random.randint(10, 100)
    sunlight = random.randint(10, 100)
    return moisture, sunlight

# Decision logic
def check_irrigation():
    try:
        alpha = int(alpha_entry.get())
        beta = int(beta_entry.get())

        moisture, sunlight = get_sensor_data()

        moisture_label.config(text=f"Soil Moisture: {moisture}%")
        sunlight_label.config(text=f"Sunlight: {sunlight}%")

        if moisture < alpha or sunlight > beta:
            result = "Water Needed 💧"
            result_label.config(text=result, fg="blue")
        else:
            result = "No Water Needed ❌"
            result_label.config(text=result, fg="green")

    except ValueError:
        result_label.config(text="Enter valid numbers!", fg="red")

# Create window
root = tk.Tk()
root.title("Smart Irrigation System")
root.geometry("400x350")

# Title
title = tk.Label(root, text="🌱 Smart Irrigation System", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Alpha input
tk.Label(root, text="Moisture Threshold (α):").pack()
alpha_entry = tk.Entry(root)
alpha_entry.pack()

# Beta input
tk.Label(root, text="Sunlight Threshold (β):").pack()
beta_entry = tk.Entry(root)
beta_entry.pack()

# Button
check_btn = tk.Button(root, text="Check Irrigation", command=check_irrigation)
check_btn.pack(pady=10)

# Output labels
moisture_label = tk.Label(root, text="Soil Moisture: --")
moisture_label.pack()

sunlight_label = tk.Label(root, text="Sunlight: --")
sunlight_label.pack()

result_label = tk.Label(root, text="Result: --", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run app
root.mainloop()
