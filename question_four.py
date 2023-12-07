numbers = (1,12,123,1234,12345)
print("1")
print("12")
print("123")
print("1234")
print("12345")

#(ii)
n=5
print(n)

#(iii)
def numbers(a, b):
    output = a+b
    print(f"The sum of {a} and {b} is {output}")

numbers(3, 4)

#(iv)
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

Car1 = Car("Toyota", 1998)

print(Car1.brand)
print(Car1.year)
