import cv2
import os
import sys
from datetime import datetime

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def load_image(src_path=None):
    """
    If src_path is provided, load that image.
    Otherwise, capture a single frame from the default webcam.
    """
    if src_path:
        img = cv2.imread(src_path)
        if img is None:
            raise FileNotFoundError(f"Could not read image at: {src_path}")
        return img

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam. Pass an image path as an argument instead.")

    # give the camera a moment to adjust exposure
    for _ in range(10):
        _ = cap.read()

    ret, frame = cap.read()
    cap.release()
    if not ret:
        raise RuntimeError("Failed to capture image from webcam.")
    return frame

def main():
    # I/O paths
    in_dir = "resources/input"
    out_dir = "resources/output"
    ensure_dir(in_dir)
    ensure_dir(out_dir)

    src_path = sys.argv[1] if len(sys.argv) > 1 else None

    img = load_image(src_path)
    img_out = img.copy()

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

    if face_cascade.empty() or eye_cascade.empty():
        raise RuntimeError("Failed to load Haar cascades.")

    # Detect face
    gray = cv2.cvtColor(img_out, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(120, 120))

    if len(faces) == 0:
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=4, minSize=(80, 80))

    for (x, y, w, h) in faces[:1]:
        # Draw a GREEN CIRCLE around the face
        center = (x + w // 2, y + int(h * 0.46))
        radius = int(0.55 * max(w, h))
        cv2.circle(img_out, center, radius, (0, 255, 0), thickness=3)

        face_roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(20, 20))

        eyes = sorted(eyes, key=lambda e: e[0])[:2]
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img_out, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 0, 255), thickness=2)

        break

    label = "this is me"
    if len(faces) > 0:
        tx, ty, tw, th = faces[0]
        text_org = (tx, max(30, ty - 10))
    else:
        text_org = (20, 40)

    cv2.putText(
        img_out,
        label,
        text_org,
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255, 255, 255),
        thickness=2,
        lineType=cv2.LINE_AA
    )

    # Save output
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(out_dir, f"this_is_me_{timestamp}.jpg")
    cv2.imwrite(out_path, img_out)
    print(f"Saved result to: {out_path}")


    try:
        cv2.imshow("Result - this is me", img_out)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception:
        pass

if __name__ == "__main__":
    main()
