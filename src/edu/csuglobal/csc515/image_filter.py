import cv2
import matplotlib.pyplot as plt

inp = "resources/input/night_image_noise.jpg"
img = cv2.imread(inp)
if img is None:
    raise FileNotFoundError(f"Cannot read {inp}")

med3 = cv2.medianBlur(img, 3)
med5 = cv2.medianBlur(img, 5)
med7 = cv2.medianBlur(img, 7)
med9 = cv2.medianBlur(img, 9)

gauss_then_med = cv2.medianBlur(cv2.GaussianBlur(img, (5,5), 1.0), 3)
med_then_gauss = cv2.GaussianBlur(cv2.medianBlur(img, 3), (5,5), 1.0)

plt.figure(figsize=(14,10))
plt.subplot(2,3,1); plt.title("Original (grainy)"); plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)); plt.axis("off")
plt.subplot(2,3,2); plt.title("Median k=3"); plt.imshow(cv2.cvtColor(med3, cv2.COLOR_BGR2RGB)); plt.axis("off")
plt.subplot(2,3,3); plt.title("Median k=5"); plt.imshow(cv2.cvtColor(med5, cv2.COLOR_BGR2RGB)); plt.axis("off")
plt.subplot(2,3,4); plt.title("Median k=7"); plt.imshow(cv2.cvtColor(med7, cv2.COLOR_BGR2RGB)); plt.axis("off")
plt.subplot(2,3,5); plt.title("Median k=9"); plt.imshow(cv2.cvtColor(med9, cv2.COLOR_BGR2RGB)); plt.axis("off")
plt.subplot(2,3,6); plt.title("Gaussian -> Median vs Median -> Gaussian")

hybrid_stack = cv2.hconcat([gauss_then_med, med_then_gauss])
plt.imshow(cv2.cvtColor(hybrid_stack, cv2.COLOR_BGR2RGB)); plt.axis("off")
plt.tight_layout(); plt.show()
