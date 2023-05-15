from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  '+': add,
  '-': subtract,
  '*': multiply,
  '/': divide
}


def calculator():
  print(logo)

  game = True
  num1 = float(input("What's the first number? "))

  while game:
    for operation in operations:
      print(operation)

    operation_symbol = input('Pick an operation from the line above: ')

    num2 = float(input("What's the next number? "))

    calculation = operations[operation_symbol]
    answer = calculation(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {answer}')

    game_continued = input("Do you want to continue the calculation? Type 'y' to continue, 'n' to start a new calculation ")
    if game_continued == 'y':
      num1 = answer
    elif game_continued == 'n':
      game = False
      calculator()
    else:
      print('Not a correct operator')

calculator()