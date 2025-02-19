from typing import Callable
from decimal import Decimal
import re


def generator_numbers(text: str):
    """
    Функція, яка аналізує текст, ідентифікувуючи всі дійсні числа, що вважаються частинами доходів, 
    і повертає їх як генератор. Дійсні числа у тексті записані без помилок, 
    чітко відокремлені пробілами з обох боків. 
    
    Parameters:
        text (str): Вхідний текст, який може містити числа.
    
    Returns:
        generator: Генератор, що повертає числа у форматі str, які знаходяться у тексті.
    """
    # split the text on words
    splited_text = list(text.split(' '))

    # check if text contains numbers
    # the pattern identify numbers with a decimal point and minus
    pattern = r'\b\d+(?:\.\d+)?\b' 

    # find all numbers by pattern
    nums_from_text = re.findall(pattern, text)

    if len(nums_from_text) != 0:
        # сonvert each found string to a float and return it via yield
        for num in nums_from_text:
            yield num
    else:  
         raise ValueError("The text doesn't contain numbers")
    


def sum_profit(text: str, func: Callable):
    """
    Функція, яка використовує generator_numbers та підсумовує отримані числа,
    та обчислює загальну їх суму.

    Parameters:
        text (str): Вхідний текст, який може містити числа.
        func (Callable): Функція, що використовується для отримання чисел з тексту.
    
    Returns:
        Decimal: Загальна сума всіх чисел у тексті, округлена до двох знаків після коми.
        str: Повідомлення, якщо у тексті немає необхідних чисел.
    """

    try:
        return Decimal(sum(map(float, func(text)))).quantize(Decimal("0.00"))
    except ValueError:
        return "Нема необхідних даних для підрахунку."
    

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
