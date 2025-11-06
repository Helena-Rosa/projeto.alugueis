import ttkbootstrap as ttk
import tkinter as tk
import sqlite3
from tkinter import messagebox



class GestorDeAlugueis:
    def __init__(self):

        #arrumar essa parte do banco de dados na proxima aula
        conexao= sqlite3.connect("bd_gestor_alugueis.sqlite")

        cursor= conexao.cursor()

        #aqui vai o sql do insert
        sql_insert = """CREATE TABLE IF NOT EXISTS gestor_alugueis
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item VARCHAR(100),
                            descricao VARCHAR(200),
                            status VARCHAR(20));"""
        
        cursor.execute(sql_insert) 
        
        conexao.commit()

        sql_mostrar_itens="SELECT * FROM gestor_alugueis;"

        cursor.execute(sql_mostrar_itens)

        itens=cursor.fetchall()


        cursor.close()
        conexao.close()
    
        
        #configuração da janela principal e da Treeview
        self.janela = ttk.Window(themename="morph")
        self.janela.title("Gestor de Aluguéis")
        self.janela.geometry("950x950+0+0")

       
       
        #texto para escrever as informações de comando (item_nome)
        label_item = ttk.Label (self.janela,
                                        text= "ITEM:",
                                        font={"success" , 25})
        label_item.pack()



        #campo de espaço para escrever as infomaçoes pedidas (item_nome) 
        self.campo_item = ttk.Entry(self.janela, width=50)
        self.campo_item.pack(pady=5)



        #texto para escrever as informações de comando (descrição)
        label_senha = ttk.Label (self.janela,
                                        text= "DESCRIÇÃO:",
                                        font={"success" , 25})
        label_senha.pack()


        #campo de espaço para escrever as infomaçoes pedidas (descrição) 
        self.campo_descricao = ttk.Entry(self.janela, width=50)
        self.campo_descricao.pack(pady=5)


        self.treeview = ttk.Treeview(self.janela)
        self.treeview.pack(padx=10, pady=10, fill="both", expand=True)


        #informações do cabeçalho
        self.treeview["columns"] = ( "ID", "ITEM", "DESCRIÇÃO", "STATUS" )
        self.treeview["show"] = "headings"

        #Configuração dos cabeçalhos da self.treeview
        self.treeview.heading ("ID", text="CODIGO:")
        self.treeview.heading ("ITEM", text="NOME DO ITEM:")
        self.treeview.heading ("DESCRIÇÃO", text="DESCRIÇÃO:")
        self.treeview.heading ("STATUS", text= "STATUS:")
        

        #criar colunas
        self.treeview.column ("ID", width=50)
        self.treeview.column("ITEM", width=50)
        self.treeview.column("DESCRIÇÃO", width=50)
        self.treeview.column ("STATUS", width=50)
        
        

        #atualizar treewie
        for a in itens:
            self.treeview.insert("",tk.END,values=a)
            


       #função do botão 
        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack () 


        #função botão para ADICIONAR
        self.botao_teste = ttk.Button(frame_botao,text="ADICIONAR",command=self.adicionar).pack(side="left",pady= 40, padx=20)

         #função botão para EXCLUIR
        ttk.Button(frame_botao, text="EXCLUIR",command=self.excluir).pack(side="right", pady= 40, padx=20  )  

            #função botão para ALTERAR
        ttk.Button(frame_botao, text= "ALTERAR", command=self.alterar).pack(side="right", pady=40)

        #função botão para ALTERAR
        ttk.Button(frame_botao, text= "CHECK-IN", command=self.check_in).pack(side="left", pady=40,padx=15)

        #função botão para ALTERAR
        ttk.Button(frame_botao, text= "CHECK-OUT", command=self.check_out).pack(side="left", pady=40,padx=15)


    
    #função para adicionar o item da tabela
    def adicionar(self):
        item= self.campo_item.get()
        descricao= self.campo_descricao.get()

        if item=="" or descricao=="":
            pass
        else:
            conexao= sqlite3.connect("bd_gestor_alugueis.sqlite")

            cursor= conexao.cursor()

            #aqui vai o sql do insert
            sql_insert = "INSERT INTO gestor_alugueis(item,descricao,status) VALUES(?,?,?)"
            
            cursor.execute(sql_insert,[item,descricao,"Disponivel"])
            
            conexao.commit()
            cursor.close()
            conexao.close()

            self.atualizar_tabela()

    def check_in(self):
        escolhida= self.treeview.selection()
    
        selecionado=self.treeview.item(escolhida)

        codigo= selecionado["values"][0]

        conexao = sqlite3.connect("bd_gestor_alugueis.sqlite")

        cursor = conexao.cursor()

        cursor.execute("""UPDATE gestor_alugueis
                       SET status=?
                       where id =?;""",("Alugado",codigo))

        conexao.commit()

        conexao.close()

        self.atualizar_tabela()
    
        pass

    def check_out(self):
        escolhida= self.treeview.selection()
    
        selecionado=self.treeview.item(escolhida)

        codigo= selecionado["values"][0]

        conexao = sqlite3.connect("bd_gestor_alugueis.sqlite")

        cursor = conexao.cursor()

        cursor.execute("""UPDATE gestor_alugueis
                       SET status=?
                       where id =?;""",("Disponivel",codigo))

        conexao.commit()

        conexao.close()

        self.atualizar_tabela()
   
        pass

    def atualizar_tabela(self):
        conexao= sqlite3.connect("bd_gestor_alugueis.sqlite")

        cursor= conexao.cursor()

        #aqui vai o sql do insert
        sql_insert = "SELECT * FROM gestor_alugueis;"
        
        cursor.execute(sql_insert)
        itens=cursor.fetchall()         
        
        conexao.commit()

        for linha in self.treeview.get_children():
            self.treeview.delete(linha)

        for a in itens:
            self.treeview.insert("",tk.END,values=a)


        cursor.close()
        conexao.close()
    


    #função para excluir item da tabela
    def excluir(self):
        escolhida= self.treeview.selection()
    
        selecionado=self.treeview.item(escolhida)

        codigo= selecionado["values"][0]

        conexao = sqlite3.connect("bd_gestor_alugueis.sqlite")

        cursor = conexao.cursor()

        cursor.execute("DELETE from gestor_alugueis where ID = ?;", [codigo])

        conexao.commit()

        conexao.close()

        self.atualizar_tabela()


    def alterar (self):

        item= self.campo_item.get()
        descricao= self.campo_descricao.get()
        
        escolhida= self.treeview.selection()
    
        selecionado=self.treeview.item(escolhida)

        codigo= selecionado["values"][0]

        conexao = sqlite3.connect("bd_gestor_alugueis.sqlite")

        cursor = conexao.cursor()

        cursor.execute("""UPDATE gestor_alugueis
                       SET item= ?, descricao=?
                       where id =?""",(item, descricao, codigo ))

        conexao.commit()

        conexao.close()

        self.atualizar_tabela()
   


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    ga= GestorDeAlugueis()
    ga.run()


