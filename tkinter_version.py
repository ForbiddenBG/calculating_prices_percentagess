import tkinter as tk


def calculate_discount(event=None):
    price = float(entry_price.get())
    percent = float(entry_percent.get())
    currency = entry_currency.get()

    discount = price * (percent / 100)
    final_price = price - discount

    label_discount.config(text=f"Discount of the product is {discount:.2f} {currency}")
    label_final_price.config(text=f"The final price of the product is: {final_price:.2f} {currency}")


window = tk.Tk()
window.title("Discount Calculator")

label_price = tk.Label(window, text="Price:", bd=4, font=("Arial", 12))
label_price.pack()
entry_price = tk.Entry(window, bd=4, font=("Arial", 12))
entry_price.pack()
entry_price.bind("<Return>", lambda event: entry_percent.focus())

label_percent = tk.Label(window, text="Discount Percentage:", bd=4, font=("Arial", 12))
label_percent.pack()
entry_percent = tk.Entry(window, bd=4, font=("Arial", 12))
entry_percent.pack()
entry_percent.bind("<Return>", lambda event: entry_currency.focus())

label_currency = tk.Label(window, text="Currency:", bd=4, font=("Arial", 12))
label_currency.pack()
entry_currency = tk.Entry(window, bd=4, font=("Arial", 12))
entry_currency.pack()
entry_currency.bind("<Return>", calculate_discount)

button_calculate = tk.Button(window, text="Calculate", command=calculate_discount, bd=4, font=("Arial", 12))
button_calculate.pack()

label_discount = tk.Label(window, bd=4, font=("Arial", 12))
label_discount.pack()

label_final_price = tk.Label(window, bd=4, font=("Arial", 12))
label_final_price.pack()

window.mainloop()
