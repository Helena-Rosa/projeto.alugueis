import ttkbootstrap as ttk
import tkinter as tk
import sqlite3



class GestorDeAlugueis:
    def __init__(self):
        
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



        self.treeview["columns"] = ("ITEM", "DESCRIÇÃO", "STATUS" )
        self.treeview["show"] = "headings"

        #Configuração dos cabeçalhos da self.treeview
        self.treeview.heading ("ITEM", text="NOME DO ITEM:")
        self.treeview.heading ("DESCRIÇÃO", text="DESCRIÇÃO:")
        self.treeview.heading ("STATUS", text= "STATUS:")
        


        self.treeview.column("ITEM", width=50)
        self.treeview.column("DESCRIÇÃO", width=50)
        self.treeview.column ("STATUS", width=50)


       #função do botão 
        frame_botao = ttk.Frame(self.janela)
        frame_botao.pack () 


        #função botão para LOGAR, comando de verificação para ver se esta certo e a posição que o botão LOGAR esta posicionado
        self.botao_teste = ttk.Button(frame_botao,text="ADICIONAR",command=self.adicionar).pack(side="left",pady= 40, padx=20)

        #função botão para SAIR, comando par confirmar se deseja sair mesmo e a posição que o botão SAIR esta posicionado
        ttk.Button(frame_botao,text="CONCLUIR", command=self.concluir).pack(side="right", pady= 40, padx=20  )  


        ttk.Button(frame_botao, text="EXCLUIR",command=self.excluir).pack(side="right", pady= 40, padx=20  )  
    
    
    def adicionar(self):
        item= self.campo_item.get()
        descricao= self.campo_descricao.get()
        status= self.campo_status.get()
        if item=="" or descricao=="" or status=="":
            pass
        else:
            self.treeview.insert("",tk.END,values=[item,descricao,status])

    def excluir(self):
        escolhida= self.treeview.selection()
    
        selecionado=self.treeview.item(escolhida)
        self.treeview.delete(escolhida)

    
    def botao_concluir (self):
        selecionado = self.janela.curselection()
        self.janela.itemconfig(selecionado[0], {"bg": "green"})
                            
         #daqui para baixo é a função para jogar no banco de dados
        conclusao = selecionado[0] + 1
        
                            
        



    def run(self):
        self.janela.mainloop()

if __name__ == "__main__":
    ga= GestorDeAlugueis()
    ga.run()


