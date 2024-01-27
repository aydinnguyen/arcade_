import time, random, sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

    return ("stop")


print(
    "welcome!!! this is an arcade called:A Arcade!!! its also the best arcade in the universe! not kidding!! (theres a toe fungus spread, so be careful!!)")
print()
tickets = 0

print("please select your location!!")
print("0. ticket booth")
print("1. math whizzzžžźźżż")
print("2.find the corn")
print("3.FIGHT THE MIGHTY FFFFOOORRRRK!!!!!")
print("4.bathroom break! (so we can watch you poo!!!)")
print()

l = int(input("where would you like to go, dude?"))
print()
if (l == 0):
    print("welcome to the ticket booth!!")
    print()
    p = ["robux ", "more robux ", "even more robux "]
    pc = [1000, 1500, 5999]
    print("here are the prizes...hope you get none.")
    for i in range(len(p)):
        print(p[i] + "costs: " + str(pc[i]))
elif (l == 1):
    print("Welcome to math whizzzžžźźżż")
    countdownstopped = "not stopped"
    while (countdownstopped != "stop"):
        num = list(range(100))
        num1 = random.choice(num)
        num2 = random.choice(num)
        print("What is " + str(num1) + " + " + str(num2))
        answer = int(input("Answer here: "))

        if (num1 + num2 == answer):
            print("Correct!! you get a ticket")
            tickets += 1
            print("You current have this many tickets: " + str(tickets))

elif (l == 4):
    print_slow("we seee youuuu....")
    print_slow("we know when you are pooping..")
    print_slow("we know when you pee...")

