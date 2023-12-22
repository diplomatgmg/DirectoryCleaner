from config_manager import get_config


def main():
    config_name = "config.yaml"
    config = get_config(config_name)


if __name__ == "__main__":
    main()
