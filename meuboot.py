# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:38:37 2020

@author: tacio
"""

from time import sleep
from whatsapp_api import WhatsApp

# inicializar o whatapp
wp = WhatsApp()

input("Pressione enter após escaniar")

#lista com palavras chaves
nomes_palavras_chaves = ['Andre Brasil','Tania oi','Thais tim']
#primeiros_nomes=[n.split(' ')[0] for n in nomes_palavras_chaves]
primeiros_nomes=['Andre','Tania','Thais']

for primeiro_nome, nome_pesquisar in zip(primeiros_nomes,nomes_palavras_chaves):
    wp.search_contact(nome_pesquisar)
    mensagem = f"Olá {primeiro_nome} Testando via software"
    wp.send_message(mensagem)

# Esperar 10 segundos para depois fechar a tela do whatsappweb
sleep(10)
wp.driver.close()
