import cv2
from super_gradients.common.object_names import Models
from super_gradients.training import models


class ObjectDetect:
    def __init__(self, model = Models.YOLO_NAS_L, weight = 'coco') -> None:
        self.model = models.get(model, pretrained_weights=weight)

    def start_video_cam(self):
        video = cv2.VideoCapture(0)
        return video
    
    def video_data(self, player):
        _, frame = player.read()
        return frame
    
    def stop_video(self, player):
        player.release()
        cv2.destroyAllWindows()

    def predict(self, image):
        pre_ = self.model.predict(image)
        data = pre_._images_prediction_lst

        arr = []
        for i in data:
            arr.append(i)
        return arr[0].draw(), arr[0]



# for example
if __name__ == '__main__':
        
    data = ObjectDetect()

    player = data.start_video_cam()

    while True:

        image = data.video_data(player)

        output, _ = data.predict(image)

        cv2.imshow("", output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    data.stop_video(player)


