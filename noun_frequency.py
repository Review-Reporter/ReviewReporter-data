import csv

file_list = ['무신사 트레이드 시리즈 백팩 블랙.csv','무신사 칼하트 레거시 클래식 백팩 블랙.csv','무신사 칼하트 레거시 스탠다드 워크팩 블랙.csv','무신사 칼하트 레거시 스탠다드 워크백(블랙).csv','무신사 칼하트 레거시 디럭스 워크팩 블랙.csv']

from konlpy.tag import Okt
from collections import Counter

okt = Okt()

all_noun = []
for filename in file_list:
    f = open('C:/github/Review-Reporter/ReviewReporter-data/review_data' + filename, 'r', encoding='cp949')
    data = csv.reader(f, delimiter=',')
    for review in data:
        all_noun = all_noun + (okt.nouns(review[1]))
    f.close()

count = Counter(all_noun)

noun_list = count.most_common(len(count))
with open('noun_frequency.csv', 'w', newline='', encoding='UTF-8') as f:
    csvw = csv.writer(f)
    csvw.writerow(['명사','빈도수'])
    for v in noun_list:
        csvw.writerow(v)