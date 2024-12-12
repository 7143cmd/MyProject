import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\pytak\PycharmProjects\pythonProject\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Ошибка при подключении к камере")
    exit()

window_width, window_height = 640, 480

cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam", window_width, window_height)

x,y,w,h = 0,0,0,0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Ошибка при чтении кадра из камеры")
        break

    faces = face_cascade.detectMultiScale(frame,minNeighbors=5,minSize =(20,20))

    height, width, _ = frame.shape
    cv2.putText(frame, 'Test', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    face_center_x = int(x + w / 2)
    face_center_y = int(y + h / 2)
    cv2.circle(frame, (face_center_x, face_center_y), 2, (0, 0, 255), 2)

    cv2.imshow("Webcam", frame)

    if cv2.waitKey(1) == ord('1'):
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cap.release()
cv2.destroyAllWindows()


