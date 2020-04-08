import cv2
import os
import numpy as np

lbph = cv2.face.createLBPHFaceRecognizer()

def getImagemComID():
    caminhos = [os.path.join('pics', f) for f in os.listdir('pics')]    
    faces = []
    ids = []
    for caminhoImage in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImage), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImage) [-1].split('.')[1])        
        ids.append(id)
        faces.append(imagemFace)
    return np.array(ids), faces

ids, faces = getImagemComID()

print("Treinando...")

lbph.train(faces, ids)
lbph.save('files/classificate.yml')
print("Treinamento Realizado!")