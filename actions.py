from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By 
import csv
import os

driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()))
#Encontrando o campo de pesquisa para pesquisarmos o produto desejado

def FIND_SEARCH(site):
    if site == 'https://amazon.com':
        search_box = driver.find_element(By.ID, 'twotabsearchtextbox')
        search_box.send_keys ('Acer Aspire 5')
    elif site == 'https://www.olx.com.br/':
        search_box = driver.find_element(By.XPATH,'//input[@aria-label = "Autocomplete"]')
        search_box.send_keys ('Acer Aspire 5')
    elif site == 'https://www.mercadolivre.com.br/':    
        search_box = driver.find_element(By.XPATH,'//input[@class = "nav-search-input"]')
        search_box.send_keys ('Acer Aspire 5')

#Encontrando o botão de pesquisa para enviarmos a busca

def FIND_GO(site):
    if site == 'https://amazon.com':
        button_search = driver.find_element(By.ID, 'nav-search-submit-button')
        button_search.click()
    elif site == 'https://www.olx.com.br/':
        button_search = driver.find_element(By.XPATH,'//button[@class = "search-button-submit"]')
        button_search.click()
    elif site == 'https://www.mercadolivre.com.br/':
        button_search = driver.find_element(By.XPATH, '//button[@class="nav-search-btn"]')
        button_search.click()

#Localizando o preço

def SEARCH_PRICE(site):
    global price_amazon,price_olx,price_ml
    if site == 'https://amazon.com':
        price_amazon = driver.find_element(By.XPATH, '//span[@class="a-price-whole"]')
    elif site == 'https://www.olx.com.br/':
        price_olx = driver.find_element(By.XPATH, '//*[@id="ad-list"]/li[1]/div/a/div/div[2]/div[1]/div[1]/div[2]/div/div/div[1]/span')
    elif site == 'https://www.mercadolivre.com.br/':
        price_ml = driver.find_element(By.XPATH, '//span[@class="price-tag-fraction"]')   

#Transformando o preço em texto

def COPY_PRICE(site):
    global price_text
    if site == 'https://amazon.com':
        price_text = price_amazon.text 
    elif site == 'https://www.olx.com.br/':
        price_text = price_olx.text.split(' ')[1]
    elif site == 'https://www.mercadolivre.com.br/':
        price_text = price_ml.text
#Colocando valor na planilha



def VALUE_CSV(site):
        with open('precos.csv', 'a', newline='', encoding='utf-8') as arquivo:
            writer_csv = csv.writer(arquivo)
            writer_csv.writerow([site,price_text])

def COLUMN_CSV():
    filename = 'precos.csv'
    if not os.path.isfile(filename) or os.path.getsize(filename) == 0:
        with open(filename, 'a', newline='', encoding='utf-8') as arquivo:
            writer_csv = csv.writer(arquivo)
            writer_csv.writerow(['site', 'preço'])