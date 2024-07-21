#from fastapi import FastAPI
#from pydantic import BaseModel
#from sklearn.ensemble import RandomForestClassifier
#import pickle
#
## インスタンス化
#app = FastAPI()
#
## 入力するデータ型の定義
#class doku(BaseModel):
#    odors: int
#    gill_size: int
#    gill_color: int
#    stalk_surface_above_ring: int
#    spore_print_color: int
#    population: int
#
#import os
#
## 保存したディレクトリとファイル名
##save_directory = 'C:\\Users\\tomit\\code\\毒キノコアプリ3'
##model_filename = 'model_毒.pkl'
#
## モデルの読み込み
##model_path = os.path.join(save_directory, model_filename)
##model = pickle.load(open(model_path, 'rb'))
#
## 実行中のスクリプトのディレクトリを取得
#current_directory = os.path.dirname(os.path.realpath(__file__))
#
## 保存したディレクトリとファイル名
#save_directory = os.path.join(current_directory)
#model_filename = 'model_毒.pkl'
#
## モデルの読み込み
#model_path = os.path.join(save_directory, model_filename)
#print("Model Path:", model_path)
#model = pickle.load(open(model_path, 'rb'))
#
## トップページ
#@app.get('/')
#def index():
#    return {"毒キノコ": 'doku_prediction'}

## POST が送信された時（入力）と予測値（出力）の定義
#@app.post('/predict')
#def make_predictions(features: doku):
#    return({'prediction':str(model.predict([[features.odors, features.gill_size, features.gill_color, features.stalk_surface_above_ring, features.spore_print_color, features.population]])[0])})

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import logging

app = FastAPI()

# CORS設定
from fastapi.middleware.cors import CORSMiddleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 入力するデータ型の定義
class Doku(BaseModel):
    odors: int
    gill_size: int
    gill_color: int
    stalk_surface_above_ring: int
    spore_print_color: int
    population: int

# モデルの読み込み
model_path = 'model_毒.pkl'
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    logger.info("モデルが正常にロードされました。")
else:
    model = None  # モデルが存在しない場合の処理
    logger.error("モデルがロードされませんでした。")

@app.get('/')
def index():
    return {"message": 'Welcome to the FastAPI application'}

@app.post('/predict')
def make_predictions(features: Doku):
    if not model:
        logger.error("モデルがロードされていません。")
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    try:
        prediction = model.predict([[features.odors, features.gill_size, features.gill_color, features.stalk_surface_above_ring, features.spore_print_color, features.population]])[0]
        logger.info(f"予測が正常に行われました。結果: {prediction}")
        return {'prediction': str(prediction)}
    except Exception as e:
        logger.error(f"予測中にエラーが発生しました: {e}")
        raise HTTPException(status_code=500, detail=str(e))
