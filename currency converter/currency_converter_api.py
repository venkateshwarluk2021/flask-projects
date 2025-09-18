import requests

def convert_currency(amount, from_currency, to_currency):
    """convert currency using real-time exchange rates from exchangerate.host"""
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error getting exchange raes")
        return None

    data = response.json()
    print("DEBUG..", data)

    if not data.get("success", True):
        print("API returned error: ", data.get("error"))
        return None
    
  
    return data["rates"].get(to_currency)


if __name__ == "__main__":
    print("Currency converter(live rates)")
    print("Example currency codes: USD, INR, EUR, GBP, JPY")

    try:
        amount = float(input("Enter the amount:\t "))
        from_curr = input("From currency:\t").upper()
        to_curr = input("To currency:\t").upper()

        result = convert_currency(amount, from_curr, to_curr)

        if result is not None:
            print(f"\n{amount:.2f} {from_curr}={result:.2f} {to_curr}")
        else:
            print("Invalid currency code entered.")
    except ValueError:
        print("Invalid number amount entered:")
