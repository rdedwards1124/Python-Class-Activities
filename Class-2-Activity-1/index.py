#1:
def arb_args(*args):
    for stuff in args:
        print(stuff)

arb_args(1,2,3,4,5,6)

#2:
def inner_func(a, b):
    def nest_1(a, b):
        return a * b
    def nest_2(a, b):
        return b + a
    print(nest_1(a, b) + nest_2(a, b))

inner_func(5, 2)

#3:
def lunch_lady(name, lunch = "mystery meat"):
    print(name, "wants", lunch, "for lunch")

lunch_lady("Bob")
lunch_lady("Mandy", "Nachos")

#4:


#5:

