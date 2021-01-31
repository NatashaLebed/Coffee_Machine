resources = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'money': 550}

espresso = {'water': 250, 'milk': 0, 'beans': 16, 'cups': 1, 'money': 4}
latte = {'water': 350, 'milk': 75, 'beans': 20, 'cups': 1, 'money': 7}
cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'cups': 1, 'money': 6}

def remaining():
    print(f"""The coffee machine has:
    {resources['water']} of water
    {resources['milk']} of milk
    {resources['beans']} of coffee beans
    {resources['cups']} of disposable cups
    ${resources['money']} of money
    """)


def check_resources_for(for_drink):
    if resources['water'] - for_drink['water'] < 0:
        print('Sorry, not enough water!')
        return False
    elif resources['milk'] - for_drink['milk'] < 0:
        print('Sorry, not enough milk!')
        return False
    elif resources['beans'] - for_drink['beans'] < 0:
        print('Sorry, not enough beans!')
        return False
    elif resources['beans'] - for_drink['cups'] < 0:
        print('Sorry, not enough cups!')
        return False
    else:
        print('I have enough resources, making you a coffee!')
        return True


def change_resources(for_drink):
    global resources
    resources['water'] -= for_drink['water']
    resources['milk'] -= for_drink['milk']
    resources['beans'] -= for_drink['beans']
    resources['cups'] -= for_drink['cups']
    resources['money'] += for_drink['money']


def buy():
    buy_item = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
    if buy_item == '1' and check_resources_for(espresso):
        change_resources(espresso)
    elif buy_item == '2' and check_resources_for(latte):
        change_resources(latte)
    elif buy_item == '3' and check_resources_for(cappuccino):
        change_resources(cappuccino)


def fill():
    global resources
    resources['water'] += int(input('Write how many ml of water do you want to add:'))
    resources['milk'] += int(input('Write how many ml of milk do you want to add:'))
    resources['beans'] += int(input('Write how many grams of coffee beans do you want to add:'))
    resources['cups'] += int(input('Write how many disposable cups of coffee do you want to add:'))


def take():
    global resources
    print(f"I gave you ${resources['money']}")
    resources['money'] = 0


while True:
    action = input('Write action (buy, fill, take, remaining, exit):')
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    elif action == 'remaining':
        remaining()
    else:
        break
