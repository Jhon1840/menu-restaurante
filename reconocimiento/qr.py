import cv2
from pyzbar import pyzbar

def reconocer_codigos(imagen):
    
    imagen = cv2.imread(imagen)

    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    codigos = pyzbar.decode(imagen_gris)

    
    for codigo in codigos:
        tipo = codigo.type
        datos = codigo.data.decode("utf-8")     
        print("Tipo: {}, Datos: {}".format(tipo, datos))

        
        x, y, w, h = codigo.rect
        cv2.rectangle(imagen, (x, y), (x + w, y + h), (0, 255, 0), 2)

    
    cv2.imshow("Reconocimiento de códigos", imagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ruta_imagen = "ruta/de/la/imagen.png"

reconocer_codigos(ruta_imagen)
