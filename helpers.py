import math

def tables_needed(people, seats):
    return math.ceil(people / seats)  # Returns people divided by seats, rounded up

def welcome(name):
    return f"Welcome to PLP, {name}!"  # Returns the formatted welcome message

if __name__ == "__main__":
    print(tables_needed(10, 4))