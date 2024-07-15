num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2)) 

num2 = 22 

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2) 

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


#####################################


dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


#####################################
class Test:
    def __init__(self, age):
        self.age = age
    
    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age


dict1 = Test(11)

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1.get_age())
print("dict2 =", dict2.get_age())

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2.set_age(22)

print("\nAfter value is updated:")
print("dict1 =", dict1.get_age())
print("dict2 =", dict2.get_age()) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


