import unittest
from unittest.mock import patch, Mock
from database import DatabaseMercadoLivre


class TestDatabaseMercadoLivre(unittest.TestCase):
    @patch('database.mysql.connector.connect')
    def test_initialize_database(self, mock_connect):
        mock_cursor = Mock()
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        database = DatabaseMercadoLivre()
        result = database.initialize_database()
        
        self.assertEqual(result, [1])
    
    @patch('database.mysql.connector.connect')
    def test_search_product(self, mock_connect):
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [('aaa', 'smartphone1', 700.0, 4.5, 'url1', 0)]
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        database = DatabaseMercadoLivre()
        result = database.search_product('aaa')
        self.assertEqual(result, [('aaa', 'smartphone1', 700.0, 4.5, 'url1', 0)])
        
    
    @patch('database.mysql.connector.connect')
    def test_search_cheaper_products(self, mock_connect):
        mock_cursor = Mock()
        mock_cursor.fetchall.return_value = [('aaa', 'smartphone1', 700.0, 4.5, 'url1', 0)]
        mock_connect.return_value.cursor.return_value = mock_cursor
        
        database = DatabaseMercadoLivre()
        result = database.search_cheaper_products()
        print(result)
        self.assertEqual(result, [('aaa', 'smartphone1', 700.0, 4.5, 'url1', 0)])
        
if __name__ == '__main__':
    unittest.main()