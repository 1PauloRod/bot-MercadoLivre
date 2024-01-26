import unittest
import scraping_mercado_livre as sml

class TestScrapingMercadoLivre(unittest.TestCase):
    
    def test_sort_product_price(self):
        products = [
            ["bbb", "smartphone2", 900.0, 4.5, "https://smartphone2.com", 0], 
            ["ddd", "smartphone4", 1200.0, 4.5, "https://smartphone4.com", 0],
            ["aaa", "smartphone1", 700.0, 4.5, "https://smartphone1.com", 0],
            ["eee", "smartphone5", 1200.5, 4.5, "https://smartphone5.com", 0],
            ["ccc", "smartphone3", 1000.0, 4.5, "https://smartphone3.com", 0]
        ]
        
        expected_value = [
            ["aaa", "smartphone1", 700.0, 4.5, "https://smartphone1.com", 0], 
            ["bbb", "smartphone2", 900.0, 4.5, "https://smartphone2.com", 0],
            ["ccc", "smartphone3", 1000.0, 4.5, "https://smartphone3.com", 0],
            ["ddd", "smartphone4", 1200.0, 4.5, "https://smartphone4.com", 0],
            ["eee", "smartphone5", 1200.5, 4.5, "https://smartphone5.com", 0]
        ]
        
        self.assertEqual(expected_value, sml.sort_products_price(products))
        
        
    def test_scraping_mercado_livre(self):
        products = sml.scraping_mercado_livre()
        print(len(products))
        self.assertTrue(len(products) > 0, "Nenhum produto encontrado.")
        for product in products:
            self.assertTrue(len(product) == 6, "não há os campos necessários.")
            
            id_product, title, price, rating, url, processed = product
            self.assertIsNotNone(id_product, "ID o produto não pode ser Nulo.")
            self.assertIsNotNone(title, "O título não pode ser Nulo.")
            self.assertIsInstance(price, float, "O preço tem que ser um float.")
            self.assertIsInstance(rating, float, "O valor da avaliação tem que ser um float.")
            self.assertIsNotNone(url, "O link não pode ser Nulo.")
            self.assertIsInstance(processed, int, "O campo 'processado' tem quer ser um valor binário")
            
            
if __name__ == '__main__':
    unittest.main()
        