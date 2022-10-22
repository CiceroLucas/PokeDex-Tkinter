from tkinter import *
from dados import *
from tkinter import ttk
from PIL import Image, ImageTk

co0 = "#444466" #Preta
co1 = "#feffff" #Branca
co2 = "#6f9fbd" #Azul
co3 = "#38576b" #Valor
co4 = "#403d3d" #Letra
co5 = "#ef5350" #Vermelha

janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

def trocar_pok(i):
    global imagem_pokemon, pok_image

    frame_pokemon['bg'] = pokemon[i]['tipo'][3]

    pok_nome['text'] = i
    pok_nome['bg'] = pokemon[i]['tipo'][3]
    pok_tipo['text'] = pokemon[i]['tipo'][1]
    pok_tipo['bg'] = pokemon[i]['tipo'][3]
    pok_id['text'] = pokemon[i]['tipo'][0]
    pok_id['bg'] = pokemon[i]['tipo'][3]

    imagem_pokemon = pokemon[i]['tipo'][2]

    imagem_pokemon = Image.open(imagem_pokemon)
    imagem_pokemon = imagem_pokemon.resize((238, 238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

    pok_image = Label(frame_pokemon, relief='flat', image=imagem_pokemon, font=('Ivy 10 bold'), bg=pokemon[i]['tipo'][3], fg=co1)
    pok_image.place(x=60, y=50)

    pok_tipo.lift()

    #status
    pok_hp['text'] = pokemon[i]['status'][0]
    pok_atack['text'] = pokemon[i]['status'][1]
    pok_defesa['text'] = pokemon[i]['status'][2]
    pok_velocidade['text'] = pokemon[i]['status'][3]
    pok_total['text'] = pokemon[i]['status'][4]

    #habilidades
    pok_hb1['text'] = pokemon[i]['habilidades'][0]
    pok_hb2['text'] = pokemon[i]['habilidades'][1]

#Frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

#nome
pok_nome = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Fixedsys 20'), fg=co1)
pok_nome.place(x=12, y=15)
#categoria
pok_tipo = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_tipo.place(x=12, y=50)
#id
pok_id = Label(frame_pokemon, text='', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co1)
pok_id.place(x=12, y=75)

#Status
pok_status = Label(janela, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

#hp
pok_hp = Label(janela, text='Hp: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

#atack
pok_atack = Label(janela, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atack.place(x=15, y=385)

#defesa
pok_defesa = Label(janela, text='Dedesa: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=410)

#velocidade
pok_velocidade = Label(janela, text='velocidade: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=435)

#total
pok_total = Label(janela, text='total: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)

# Habilidades
pok_habilidades = Label(janela, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_habilidades.place(x=180, y=310)

#habilidade 1
pok_hb1 = Label(janela, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb1.place(x=195, y=360)

#habiliade 2
pok_hb2 = Label(janela, text='Soco eletrico', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb2.place(x=195, y=385)

#botões
imagem_pokemon_1 = Image.open('images/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40, 40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_pok_1 = Button(janela, command=lambda:trocar_pok('Pikachu'), relief='flat', image=imagem_pokemon_1,  text='Pikachu', width=150 ,  overrelief=RIDGE,compound=LEFT , anchor=NW, padx=5 ,font=('Verdana 12'),  bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

imagem_pokemon_2 = Image.open('images/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40, 40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_pok_2 = Button(janela, command=lambda:trocar_pok('Bulbasaur'), relief='flat', image=imagem_pokemon_2,  text='Bulbasaur', width=150 ,  overrelief=RIDGE,compound=LEFT , anchor=NW, padx=5 ,font=('Verdana 12'),  bg=co1, fg=co0)
b_pok_2.place(x=375, y=65)

imagem_pokemon_3 = Image.open('images/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40, 40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_pok_3 = Button(janela, command=lambda:trocar_pok('Charmander'), relief='flat', image=imagem_pokemon_3,  text='Charmander', width=150 ,  overrelief=RIDGE,compound=LEFT , anchor=NW, padx=5 ,font=('Verdana 12'),  bg=co1, fg=co0)
b_pok_3.place(x=375, y=120)

imagem_pokemon_4 = Image.open('images/cabeca-dragonite.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40, 40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_pok_4 = Button(janela, relief='flat', command=lambda:trocar_pok('Dragonite'), image=imagem_pokemon_4,  text='Dragonite', width=150 ,  overrelief=RIDGE,compound=LEFT , anchor=NW, padx=5 ,font=('Verdana 12'),  bg=co1, fg=co0)
b_pok_4.place(x=375, y=175)

imagem_pokemon_5 = Image.open('images/cabeca-gengar.png')
imagem_pokemon_5 = imagem_pokemon_5.resize((40, 40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_pok_5 = Button(janela, relief='flat', command=lambda:trocar_pok('Gengar'), image=imagem_pokemon_5,  text='Gengar', width=150 ,  overrelief=RIDGE,compound=LEFT , anchor=NW, padx=5 ,font=('Verdana 12'),  bg=co1, fg=co0)
b_pok_5.place(x=375, y=230)

imagem_pokemon_6 = Image.open('images/cabeca-gyarados.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40, 40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_pok_6 = Button(janela, relief='flat', command=lambda:trocar_pok('Gyarados'), image=imagem_pokemon_6,  text='Gyarados', width=150 ,  overrelief=RIDGE,compound=LEFT , anchor=NW, padx=5 ,font=('Verdana 12'),  bg=co1, fg=co0)
b_pok_6.place(x=375, y=285)

trocar_pok('Charmander')

janela.mainloop()