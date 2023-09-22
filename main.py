from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# storage in memory
agenda = []
index = 0


def adicionarContato() -> None:
    # Pegando o valor digitado em txt_nome
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria = cb_categorias.get()
    contato = {
        "nome":nome,
        "telefone":telefone,
        "categoria":categoria
    }
    agenda.append(contato)
    atualizarTabela()
    limparCampos()
    #print(agenda)

    #limpandoo os campos
    # txt_nome.delete(0, END)
    # txt_telefone.delete(0,END)
    # cb_categorias.set("")
    # messagebox.showinfo("Enviado!", f"Bem vindo, {nome}")


def editarContato() -> None:
    agenda[index] = {
        "nome": txt_nome.get(),
        "telefone": txt_telefone.get(),
        "categoria": cb_categorias.get()
    }
    messagebox.showinfo("Editado!", f"contato editado")
    atualizarTabela()
    limparCampos()



def deletarContato() -> None:
    agenda.remove(agenda[index])
    messagebox.showinfo("Deletado!", "foi DELETADO!")
    limparCampos()
    atualizarTabela()





def limparCampos() -> None:
    # limpandoo os campos
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categorias.set("")
    #messagebox.showinfo("Enviado!", f"Bem vindo, {nome}")

def atualizarTabela() -> None:
    for linha in tabela.get_children():
        tabela.delete(linha)


    for contato in agenda:
     tabela.insert("",END,values=(contato["nome"],
                                 contato["telefone"],
                                 contato["categoria"]))



def tabelaClique(event) -> None:
    #obter linhaclicada
    linha_selecionada = tabela.selection()
    global index
    index=tabela.index(linha_selecionada[0])
    contato=agenda[index]
    limparCampos()

    txt_nome.insert(0,contato['nome'])
    txt_telefone.insert(0, contato['telefone'])
    cb_categorias.set(contato['categoria'])











janela = Tk()
janela.title("Agenda telefonica")

label_nome = Label(janela, text="Nome:", fg="red", font="Tahoma 14 bold")
label_nome.grid(row=0, column=0)

# Entry
txt_nome = Entry(janela, font="Tahoma 14", width=27)
txt_nome.grid(row=0, column=1)

label_telefone = Label(janela, text="Telefone:", fg="red", font="Tahoma 14 bold")
label_telefone.grid(row=1, column=0)

# Entry
txt_telefone = Entry(janela, font="Tahoma 14", width=27)
txt_telefone.grid(row=1, column=1)

# Combobox

label_categorias = Label(janela, text="Categoria:", fg="red", font="Tahoma 14 bold")
label_categorias.grid(row=2, column=0)

categorias = ["Amigos", "Família", "Trabalho"]
cb_categorias = ttk.Combobox(janela, values=categorias, width=25, font="Tahoma 14")
cb_categorias.grid(row=2, column=1)

# botão
btn_adicionar = Button(janela, text="Adicionar", fg="red",
                       font="Tahoma 12 bold", width=8, command=adicionarContato)
btn_adicionar.grid(row=3, column=0)

btn_editar = Button(janela, text="Editar", fg="red",
                    font="Tahoma 12 bold", width=8, command=editarContato)
btn_editar.grid(row=3, column=1)

btn_deletar = Button(janela, text="Deletar", fg="red",
                     font="Tahoma 12 bold", width=8, command=deletarContato)
btn_deletar.grid(row=3, column=2)

colunas = ["Nome","Telefone","Categoria"]

#Criando uma tabela/TreeView
tabela = ttk.Treeview(janela,columns=colunas,show="headings")

#uma forma de nomear as colunas
# tabela.heading("Nome",text="Nome")
# tabela.heading("Telefone",text="Telefone")
# tabela.heading("Categoria",text="Categoria")

#outra forma de nomear as colunas

for coluna in colunas:
    tabela.heading(coluna,text=coluna)
tabela.grid(row=4,columnspan=3)


tabela.bind("<ButtonRelease-1>",tabelaClique)






























# executa a janela

janela.mainloop()
