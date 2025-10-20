import tkinter as tk
from tkinter import ttk, messagebox

# ===== Fixed Exchange Rates (Base: USD) =====
exchange_rates = {
    "USD": 1,
    "EUR": 0.92,
    "GBP": 0.81,
    "INR": 83.5,
    "JPY": 150.2,
    "AUD": 1.5,
}

# ===== Function to Convert Currency =====
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            messagebox.showerror("Error", "Please select valid currencies.")
            return

        # Convert amount to USD first, then to target
        usd_amount = amount / exchange_rates[from_currency]
        converted_amount = usd_amount * exchange_rates[to_currency]

        label_result.config(text=f"{converted_amount:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for amount.")

# ====== Main Window ======
root = tk.Tk()
root.title("Professional Currency Converter")
root.geometry("420x380")
root.config(bg="#e6f0ff")

# ====== Title ======
title = tk.Label(root, text="Currency Converter", font=("Poppins", 18, "bold"),
                 bg="#e6f0ff", fg="#0F4C75")
title.pack(pady=20)

# ====== Amount Input ======
lbl_amount = tk.Label(root, text="Enter Amount:", font=("Poppins", 12), bg="#e6f0ff", fg="#333")
lbl_amount.pack(pady=(10,0))
entry_amount = tk.Entry(root, font=("Poppins", 12), width=20, bd=2, relief="groove", justify="center")
entry_amount.pack(pady=5, ipady=5)

# ====== Currency Selection ======
currencies = list(exchange_rates.keys())

frame_currency = tk.Frame(root, bg="#e6f0ff")
frame_currency.pack(pady=10)

lbl_from = tk.Label(frame_currency, text="From:", font=("Poppins", 12), bg="#e6f0ff", fg="#333")
lbl_from.grid(row=0, column=0, padx=5, pady=5)
combo_from = ttk.Combobox(frame_currency, values=currencies, font=("Poppins", 12), state="readonly", width=10)
combo_from.grid(row=0, column=1, padx=5, pady=5)
combo_from.set("USD")

lbl_to = tk.Label(frame_currency, text="To:", font=("Poppins", 12), bg="#e6f0ff", fg="#333")
lbl_to.grid(row=0, column=2, padx=5, pady=5)
combo_to = ttk.Combobox(frame_currency, values=currencies, font=("Poppins", 12), state="readonly", width=10)
combo_to.grid(row=0, column=3, padx=5, pady=5)
combo_to.set("EUR")

# ====== Convert Button ======
convert_btn = tk.Button(root, text="Convert", font=("Poppins", 12, "bold"),
                        bg="#0078D7", fg="white", activebackground="#005EA2",
                        activeforeground="white", width=20, command=convert_currency)
convert_btn.pack(pady=15, ipadx=5, ipady=5)

# ====== Result Label ======
label_result = tk.Label(root, text="--", font=("Poppins", 16, "bold"), bg="#e6f0ff", fg="#0047AB")
label_result.pack(pady=10)

# ====== Footer ======
footer = tk.Label(root, text="Professional Currency Converter by Aman", font=("Poppins", 9),
                  bg="#e6f0ff", fg="#333")
footer.pack(side="bottom", pady=10)

# ====== Run App ======
root.mainloop()
