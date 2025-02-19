
def caching_fibonacci():
    """
    Створює функцію для обчислення чисел Фібоначчі з використанням кешування.

    Ця функція повертає внутрішню функцію, яка обчислює n-те число Фібоначчі за допомогою рекурсії.
    Для оптимізації обчислень, результати вже обчислених чисел зберігаються в локальному кеші.
    Таким чином, при повторних викликах з однаковими значеннями n, функція повертає збережене значенняn.

    Returns:
        callable: Функція fibonacci, яка приймає один параметр n (ціле число) і повертає n-те число Фібоначчі.

    """

    cash = {}

    def fibonacci(n):
        if n <= 0:
            cash['0'] = 0
            return cash['0']
        elif n == 1:
            cash['1'] = 1
            return cash['1']
        elif cash.get(n) is not None:
            # повертає збережене значення n
            return cash[n]
        else:
            # обчислює n-те число Фібоначчі за допомогою рекурсії
            cash[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cash[n]
        
    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
print(fib(12))  # Виведе із кешу 144
