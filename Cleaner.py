import os


class Cleaner:
    def __init__(self):
        self.total_size = 0

    def handle_remove(self, remove_func, path):
        try:
            file_size = os.path.getsize(path)
            remove_func(path)
            self.total_size += file_size
            print(f"Успешно удалено: {path}")
        except OSError:
            pass

    def remove_file_or_dir(self, path):
        if os.path.isfile(path):
            self.handle_remove(os.remove, path)
        elif os.path.isdir(path):
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                self.remove_file_or_dir(item_path)
            self.handle_remove(os.rmdir, path)

    def clean_file_or_directory(self, file_or_dir_path):
        if os.path.isdir(file_or_dir_path):
            directory_contents = os.listdir(file_or_dir_path)

            for file_or_directory in directory_contents:
                path = os.path.join(file_or_dir_path, file_or_directory)
                self.remove_file_or_dir(path)
        else:
            self.handle_remove(os.remove, file_or_dir_path)

    def clean(self, directories):
        for path in directories:
            self.clean_file_or_directory(path)

        size_megabytes = self.total_size / (1024 * 1024)

        if size_megabytes >= 1000:
            size_gigabytes = size_megabytes / 1024
            print(f"Успешно очищено {size_gigabytes:.2f} ГБ")
        else:
            print(f"Успешно очищено {size_megabytes:.2f} МБ")
