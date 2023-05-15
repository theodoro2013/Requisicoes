import requests as req
import re
import firebirdsql
import tkinter as tk
global banco


with open('C:/COLISEU/Requisicoes/banco.txt', 'r') as arquivo:
    banco= arquivo.read()
    print(banco)

def select(query):
    global banco
    con = firebirdsql.connect(
        host='localhost',
        database=banco,
        user='SYSDBA',
        password='masterkey',
        port=3050,
        charset='WIN1252'
    )
    cur = con.cursor()
    cur.execute(query)
    resultado = cur.fetchall()
    cur.close()
    con.close()
    return resultado

def execute(query):
    global banco
    con = firebirdsql.connect(
        host='localhost',
        database=banco,
        user='SYSDBA',
        password='masterkey',
        port=3050,
        charset='WIN1252'
    )
    cur = con.cursor()
    cur.execute(query)
    cur.close()
    con.commit()
    con.close()

def htmlResponseText(link):
    user='CampFacil'
    senha='dsffjyxtf4x'
    response = req.get(link, auth=(user,senha))
    return(response.text)

def opcoes():
    global banco
    html=htmlResponseText("https://messaging.covisint.com/invoke/HTTPConnector.Mailbox/get")
    MessageId=[]
    Data=[]
    Hora=[]
    Size=[]
    
    X = re.findall("&nbsp;[0-9]+&nbsp",html)
    for v in X:
        message = re.sub("&nbsp;","",v)
        Size.append(re.sub("&nbsp","",message))

    X = re.findall("<td><tt>&nbsp;........&nbsp;",html)
    for v in X:
        message = re.sub("<td><tt>&nbsp;","",v)
        MessageId.append(re.sub("&nbsp;","",message))
    
    X = re.findall("<nobr>&nbsp;........",html)
    for v in X:
        dia = re.sub("<nobr>&nbsp;","",v)
        Data.append(dia)
    
    X = re.findall("&nbsp;.....:..",html)
    for v in X:
        hora = re.sub("&nbsp;","",v)
        Hora.append(hora)

    return {'MessageID':MessageId,'Data':Data,'Hora':Hora, 'Size' :Size}
        

