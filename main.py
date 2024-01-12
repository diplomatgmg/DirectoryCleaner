import time

from Cleaner import Cleaner
from config_manager import get_config


def main():
    config_name = "config.txt"
    config = get_config(config_name)
    directories_to_clean = config["directories"]
    cleaner = Cleaner()
    cleaner.clean(directories_to_clean)

    print("Это окно закроется автоматически через 10 секунд...")
    time.sleep(10)


if __name__ == "__main__":
    main()
