def create_config(config_name) -> None:
    with open(config_name, "w"):
        pass


def read_config(config_name) -> dict:
    with open(config_name, "r", encoding="utf-8") as config_file:
        lines = config_file.readlines()
        return {"directories": [line.strip() for line in lines]}


def write_config(config_name, config_data) -> None:
    with open(config_name, "w", encoding="utf-8") as config_file:
        if "directories" in config_data:
            for directory in config_data["directories"]:
                config_file.write(f"{directory}\n")


def write_base_settings_config(config_name) -> None:
    config_data = read_config(config_name)
    config_data["directories"] = ["first/path/example", "second/path/example"]
    write_config(config_name, config_data)


def get_config(config_name) -> dict:
    try:
        config = read_config(config_name)
    except FileNotFoundError:
        print("Не был найден файл конфигурации...")
        create_config(config_name)
        write_base_settings_config(config_name)
        print("Файл конфигурации создан. Добавьте нужные пути в него.\n")
        config = read_config(config_name)

    return config
