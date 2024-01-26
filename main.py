from scraping_mercado_livre import scraping_mercado_livre
from database import DatabaseMercadoLivre
from time import sleep
from bot_send_message import botSender

def main():
    database = DatabaseMercadoLivre()
    database.initialize_database()
    bot_sender = botSender()
    
    while True:
        send_products = []
        get_products_from_the_website = scraping_mercado_livre()
            
            
        for product in get_products_from_the_website:
            id_product = product[0]
            if not database.search_product(id_product):
                database.insert_product(product)
        
                
        get_cheaper_products = database.search_cheaper_products()
        
        for product in get_cheaper_products:
            processed_product = product[5]
            if processed_product == 0:
                product_id, title, price, rating, url, processed = product
                processed = 1
                updated_product = [product_id, title, price, rating, url, processed]
                database.update_product_processed(updated_product)
                send_products.append(updated_product)
            
            else:
                print("Nenhum produto novo.")
        
        if send_products:
            bot_sender.send_product(send_products)
            
        sleep(2)
        
if __name__ == "__main__":
    main()
    
            
        
         
        
    
   
    
    
        
        
      