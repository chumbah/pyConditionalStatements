price = float(input("enter price: "))
discount_percent = float(input("enter discount percent: "))

def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
    else:
        final_price = price
    return final_price

print("final price is:", calculate_discount(price, discount_percent))