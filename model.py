import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# データセット読み込み
import pandas as pd
df = pd.read_table("C:\\Users\\tomit\\code\\毒キノコアプリ2\\train.tsv")

#　いらない特定のカラムを削除
df = df.drop(['id','cap-shape','cap-surface','cap-color','gill-attachment','stalk-shape','stalk-surface-below-ring','stalk-color-above-ring','stalk-color-below-ring','veil-type','veil-color','ring-number','habitat','gill-spacing','stalk-root','ring-type','bruises'], axis=1)

# 前処理用の関数を定義
def preprocessing(df):
    # カテゴリデータのみ抽出
    df_obj = df.select_dtypes(include='object')

    for col in df_obj.columns:
        # ラベルエンコーディング
        le = LabelEncoder()
        le.fit(df[col])
        # 元のデータフレームの列を更新
        df[col] = le.transform(df[col])
    return df

# 前処理の実行
df = preprocessing(df)

# 目的変数
t = df['Y']
# 入力変数
x =df.drop('Y', axis=1)

# 目標値を数字から毒のありなしに変更
df.loc[df['Y'] == 0, 'p'] = '毒だよ'
df.loc[df['Y'] == 1, 'e'] = '毒じゃないよ'

# ランダムフォレスト
model = RandomForestClassifier(n_estimators=30, max_depth=20)
model.fit(x, t)

# モデルの保存
import pickle
model_filename = 'model_毒.pkl'
model_path = model_filename
with open(model_path, 'wb') as file:
    pickle.dump(model, file)
