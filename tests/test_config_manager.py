import os
import unittest
import config_manager


class TestConfigManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.abspath(__file__))
        self.config_path = os.path.join(self.test_dir, 'test_config.yaml')

    def tearDown(self):
        if os.path.exists(self.config_path):
            os.remove(self.config_path)

    def test_create_config(self):
        """
        Тест для создания конфига
        """
        self.assertFalse(os.path.exists(self.config_path))
        config_manager.create_config(self.config_path)
        self.assertTrue(os.path.exists(self.config_path))

    def test_read_not_exist_config(self):
        """
        Тест для чтения несуществующего файла
        """
        with self.assertRaises(FileNotFoundError):
            config_manager.read_config(self.config_path)

    def test_read_empty_config(self):
        """
        Тест для чтения пустого конфига
        """
        config_manager.create_config(self.config_path)
        config_data = config_manager.read_config(self.config_path)
        self.assertEqual(config_data, {})

    def test_read_not_empty_config(self):
        """
        Тест для чтения не пустого файла
        """
        config_manager.create_config(self.config_path)
        config_manager.write_base_settings_config(self.config_path)
        config_data = config_manager.read_config(self.config_path)

        expect_data = {'directories_to_clean': ['first/path/example', 'second/path/example']}
        self.assertEqual(config_data, expect_data)

    def test_write_config_formatter(self):
        """
        Тест на проверку форматера при создании конфига
        """
        config_manager.create_config(self.config_path)
        config_manager.write_base_settings_config(self.config_path)

        with open(self.config_path, 'r', encoding='utf-8') as config_file:
            config_data = config_file.read()

            expect_data = (f'directories_to_clean:\n'
                           f'  - first/path/example\n'
                           f'  - second/path/example\n')

            self.assertEqual(config_data, expect_data)


if __name__ == '__main__':
    unittest.main()
