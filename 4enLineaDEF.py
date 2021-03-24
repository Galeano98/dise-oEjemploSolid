
import tkinter
from tkinter import *
# variable que controla el turno

turno = True





#Hacer crecer lista y matriz al mismo tiempo, matriz es la que aumenta,
#boton es solo lo que se muestra

# matriz logica infinita
listaindice = [0,1,2,3,4,5,6]

Matriz=[]

#En realidad guarda algo similar a:

#[[0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0],

# [0,0,0,0,0,0,0]]

#Lista que tiene el contador de cada fila existente en la matriz

contadores = []


#matriz de botones, es de 6 filas por 7 columnas, solo que

# el la primera fila la uso como boton de indicar columna de juego

# aunque la incio con ceros, luego la cargo de botones

boton=[

        [0,0,0,0,0,0,0,0],

        [0,0,0,0,0,0,0,0],

        [0,0,0,0,0,0,0,0],

        [0,0,0,0,0,0,0,0],

        [0,0,0,0,0,0,0,0],

        [0,0,0,0,0,0,0,0],

        [0,0,0,0,0,0,0,0]]



#inicio de la clase

class App(tkinter.Tk):
    def __init__(self, cols, rows):
        global Matriz,turno,flecha
        tkinter.Toplevel.__init__(self)
        self.title("4 in line")
        self.geometry('900x900') 
        self.flecha = Label(self,text='<- Turno',font='Verde')
        self.flecha.place(x=165,y=547)  
        self.cargarDatosMatriz()
        self.contadoresBotones ()
        self.cols = len(matriz[0])
        self.rows = len(matriz)
        self.mainFrame = tkinter.Frame(self)
        self.minsize(800,660)
        self.maxsize(800,800)
        self.mainFrame.grid()
        self.create_buttons()
        self.pintarMatriz ()
        menubar = tkinter.Menu(self)
        menubar.add_command(label="Salir",command =self.destroy)
        menubar.add_command(label = "Guardar Partida", command = self.guardarPartida)
        self.config(menu=menubar)




    def create_buttons(self):
        global matriz 
        for i in range(self.rows): 
            for j in range(self.cols): 
                btn = tkinter.Button(self.mainFrame,bg="white",
                                    width=10,height =5,fg="white",
                                    command = self.say_hi)
                btn.grid(row=i, column=j)
                boton[i][j] = btn
        boton[0][0].config(bg = 'Lime Green', command = lambda: self.rellenar (0))
        boton[0][1].config(bg = 'Tomato', command = lambda: self.rellenar (1))
        boton[0][2].config(bg = 'Lime Green', command = lambda: self.rellenar (2))
        boton[0][3].config(bg = 'Tomato', command = lambda: self.rellenar (3))
        boton[0][4].config(bg = 'Lime Green', command = lambda: self.rellenar(4))
        boton[0][5].config(bg = 'Tomato', command = lambda: self.rellenar (5))
        boton[0][6].config(bg = 'Lime Green', command = lambda: self.rellenar (6))



    def say_hi(self):
        print ('Hello')


    def rellenar (self, col):
        global turno, contadores,flechas
        if turno:
            self.flecha.place(x=165,y=592)
        else:
            self.flecha.place(x=165,y=547)

        if contadores [col] < 0:

            return ''
        elif turno:
            if matriz [contadores [col]][col] == 0:
                matriz [contadores[col]][col] = 1
                boton [contadores[col]][col].config (bg = "red")
            contadores [col] -= 1
        else:
            if matriz [contadores[col]][col] == 0:
                matriz [contadores[col]][col] = 2
                boton [contadores[col]][col].config (bg = "green")
            contadores [col] -= 1
        turno = not turno
        




    def guardarPartida (self):
        self.sobreescribir ('matriz.txt', str(matriz))



    def cargarDatosMatriz (self):
        global matriz

        lectura = self.leerTodo ('matriz.txt')
        if lectura == '':
            matriz=[
                [0,0,0,0,0,0,0],

                [0,0,0,0,0,0,0],

                [0,0,0,0,0,0,0],

                [0,0,0,0,0,0,0],

                [0,0,0,0,0,0,0],

                [0,0,0,0,0,0,0]]
        else:
            matriz = eval (lectura)



