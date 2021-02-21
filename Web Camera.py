import numpy as np
import cv2
from tensorflow.keras.models import load_model

model = load_model('garbage_recognition.h5')

def prediction(img):
    img = cv2.resize(img, (50, 50))
    pred = model.predict(np.array([img]))
    pred = np.where(pred > 0.6, 1, 0).flatten()
    return pred[0]

def camera():
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        cv2.imshow("video", img)
        pred = prediction(img)
        if pred == 1:
            print("Yes")
        else:
            pass
        if cv2.waitKey(1) == 'q' and 0xFF == 27:
           cv2.destroyAllWindows()


if __name__ == '__main__':
    camera()