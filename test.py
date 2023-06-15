from .yolo_nas_imp import ObjectDetect, cv2

data = ObjectDetect()

player = data.start_video_cam()

while True:

    image = data.video_data(player)

    output, _ = data.predict(image)

    cv2.imshow("", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

data.stop_video(player)