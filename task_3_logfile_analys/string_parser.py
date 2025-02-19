

def parse_log_line(line: str) -> dict:
    """
    Parses a log line into structured components: date, time, level, and message.

    Parameters:
        line (str): A log entry in the format "YYYY-MM-DD HH:MM:SS LEVEL Message".

    Returns:
        dict: A dictionary containing the parsed components.
    """
    # split the line up to 3rd component and leave a user message without splitting
    try: 
        #log_date, log_time, level, *args = line.split()
        log_line = line.strip().split(maxsplit=3)
        components = ['log_date', 'log_time', 'level', 'message']
   
        return {component: log_line[i] for i, component in enumerate(components)}
    except ValueError:
        return f'The string has unexpected format.'

