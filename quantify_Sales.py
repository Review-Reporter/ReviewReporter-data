import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:/Users/82109/Desktop/꽉잡아 캡스톤/백팩 통합 리뷰2.csv'
df = pd.read_csv(filename, encoding='euc-kr')
df.columns = ['date', 'review']
df['datetime'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y.%m.%d'))
df['all_review_num'] = 1
df.set_index(df['datetime'], inplace=True)
df = df.drop('datetime', 1)
weekly_df = df.resample('W-Mon', how={'all_review_num'}).fillna(0)
df.head()

#plt.rc('font', family = 'Malgun Gothic')
#filename = 'C:/Users/82109/Desktop/꽉잡아 캡스톤/백팩 통합 리뷰.csv'
#data = pd.read_csv(filename, encoding = 'euc-kr', index_col='날짜')
#data.columns