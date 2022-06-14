import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
font_path = 'c:/Windows/Fonts/KoPubDotumMedium.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv("C:/Users/rvmin/Desktop/totebag/토트백_호보.csv", encoding='cp949')

fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot()

ax.plot(df['날짜'],df['개수'],color='red',linewidth=3)

ax.set_xlabel('날짜')
ax.set_ylabel('개수')

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('none')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('none')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(colors='white')
plt.xticks(rotation=45)
ax.xaxis.label.set_size(17)
ax.yaxis.label.set_size(17)
#plt.grid(True,axis='y')

#plt.show()
plt.savefig('토트백_판매량.png', transparent=True)
