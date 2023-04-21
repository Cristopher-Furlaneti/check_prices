from actions import FIND_SEARCH, FIND_GO, SEARCH_PRICE, COPY_PRICE,VALUE_CSV, driver, COLUMN_CSV
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By 
import csv
import os


urls = ['https://amazon.com', 'https://www.olx.com.br/', 'https://www.mercadolivre.com.br/']
COLUMN_CSV()

#Acessar o site
for site in urls:
    driver.get(site)
#Buscar o produto desejado
    FIND_SEARCH(site)
#Confirmar o produto desejado
    FIND_GO(site)
#Localizando o preço do produto
    SEARCH_PRICE(site)
#Copiando o preço do produto
    COPY_PRICE(site)
#Colocando o valor na planilha
    VALUE_CSV(site)
