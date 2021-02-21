import numpy as np
import cv2
from tensorflow.keras.models import load_model
import time
import requests
import key

model = load_model('garbage_recognition.h5')

def fetch_data(address):
    import pandas as pd
    from firebase import firebase
    try:
        firebase = firebase.FirebaseApplication('https://sweeper-73435.firebaseio.com', None)
        result = firebase.get('/user', None)
        data = pd.DataFrame(result.values())
        data = list(data[(data['address'] == address)]['phoneNo'])
    except Exception as e:
        print(e)
    return data

def update_task(PhoneNo, task):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://sweeper-73435.firebaseio.com', None)
    for i in PhoneNo:
        firebase.put('/user/'+i, "task", task)

def send_message(PhoneNo, task):
    numbers = ','.join(list(map(str, PhoneNo)))
    url = "https://www.fast2sms.com/dev/bulk"
    params = {"authorization": key.key(),
                   "sender_id": "FSTSMS",
                   "message": task,
                   "language": "english",
                   "route": "p",
                   "numbers": numbers}

    headers = {
        'cache-control': "no-cache"
    }
    try:
        response = requests.request("GET", url, headers=headers, params=params)
        dict = response.json()
        print(dict)
    except:
        print("Not send. please try again")

def alert(pred, img, location="Hakak Tola"):
    if pred == 0:
        pass
    elif pred == 1:
        print("Gabage is there")
        #cv2.imwrite("img.jpg", img)

        phoneNo = fetch_data(location)
        task = "You will sweep at  the location " +location +". Garbage Frequency: 80%"

        # update_task(phoneNo, task)
        # send_message(phoneNo, task)

        # for i in range(2):
        #    time.sleep(3600)

def prediction(img):
    img = cv2.resize(img, (50, 50))
    pred = model.predict(np.array([img]))
    pred = np.where(pred > 0.6, 1, 0).flatten()
    alert(pred[0], img)

def camera(url=0):
    p_cam = cv2.VideoCapture(0)
    try:
        url = url
        p_cam.open(url)
    except:
        pass

    while True:
        _, p_img = p_cam.read()
        cv2.imshow('Camera', p_img)
        prediction(p_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    p_cam.release()

if __name__ == '__main__':
    camera()