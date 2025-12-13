def calculate_discount(price):
    if price > 100:
        return "10%"
    else:
        return 0.05

final_price = 200 - calculate_discount(200)
print(final_price)

