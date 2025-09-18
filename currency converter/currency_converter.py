conversion_rates = {
    "USD": 1.0,
    "INR": 85.0,
    "EUR": 0.92,
    "GBP": 0.78,
    "JPY": 146.0
    }

def convert_currency(amount, from_currency, to_currency):
    """convert amount from one currency to another using static rates"""
    if from_currency not in conversion_rates and to_currency not in conversion_rates:
        return None

    # convert from source currency to USD
    amount_in_usd = amount / conversion_rates[from_currency]

    # convert from USD to target currency
    converted_amount = amount_in_usd * conversion_rates[to_currency]
    return converted_amount

if __name__ == "__main__":
    print("Currency converter (static rates)\n")
    print("Available currencies: ",",".join(conversion_rates.keys()))

    try:
        amount = float(input("Enter the amount: "))
        print("currency types are: ", end="")
        for keys in conversion_rates.keys():
            print(keys, end=",\t")
        from_curr = input("\nenter from currency: ").upper()
        to_curr = input("\nenter to currency: ").upper()

        result = convert_currency(amount, from_curr, to_curr)

        if result is None:
            print("\nInvalid currency entered\n")
        else:
            print(f"{amount:.2f} {from_curr} = {result:.2f} {to_curr}")
    except ValueError:
        print("\ninvalid number amount entered.\n")
          
    
