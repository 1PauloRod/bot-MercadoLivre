import mysql.connector
from mysql.connector import errorcode
from config import VERIFY_DB_EXIST, CREATE_DB, CREATE_TABLE, INSERT_PRODUCT, SEARCH_CHEAPER_PRODUCTS, SEARCH_PRODUCT, UPDATE_PRODUCT


class DatabaseMercadoLivre:
    
    def initialize_database(self):
        try:
            
            self.__create_database()
            self.__create_table()
            
            return [1]
            
        except Exception as err:
            print(err)
            return [-5]
        
    def insert_product(self, product):
        try:
            id_product, title, price, rating, url, processed = product
            
            script = INSERT_PRODUCT % (id_product, title, price, rating, url, processed)
            
            return self.__execute_script(script)

        except Exception as err:
            print(err)
            return [-5]
        
    def search_cheaper_products(self):
        try:
            script = SEARCH_CHEAPER_PRODUCTS
            
            return self.__execute_script(script)
        
        except Exception as err:
            print(err)
            return [-5]
    
    def search_product(self, id_product):
        try:
            script = SEARCH_PRODUCT % id_product
            
            return self.__execute_script(script)
        
        except Exception as err:
            print(err)
            return [-5]
        
    def update_product_processed(self, product):
        try:
            id_product, title, price, rating, url, processed = product
            script = UPDATE_PRODUCT % (id_product, title, price, rating, 
                                       url, processed, id_product)

            return self.__execute_script(script)
        except Exception as err:
            print(err)
            return [-5]
    
    @staticmethod
    def __create_database() -> list:
        try:
            
            cnx = mysql.connector.connect(host='localhost', 
                                          user='root', 
                                          password='secret', 
                                          port=3306)
            
        
            cursor = cnx.cursor()
            cursor.execute(VERIFY_DB_EXIST)
            result = cursor.fetchall()
            
            if result:
                print("Banco de dados já existe.")
            else: 
                print("Criando o banco de dados.")
                cursor.execute(CREATE_DB)
        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com o usuário ou senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
                return [-2]
            else:
                print(err)
                return [-3]
        
        finally:
            if cnx:
                cnx.close()
    
    @staticmethod
    def __create_table() -> list:
        try: 
            
            cnx = mysql.connector.connect(host='localhost', 
                                          user='root', 
                                          password='secret', 
                                          database='mercadolivre', 
                                          port=3306)
            
            cursor = cnx.cursor()
            cursor.execute(CREATE_TABLE[0])
            result = cursor.fetchall()
            
            if result:
                print("Tabela {} já existe.".format(CREATE_TABLE[2]))
            else:
                print("Criando tabela {}.".format(CREATE_TABLE[2]))
                cursor.execute(CREATE_TABLE[1])

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com o usuário ou senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
                return [-2]
            else:
                print(err)
                return [-3]
        finally:
            if cnx:
                cnx.close()
                
    @staticmethod
    def __execute_script(script):
        try:
            cnx = mysql.connector.connect(host='localhost', 
                                          user='root', 
                                          password='secret', 
                                          database='mercadolivre', 
                                          port=3306)
            
            cursor = cnx.cursor()
            cursor.execute(script)
            result = cursor.fetchall()
            cnx.commit()
            
            return result
        except mysql.connector.Error as err:
            if cnx:
                cnx.rollback()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Algo deu errado com usuário e senha.")
                return [-1]
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Banco de dados não existe.")
                return [-2]
            elif err.errno == errorcode.ER_BAD_TABLE_ERROR: 
                print("Tabela de dados não existe.")
                return [-3]
            else:
                print(err)
                return [-4]
        finally:
            if cnx:
                cnx.close()
            
                
            
        
'''busca = SELECT * FROM ... WHERE title = %s, price = %f, rating = %f'''
