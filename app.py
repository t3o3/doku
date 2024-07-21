#import streamlit as st
#import pandas as pd
#import requests
#from PIL import Image
#
#
## メインパネル
#st.title('毒キノコ Classifier')
#st.image("ヘッダー.jpg", use_column_width=True)
#st.write('### 手にしているキノコについて質問に答えて下さい。')
#
## 選択ボックスを作成
#odors = [0, 1, 2, 3, 4, 5, 6, 7, 8] 
#selected_odors = st.selectbox('キノコはどんな臭いは？', odors)
#st.write('【0: アーモンド】 ', '【1: クレオソート】', '【2: ファウル】', '【3: アニス】', '【4: ミューズイ】', '【5: なし】  \n【6: 辛味】', '【7: スパーシー】', '【8: フィッシュ】')
#
#gill_size = [0, 1]
#selected_gillsize = st.selectbox('ひだの大きさは？', gill_size)
#st.write('【0: 広い】 ', '【1: 狭い】')
#
#gill_color = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#selected_gillcolor = st.selectbox('ひだの色は？', gill_color)
#st.write('【0: バフ】 ', '【1: レッド】', '【2: グレー】', '【3: チョコレート】', '【4: ブラック】', '【5: ブラウン】  \n【6: オレンジ】', '【7: ピンク】', '【8: グリーン】', '【9: パープル】', '【10: ホワイト】', '【11: イエロー】')
#
#stalk_surface_above_ring = [0, 1, 2, 3]
#selected_stalk_surface_above_ring = st.selectbox('柄の表面下のリングの質感は？', stalk_surface_above_ring)
#st.write('【0: 繊維状】 ', '【1: 絹毛】', '【2: 滑らか】', '【3: 鱗片状】')
#
#spore_print_color = [0, 1, 2, 3, 4, 5, 6, 7, 8]
#selected_spore_print_color = st.selectbox('胞子の色は？', spore_print_color)
#st.write('【0: バフ】 ', '【1: チョコレート】', '【2: ブラック】', '【3: ブラウン】  \n【4: オレンジ】', '【5: グリーン】', '【6: パープル】', '【7: ホワイト】', '【8: イエロー】')
#
#population = [0, 1, 2, 3, 4]
#selected_population = st.selectbox('どんなはえ方？', population)
#st.write('【0: 大多数で】 ', '【1: 群れをなして】', '【2: 多数で】', '【3: 分散して】', '【4: 数個で】')
#
## インプットデータ（1行のデータフレーム）
#value_df = pd.DataFrame([],columns=['data','臭い','ひだの大きさ','ひだの色','リングの質感','胞子の色','はえ方'])
## 新しい行のデータを作成
#record = pd.Series(['data', selected_odors, selected_gillsize, selected_gillcolor, selected_stalk_surface_above_ring, selected_spore_print_color, selected_population], index=value_df.columns)
#value_df = pd.concat([value_df, record.to_frame().T], ignore_index=True)
#value_df.set_index('data',inplace=True)
#
## 入力値の値
#st.write('### あなたの解答')
#st.write(value_df)
#
## Pandas Series を辞書に変換
## record_dict = record.drop('data').to_dict()
#
#doku = {
#    "odors": selected_odors,
#    "gill_size": selected_gillsize,
#    "gill_color": selected_gillcolor,
#    "stalk_surface_above_ring": selected_stalk_surface_above_ring,
#    "spore_print_color": selected_spore_print_color,
#    "population": selected_population
#}
#
#
#
#
#if st.button("予測開始"):
#
#    # 予測の実行
#    response = requests.post("https://doku-main.onrender.com/predict", json=doku)
#    prediction = response.json()["prediction"]
#
#    # 予測結果の表示
#
#    st.write('## 毒判定')
#
#    targets = ['毒', '毒じゃない']
#    st.write('# たぶん',str(targets[int(prediction)]),'deathよ!')
#
#    # 予測が0の場合
#    if prediction == "0":
#        st.image("_db16819f-2dbf-4ea0-97c0-4bf97c9b8737.jpg", caption="食べてみたら", use_column_width=True)
#    # 予測が1の場合
#    elif prediction == "1":
#        st.image("_6c5dcce1-b701-4e7f-9727-351e6ff5a21c.jpg", caption="食べないほうがいいけどね", use_column_width=True)
#
## まとめた文言
#summary_text = """
### 毒キノコ Classifierについて
#
#このアプリは毒キノコの判定を提供しますが、その結果は絶対的なものではありません。安全のためにも、専門家の意見や追加の調査を参考にし、判断を慎重に行ってください。判定結果に依存せず、不明瞭な場合は毒キノコを摂取しないようにしてください。
#
#このアプリは娯楽を目的としており、正確な医療助言ではありません。機械学習に基づいているため、全ての変数を考慮することは難しく、100％の正確性は保証できません。
##
#
#アプリに関するフィードバックや改善点についての情報は歓迎しています。お気軽にお知らせください。
#
#なお、画像はAIで作成されています。
#"""
#
## サイドバーにまとめた文言を表示
#st.sidebar.markdown(summary_text)
#
#

import streamlit as st
import pandas as pd
import requests
from PIL import Image

st.title('毒キノコ Classifier')
st.image("ヘッダー.jpg", use_column_width=True)
st.write('### 手にしているキノコについて質問に答えて下さい。')

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

value_df = pd.DataFrame([], columns=['data', '臭い', 'ひだの大きさ', 'ひだの色', 'リングの質感', '胞子の色', 'はえ方'])
record = pd.Series(['data', selected_odors, selected_gillsize, selected_gillcolor, selected_stalk_surface_above_ring, selected_spore_print_color, selected_population], index=value_df.columns)
value_df = pd.concat([value_df, record.to_frame().T], ignore_index=True)
value_df.set_index('data', inplace=True)

st.write('### あなたの解答')
st.write(value_df)

doku = {
    "odors": selected_odors,
    "gill_size": selected_gillsize,
    "gill_color": selected_gillcolor,
    "stalk_surface_above_ring": selected_stalk_surface_above_ring,
    "spore_print_color": selected_spore_print_color,
    "population": selected_population
}

if st.button("予測開始"):
    try:
        response = requests.post("https://doku-main.onrender.com/predict", json=doku)
        response.raise_for_status()
        st.write(response.text)  # レスポンスの内容を確認するために追加
        prediction = response.json()["prediction"]

        st.write('## 毒判定')
        targets = ['毒', '毒じゃない']
        st.write('# たぶん', str(targets[int(prediction)]), 'deathよ!')

        if prediction == "0":
            st.image("_db16819f-2dbf-4ea0-97c0-4bf97c9b8737.jpg", caption="食べてみたら", use_column_width=True)
        elif prediction == "1":
            st.image("_6c5dcce1-b701-4e7f-9727-351e6ff5a21c.jpg", caption="食べないほうがいいけどね", use_column_width=True)
    except requests.exceptions.RequestException as e:
        st.error(f"APIリクエストに失敗しました: {e}")
    except requests.exceptions.JSONDecodeError as e:
        st.error(f"APIレスポンスのJSONデコードに失敗しました: {e}")
        st.write(response.text)  # デコードに失敗したレスポンス内容を表示
