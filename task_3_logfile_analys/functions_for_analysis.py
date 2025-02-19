from string_parser import parse_log_line
from pathlib import Path
from collections import Counter
from tabulate import tabulate 


def load_logs(file_path: Path) -> list:
    """
    Завантажує лог-файл, парсить кожен рядок та зберігає результати у список.

    Функція відкриває файл, читає його построчно та застосовує `parse_log_line()` 
    для перетворення кожного запису в структурований формат (словник). 
    Усі оброблені записи зберігаються у список, який повертається.

    Parameters:
        file_path (Path): Шлях до файлу логів.

    Returns:
        list: Список словників, де кожен запис містить розібрані компоненти логу (дата, час, рівень, повідомлення).

    Raises:
        FileNotFoundError: Якщо файл за вказаним шляхом не існує.
        IOError: Якщо виникає помилка при читанні файлу.
    """
    parsed_logs = []
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            for line in file:
                parsed_logs.append(parse_log_line(line))
        return parsed_logs
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
        return []


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters log entries by a specific logging level.

    The function iterates through the list of logs and returns only those entries whose level matches the specified value.

    Parameters:
        logs (list): A list of logs, where each entry is represented as a dictionary with the key "level".
        level (str): The logging level by which to filter entries (for example, "ERROR", "INFO", "WARNING").

    Returns:
        list: A list of logs that match the specified level.
    """
  
    filtered_logs = list(filter(lambda log: log.get('level', '').lower() == level.lower(), logs))
    return filtered_logs
   

def count_logs_by_level(logs: list) -> dict:
    """
    Counts the number of records for each logging level.
    The function goes through the list of logs, analyzes the logging level (for example, "ERROR", "INFO", "WARNING")
    and counts the number of records for each level.

    Parameters:
        logs (list): A list of logs, where each record is represented as a dictionary with the key "level".

    Returns:
        dict: A dictionary, where the key is the logging level, the value is the number of records for this level.
    """
    log_levels = [log['level'] for log in logs]
    count_logs = Counter(log_levels)
    return dict(count_logs)

    
def display_log_counts(counts: dict):
    """
    Outputs the results of counting logging levels in a table format.
    The function accepts a dictionary where the keys are logging levels,
    and the values ​​are the number of logs of each level. The results are formed in the form of a table.

    Parameters:
        counts (dict): Dictionary, where the key is the logging level, the value is the number of records.

    Returns:
        None: The function only outputs the table to the console.
    """
    table_data = [[level, count] for level, count in counts.items()]
    print(tabulate(table_data, headers = ["Рівень логування ", "Кількість"], tablefmt = 'pipe'))

