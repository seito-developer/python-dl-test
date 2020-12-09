#visionをインポート
from google.cloud import vision

#image.jpgを開いて読み込む
with open('./image.jpg', 'rb') as image_file:
	content = image_file.read()

#vision APIが扱える画像データにする
image = vision.Image(content=content)

#ImageAnnotatorClientのインスタンスを生成
annotator_client = vision.ImageAnnotatorClient()

response_data = annotator_client.label_detection(image=image)
labels = response_data.label_annotations

print('----RESULT----')
for label in labels:
	print(label.description, ':', round(label.score * 100, 2), '%')
print('----RESULT----')