# Real-time Hand Landmark UDP Tracking

This project detects 21 hand landmarks from a webcam and sends the first detected hand's 63 coordinate values to a UDP receiver.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the virtual environment with:

```powershell
.venv\Scripts\activate
```

## Run

```bash
python main.py
```

The default receiver is `127.0.0.1:5052`. Override it when needed:

```bash
python main.py --host 127.0.0.1 --port 5052
```

Press `Q` or `Esc` to stop.
