# Модуль для работы с комплексными числами
# Предоставлен для задания по МДК.01.02

import math
from typing import List, Optional, Union

class ComplexNumber:

    
    def __init__(self, real: float, imaginary: float):

        self.real = real
        self.imaginary = imaginary
    
    def _validate_other(self, other: 'ComplexNumber') -> None:

        if not isinstance(other, ComplexNumber):
            raise TypeError(f"Операнд должен быть ComplexNumber, получен {type(other).__name__}")
    
    def __add__(self, other: 'ComplexNumber') -> 'ComplexNumber':

        self._validate_other(other)
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        self._validate_other(other)
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other: 'ComplexNumber') -> 'ComplexNumber':
        self._validate_other(other)
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)
    
    def __str__(self) -> str:
        if self.imaginary == 0:
            return f"{self.real}"
        elif self.imaginary > 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"
    
    def __repr__(self) -> str:
        return f"ComplexNumber({self.real}, {self.imaginary})"
    
    def magnitude(self) -> float:
        return math.sqrt(self.real**2 + self.imaginary**2)
    
    def conjugate(self) -> 'ComplexNumber':
        return ComplexNumber(self.real, -self.imaginary)


def find_largest_magnitude(numbers_list: List[ComplexNumber]) -> Optional[ComplexNumber]:
    if not numbers_list:
        return None

    largest_num = numbers_list[0]
    largest_magnitude = largest_num.magnitude()
    
    for num in numbers_list[1:]:
        current_magnitude = num.magnitude()
        if current_magnitude > largest_magnitude:
            largest_num = num
            largest_magnitude = current_magnitude
    
    return largest_num


def print_summary(real_part: float, imag_part: float) -> None:
    print(f"Действительная часть: {real_part}, Мнимая часть: {imag_part}")


def main() -> None:
    num1 = ComplexNumber(3, 4)
    num2 = ComplexNumber(1, -2)
    num3 = ComplexNumber(0, 5)
    num4 = ComplexNumber(-2, -3)
    num5 = ComplexNumber(0, 0)
    
    print("Демонстрация работы комплексных чисел")
    print(f"Число 1: {num1}")
    print(f"Число 2: {num2}")
    print(f"Число 3: {num3}")
    print(f"Число 4: {num4}")
    print(f"Число 5: {num5}")
    print()
    
    print("Арифметические операции")
    print(f"Сложение ({num1} + {num2}): {num1 + num2}")
    print(f"Вычитание ({num1} - {num2}): {num1 - num2}")
    print(f"Умножение ({num1} * {num2}): {num1 * num2}")
    print()
    
    print("Методы комплексных чисел")
    print(f"Модуль числа {num1}: {num1.magnitude():.2f}")
    print(f"Модуль числа {num2}: {num2.magnitude():.2f}")
    print(f"Модуль числа {num3}: {num3.magnitude():.2f}")
    print(f"Сопряженное для {num2}: {num2.conjugate()}")
    print()

    numbers = [num1, num2, num3, num4]
    largest_num = find_largest_magnitude(numbers)
    print("Поиск числа с наибольшем модулем")
    print(f"Список чисел: {numbers}")
    print(f"Число с наибольшим модулем: {largest_num}")
    print(f"Модуль: {largest_num.magnitude():.2f}" if largest_num else "Список пуст")
    print()
    
    print(" Граничные случаи ")
    empty_list = []
    result_empty = find_largest_magnitude(empty_list)
    print(f"Результат для пустого списка: {result_empty}")
    
    print_summary(10, 20)


if __name__ == "__main__":
    main()