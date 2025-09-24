exchange = ('USD', 'EUR', 'CAD')

exchange_rates = {
    'USD': {'EUR': 0.85, 'CAD': 1.25},
    'EUR': {'USD': 1.18, 'CAD': 1.47},
    'CAD': {'USD': 0.80, 'EUR': 0.68}
}

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

def source_currency_input():
    while True:
        source_currency = input('Source currency (USD/EUR/CAD): ').upper()
        if source_currency not in exchange:
            print('Invalid Currency')
        else: 
            break
    return source_currency

def target_currency_input():
    while True:
        target_currency = input('Target currency (USD/EUR/CAD): ').upper()
        if target_currency not in exchange:
            print('Invalid currency')
        else:
            break
    return target_currency
    
def print_info(amount, source_currency, converted_amount):
    print(f"{amount} {source_currency} is equal to {converted_amount}")

def conversion():
    amount = user_input()

    source_currency = source_currency_input()

    target_currency = target_currency_input()


    if source_currency == target_currency:
        converted_amount == amount
    else:
        converted_amount = amount * exchange_rates[source_currency][target_currency]

    print_info(amount, source_currency, converted_amount)

conversion()





