import face_recognition as fr
import cv2
import numpy as np
import os


def my_face_recognition(train_path, test_image):
    # path = r"C:\Users\Nechama\Downloads\face-recognition-python-code\train"

    known_names = []
    known_name_encodings = []
    images = os.listdir(train_path)
    for _ in images:
        image = fr.load_image_file(train_path + "\\" + _)
        image_path = train_path + "\\" + _
        encoding = fr.face_encodings(image)[0]

        known_name_encodings.append(encoding)
        known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())

    print(known_names)
    # test_image = r"C:\Users\Nechama\Downloads\face-recognition-python-code\test\test.jpg"
    image = cv2.imread(test_image)
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # cv2.imshow("aaa",image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    face_locations = fr.face_locations(image)
    face_encodings = fr.face_encodings(image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = fr.compare_faces(known_name_encodings, face_encoding)
        name = ""

        face_distances = fr.face_distance(known_name_encodings, face_encoding)
        best_match = np.argmin(face_distances)

        if matches[best_match]:
            name = known_names[best_match]
    return name