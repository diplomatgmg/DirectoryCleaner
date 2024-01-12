from Cleaner import Cleaner
from config_manager import get_config


def main():
    config_name = "config.yaml"
    config = get_config(config_name)

    directories_to_clean = config['directories_to_clean']
    cleaner = Cleaner()
    cleaner.clean(directories_to_clean)


if __name__ == "__main__":
    main()
