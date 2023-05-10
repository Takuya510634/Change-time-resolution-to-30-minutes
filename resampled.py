import pandas as pd
import numpy as np

# CSVファイルを読み込み
df = pd.read_csv('input.csv')

#空列定義用数列
odd_numbers = [num for num in range(1, 1440, 2)]
#日付変更時の処理用数列
nums = [num_ for num_ in range(1, 1440, 48)]

df_T = df.T    #転置
list_a = (odd_numbers)  #空の列挿入(毎時30分用)
for i in list_a:  
    df_T.insert(i, i + 0.5, np.nan)
df_ = df_T.T    #転置

#index整理・線形補間
df_ = df_.reset_index(drop=True)
df_ = df_.interpolate()

#値修正(0:30用)
list_b = (nums)
for j in list_b:
    #df.at[j, 'year'] = df.at[j-1, 'year']
    df_.at[j, 'month'] = df_.at[j+1, 'month']
    df_.at[j, 'day'] = df_.at[j+1, 'day']
    df_.at[j, 'hour'] = 0.5

#int化
df_['year'] = df_['year'].astype('int')
df_['month'] = df_['month'].astype('int')
df_['day'] = df_['day'].astype('int')

# 結果をCSVファイルに保存
df_.to_csv('resampled_output.csv')
