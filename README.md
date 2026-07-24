# My Portfolio

Computer vision and interactive application projects built with Python, OpenCV, Unity, and C#.

## Featured Projects

### 1. Real-time Hand Landmark UDP Tracking

Webcam frames are processed in real time to detect 21 hand landmarks. The landmark coordinates are serialized and sent over UDP so another application, such as Unity, can consume the motion data.

- Python, OpenCV, cvzone, MediaPipe
- Real-time webcam hand detection
- 21-point landmark coordinate extraction
- UDP communication with configurable host and port

[View project](projects/hand-tracking-udp)

### 2. Unity Roll-a-Ball Game

A Unity physics game featuring player movement, jumping, collectible items, score and win UI, camera tracking, collision feedback, and random item spawning.

- Unity 2020.3.29f1, C#
- Rigidbody-based movement and collision handling
- Pickup, score, and victory systems
- Coroutine-based random respawning

[View project](projects/unity-roll-a-ball)

## Repository Structure

```text
projects/
├── hand-tracking-udp/
└── unity-roll-a-ball/
```

Each project directory contains its own setup and execution information.
