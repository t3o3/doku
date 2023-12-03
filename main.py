from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
import pickle

# インスタンス化
app = FastAPI()

# 入力するデータ型の定義
class doku(BaseModel):
    odors: int
    gill_size: int
    gill_color: int
    stalk_surface_above_ring: int
    spore_print_color: int
    population: int

import os

# 保存したディレクトリとファイル名
save_directory = 'C:\\Users\\tomit\\code\\毒キノコアプリ3'
model_filename = 'model_毒.pkl'

# モデルの読み込み
model_path = os.path.join(save_directory, model_filename)
model = pickle.load(open(model_path, 'rb'))

# トップページ
@app.get('/')
def index():
    return {"毒キノコ": 'doku_prediction'}

# POST が送信された時（入力）と予測値（出力）の定義
@app.post('/predict')
def make_predictions(features: doku):
    return({'prediction':str(model.predict([[features.odors, features.gill_size, features.gill_color, features.stalk_surface_above_ring, features.spore_print_color, features.population]])[0])})

