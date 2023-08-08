from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
#declaring database and forms url
nome_arquivo = 'teste.xlsx'
url_forms = "https://forms.gle/mk1bjYocJvJwHK776"

#reading database and opening chrome
df = pd.read_excel(nome_arquivo)
for index, row in df.iterrows():
    print("Index: " + str(index) + "Nome:" + row["Nome"])
    #opening chrome
    chrome = webdriver.Chrome()
    #searching url
    chrome.get(url_forms)
    time.sleep(1)
    #answering name
    elemento_nometxt = chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    elemento_nometxt.send_keys(row["Nome"])
    #answering age
    if row["Idade"] == 1:
        elemento_idade = chrome.find_element(By.XPATH,'//*[@id="i9"]')
        elemento_idade.click()
    elif row["Idade"] == 2:
        elemento_idade = chrome.find_element(By.XPATH, '//*[@id="i12"]')
        elemento_idade.click()
    elif row["Idade"] == 3:
        elemento_idade = chrome.find_element(By.XPATH, '//*[@id="i15"]')
        elemento_idade.click()
    elif row["Idade"] == 4:
        elemento_idade = chrome.find_element(By.XPATH, '//*[@id="i18"]')
        elemento_idade.click()
    elif row["Idade"] == 5:
        elemento_idade = chrome.find_element(By.XPATH, '//*[@id="i21"]')
        elemento_idade.click()
    elif row["Idade"] == 6:
        elemento_idade = chrome.find_element(By.XPATH, '//*[@id="i24"]')
        elemento_idade.click()
    elif row["Idade"] == 7:
        elemento_idade = chrome.find_element(By.XPATH, '//*[@id="i27"]')
        elemento_idade.click()
    else:
        print("algo deu errado")


    #answering Q1
    if row["Q1"] == 1:
        elemento_Q1 = chrome.find_element(By.XPATH,'//*[@id="i34"]')
        elemento_Q1.click()
    elif row["Q1"] == 2:
        elemento_Q1 = chrome.find_element(By.XPATH, '//*[@id="i37"]')
        elemento_Q1.click()
    else:
        print("algo deu errado")

    #answering Q2
    if row["Q2"] == 1:
        elemento_Q2 = chrome.find_element(By.XPATH,'//*[@id="i44"]')
        elemento_Q2.click()
    elif row["Q2"] == 2:
        elemento_Q2 = chrome.find_element(By.XPATH, '//*[@id="i47"]')
        elemento_Q2.click()
    else:
        print("algo deu errado")

    #answering Q3
    if row["Q3"] == 1:
        elemento_Q3 = chrome.find_element(By.XPATH,'//*[@id="i54"]')
        elemento_Q3.click()
    elif row["Q3"] == 2:
        elemento_Q3 = chrome.find_element(By.XPATH, '//*[@id="i57"]')
        elemento_Q3.click()
    else:
        print("algo deu errado")

    #answering Q4
    if row["Q4"] == 1:
        elemento_Q4 = chrome.find_element(By.XPATH,'//*[@id="i64"]')
        elemento_Q4.click()
    elif row["Q4"] == 2:
        elemento_Q4 = chrome.find_element(By.XPATH, '//*[@id="i67"]')
        elemento_Q4.click()
    else:
        print("algo deu errado")

    #answering Q5
    if row["Q5"] == 1:
        elemento_Q5 = chrome.find_element(By.XPATH,'//*[@id="i74"]')
        elemento_Q5.click()
    elif row["Q5"] == 2:
        elemento_Q5 = chrome.find_element(By.XPATH, '//*[@id="i77"]')
        elemento_Q5.click()
    else:
        print("algo deu errado")

    #answering E1
    elemento_E1 = chrome.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[' + str(row["E1"]) + ']/div[2]/div/div')
    elemento_E1.click()

    #answering E2
    elemento_E2 = chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[' + str(row["E2"]) + ']/div[2]/div/div')
    elemento_E2.click()

    #sending answers
    enviar = chrome.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    enviar.click()

    #closing chrome
    chrome.quit()