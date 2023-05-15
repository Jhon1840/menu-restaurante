from rfidiot.protocols import iso14443a

# Función para leer una tarjeta RFID
def leer_tarjeta_rfid():
    with iso14443a.Iso14443a() as rfid:
        print("Acerca la tarjeta RFID al lector...")
        uid = rfid.get_uid()
        if uid is not None:
            print("Tarjeta RFID detectada.")
            print("UID:", uid)
        else:
            print("No se detectó ninguna tarjeta RFID.")

# Llamar a la función de lectura de tarjetas RFID
leer_tarjeta_rfid()
