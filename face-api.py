import cv2
import numpy as np
from keras.preprocessing.image import img_to_array
from keras.models import load_model

from google.colab.patches import cv2_imshow

face_detection=cv2.CascadeClassifier ('/content/gdrive/My Drive/data/haarcascade_frontalface_default.xml')
emotion_classifier=load_model('/content/gdrive/My Drive/data/emotion_model.hdf5'), compile=False)
EMOTIONS= ["Angry", "Disgusting", "Fearful","Happy","Sad","Surprising","Neutral"]

#webcam활용한 안면이미지 취득
from IPython.display import Image
try:
   filename=take_photo()
   print('Saved to {}'.format(filename))

#webcam에서 저장된 이미지 표시
#display(Image(filename))
expect Expection as err:
print(str(err))

#cv2 이미지 로딩
frame=cv2.imread(filename, cv2.IMREAD_COLOR)

#grey color 변환
gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
