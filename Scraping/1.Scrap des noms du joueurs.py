# cette algorithme affiche les noms des joueurs qui ont representer une équipe dans deux années
# vous devez donner url au variable url1 et url2 du site transfer market
# par example ici il vas retourner la liste des joueurs marocains qui ont representer le maroc dans 2024 et 2023

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url1='https://www.transfermarkt.com/morocco/kader/verein/3575/plus/0/galerie/0?saison_id=2023'
url2='https://www.transfermarkt.com/morocco/kader/verein/3575/plus/0/galerie/0?saison_id=2022'
os.environ['PATH'] += r'C:\Users\ULTRAPC\Downloads\Chrome'

driver = webdriver.Firefox()

driver.get(url1)

driver.implicitly_wait(30)

time.sleep(5)

elements = driver.find_elements(By.CLASS_NAME, 'hauptlink')

L=[]

for element in elements :
    L.append(element.text)


L = L[:len(L)-4]
L = L[::2]

os.environ['PATH'] += r'C:\Users\ULTRAPC\Downloads\Chrome'

driver = webdriver.Firefox()

driver.get(url2)

driver.implicitly_wait(30)

time.sleep(5)

elements = driver.find_elements(By.CLASS_NAME, 'hauptlink')

A = []

for element in elements:
        A.append(element.text)

A = A[:len(A)-4]
A = A[::2]

for a in A:
    if a not in L:
        L.append(a)

print(L)
print(len(L))