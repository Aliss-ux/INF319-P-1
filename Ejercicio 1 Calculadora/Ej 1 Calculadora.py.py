from tkinter import *

ventana= Tk()
ventana.title("Calculadora")

ventana.configure(background = 'gray10')

i=0
#Entrada de texto
e_texto = Entry(ventana, font=('Comic sens MC', 23, 'bold'), bg = 'light blue')
e_texto.grid(row=0, column = 0, columnspan = 4, padx=5, pady=5)

#FUNCIONES
def presionaBoton(res):
	global i
	e_texto.insert(i,res)
	i+=1

def borrarTodo():
	e_texto.delete(0,END)
	i=0

def borrarUno():
	global i
	if i!=0:
		
		i-=1
		e_texto.delete(i,END)
	
	#i-=1

def hacer_operacion():
	ecuacion = e_texto.get()
	resultado = eval(ecuacion)
	e_texto.delete(0,END)
	e_texto.insert(0,resultado)
	i = 0

def hacer_operacion2():
	global i
	ecuacion = e_texto.get()
	if i!=0:
		try:
			resultado = str(eval(ecuacion))
			e_texto.delete(0,END)
			e_texto.insert(0,resultado)
			longitud = len(resultado)
			i = longitud
		except:
			resultado= "ERROR"
			e_texto.delete(0,END)
			e_texto.insert(0,resultado)
		else:
			pass

#botones
boton1 = Button(ventana, text = "1", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center", command = lambda: presionaBoton(1))
boton2 = Button(ventana, text = "2", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center", command = lambda: presionaBoton(2))
boton3 = Button(ventana, text = "3", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center", command = lambda: presionaBoton(3))
boton4 = Button(ventana, text = "4", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center",command = lambda: presionaBoton(4))
boton5 = Button(ventana, text = "5", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center",command = lambda: presionaBoton(5))
boton6 = Button(ventana, text = "6", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center",command = lambda: presionaBoton(6))
boton7 = Button(ventana, text = "7", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center",command = lambda: presionaBoton(7))
boton8 = Button(ventana, text = "8", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center",command = lambda: presionaBoton(8))
boton9 = Button(ventana, text = "9", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center",command = lambda: presionaBoton(9))
boton0 = Button(ventana, text = "0", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='IndianRed3', anchor="center",command = lambda: presionaBoton(0))

boton_borrar = Button(ventana, text = "AC", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='brown4', anchor="center", command = lambda: borrarTodo())
boton_borrar1 = Button(ventana, text = "⌫", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='brown1', anchor="center",command = lambda: borrarUno())
boton_parentesis1 = Button(ventana, text = "(", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='sienna1', anchor="center",command = lambda: presionaBoton("("))
boton_parentesis2 = Button(ventana, text = ")", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12),relief="raised", bg='sienna1', anchor="center",command = lambda: presionaBoton(")"))
boton_punto = Button(ventana, text = ".", width = 5, height = 2,borderwidth=2,  font=('Comic sens MC', 12, 'bold'),relief="raised", bg='RosyBrown1', anchor="center", command = lambda: presionaBoton("."))

boton_div = Button(ventana, text = "÷", width = 5, height = 2,borderwidth=2,  font=('Comic sens MC', 12,'bold'),relief="raised", bg='sienna1', anchor="center",command = lambda: presionaBoton("/"))
boton_mult = Button(ventana, text = "×", width = 5, height = 2,borderwidth=2,  font=('Comic sens MC', 12,'bold'),relief="raised", bg='sienna1', anchor="center", command = lambda: presionaBoton("*"))
boton_sum = Button(ventana, text = "+", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12,'bold'),relief="raised", bg='sienna1', anchor="center",command = lambda: presionaBoton("+"))
boton_res = Button(ventana, text = "-", width = 5, height = 2,borderwidth=2,  font=('Comic sens MC', 12,'bold'),relief="raised", bg='sienna1', anchor="center", command = lambda: presionaBoton("-"))
boton_igual = Button(ventana, text = "=", width = 5, height = 2, borderwidth=2,  font=('Comic sens MC', 12,'bold'),relief="raised", bg='green', anchor="center",command = lambda: hacer_operacion2())

#posiciones
#boton.grid(row= , column = , padx = 5, pady=5)

boton_borrar1.grid(row=1 , column =0 , padx =1, pady=1)
boton_parentesis1.grid(row=1 , column =1 , padx =0, pady=1)
boton_parentesis2.grid(row=1, column =2 , padx =0, pady=1)
boton_div.grid(row=1, column =3 , padx =1, pady=1)

boton7.grid(row=2 , column =0 , padx =1, pady=1)
boton8.grid(row= 2, column = 1, padx =1, pady=1)
boton9.grid(row=2 , column =2 , padx =1, pady=1)
boton_mult.grid(row=2, column =3 , padx =1, pady=1)

boton4.grid(row=3, column = 0, padx =1, pady=1)
boton5.grid(row=3, column = 1, padx =1, pady=1)
boton6.grid(row=3, column = 2, padx =1, pady=1)
boton_res.grid(row=3, column = 3, padx = 1, pady=1)



boton1.grid(row=4, column = 0, padx = 1, pady=1)
boton2.grid(row=4, column = 1, padx = 1, pady=1)
boton3.grid(row=4, column = 2, padx = 1, pady=1)
boton_sum.grid(row=4, column = 3, padx = 1, pady=1)

boton0.grid(row=5, column = 0,columnspan=1, padx = 1, pady=1)
boton_punto.grid(row=5, column = 1, padx =1, pady=1)
boton_borrar.grid(row=5, column = 2, padx =1, pady=1)
boton_igual.grid(row=5, column = 3, padx =1, pady=1)


ventana.mainloop()