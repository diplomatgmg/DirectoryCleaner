import os
import tempfile
import unittest

import config_manager


class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.test_config_file = tempfile.mktemp()

    def tearDown(self):
        if os.path.exists(self.test_config_file):
            os.remove(self.test_config_file)

    def test_create_config(self):
        """
        Тест для создания конфига
        """
        self.assertFalse(os.path.exists(self.test_config_file))
        config_manager.create_config(self.test_config_file)
        self.assertTrue(os.path.exists(self.test_config_file))

    def test_read_not_exist_config(self):
        """
        Тест для чтения несуществующего файла
        """
        with self.assertRaises(FileNotFoundError):
            config_manager.read_config(self.test_config_file)

    def test_read_empty_config(self):
        """
        Тест для чтения пустого конфига
        """
        config_manager.create_config(self.test_config_file)
        config_data = config_manager.read_config(self.test_config_file)
        self.assertEqual(config_data, {"directories": []})

    def test_read_not_empty_config(self):
        """
        Тест для чтения не пустого файла
        """
        config_manager.create_config(self.test_config_file)
        config_manager.write_base_settings_config(self.test_config_file)
        config_data = config_manager.read_config(self.test_config_file)

        expect_data = {"directories": ["first/path/example", "second/path/example"]}
        self.assertEqual(config_data, expect_data)

    def test_write_config_formatter(self):
        """
        Тест на проверку форматера при создании конфига
        """
        config_manager.create_config(self.test_config_file)
        config_manager.write_base_settings_config(self.test_config_file)

        with open(self.test_config_file, "r", encoding="utf-8") as config_file:
            config_data = config_file.read()

            expect_data = f"first/path/example\n" f"second/path/example\n"

            self.assertEqual(config_data, expect_data)


if __name__ == "__main__":
    unittest.main()
