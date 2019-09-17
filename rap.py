# -*- coding: utf-8 -*-

from selenium import webdriver
import smtplib

from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://visao.sapo.pt/opiniao/ricardo-araujo-pereira")

ultimopost = driver.find_element_by_css_selector('.latestList > li:nth-child(1) > article:nth-child(1) > div:nth-child(1) > h1:nth-child(2) > a:nth-child(1)')
ultimopost.click()
a = driver.find_element_by_css_selector('.especialistasHeaderContainer > h1:nth-child(2)')
titulo = a.text
print(titulo + '\n\n')

corpo1 = driver.find_element_by_css_selector('.articleContent')

print(corpo1.text)

#Configuração de smtplib para enviar o mail
server = smtplib.SMTP('smtp.gmail.com', 587)
#Next, log in to the server
server.ehlo()
server.starttls()
server.ehlo()
server.login("USER@mail.com", "PASSWORD")
#Send the mail with input
#o texto é o json form que é recebido com o api request
#para já só tem o nome do evento
subject = 'Crónica semanal Ricardo Araújo Pereira' + '\n\n'
message = 'Subject: {}\n\n{}'.format(subject, titulo + '\n\n' + corpo1.text) # The  /n separates the message from the headers
server.sendmail("FROM@mai.com", "TO@gmail.com",  message.encode("utf8"))
driver.close()

print("Já está !!!")
