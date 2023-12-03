import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# データセット読み込み
import pandas as pd
df = pd.read_table("C:\\Users\\tomit\\code\\毒キノコアプリ\\train.tsv")

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

# メインパネル
st.title('毒キノコ Classifier')
st.write('### 手にしているキノコについて質問に答えて下さい。')

# 選択ボックスを作成
odors = [0, 1, 2, 3, 4, 5, 6, 7, 8]
selected_odors = st.selectbox('キノコはどんな臭いは？', odors)
st.write('【0: アーモンド】 ', '【1: クレオソート】', '【2: ファウル】', '【3: アニス】', '【4: ミューズイ】', '【5: なし】  \n【6: 辛味】', '【7: スパーシー】', '【8: フィッシュ】')

gill_size = [0, 1]
selected_gillsize = st.selectbox('ひだの大きさは？', gill_size)
st.write('【0: 広い】 ', '【1: 狭い】')

gill_color = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
selected_gillcolor = st.selectbox('ひだの色は？', gill_color)
st.write('【0: バフ】 ', '【1: レッド】', '【2: グレー】', '【3: チョコレート】', '【4: ブラック】', '【5: ブラウン】  \n【6: オレンジ】', '【7: ピンク】', '【8: グリーン】', '【9: パープル】', '【10: ホワイト】', '【11: イエロー】')

stalk_surface_above_ring = [0, 1, 2, 3]
selected_stalk_surface_above_ring = st.selectbox('柄の表面下のリングの質感は？', stalk_surface_above_ring)
st.write('【0: 繊維状】 ', '【1: 絹毛】', '【2: 滑らか】', '【3: 鱗片状】')

spore_print_color = [0, 1, 2, 3, 4, 5, 6, 7, 8]
selected_spore_print_color = st.selectbox('胞子の色は？', spore_print_color)
st.write('【0: バフ】 ', '【1: チョコレート】', '【2: ブラック】', '【3: ブラウン】  \n【4: オレンジ】', '【5: グリーン】', '【6: パープル】', '【7: ホワイト】', '【8: イエロー】')

population = [0, 1, 2, 3, 4]
selected_population = st.selectbox('どんなはえ方？', population)
st.write('【0: 大多数で】 ', '【1: 群れをなして】', '【2: 多数で】', '【3: 分散して】', '【4: 数個で】')

# インプットデータ（1行のデータフレーム）
value_df = pd.DataFrame([],columns=['data','odor','gill-size','gill-color','stalk-surface-above-ring','spore-print-color','population'])
# 新しい行のデータを作成
record = pd.Series(['data', selected_odors, selected_gillsize, selected_gillcolor, selected_stalk_surface_above_ring, selected_spore_print_color, selected_population], index=value_df.columns)
value_df = pd.concat([value_df, record.to_frame().T], ignore_index=True)
value_df.set_index('data',inplace=True)

# 入力値の値
st.write('### あなたの解答')
st.write(value_df)

# カラム名の取得
columns_used = value_df.columns.tolist()

# 予測値のデータフレーム
pred_probs = model.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs,columns=['毒だよ','毒じゃないよ'],index=['probability'])

st.write('### 毒確率')
st.write(pred_df)

# 予測結果の出力
name = pred_df.idxmax(axis=1).tolist()
st.write('### 毒判定')
st.write('## 『そのキノコはきっと',str(name[0]),'。  』')

# まとめた文言
summary_text = """
## 毒キノコ Classifierについて

このアプリは毒キノコの判定を提供しますが、その結果は絶対的なものではありません。安全のためにも、専門家の意見や追加の調査を参考にし、判断を慎重に行ってください。判定結果に依存せず、不明瞭な場合は毒キノコを摂取しないようにしてください。

このアプリは娯楽を目的としており、正確な医療助言ではありません。機械学習に基づいているため、全ての変数を考慮することは難しく、100％の正確性は保証できません。疑問がある場合は、本アプリを専門家の意見や正確な情報源と併用し、自己判断を行ってください。


アプリに関するフィードバックや改善点についての情報は歓迎しています。お気軽にお知らせください。
"""

# サイドバーにまとめた文言を表示
st.sidebar.markdown(summary_text)
