import tkinter as tk
from tkinter import ttk
from datetime import datetime
import cv2
from PIL import Image, ImageTk
import os
import sys

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro de personal")
ventana.geometry("500x500")
# Crear un estilo para el Notebook
style = ttk.Style()

# Cambiar el color de fondo de las pestañas
style.configure("TNotebook", tabposition="nw")  # Cambiar la posición de las pestañas si es necesario
style.configure("TNotebook.Tab", background="blue", padding=[10, 5], font=("Arial", 10, "bold"))

style.configure("TNotebook", background="#212121")
# Crear un Notebook (gestor de pestañas)
notebook = ttk.Notebook(ventana, style="TNotebook")
notebook.pack(fill="both", expand=True)

# Crear un estilo para los frames dentro del Notebook
style.configure("TFrame", background="black")

# Crear las pestañas
frame1 = ttk.Frame(notebook, style="TFrame")
frame2 = ttk.Frame(notebook, style="TFrame")
frame3 = ttk.Frame(notebook, style="TFrame")

notebook.add(frame1, text="Registro")
def enviar():
    personal = ["Juan", "Pedro", "Maria","Julio","Santiago"]
    passw = ["a@DOU2@Sds","ppD2ddDDO","DTD2O##Dp" ,"UaSaos#sa#","admin"]
#SE MEJORO LA PARTE DE SESIÓN
    if str(nombre_c.get()).lower() in [nombre.lower() for nombre in personal]:  # Verificar si el nombre ingresado está en la lista
        if str(passw_c.get()) in passw:
            label2.config(text=f"Bienvenido {nombre_c.get()} al Gestor de tareas")
            # Cerrar la primera pestaña
            notebook.forget(frame1)

            # Agregar la segunda pestaña
            notebook.add(frame2,text="Gestor de tareas")
            notebook.select(frame2)
        else:
            notebook.forget(frame1)
            notebook.add(frame3,text="Error")
            notebook.select(frame3)
            error.pack(pady=5)
            error.config(text="Su contraseña es incorrecto.")

    else:
        notebook.forget(frame1)
        notebook.add(frame3,text="Error")
        notebook.select(frame3)
        error.pack(pady=5)
        error.config(text="Su nombre es incorrecto.")
    

def noticias():
    textos_inf.config(text="No hay noticias nuevas",fg="red")
    textos_inf.pack(pady=5)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara")


# Obtener la ruta al archivo Haar dentro del ejecutable
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
cascade_path = os.path.join(base_path, 'ha<arcascades', 'haarcascade_eye.xml')

# Cargar el clasificador Haar
body_cascade = cv2.CascadeClassifier(cascade_path)

# Función para detectar cuerpos
def detectar_cuerpo(frame):
    # Convertir a escala de grises para mejorar la detección
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar los cuerpos en la imagen
    bodies = body_cascade.detectMultiScale(gray, 1.1, 3)
    
    # Dibujar rectángulos alrededor de los cuerpos detectados
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return frame

# Función para actualizar la imagen de la cámara en la interfaz de Tkinter
def actualizar_camara():
    label_camara.pack(pady=5)
    ret, frame = cap.read()
    if ret:
        # Detectar el cuerpo en la imagen
        frame = detectar_cuerpo(frame)

        # Convertir la imagen de BGR a RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convertir a imagen de PIL
        img_pil = Image.fromarray(frame_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        # Actualizar el label con la nueva imagen
        label_camara.config(image=img_tk)
        label_camara.image = img_tk  # Mantener una referencia a la imagen

    # Llamar a la función nuevamente después de 10 ms
    frame2.after(10, actualizar_camara)



#Ventana 1
nombre = tk.Label(frame1,text="Colocar su nombre",bg="black",fg="white")
nombre.pack(pady=5)
nombre_c = tk.Entry(frame1)
nombre_c.pack(pady=5)

passw = tk.Label(frame1,text="Colocar su contraseña",bg="black",fg="white")
passw.pack(pady=5)
passw_c = tk.Entry(frame1, show="*")
passw_c.pack(pady=5)

enviar = tk.Button(frame1,text="Enviar",command=enviar)
enviar.pack(pady=5)
#Ventana 2

label2 = tk.Label(frame2, text="",bg="black",fg="white")
label2.pack(pady=20)

label_camara = tk.Label(frame2)


def actualizar_hora():
    hora.config(text=datetime.now().strftime("%H:%M:%S"))
    hora.after(1000, actualizar_hora)

hora = tk.Label(frame2,text=datetime.now().strftime("%H:%M:%S"),bg="black",fg="white")
hora.after(1000, actualizar_hora)
hora.pack(pady=5)


botones = tk.Label(frame2,text="¿Qué quieres hacer?",bg="black",fg="white")
botones.pack(pady=5)

botones_1 = tk.Button(frame2,text="Noticias", command=noticias,bg="black",fg="white")
botones_1.pack(pady=5)

botones_2 = tk.Button(frame2,text="Buscar camara",command=actualizar_camara,bg="black",fg="white")
botones_2.pack(pady=5)


textos_inf = tk.Label(frame2,text="",bg="black")

#Ventana 3

no_inc = tk.Label(frame3,text="Vuelve a intetar mas tarde",bg="black",fg="white")
no_inc.pack(pady=5)
error = tk.Label(frame3,text="",bg="black",fg="white")
# Ejecutar el bucle principal de la aplicación

ventana.mainloop()