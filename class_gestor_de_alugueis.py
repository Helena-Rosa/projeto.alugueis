import ttkbootstrap as ttk
import tkinter as tk
import sqlite3



class GestorDeAlugueis:
    def __init__(self):

        #arrumar essa parte do banco de dados na proxima aula
        conexao= sqlite3.connect("05_lista_tarefas/bd_lista_tarefa.sqlite")

        cursor= conexao.cursor()

        #aqui vai o sql do insert
        sql_insert = ""
        
        cursor.execute(sql_insert)
        
        conexao.commit()
        cursor.close()
        conexao.close()
    
        
        #configuração da janela principal e da Treeview
        self.janela = ttk.Window(themename="morph")
        self.janela.title("Gestor de Aluguéis")
        self.janela.geometry("950x950+0+0")

       
       
        #texto para escrever as informações de comando (item_nome)
        item= label_item = ttk.Label (self.janela,
                                        text= "ITEM:",
                                        font={"success" , 25})
        item= label_item.pack()



        #campo de espaço para escrever as infomaçoes pedidas (item_nome) 
        self.campo_item = ttk.Entry(self.janela, width=50)
        self.campo_item.pack(pady=5)



        #texto para escrever as informações de comando (descrição)
        descricao= label_senha = ttk.Label (self.janela,
                                        text= "DESCRIÇÃO:",
                                        font={"success" , 25})
        descricao= label_senha.pack()


        #campo de espaço para escrever as infomaçoes pedidas (descrição) 
        self.campo_descricao = ttk.Entry(self.janela, width=50)
        self.campo_descricao.pack(pady=5)

    
        #texto para escrever as informações de comando (status)
        status= label_status = ttk.Label (self.janela,
                                        text= "STATUS:",
                                        font={"success" , 25})
        status= label_status.pack()


        #campo de espaço para escrever as infomaçoes pedidas (status) 
        self.campo_status = ttk.Entry(self.janela, width=50)
        self.campo_status.pack(pady=5)

        self.treeview = ttk.Treeview(self.janela)
        self.treeview.pack(padx=10, pady=10, fill="both", expand=True)


        #informações do cabeçalho
        self.treeview["columns"] = ("ITEM", "DESCRIÇÃO", "STATUS" )
        self.treeview["show"] = "headings"

        #Configuração dos cabeçalhos da self.treeview
        self.treeview.heading ("ITEM", text="NOME DO ITEM:")
        self.treeview.heading ("DESCRIÇÃO", text="DESCRIÇÃO:")
        self.treeview.heading ("STATUS", text= "STATUS:")
        

        #criar colunas
        self.treeview.column("ITEM", width=50)
        self.treeview.column("DESCRIÇÃO", width=50)
        self.treeview.column ("STATUS", width=50)


       #função do botão 
        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack () 


        #função botão para ADICIONA, comando de verificação para ver se esta certo e a posição que o botão ADICIONAR esta posicionado
        self.botao_teste = ttk.Button(frame_botao,text="ADICIONAR",command=self.adicionar).pack(side="left",pady= 40, padx=20)

        #função botão para CONCLUIR, comando par confirmar se deseja sair mesmo e a posição que o botão CONCLUIR esta posicionado
        ttk.Button(frame_botao,text="CONCLUIR", command=self.concluir).pack(side="right", pady= 40, padx=20  )  

         #função botão para EXCLUIR, comando par confirmar se deseja sair mesmo e a posição que o botão EXCLUIR esta posicionado
        ttk.Button(frame_botao, text="EXCLUIR",command=self.excluir).pack(side="right", pady= 40, padx=20  )  
    
    
    #função para adicionar o item da tabela
    def adicionar(self):
        item= self.campo_item.get()
        descricao= self.campo_descricao.get()
        status= self.campo_status.get()
        if item=="" or descricao=="" or status=="":
            pass
        else:
            self.treeview.insert("",tk.END,values=[item,descricao,status])


    #função para excluir item da tabela
    def excluir(self):
        escolhida= self.treeview.selection()
    
        selecionado=self.treeview.item(escolhida)
        self.treeview.delete(escolhida)



    #função para concluir algum item da tabela
    def concluir(self):
        self.treeview.tag_configure('cor_especial', background='lightblue', foreground='black')
        self.treeview.tag_configure('outra_cor', background='yellow', foreground='red')

        selecionado=self.treeview.selection()

        self.treeview.item(selecionado,tags='cor_especial')

        


    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    ga= GestorDeAlugueis()
    ga.run()


