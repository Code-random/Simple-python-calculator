# create a dictionary to store the translated strings
lang_dict = {
    'english': {
        'operation_prompt': 'Select an operation:',
        'choice_prompt': 'Enter choice(1/2/3/4): ',
        'num1_prompt': 'Enter first number: ',
        'num2_prompt': 'Enter second number: ',
        'invalid_input': 'Invalid input',
        'add': 'Add',
        'subtract': 'Subtract',
        'multiply': 'Multiply',
        'divide': 'Divide'
    },
    'polish': {
        'operation_prompt': 'Wybierz operację:',
        'choice_prompt': 'Wybierz (1/2/3/4): ',
        'num1_prompt': 'Wprowadź pierwszą liczbę: ',
        'num2_prompt': 'Wprowadź drugą liczbę: ',
        'invalid_input': 'Nieprawidłowe dane wejściowe',
        'add': 'Dodaj',
        'subtract': 'Odejmij',
        'multiply': 'Pomnóż',
        'divide': 'Podziel'
    },
    'german': {
        'operation_prompt': 'Wählen Sie einen Vorgang:',
        'choice_prompt': 'Auswahl eingeben(1/2/3/4): ',
        'num1_prompt': 'Erste Zahl eingeben: ',
        'num2_prompt': 'Zweite Nummer eingeben: ',
        'invalid_input': 'Ungültige Eingabe',
        'add': 'Hinzufügen',
        'subtract': 'Subtrahieren',
        'multiply': 'Multiplizieren',
        'divide': 'Dividieren'
    }
}

# define the functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    else:
        return result

# ask the user to select a language
while True:
    print("Select a language:")
    print("1. English")
    print("2. Polski")

    lang_choice = input("Enter choice (1/2): ")
    if lang_choice in ('1', '2', '3'):
        break

# select the appropriate language dictionary
if lang_choice == '1':
    lang = lang_dict['english']
elif lang_choice == '2':
    lang = lang_dict['polish']
elif lang_choice == '3':
    lang = lang_dict['german']

# ask the user to select an operation
print(lang['operation_prompt'])
print("1. " + lang['add'])
print("2. " + lang['subtract'])
print("3. " + lang['multiply'])
print("4. " + lang['divide'])

# ask the user to choose an operation
while True:
    choice = input(lang['choice_prompt'])
    if choice in ('1', '2', '3', '4'):
        break

# ask the user to enter the numbers for the chosen operation
num1 = input(lang['num1_prompt'])
num2 = input(lang['num2_prompt'])

# convert the numbers to floats
try:
    num1 = float(num1)
    num2 = float(num2)
except ValueError:
    print(lang['invalid_input'])
else:
    # perform the chosen operation
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)

    # print the result of the operation
    print(result)
