# Hand Gesture Controlled Screen Brightness

This Python project uses **OpenCV**, **MediaPipe**, and **Screen Brightness Control** to adjust your computer's screen brightness in real-time based on the distance between your thumb and index finger, detected via webcam.

## 🚀 Features
- Real-time hand tracking using **MediaPipe**.
- Detects the distance between thumb and index finger tips.
- Adjusts screen brightness proportionally to the distance.
- Displays current brightness level on screen.
- Works with any standard webcam.

## 🛠️ Technologies Used
- **Python 3.x**
- **OpenCV** (`cv2`)
- **MediaPipe**
- **NumPy**
- **screen-brightness-control**

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hand-gesture-brightness-control.git
   cd hand-gesture-brightness-control
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage
Run the Python script:
```bash
python hand_brightness_control.py
```

- Place your hand in front of the webcam.
- Move your thumb and index finger closer/farther to decrease/increase brightness.
- Press **`q`** to quit.

## 📷 How It Works
1. The webcam captures frames in real-time.
2. **MediaPipe** detects and tracks hand landmarks.
3. The Euclidean distance between thumb tip (landmark 4) and index finger tip (landmark 8) is calculated.
4. This distance is mapped to a brightness percentage (0–100%).
5. **screen-brightness-control** updates the system brightness accordingly.

## 🔮 Future Improvements
- Add gesture support for volume control.
- Multi-hand support for advanced gestures.
- GUI to toggle features.

## 📜 License
This project is licensed under the MIT License.
