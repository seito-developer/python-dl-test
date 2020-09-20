#各種インポート
import io 
import os
from google.protobuf.json_format import MessageToJson
import json
from google.cloud import vision
from google.cloud.vision import types

#今回の作業用ディレクトリ
# base_dir = r'path\to\directory'
base_dir = './'

#さっきのJSONファイルのファイル名
# credential_path = base_dir + r'test-7d10963ea8c8.json'
credential_path = base_dir + 'test-ai-415bb71333ef.json'

#サービスアカウントキーへのパスを通す
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

#visionクライアントの初期化
client = vision.ImageAnnotatorClient()

#対象となる画像のファイル名
# file_name = base_dir + r"\image.jpg"
file_name = base_dir + 'image.jpg'

#画像を読み込み
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
image = types.Image(content=content)

#実際に扱うメソッド名はここを参照
#https://googleapis.dev/python/vision/latest/gapic/v1p4beta1/api.html

#たとえば、ラベル検出の場合
response = client.label_detection(image=image)

#結果を表示
print(response)