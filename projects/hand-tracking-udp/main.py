"""Detect hand landmarks from a webcam and stream them over UDP."""

import argparse
import socket

import cv2
from cvzone.HandTrackingModule import HandDetector


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Stream 21 hand-landmark coordinates over UDP."
    )
    parser.add_argument("--host", default="127.0.0.1", help="UDP receiver host")
    parser.add_argument("--port", default=5052, type=int, help="UDP receiver port")
    parser.add_argument("--camera", default=0, type=int, help="Webcam device index")
    parser.add_argument("--width", default=1280, type=int, help="Capture width")
    parser.add_argument("--height", default=720, type=int, help="Capture height")
    parser.add_argument("--max-hands", default=2, type=int, help="Hands to detect")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    capture = cv2.VideoCapture(args.camera)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)

    if not capture.isOpened():
        raise RuntimeError(f"Unable to open camera device {args.camera}.")

    detector = HandDetector(detectionCon=0.8, maxHands=args.max_hands)
    receiver = (args.host, args.port)

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
        try:
            while True:
                success, frame = capture.read()
                if not success:
                    raise RuntimeError("Unable to read a frame from the camera.")

                hands, annotated_frame = detector.findHands(frame, draw=True)

                if hands:
                    frame_height = frame.shape[0]
                    landmarks = []
                    for x, y, z in hands[0]["lmList"]:
                        landmarks.extend((x, frame_height - y, z))

                    udp_socket.sendto(str(landmarks).encode("utf-8"), receiver)

                cv2.imshow("Hand Landmark Tracking", annotated_frame)
                key = cv2.waitKey(1) & 0xFF
                if key in (27, ord("q")):
                    break
        finally:
            capture.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
