#rafael castillo
#cs50 python
#program problems set 1 #4





def main():
    # Prompt the user for an arithmetic expression
    expression = input("Enter an arithmetic expression (e.g., 'x + y', 'x - y', 'x * y', 'x / y'): ")

    try:
        # Split the expression into its components (x, operator, y)
        x, operator, y = expression.split()
        x = float(x)
        y = float(y)

        # Perform the calculation based on the operator
        result = calculate(x, operator, y)

        # Print the result formatted to one decimal place
        print(f"Result: {result:.1f}")
    except (ValueError, ZeroDivisionError, TypeError):
        print("Invalid input. Please enter a valid arithmetic expression.")

def calculate(x, operator, y):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y

if __name__ == "__main__":
    main()
