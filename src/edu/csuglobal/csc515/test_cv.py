import cv2

# Relative paths
input_path = "resources/input/shutterstock93075775--250.jpg"
output_path = "resources/output/brain_copy.jpg"

image = cv2.imread(input_path)

if image is None:
    raise FileNotFoundError(f"Could not read the image at {input_path}")

cv2.imshow("Brain Image", image)

# Wait until a key is pressed while the window is focused
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(output_path, image)

print(f"Image saved successfully to: {output_path}")
