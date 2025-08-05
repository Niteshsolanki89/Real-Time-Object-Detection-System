
# 🎯 Real-Time Object Detection System (YOLOv8 + OpenCV)

This project is a **real-time object detection system** using the **YOLOv8 model**, **OpenCV**, and **Python**. It captures webcam feed, detects objects live, and draws bounding boxes with labels. It also plays an **alarm sound** when detecting specific objects (like people).

---

## 🚀 Features

- 🎥 Real-time object detection using webcam feed
- 🤖 YOLOv8 (Ultralytics) for robust, fast object detection
- 🧠 Detects 80+ common objects from the COCO dataset
- 🔊 Plays an alarm sound if a "person" is detected
- ⚙️ Modular and easy to customize for new object categories

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|--------|
| Python     | Programming language |
| OpenCV     | Webcam and frame processing |
| YOLOv8     | Object detection model (via `ultralytics`) |
| pygame     | Audio alarm playback |
| threading  | Async alarm control |

---

## 📁 File Structure

```
📦 Real-Time Object Detection System
 ┣ 📜 Real-Time Object Detecting System.py
 ┣ 🔊 iphone_alarm.mp3
```

---

## ⚙️ How to Run

1. Make sure you have Python installed.
2. Install dependencies:
```bash
pip install ultralytics opencv-python pygame
```
3. Replace the alarm file path in the script with your own local path or place the `.mp3` in the project directory and use:
```python
pygame.mixer.music.load("iphone_alarm.mp3")
```
4. Run the script:
```bash
python "Real-Time Object Detecting System.py"
```

---

## 📸 Output Demo

- Bounding boxes drawn live around objects in webcam feed.
- Label text (like `person`, `bottle`, etc.) appears above each box.
- Alarm sounds when a "person" is detected.

---

## 📌 Use Cases

- 🔐 Security and surveillance cameras
- 🧠 AI-assisted monitoring systems
- 🚗 Smart vehicles & driver assistance
- 🤖 Robotics and automation

---

## ✅ Future Improvements

- 🔍 Add support for custom-trained YOLO models (e.g., gun, knife detection)
- 📧 Trigger SMS/email alerts on detection
- 💻 Add Streamlit or GUI interface for settings
- 📊 Save detection logs (CSV or database)

---

## 🧠 Credits

Developed by **Nitesh Solanki**  
Pre-trained YOLO models provided by **Ultralytics**

---

## 🔗 License

MIT License — free for personal and educational use.
