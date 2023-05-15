import os
import speech_recognition as sr
import pyttsx3
import sqlite3
import webbrowser

# Configuración del reconocedor de voz
reconocedor = sr.Recognizer()

# Configuración del sintetizador de voz
configuracion = pyttsx3.init()
configuracion.setProperty('voice', 'es-la')
configuracion.setProperty('rate', 100)
sintetizador = configuracion

# Función para reconocer voz


def reconocer_voz():
    with sr.Microphone() as source:
        print("Di algo...")
        audio = reconocedor.listen(source)

        try:
            texto = reconocedor.recognize_google(audio, language="es-ES")
            return texto
        except sr.UnknownValueError:
            print("No se pudo reconocer la voz.")
        except sr.RequestError as e:
            print("Error al realizar la solicitud: {0}".format(e))

# Función para obtener los datos de un estudiante por correo


def obtener_datos_estudiante(correo):
    conexion = sqlite3.connect('estudiantes.db')
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT Nombre, EstadoEconomico FROM Estudiantes WHERE Correo=?", (correo,))
    resultado = cursor.fetchone()

    conexion.close()

    return resultado

# Función para sintetizar voz


def sintetizar_voz(texto):
    sintetizador.say(texto)
    sintetizador.runAndWait()

# Función principal


def identificador_voz():
    while True:
        texto = reconocer_voz()

        if texto and texto.lower() == "hola":
            sintetizar_voz(
                "Buenos días, bienvenido a la única facultad sin cowork, introduce tu tarjeta.")
            tarjeta = input("Introduce tu tarjeta: ")

            # Obtener datos del estudiante
            datos_estudiante = obtener_datos_estudiante(tarjeta)

            if datos_estudiante:
                nombre, estado_economico = datos_estudiante
                mensaje = f"Hola {nombre}, tu estado económico es {estado_economico}."
                sintetizar_voz(mensaje)
                sintetizar_voz("Se te ofrece algo más?")
                respuesta = reconocer_voz()
                if respuesta and respuesta.lower() == "director":
                    sintetizar_voz(
                        "La oficina del ingeniero Sebastián Arce se encuentra en el primer piso, última oficina a la derecha.")
                elif respuesta and respuesta.lower() == "nula autoestima":
                    webbrowser.open(
                        "https://www.youtube.com/watch?v=NG6s_dD8pSc")
                sintetizar_voz("Se te ofrece algo más?")
                respuesta = reconocer_voz()
                if respuesta and respuesta.lower() == "no":
                    sintetizar_voz("Adiós, fue un placer.")
                    webbrowser.open(
                        "https://www.youtube.com/watch?v=BEFH2_kkBAk")
                break
            else:
                sintetizar_voz(
                    "Tarjeta no reconocida. Por favor, inténtalo de nuevo.")
                continue


identificador_voz()
