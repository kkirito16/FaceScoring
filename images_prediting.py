# coding:utf8
import cv2
import sys
import numpy as np

from keras.models import load_model
import face_recognition as fr


class BeautyDetector():
    def __init__(self):
        self.model = load_model("face_rank_model.h5", compile=False)

    def draw(self, frame):
        locations = fr.face_locations(frame)
        for location in locations:
            x1, x2 = location[3], location[1]
            y1, y2 = location[0], location[2]
            face = cv2.resize(frame[y1:y2, x1:x2, :], (128, 128))
            point = (x1 + (x2-x1)//3, y1 - 10)

            # face landmark feature points
            face_encoding = np.array(fr.face_encodings(face))
            if len(face_encoding) == 1:
                score = self.model.predict(face_encoding)[0][0]
                score = int(score/5 * 100)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                cv2.putText(frame, str(score), point,
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        return frame


def main():
    detector = BeautyDetector()

    # 加载图像文件
    image = cv2.imread("face.png")

    # 进行人脸检测和美丑评分
    frame = detector.draw(image)

    # 显示结果
    cv2.imshow("Beauty Detector", frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()