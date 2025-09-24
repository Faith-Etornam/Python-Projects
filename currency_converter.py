def user_input():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Invalid amount")
    return amount

def currency_input(label):
    exchange = ('USD', 'EUR', 'CAD')
    while True:
        currency = input(f'{label} currency (USD/EUR/CAD): ').upper()
        if currency not in exchange:
            print('Invalid Currency')
        else: 
            break
    return currency
    
def conversion_logic(source_currency, target_currency, amount) -> float:

    exchange_rates = {
    'USD': {'EUR': 0.85, 'CAD': 1.25},
    'EUR': {'USD': 1.18, 'CAD': 1.47},
    'CAD': {'USD': 0.80, 'EUR': 0.68}
}
    
    if source_currency == target_currency:
        return amount
    else:
        return amount * exchange_rates[source_currency][target_currency]
    

def print_info(amount, source_currency, converted_amount):
    print(f"{amount} {source_currency} is equal to {converted_amount}")

def conversion():
    amount = user_input()

    source_currency = currency_input('Source')

    target_currency = currency_input('Target')

    converted_amount = conversion_logic(source_currency, target_currency, amount)

    print_info(amount, source_currency, converted_amount)

conversion()





