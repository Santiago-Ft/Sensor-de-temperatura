import tkinter as Ventana
import random

class Sensor:
    def __init__(self):
        self.ventana = ""
        self.labeltemperatura = None
        self.labelhumedad = None
        self.labelnumero = 0
        self.dato = {}
        self.base = []
        self.temperatura = ""
        self.humedad = ""
    def Iniciar(self):
        self.ventana = Ventana.Tk()
        self.ventana.geometry("500x500")
        self.ventana.title("Terminal de sensor de temperatura")
        self.ventana.resizable(False, False)
        self.labeltitulo = Ventana.Label(self.ventana, text="Muestreo del sensor").pack()
        self.labeltemperatura = Ventana.Label(self.ventana, text="Temperatura:")
        self.labeltemperatura.pack()
        self.labelhumedad = Ventana.Label(self.ventana, text="Humedad:")
        self.labelhumedad.pack()
        self.labelcontador = Ventana.Label(self.ventana, text="Lectura #: 0")
        self.labelcontador.pack()
        self.botonterminar = Ventana.Button(self.ventana, text="Finalizar muestreo de datos", command=self.Terminar)
        self.botonterminar.pack()
        self.Calcular()
        self.ventana.mainloop()
        pass
    def Medir(self):
        temperatura = random.uniform(-20, 60)
        humedad = random.uniform(0, 100)
        return temperatura, humedad
    def Calcular(self):
        self.labelnumero += 1
        self.temperatura, self.humedad = self.Medir()
        self.dato = {}
        self.labelcontador.config(text=f"Lectura #: {self.labelnumero}")
        if not (0 <= self.temperatura <= 50):
            self.labeltemperatura.config(text=f"Temperatura fuera de rango: {self.temperatura:.2f}°")
        else:
            self.labeltemperatura.config(text=f"Temperatura: {self.temperatura:.2f}°")
        if not (20 <= self.humedad <= 90):
            self.labelhumedad.config(text=f"Humedad fuera de rango: {self.humedad:.2f}%")
        else:
            self.labelhumedad.config(text=f"Humedad: {self.humedad:.2f}%")
        self.dato["Lectura"] = self.labelnumero
        self.dato["Temperatura"] = self.temperatura
        self.dato["Humedad"] = self.humedad
        self.base.append(self.dato)
        self.ventana.after(2000, self.Calcular)
    def Terminar(self):
        self.ventana.destroy()
        print("Datos registrados:")
        for dato in self.base:
            print(dato)

objSensor=Sensor().Iniciar()
