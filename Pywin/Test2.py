'''import sys
list = ['A', 1]

for i in list:
    try:
        r = 1/int(i)
        break
    except ValueError:
        print("Exception:", sys.exc_info()[0], 'occured')
        print()
    except ZeroDivisionError:
        print("Exception:", sys.exc_info()[0], 'occured')
print("Result is", r)


try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)'''

'''class parrot():

    type = 'Bird'

    def character(self, color, name):
        #self.name = name
        #self.color = color
        print("Parrot's name is {} & color is {}".format(name, color))

parrot1 = parrot()
parrot1.character("Red", 'Dave')

print("test")
print("project"
   '''

'''
class computer:

    def __init__(self, cpu, ram, name, age):
        self.cpu = cpu
        self.ram = ram
        self.name = name
        self.age = age
        self.stu = self.student()

    def config(self):
        print("Config is:", self.cpu, self.ram, self.age, self.name)
        self.stu.show()

    def compare(self, obj2):
        pass

    class student:  # Inner class

        def __init__(self):
            self.sname = "Ranj"
            self.srollno = 232

        def show(self):
            print("Name and roll no of a student is: ", self.sname, self.srollno)

obj1 = computer("AMD", 8, "Ranjith", 100)
obj1.config()
'''
''''# LINEAR SEARCH
lis = [1, 2, 3, 4, 5]
n = int(input("Which number you want to search?"))
for i in range(len(lis)):
    if lis[i] == n:
        print("Requested element found at", i)
    else:
        print("ELe not found")
'''
lis = [100, 101, 200, 300, 450, 600, 700, 800]

pos = 0
n = int(input("Enter a number"))

def binary_search(lis, n):
    lower_bound_pos = 0
    upper_bound_pos = len(lis) - 1
    while lower_bound_pos <= upper_bound_pos:
        mid_pos = (lower_bound_pos + upper_bound_pos) // 2
        if lis[mid_pos] == n:
            globals()['pos'] = mid_pos
            return True
        else:
            if lis[mid_pos] < n:
                lower_bound_pos = mid_pos + 1
            else:
                upper_bound_pos = mid_pos - 1

if binary_search(lis, n):
    print("Element found at", pos + 1)
else:
    print("Element not found")
