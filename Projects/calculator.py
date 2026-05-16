#calculator which saves history

#concepts which we use - input, function, conditions, file handaling, loops, basic maths

#features - calculation, history, show history, show, exit, for multi number calculation, eval function(eval function used for taking expressions)

HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r') #r for read mode   we can also use these mode under double quotes.
    lines = file.readlines()
    if len(lines) == 0:
        print("No history found!")
    else:
        for line in reversed(lines):
            print(line.strip())  #.strip Return a copy of the string with leading and trailing whitespace removed
    file.close()

def clear_history():
    file = open(HISTORY_FILE, 'w') #w for overwrite which mean erase old data and store onlynew data which is write using w   we can also use these mode under double quotes.
    file.close()
    print("History clear!")

#to save history
def save_to_history(equation, result): 
    file = open(HISTORY_FILE, 'a') #a for append(adding data)    we can also use these mode under double quotes.
    file.write(equation + "=" + str(result) + "\n")
    file.close()


def calculate(user_input):
    parts =  user_input.split()
    if len(parts) !=3:
        print("invalid input. Use format: Operator number (e.g 9 + 8)")
        return
    num1 = float(parts[0])
    op = parts[1]  #op is operator
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("cannot divide by zero")
            return
        result = num1 / num2
    elif op == "%":
        result = num1 % num2
    elif op == "**":
        result = num1 ** num2
    else:
        print("Invalid operator")
        return
    
    if int(result) == result:  #if result in float then this can change result into integer
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

#this is brain of our code
def main():
     print("---SIMPLE CALCULATION (type history, clear or exit )")
     while True:
         user_input = input("Enter calculation (+ - * / % **) or command (history, clear, exit)")
         if user_input == exit:
             print("Good bye")
             break
         elif user_input == "history":
             show_history()
         elif user_input == "clear":
              clear_history()
         else:
             calculate(user_input)
main()

             






