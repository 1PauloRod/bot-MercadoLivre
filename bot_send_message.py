import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import SENDER_EMAIL, RECEIVERS_EMAIL, PASSWORD_EMAIL, URL_WHATSAPP, RECEIVERS_WHATSAPP
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import os
from time import sleep

class botSender:
    def __init__(self):
        self.path = os.getcwd()
        self.chrome_options = Options()
        self.chrome_options.add_argument(r"user-data-dir=" + self.path + "\profile\wpp")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        
    
    def send_product(self, products):
        message = []
        url = []
        price = []
        for product in products:
            message.append(product[1])
            price.append(product[2])
            url.append(product[4])
        
        self.__send_email(message, url)
        print("email enviado.")
        sleep(5)
        self.send_whatsapp_message(message, url, price)
        print("mensagem enviada.")
    
    @staticmethod
    def __send_email(content_email, url_email):
            try:
                subject = """<h1>Olá, Paulo</h1>
                            <h2>Algumas ofertas interessantes:</h2>
                """
                
                for i in range(len(content_email)):
                        subject += "<a href={}>{}<br>".format(url_email[i], content_email[i])
                
                message = MIMEMultipart()
                message['Subject'] = "Melhores ofertas Xiaomi"
                message['From'] = SENDER_EMAIL
                message['To'] = ','.join(RECEIVERS_EMAIL)
                message.attach(MIMEText(subject, 'html'))
                
                server = smtplib.SMTP('smtp.gmail.com: 587')
                server.starttls()
                
                server.login(SENDER_EMAIL, PASSWORD_EMAIL)
                server.sendmail(SENDER_EMAIL, RECEIVERS_EMAIL, message.as_string())
                
            except Exception as err:
                print(err)
            finally:
                server.quit()
                
    
    def send_whatsapp_message(self, message, url, price):
        try:
            self.driver.get(URL_WHATSAPP)
            sleep(30)
            
            for receiver in RECEIVERS_WHATSAPP:
                chat_box = self.driver.find_element(By.XPATH, "//span[@title='{}']".format(receiver))
                chat_box.click()
                sleep(2)
                
                box_message = self.driver.find_elements(By.XPATH, "//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")
                for i in range(len(message)):
                    box_message[1].send_keys("*{}*".format(message[i]) + (Keys.SHIFT) + (Keys.ENTER))
                    box_message[1].send_keys(url[i] + (Keys.SHIFT) + (Keys.ENTER))
                    box_message[1].send_keys("*PREÇO:* {} Reais".format(price[i]) + (Keys.SHIFT) + (Keys.ENTER))
                    box_message[1].send_keys((Keys.SHIFT) + (Keys.ENTER))
                    sleep(2)
                
                button_send = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
                button_send.click()
                sleep(2)
                
        except Exception as err:
            print(err)
       
            
        


    