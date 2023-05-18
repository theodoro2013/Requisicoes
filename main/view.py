import requests as req
import re
import firebirdsql
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

class Interface():

    cor = {"verde" : "#ADC178","azul" : "#1D3557","azulClaro" : "#457B9D","branco" : "#F1FAEE","vermelho" : "#E63946", "cinza" : "#8D99AE"}
    
    root = tk.Tk()
    root.geometry("800x600")
    root.config(bg=cor["branco"])
    root.state('zoomed')
    root.title("Requisições")
    root.iconbitmap(default='')

    imgColiseu =PhotoImage(file="C:/COLISEU/REQUISICOES/assets/COLISEUsFundo.png")
    imgColiseu = imgColiseu.subsample(2, 2)
    frameCabecario = tk.Frame(root,height=100,bg=cor["azul"],padx=10)
    frameCabecario.columnconfigure(0, weight=1)
    frameCabecario.columnconfigure(1, weight=4)
    frameCabecario.columnconfigure(2, weight=1)
    frameCabecario.rowconfigure(0, weight=1)
    frameTabelas = tk.Frame(root,bg=cor["vermelho"])
    frameTabelas.rowconfigure(0, weight=4)
    frameTabelas.rowconfigure(1, weight=2)
    frameTabelas.rowconfigure(2, weight=1)
    frameTabelas.columnconfigure(0, weight=1)
    frameOpcoes = tk.Frame(frameTabelas,bg=cor["cinza"])
    frameTabelaOpcoes = tk.Frame(frameOpcoes,bg=cor["azul"])
    frameVisu = tk.Frame(frameTabelas,bg=cor["cinza"])
    frameTabelaVisu = tk.Frame(frameVisu,bg=cor["azul"])
    tabelaOpcoes = ttk.Treeview(frameTabelaOpcoes, columns=("Message Id","Size", "Data","Hora"), show='headings')
    tabelaOpcoes.column("Message Id", anchor="center")
    tabelaOpcoes.column("Size", anchor="center")
    tabelaOpcoes.column("Data", anchor="center")
    tabelaOpcoes.column("Hora", anchor="center")
    tabelaOpcoes.heading("Message Id", text="Message Id")
    tabelaOpcoes.heading("Size", text="Size")
    tabelaOpcoes.heading("Data", text="Data")
    tabelaOpcoes.heading("Hora", text="Hora")
    tabelaOpcoes.tag_configure("branco", background=cor["branco"])
    tabelaOpcoes.tag_configure("verde", background=cor["verde"])
    tabelaVisu = ttk.Treeview(frameTabelaVisu, columns=("codCliente","cliente","produto","referencia","quantidade"), show='headings')
    tabelaVisu.column("codCliente", anchor="center")
    tabelaVisu.column("cliente", anchor="center")
    tabelaVisu.column("produto", anchor="center")
    tabelaVisu.column("referencia", anchor="center")
    tabelaVisu.column("quantidade", anchor="center")
    tabelaVisu.heading("codCliente", text="Cód.Cliente")
    tabelaVisu.heading("cliente", text="Cliente")
    tabelaVisu.heading("produto", text="Produto")
    tabelaVisu.heading("referencia", text="Ref.")
    tabelaVisu.heading("quantidade", text="Uni.")
    scrollY_opcoes = ttk.Scrollbar(frameTabelaOpcoes, orient="vertical", command=tabelaOpcoes.yview)
    tabelaOpcoes.configure(yscrollcommand=scrollY_opcoes.set)
    scrollY_vizu = ttk.Scrollbar(frameTabelaVisu, orient="vertical", command=tabelaVisu.yview)
    tabelaVisu.configure(yscrollcommand=scrollY_vizu.set)
    pbVizu = ttk.Progressbar(frameOpcoes, mode='determinate')
    btVizu = tk.Button(frameOpcoes,text='Carregar Visualização',bg=cor["azul"], fg=cor["branco"])
    btEnvia = tk.Button(frameOpcoes,text='Importar',bg=cor["azul"], fg=cor["branco"])
    lbLogo = ttk.Label(frameCabecario, image=imgColiseu,background=cor["azul"])
    lbRequisicoes = ttk.Label(frameCabecario, text="Requisições",background=cor["azul"],foreground=cor["branco"],font=("Arial", 24,"bold"))

    btVizu.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
    btVizu.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
    pbVizu.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
    btEnvia.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
    btEnvia.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
    lbLogo.grid(row=0,column=2)
    lbRequisicoes.grid(row=0,column=0)
    frameOpcoes.grid(row=0, column=0, sticky='nsew', rowspan=2)
    frameOpcoes.grid_rowconfigure(0, weight=1)
    frameOpcoes.grid_columnconfigure(0, weight=1)
    frameTabelaOpcoes.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    frameVisu.grid(row=2, column=0, sticky='nsew')
    frameVisu.grid_rowconfigure(0, weight=1)
    frameVisu.grid_columnconfigure(0, weight=1)
    frameTabelaVisu.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    btVizu.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

    frameCabecario.pack(side="top", fill="x")
    frameTabelas.pack(fill="both", expand=True, padx=10, pady=10)
    scrollY_opcoes.pack(side="right", fill="y")
    tabelaOpcoes.pack(fill="both", expand=True,pady=5,padx=2)
    scrollY_vizu.pack(side="right", fill="y")
    tabelaVisu.pack(fill="both", expand=True,pady=5,padx=2)

    def executar(self):
        self.root.mainloop()



