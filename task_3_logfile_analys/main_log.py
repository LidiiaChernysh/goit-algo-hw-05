# import needed functions
from pathlib import Path
import sys
from functions_for_analysis import load_logs, filter_logs_by_level, count_logs_by_level, display_log_counts


def main():

    # Check if command line has an argument
    if len(sys.argv) < 2:
        print("Usage: python3 [main.py](<http://main.py/>) /path/to/logfile.log  [log_level]")
        sys.exit(1)

    # Getting the path from a command line argument
    log_file_path = Path(sys.argv[1])
    log_level = (sys.argv[2]).strip().upper() if len(sys.argv) > 2 else None

    # Checking the existence of a path
    if not log_file_path.exists():
        print(f"Path {log_file_path.absolute()} does not exsist. Check the inputed path.")
        sys.exit(1)
        
    # Get list of logs from file
    log_list = load_logs(log_file_path)

    if log_level is None:
        display_log_counts(count_logs_by_level(log_list))
    else:
        display_log_counts(count_logs_by_level(log_list))
        print(f'Деталі логів для рівня "{log_level}":')
        fitered_logs = filter_logs_by_level(log_list, log_level)
        for line in fitered_logs:
            print(f"{line['log_date']} {line['log_time']} - {line['message']}")


if __name__ == "__main__":
    main()
