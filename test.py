
import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)
    
    def __str__(self):
        if self.imaginary == 0:
            return f"{self.real}"
        elif self.imaginary > 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
    
    def magnitude(self):
        return math.sqrt(self.real**2 + self.imaginary**2)
    
    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

def find_largest_magnitude(numbers_list):
    if not numbers_list:
        return None
    largest = numbers_list[0]
    for num in numbers_list[1:]:
        if num.magnitude() > largest.magnitude():
            largest = num
    return largest

# ТЕСТИРОВАНИЕ
print("Тест комплексных чисел")

# Тест 1: Основные операции
print("1. Основные операции:")
a = ComplexNumber(3, 4)
b = ComplexNumber(1, 2)
print(f"   a = {a}")
print(f"   b = {b}")
print(f"   a + b = {a + b}")
print(f"   a - b = {a - b}")
print(f"   a * b = {a * b}")

# Тест 2: Методы
print("\n2. Методы:")
print(f"   Модуль a = {a.magnitude()}")
print(f"   Сопряженное b = {b.conjugate()}")

# Тест 3: Поиск максимального
print("\n3. Поиск максимального модуля:")
numbers = [ComplexNumber(1,1), ComplexNumber(3,4), ComplexNumber(6,8)]
largest = find_largest_magnitude(numbers)
print(f"   Числа: {[str(n) for n in numbers]}")
print(f"   Максимальный: {largest}")

print("\n Все тесты пройдены!")