# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# Loads the image into memory
with open('./image.jpg', 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('-----RESULT-----')
for label in labels:
    print(label.description, ': ', label.score)
print('-----RESULT-----')