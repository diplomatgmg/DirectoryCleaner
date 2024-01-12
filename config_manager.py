import os


def create_config(config_path) -> None:
    directory_path = os.path.dirname(config_path)
    os.makedirs(directory_path, exist_ok=True)

    with open(config_path, "w"):
        pass


def read_config(config_path) -> dict:
    with open(config_path, "r", encoding="utf-8") as config_file:
        lines = config_file.readlines()
        return {"directories": [line.strip() for line in lines]}


def write_config(config_path, config_data) -> None:
    with open(config_path, "w", encoding="utf-8") as config_file:
        if "directories" in config_data:
            for directory in config_data["directories"]:
                config_file.write(f"{directory}\n")


def write_base_settings_config(config_path) -> None:
    config_data = read_config(config_path)
    config_data["directories"] = ["first/path/example", "second/path/example"]
    write_config(config_path, config_data)


def get_config(config_path) -> dict:
    try:
        config = read_config(config_path)
    except FileNotFoundError:
        print("Не был найден файл конфигурации...")
        create_config(config_path)
        write_base_settings_config(config_path)
        print(
            f"Файл конфигурации создан. Добавьте нужные пути в него.\n{config_path}\n"
        )
        config = read_config(config_path)

    return config
