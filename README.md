# Virtual Keyboard with Hand Tracking

![Project Demo](demo.gif) <!-- Add a demo gif if available -->

A virtual keyboard that can be controlled using hand gestures, powered by OpenCV and CVZone's hand tracking module.

## Features

- Real-time hand tracking for keyboard interaction
- Three visual states for keys:
  - Inactive (Dark Gray)
  - Active/Hover (Light Gray)
  - Clicked (Black)
- Text display area showing typed characters
- Adjustable sensitivity for key presses

## Requirements

- Python 3.6+
- OpenCV
- CVZone
- MediaPipe (dependency of CVZone)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sriraghavi-raja/Visual-KeyBoard-With-CVZone.git
```
2. Install dependencies:
```bash
pip install opencv-python cvzone mediapipe
```

3. Run the application:
```bash
python virtual_keyboard.py
```

## Usage

1. Position your hand in front of the camera
2. Hover over keys to highlight them (Light Gray)
3. Bring index and middle fingers close together (<20px distance) to "click" a key (Black)
4. Typed text will appear in the output box at the bottom

## Customization

- Adjust key press sensitivity by changing the threshold in line 79:
```python
if length < 20:  # Change this value (lower = more sensitive)
```

- Modify keyboard layout by editing the `keys` matrix in the code

- Change colors by editing the RGB values in the `draw()` function

## Known Issues

- May have false detections in complex backgrounds
- Requires good lighting conditions for optimal performance
- Limited to QWERTY layout in current version

## Future Improvements

- Add backspace/space functionality
- Implement different keyboard layouts
- Add visual feedback for key presses
- Improve hand tracking accuracy

## Credits

Developed using:
- OpenCV
- CVZone Hand Tracking Module
- MediaPipe

---
