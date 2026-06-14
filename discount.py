``
TAX_RATE = 0.13

def apply_discount(price, percent):
    discount_amount = price * percent / 100
    discounted_price = price - discount_amount
    return discounted_price

def apply_tax(price):
    tax_amount = price * TAX_RATE
    final_amount = price + tax_amount
    return final_amount

def final_price(price, discount_pct):
    price_after_discount = apply_discount(price, discount_pct)
    price_after_tax = apply_tax(price_after_discount)
    return price_after_tax
