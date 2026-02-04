# a product would cost $100, how much tax do we pay?

product = 100 # in dollars
tax_rate = 0.0625
tax = product * tax_rate
print ("f 'The tax for a product which costs $ {product} is ${tax}.")

def calc_tax(price, tax_rate):
    """Calculate the product tax based on given price, and return the tax amount"""
    tax_rate = 0.0625
    tax = price * tax_rate
    #print (f'The tax for a product while costs $ {price} is ${tax}.')
    return tax

computer_price = 900
iphone_price = 1100
mass_rate = 0.0625
ny_rate = 8.875 / 100
tax_computer = calc_tax(computer_price, mass_rate)
tax_iphone = calc_tax(iphone_price, ny_rate)

total_tax = tax_computer + tax_iphone
print (total_tax)