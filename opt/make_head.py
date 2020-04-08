import pandas as pd
import csv

# ファイル名を設定する
file_name = 'ｻﾝﾌﾟﾙﾃﾞｰﾀ'

df = pd.read_excel(f'./{file_name}.xlsx')

df_arr = df.values.tolist()

print(df_arr)