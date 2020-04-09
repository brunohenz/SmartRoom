import cv2
from services import *
from kivy.app import App
from confirmCustomer import *

class RecognizerFace:
    def startRecognizer(self):
        detectorFace = cv2.CascadeClassifier("files/haarcascade_frontalface_default.xml")
        reconhecedor = cv2.face.createLBPHFaceRecognizer()
        reconhecedor.load("files/classificate.yml")
        largura, altura = 220,220
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        camera = cv2.VideoCapture(0)

        while(True):
            conectado, imagem = camera.read()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = detectorFace.detectMultiScale(imagemCinza,
                                                            scaleFactor=1.5,
                                                            minSize=(150, 150))

            for(x, y, l, a) in facesDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + 1], (largura, altura))
                cv2.rectangle(imagem, (x, y),  (x + l, y + a), (0,0,255), 2)
                id, confianca = reconhecedor.predict(imagemFace)
                cv2.putText(imagem, str(id), (x,y + (a + 30)), font, 2, (0,0,255))

            cv2.imshow("Face", imagem)
            if cv2.waitKey(1) == ord('q'):                
                service = Services()
                customer = service.getUserIdentify(id)
                self.confirmCustomer(customer)
                break

        camera.release()
        cv2.destroyAllWindows()

    def confirmCustomer(self, customer):        
        confirm = ConfirmPopup(customer)
        confirm.open()

