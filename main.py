import datetime

if __name__ == '__main__':
    # Input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    number = int(input("Enter some number: "))

    # Processing
    now = datetime.datetime.now()
    years_to_hundred = 100 - age

    # Output
    for i in range(number):
        print("Hi! " + name)
        print("You will turn 100 years old in " + str(now.year + years_to_hundred) + " year")
