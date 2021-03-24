import datetime

if __name__ == '__main__':
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    print("Hi! " + name)

    now = datetime.datetime.now()
    years_to_hundred = 100 - age
    print("You will turn 100 years old in " + str(now.year + years_to_hundred) + " year")
