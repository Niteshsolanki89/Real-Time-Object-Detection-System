import cv2
from ultralytics import YOLO
import pygame
import threading

# Load YOLOv8 : it is pre-trained model that identifyies the object that are saved in his data or module
model = YOLO("yolov8m.pt")  # lightweight model, you can swap for (yolov8s.pt) or (yolov8n.pt) if needed

# Initialize pygame for sound
pygame.mixer.init()
pygame.mixer.music.load("D:\\Projects\\Real-Time Object Detection System\\iphone_alarm.mp3")
# Alarm thread
def play_alarm():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()

# Webcam capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect objects
    results = model(frame)

    # Process detection results
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            class_name = model.names[cls_id]

            # Get bounding box coordinates
            xyxy = box.xyxy[0].cpu().numpy()
            x1, y1, x2, y2 = map(int, xyxy)

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, class_name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Check for alarm condition (example: 'person')
            if class_name == 'person':
                threading.Thread(target=play_alarm).start()

    cv2.imshow("YOLOv8 Real-Time Object Detection", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
