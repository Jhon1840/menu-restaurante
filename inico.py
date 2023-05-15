import speech_recognition as sr
reconocedor = sr.Recognizer()


def reconocer_voz():

    with sr.Microphone() as source:
        print("Escuchando...")
        audio = reconocedor.listen(source)

        try:
            texto = reconocedor.recognize_google(audio, language="es-ES")
            return texto
        except sr.UnknownValueError:
            print("No se pudo reconocer la voz.")
        except sr.RequestError as e:
            print("Error al realizar la solicitud: {0}".format(e))


def saludar():
    print("¡Buenos días!")
    print("Bienvenido")
    print("Por favor, introduzca su tarjeta.")


texto_transcrito = reconocer_voz()


if "buenos días" in texto_transcrito.lower():
    saludar()
else:
    print("No se reconoció el saludo de buenos días.")


texto_tarjeta = reconocer_voz()
print("Tarjeta introducida:", texto_tarjeta)
