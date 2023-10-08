price = float(input("Enter the price: "))
raw_percent = float(input("Enter the discount percentage: "))
currency = str(input("Enter the currency or its relevant symbol: "))

discount = price * (raw_percent / 100)
final_price = price - discount

print(f'Discount of the product is {discount:.02f} {currency}')
print(f"The final price of the product is: {final_price:.02f} {currency}")
