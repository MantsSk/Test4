import logging

logging.basicConfig(filename='terminal_log.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s]: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def log_input(input_text, log_level=logging.INFO):
    logging.log(log_level, input_text)

while True:
    user_input = input("Enter something (or type 'exit' to end): ")

    log_input(user_input)

    if user_input.lower() == 'exit':
        break

print("Logging complete. Check 'terminal_log.log' for the log.")
