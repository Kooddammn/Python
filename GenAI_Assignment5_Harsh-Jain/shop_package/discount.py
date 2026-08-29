#Function to return discounted price
def apply_discount(price,percentage):
    return price - ((percentage/100)*price)

#Function to return flat discount 
def flat_discount(price):
    return price - 50
