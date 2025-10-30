import ttkbootstrap as ttk
from tkinter import END

class GestorDeAlugueis:
    def __init__(self):
        self.alugueis = []
        self.carregar_alugueis()



#configuração da janela principal e da Treeview
janela = ttk.Window(themename="morph")
janela.title("Gestor de Aluguéis")
janela.geometry("2000x2000")

treeview = ttk.Treeview(janela)
treeview.pack(padx=10, pady=10, fill="both", expand=True)

treeview["columns"] = ("ID", "Clientes", "Imóveis", "Data de Início", "Data de Término", "Valor Mensal")
treeview["show"] = "headings"

#Configuração dos cabeçalhos da Treeview
treeview.heading ("ID", text="ID:")
treeview.heading ("Clientes", text="Clientes:")
treeview.heading ("Imóveis", text="Imóveis:")
treeview.heading ("Data de Início", text="Data de Início:")
treeview.heading ("Data de Término", text= "Data de Término:")
treeview.heading ("Valor Mensal", text="Valor Mensal:")


treeview.column("ID", width=50)
treeview.column("Clientes", width=50)
treeview.column ("Imóveis", width=50)
treeview.column ("Data de Início", width=50)
treeview.column ("Data de Término", width=50)
treeview.column ("Valor Mensal", width=50)







if __name__ == "__main__":
    GestorDeAlugueis()
    janela.mainloop()