#Pinta la matriz con los datos que tiene guardados el archivo
            
    def pintarMatriz (self):
        global matriz
        lin = -1
        col = -1
        for linea in matriz:
            lin += 1
            col = -1
            for ele in linea:
                col += 1
                if ele == 1:
                    boton [lin][col].config (bg = "yellow")
                elif ele == 2:
                    boton [lin][col].config (bg = "blue")
        
                    



    def leerTodo (self, nombreArchivo):
        archivo = open (nombreArchivo, "r+")
        contenido = archivo.read()
        archivo.close
        return contenido


    def sobreescribir (self, nombreArchivo, texto):
        archivo = open (nombreArchivo, "w+")
        archivo.seek (0,2)
        archivo.write(texto)
        archivo.close()


    def contadoresBotones (self):
        global matriz, contadores

        bandera = True

        contadores = [len (matriz)-1] * len (matriz [0])

        for col in range (0, len (matriz [0])):
            bandera = True
            for lin in range (0, len (matriz)):
                if bandera == False:
                    break
                elif matriz [lin][col] != 0:
                    contadores [col] = lin -1
                    bandera = False
                    
def usuarios():
    global user
    user = Toplevel()
    user.title("Digite su usuario")
    user.geometry("400x400+0+0")
    user.config(bg="Lime Green")
    usuario1= StringVar()
    usuario2= StringVar()
    label = Label(user, text="Digite los nombres de usuario:",bg='Lime Green',font='Helvetica 16').place(x=14,y=14)
    label1 = Label(user, text="Usuario 1:",bg='pink',font='Helvetica 16').place(x=50,y=40)
    label2 = Label(user, text="Usuario 2:",bg='pink',font='Helvetica 16').place(x=50,y=90)
    user1 = Entry(user,textvariable=usuario1,insertbackground='pink',font='Helvetica 16',width=22,fg='#0c125c',bg='SkyBlue').place(x=50,y=60)
    user2 = Entry(user,textvariable=usuario2,insertbackground='pink',font='Helvetica 16',width=22,fg='#0c125c',bg='SkyBlue').place(x=50,y=110)
    btolis= Button(user, text="Listo",command=lambda: users(usuario1,usuario2),width=37,bg="SkyBlue").place(x=50,y=150)
def users(x,y):
    global a, user, turno,flecha
    us1=x.get()
    us2=y.get()
    if len(us1)<1 or len(us2)<1:
        return messagebox.showerror("Debe ingresar un nombre")
    a=App(6,6)
    boton1=Button(a,text="Menu",bg="pink",font="Verdana 12",width=10,command=cerrar_juego).place(x=630,y=14)
    lbluser1 = Label(a,font='Helvetica 16', text= 'Mario:').place(x=14,y=525)
    lbluser2 = Label(a,font='Helvetica 16', text= 'Luigi:').place(x=14,y=570)
    nom1= Label(a,text=us1,width=15,font='Verdana 11')
    nom1.place(x=28,y=547)
    nom2= Label(a,text=us2,width=15,font='Verdana 11')
    nom2.place(x=28,y=592)
    menu.withdraw()
    user.withdraw()

def cerrar_juego():
    global a
    a.withdraw()
    menu.deiconify()
def abrir_juego():
    global a
    usuarios()
    menu.withdraw()
            


menu=tkinter.Tk()
menu.geometry("650x650+550+150")
menu.config(bg="Ivory2")
menu.resizable(0,0)


bto1 = Button(menu, text="Puntajes",width=12, font="Helvetica 16", bg="SkyBlue")
bto1.place(x=60,y=120)
bto2 = Button(menu, text="Un Jugador",width=12,font="Helvetica 16", bg="SkyBlue")
bto2.place(x=480,y=120)
bto3 = Button(menu, text="Dos Jugadores",width=12, font="Helvetica 16", bg="SkyBlue",command=abrir_juego)
bto3.place(x=480,y=190)
bto4 = Button(menu, text="Cargar Partida",width=12, font="Helvetica 16", bg="SkyBlue")
bto4.place(x=60,y=190)
bto5 = Button(menu, text="Salir ",width=12,font="Helvetica 16", bg="light blue",command=menu.destroy)
bto5.place(x=270,y=160)


menu.mainloop()









