from tkinter import *
from tkinter import ttk
from conexion import *
import tkinter.messagebox as mb

def ventana():
    ventana = Tk()
    ventana.title("Sistema de tickets")
    ventana.config(bg = '#06283D')
    ventana.geometry('955x500')
    ventana.resizable(0,0)
    app = Registro_ingeniero(ventana)
    app.mainloop()

#La clase hereda de 'Frame', que recibe un master (ventana principal o raíz) como argumento.
class Registro_ingeniero(Frame):

    def __init__(self, master):
        super().__init__(master)

        #self.master = master
        self.background = '#06283D'
        self.letterbg = '#fff'

        self.identificacion = StringVar()
        self.nombre = StringVar()
        self.nombre_buscar = StringVar()
        self.correo = StringVar()
        self.telefono = StringVar()
        self.salario = StringVar()

        self.base_datos = Conexion()
        self.crear_widgets()

    def crear_widgets(self):
        Label(self.master, text='Bienvenido Usuario', height=1, width=10, bg='#f0687c', fg=self.letterbg, font=('Arial', '12', 'bold')).pack(side=TOP,fill=X)
        Label(self.master, text='R E G I S T R O S   D E   I N G E N I E R O', height=2, width=10, bg='#c36464', fg=self.letterbg, font=('Arial', '12', 'bold')).pack(side=TOP,fill=X)
        Entry(self.master, textvariable=self.nombre_buscar, width=15, font=('Arial','10')).place(x=650,y=35)
        Button(self.master, command=self.consultar_nombre,text='Buscar',font=('Arial', '8', 'bold'), bg='lightgreen').place(x=760,y=35)

        Label(self.master, text='Agregar nuevo registro', width=20, height=1,bg=self.background, fg=self.letterbg, font=('Arial', '12', 'bold')).place(x=70,y=75)
        Label(self.master, text='Identificacion', width=20, height=1,bg=self.background, fg=self.letterbg, font=('Arial', '12', 'bold')).place(x=0,y=120)
        Label(self.master, text='Nombre', width=20, height=1,bg=self.background, fg=self.letterbg, font=('Arial', '12', 'bold')).place(x=0,y=155)
        Label(self.master, text='Correo', width=20, height=1,bg=self.background, fg=self.letterbg, font=('Arial', '12', 'bold')).place(x=0,y=190)
        Label(self.master, text='Telefono', width=20, height=1,bg=self.background, fg=self.letterbg, font=('Arial', '12', 'bold')).place(x=0,y=225)
        Label(self.master, text='Salario', width=20, height=1,bg=self.background, fg=self.letterbg, font=('Arial', '12', 'bold')).place(x=0,y=260)

        Entry(self.master, textvariable=self.identificacion, width=15, font=('Arial','10')).place(x=200,y=120)
        Entry(self.master, textvariable=self.nombre, width=15, font=('Arial','10')).place(x=200,y=155)
        Entry(self.master, textvariable=self.correo, width=15, font=('Arial','10')).place(x=200,y=190)
        Entry(self.master, textvariable=self.telefono, width=15, font=('Arial','10')).place(x=200,y=225)
        Entry(self.master, textvariable=self.salario, width=15, font=('Arial','10')).place(x=200,y=260)
        
        Label(self.master, text='Opciones', width=20, height=1,bg=self.background, fg='white', font=('Arial', '12', 'bold')).place(x=75,y=320)
        Button(self.master, command=self.insertar_ingeniero, text="Insertar", font=('Arial', '12', 'bold'), bg='lightblue').place(x=80,y=360)
        Button(self.master, command=self.actualizar_datos, text="Actualizar", font=('Arial', '12', 'bold'), bg='lightgreen').place(x=130,y=410)
        Button(self.master, command=self.eliminar_ingeniero, text="Borrar", font=('Arial', '12', 'bold'), bg='lightpink').place(x=190,y=360)

        Button(self.master, command=self.cerrar_ventana, text="Salir", font=('Arial', '12', 'bold'), bg='lightblue').place(x=900,y=460)
        Button(self.master, command=self.mostrar_ingenieros, text="Mostrar registros ", font=('Arial', '12', 'bold'), bg='lightgreen').place(x=740,y=460)
        Button(self.master, command=self.limpiar_campos, text="Limpiar campos", font=('Arial', '12', 'bold'), bg='lightpink').place(x=590,y=460)
        Button(self.master, command=self.limpiar_tabla, text="Limpiar tabla", font=('Arial', '12', 'bold'), bg='lightblue').place(x=460,y=460)

        self.tabla = ttk.Treeview(self.master, height=18)
        self.tabla.place(x=350,y=75)

        self.tabla['columns'] = ('Nombre', 'Correo', 'Telefono', 'Salario')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=130 , anchor='center')
        self.tabla.column('Correo', minwidth=100, width=120, anchor='center' )
        self.tabla.column('Telefono', minwidth=100, width=120 , anchor='center')
        self.tabla.column('Salario', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='Identificación', anchor ='center')
        self.tabla.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla.heading('Correo', text='Correo', anchor ='center')
        self.tabla.heading('Telefono', text='Telefono', anchor ='center')
        self.tabla.heading('Salario', text='Salario', anchor ='center')

        estilo = ttk.Style(self.master)
        estilo.theme_use('default') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='black')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', '#c36464')], foreground=[('selected','black')] )

        #.bind() = Se utiliza para enlazar un evento con una función. Ejem: Obtener los valores de una fila 
        # a traves de un click
        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  #Obtiene los valores de una fila.
        self.tabla.bind("<Double-Button-1>", self.obtener_campos) #Pone los valores de una filas en cada Entry.

    def insertar_ingeniero(self):
        try:
            identificacion = self.identificacion.get()
            nombre = self.nombre.get()
            correo = self.correo.get()
            telefono = self.telefono.get()
            salario = self.salario.get()
            datos = (nombre, correo, telefono, salario)

            #Si ningún campo es vacío inserte los valores en la tabla.
            if identificacion and nombre and correo and telefono and salario !='':        
                self.base_datos.insertar_registro(identificacion, nombre, correo, telefono, salario)
                self.tabla.insert('',0, text = identificacion, values=datos)
                
        
        except Exception as e:
            self.mostrar_mensaje_error(f"Error inesperado: {str(e)}")

    def consultar_nombre(self):
        nombre_ingeniero = self.nombre_buscar.get()
        nombre_ingeniero = str("'" + nombre_ingeniero + "'")
        nombre_buscado = self.base_datos.busca_registro(nombre_ingeniero)
        self.tabla.delete(*self.tabla.get_children())

        fila = -1
        for dato in nombre_buscado:
            fila += 1                       
            self.tabla.insert('',fila, text = nombre_buscado[fila][0:1], values=nombre_buscado[fila][1:6])

    def eliminar_ingeniero(self):
        fila = self.tabla.selection()
        if len(fila) != 0:
            self.tabla.delete(fila)
            fila_borrar = ("'" + str(self.nombre_borrar) + "'")
            self.base_datos.eliminar_registro(fila_borrar)

    def actualizar_datos(self):
        fila_actualizar = self.tabla.focus() #Obtiene la fila seleccionada
        identificacion = self.identificacion.get()
        nombre = self.nombre.get()
        correo = self.correo.get()
        telefono = self.telefono.get()
        salario = self.salario.get()

        if identificacion and nombre and correo and telefono and salario !='':
            self.tabla.item(fila_actualizar, text= identificacion, values=(nombre,correo,telefono,salario))
            self.base_datos.actualizar(identificacion, nombre, correo, telefono, salario)
    
    def mostrar_ingenieros(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_registro()
        fila = -1
        for dato in registro:
            fila+=1                       
            self.tabla.insert('',fila, text = registro[fila][0:1], values=registro[fila][1:5])
    
    
    def obtener_fila(self, event):
        #.focus() = obtiene el item actualmente seleccionado
        fila_seleccionada = self.tabla.focus()
        if not fila_seleccionada:
            return
        #.item() = obtiene la información de la fila u objeto seleccionado. Retorna un diccionario (datos).
        datos = self.tabla.item(fila_seleccionada)
        #Se obtiene la clave 'values'. Se utiliza el indice [0] para acceder al primer valor de 'values',
        #en este caso el nombre.
        self.nombre_borrar = datos['values'][0]

    def obtener_campos(self, event):
        fila_seleccionada = self.tabla.focus()
        if not fila_seleccionada:
            return
        datos = self.tabla.item(fila_seleccionada)
        self.identificacion.set(datos['text'])
        self.nombre.set(datos['values'][0])
        self.correo.set(datos['values'][1])
        self.telefono.set(datos['values'][2])
        self.salario.set(datos['values'][3])

    def limpiar_campos(self):
        self.identificacion.set('')
        self.nombre.set('')
        self.correo.set('')
        self.telefono.set('')
        self.salario.set('')
        self.nombre_buscar.set('')
    
    def limpiar_tabla(self):
        self.tabla.delete(*self.tabla.get_children())

    def cerrar_ventana(self):
        self.master.destroy()

    def mostrar_mensaje_error(self, mensaje):
        # Mostrar un cuadro de diálogo con el mensaje de error
        mb.showerror("Error", mensaje)

ventana()
