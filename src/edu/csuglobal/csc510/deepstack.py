import requests

image_data = open("/Users/tigin/Downloads/reo.png", "rb").read()

response = requests.post(
    "http://localhost:5050/v1/vision/detection",
    files={"image": image_data}
)

print(response.json())
