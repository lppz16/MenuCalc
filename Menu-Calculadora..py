from tkinter import Tk, Label, Button, Entry, Menu, Listbox, Scrollbar, END, ANCHOR, simpledialog
import math

def crear_ventana():
    bg_color = "#1DC4FF"
    fg_color = "#333"
    font = ("Arial", 12)

    vent = Tk()
    vent.title("Mega Calculadora")
    vent.geometry("800x600")
    vent.configure(bg=bg_color)

    def realizar_operacion(op):
        n1 = txt1.get()
        n2 = txt2.get()
        try:
            if op == '+':
                result = float(n1) + float(n2)
                operation = f"{n1} + {n2} = {result}"
            elif op == '-':
                result = float(n1) - float(n2)
                operation = f"{n1} - {n2} = {result}"
            elif op == '*':
                result = float(n1) * float(n2)
                operation = f"{n1} * {n2} = {result}"
            elif op == '/':
                result = float(n1) / float(n2)
                operation = f"{n1} / {n2} = {result}"
            elif op == 'abs':
                result = abs(float(n1))
                operation = f"Abs({n1}) = {result}"
            elif op == 'mcm':
                n1, n2 = int(n1), int(n2)
                result = abs(n1 * n2) // math.gcd(n1, n2)
                operation = f"MCM({n1}, {n2}) = {result}"
            elif op == 'mcd':
                n1, n2 = int(n1), int(n2)
                result = math.gcd(n1, n2)
                operation = f"MCD({n1}, {n2}) = {result}"
            else:
                raise ValueError("Operación desconocida")

            txt3.delete(0, 'end')
            txt3.insert(0, result)
            append_to_history(operation)
        except ValueError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")
        except ZeroDivisionError:
            txt3.delete(0, 'end')
            txt3.insert(0, "Error")

    def append_to_history(operation):
        history_listbox.insert(END, operation)

    def delete_history():
        selected_index = history_listbox.curselection()
        if selected_index:
            history_listbox.delete(selected_index)

    def edit_history():
        selected_index = history_listbox.curselection()
        if selected_index:
            old_value = history_listbox.get(selected_index)
            new_value = simpledialog.askstring("Editar", "Ingrese el nuevo valor:", initialvalue=old_value)
            if new_value:
                history_listbox.delete(selected_index)
                history_listbox.insert(selected_index, new_value)

    def crear_menu(vent):
        barra_menu = Menu(vent)
        vent.config(menu=barra_menu)
        
        menu_inicio = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Inicio", menu=menu_inicio)
        menu_inicio.add_command(label="Salir", command=vent.destroy)

        menu_operacion = Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Operación", menu=menu_operacion)
        menu_operacion.add_command(label="Sumar", command=lambda: realizar_operacion('+'))
        menu_operacion.add_command(label="Restar", command=lambda: realizar_operacion('-'))
        menu_operacion.add_command(label="Multiplicación", command=lambda: realizar_operacion('*'))
        menu_operacion.add_command(label="División", command=lambda: realizar_operacion('/'))
        menu_operacion.add_command(label="Valor Absoluto", command=lambda: realizar_operacion('abs'))
        menu_operacion.add_command(label="Mínimo Común Múltiplo", command=lambda: realizar_operacion('mcm'))
        menu_operacion.add_command(label="Máximo Común Divisor", command=lambda: realizar_operacion('mcd'))

    # Labels y Entries
    lbl1 = Label(vent, text="Número 1:", bg=bg_color, fg=fg_color, font=font)
    lbl1.place(x=50, y=30, width=150, height=30)
    txt1 = Entry(vent, bg="#fff")
    txt1.place(x=200, y=30, width=150, height=30)
    
    lbl2 = Label(vent, text="Número 2:", bg=bg_color, fg=fg_color, font=font)
    lbl2.place(x=50, y=80, width=150, height=30)
    txt2 = Entry(vent, bg="#fff")
    txt2.place(x=200, y=80, width=150, height=30)

    lbl3 = Label(vent, text="Resultado:", bg=bg_color, fg=fg_color, font=font)
    lbl3.place(x=50, y=130, width=150, height=30)
    txt3 = Entry(vent, bg="#FFF")
    txt3.place(x=200, y=130, width=150, height=30)

    # Historial
    history_listbox = Listbox(vent, width=50, height=10)
    history_listbox.place(x=400, y=30)

    # Botones para gestionar el historial
    delete_button = Button(vent, text="Eliminar", command=delete_history)
    delete_button.place(x=400, y=500, width=100, height=30)
    edit_button = Button(vent, text="Editar", command=edit_history)
    edit_button.place(x=520, y=500, width=100, height=30)

    # Llamada a la función para crear el menú
    crear_menu(vent)

    return vent

vent = crear_ventana()
vent.mainloop()
# Hola