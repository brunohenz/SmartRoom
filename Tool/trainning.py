import cv2
import os
import numpy as np

eigenface = cv2.face.createEigenFaceRecognizer()
fisherface = cv2.face.createFisherFaceRecognizer()
lbph = cv2.face.createLBPHFaceRecognizer()

def getImagemComID():
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]    
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

eigenface.train(faces, ids)
eigenface.save('classificateEigen.yml')

# fisherface.train(faces, ids)
# fisherface.save('classificateFisher.yml')

# lbph.train(faces, ids)
# lbph.save('classificateLBPH.yml')

print("Treinamento Realizado!")