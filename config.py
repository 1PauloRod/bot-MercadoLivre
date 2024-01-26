URL = "https://lista.mercadolivre.com.br/celular-xiaomi-128gb#D[A:celular%20xiaomi%20128gb]"
HEADERS = {'User-Agent': 'Chrome/120.0.6099.199'}
URL_WHATSAPP = "https://web.whatsapp.com/"

VERIFY_DB_EXIST = "SHOW DATABASES LIKE 'mercadolivre'"
CREATE_DB = "CREATE DATABASE mercadolivre"

CREATE_TABLE = ["SHOW TABLES LIKE 'product'", 
                
                "CREATE TABLE product("
                "id_product varchar(255) NOT NULL,"
                "title varchar(255) NOT NULL,"
                "price float NOT NULL,"
                "rating float NOT NULL,"
                "url LONGTEXT NOT NULL,"
                "processed bit DEFAULT 0,"
                "PRIMARY KEY (id_product))", 
                "product"]

INSERT_PRODUCT = '''INSERT INTO mercadolivre.product (id_product, title, price, rating, url, processed)
VALUES ('%s', '%s', '%f', '%f', '%s', %d);
'''
SEARCH_CHEAPER_PRODUCTS = '''SELECT * FROM mercadolivre.product 
ORDER BY price 
LIMIT 5
'''

SEARCH_PRODUCT = '''SELECT * FROM mercadolivre.product WHERE id_product = '%s' '''


UPDATE_PRODUCT = '''UPDATE mercadolivre.product
SET id_product = '%s', title = '%s', price = '%f', rating = '%f', url = '%s', processed = %d
WHERE id_product = '%s' ; 
'''

SENDER_EMAIL = "myemail@gmail.com"
RECEIVERS_EMAIL = ["myemails@gmail.com"]
PASSWORD_EMAIL = ""

RECEIVERS_WHATSAPP = ["me"]
