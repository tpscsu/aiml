import cv2
import matplotlib.pyplot as plt

# Load the image from resources/input
img = cv2.imread("resources/input/puppy.jpg")   # OpenCV loads in BGR order

# Split into channels
b, g, r = cv2.split(img)

# Show each channel as grayscale
plt.subplot(1, 3, 1); plt.imshow(r, cmap="gray"); plt.title("Red"); plt.axis("off")
plt.subplot(1, 3, 2); plt.imshow(g, cmap="gray"); plt.title("Green"); plt.axis("off")
plt.subplot(1, 3, 3); plt.imshow(b, cmap="gray"); plt.title("Blue"); plt.axis("off")
plt.show()

# Merge back (original)
merged = cv2.merge([b, g, r])
plt.imshow(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB))
plt.title("Original Reconstructed")
plt.axis("off")
plt.show()

# Swap red and green (GRB)
swapped = cv2.merge([b, r, g])
plt.imshow(cv2.cvtColor(swapped, cv2.COLOR_BGR2RGB))
plt.title("Red and Green Swapped")
plt.axis("off")
plt.show()
