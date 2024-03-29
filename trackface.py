import face_recognition
import cv2

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encoding = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for(top, right, bottom, left) in face_locations:
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, "Unknown", (left -6, bottom +18), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()