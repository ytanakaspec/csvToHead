import pandas as pd
import csv
import itertools

# ファイル名を設定する
file_name = 'sampleHead'

df = pd.read_excel(f'./{file_name}.xlsx', header=None, index_col=None)

df_arr = df.values.tolist()
df_arr = list(itertools.chain.from_iterable(df_arr))

#print(df_arr)

head_list = list(map(lambda x: str(df_arr.index(x)) + ": { text: '" + x + "' }", df_arr))

print("******************************************")
print(head_list)