import cv2,time


cap = cv2.VideoCapture(0)

#harcascade classfier---> detect features of face
face_cascade = cv2.CascadeClassifier('C:\ProgramData\Anaconda3\envs\psosmsenv\lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\ProgramData\Anaconda3\envs\psosmsenv\lib\site-packages\cv2\data\haarcascade_eye.xml')

time.sleep(3)

id = input('enter user id: ')

sampleN=0;

while 1:

    ret, img = cap.read()
    print(img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #faces=gray

    for (x,y,w,h) in faces:

        sampleN=sampleN+1;

        cv2.imwrite("C:/Users/Radhika/Desktop/face"+str(id)+ "." +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
        cv2.putText(, str(a),(50,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,255,0), 2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        #C:\Users\Radhika\Desktop\acm\Radhika\face
        cv2.waitKey(100)

        cv2.imshow('img',img)

        cv2.waitKey(1)

        if sampleN > 20:

            break

cap.release()

cv2.destroyAllWindows()