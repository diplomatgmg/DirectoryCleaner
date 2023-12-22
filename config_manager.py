import yaml


class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)


def create_config(config_name) -> None:
    with open(config_name, "w"):
        pass


def read_config(config_name) -> dict:
    with open(config_name, "r", encoding="utf-8") as config_file:
        return yaml.safe_load(config_file) or {}


def write_config(config_name, config_data) -> None:
    with open(config_name, "w", encoding="utf-8") as config_file:
        yaml.dump(config_data, config_file, IndentDumper)


def write_base_settings_config(config_name) -> None:
    config_data = read_config(config_name)
    config_data["directories_to_clean"] = ["first/path/example", "second/path/example"]
    write_config(config_name, config_data)


def get_config(config_name) -> dict:
    try:
        config = read_config(config_name)
    except FileNotFoundError:
        create_config(config_name)
        write_base_settings_config(config_name)
        config = read_config(config_name)

    return config
