
def real_estate():
    
    print("What is the current price?")
    current_price = int(input())

    print("What was last month's price?")
    last_month_price = int(input())

    price_change = current_price - last_month_price

    mortgage  = (current_price * 0.051) / 12

    print("This house is $" + str(current_price) + ". The change is $" + str(price_change) + " since last month.")
    print("The estimated monthly mortgage is $" + f'{mortgage:.2f}' + ".")

if __name__ == "__main__":
    real_estate()