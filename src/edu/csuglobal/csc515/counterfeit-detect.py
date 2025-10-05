import cv2, os

inp = "resources/input/banknote.jpg"
out = "resources/output"
os.makedirs(out, exist_ok=True)

img = cv2.imread(inp)
if img is None:
    raise FileNotFoundError(f"Cannot read {inp}")
h, w = img.shape[:2]

# 1) Scale to target width
target_w = 400
interp = cv2.INTER_LANCZOS4 if w < target_w else cv2.INTER_AREA
scaled = cv2.resize(img, (target_w, int(h * target_w / w)), interpolation=interp)

# 2) Rotate 90° clockwise
rotated = cv2.rotate(scaled, cv2.ROTATE_90_CLOCKWISE)

# 3) Crop from all sides (top, bottom, left, right)
crop_top    = 20
crop_bottom = 20
crop_left   = 0
crop_right  = 20
final = rotated[crop_top:rotated.shape[0]-crop_bottom,
        crop_left:rotated.shape[1]-crop_right]

# Save final image
cv2.imwrite(f"{out}/banknote_final.jpg", final)
print("Saved:", f"{out}/banknote_final.jpg")
