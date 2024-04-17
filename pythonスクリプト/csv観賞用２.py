import matplotlib.pyplot as plt
import csv
import math
import os 
from matplotlib.ticker import MaxNLocator
import japanize_matplotlib
os.chdir("/Users/taniguchirei/Desktop/人間情報工学実験結果")
f = open("avg_einaga.csv","r",encoding="shift-jis")
reader1 = csv.reader(f)
word_list_1 = [row for row in reader1]
new_list = []

g = open("avg_yano.csv","r",encoding="shift-jis")
reader2 = csv.reader(g)
word_list_2 = [row for row in reader2]

x=[0,1,2,3,4,5,6,7]
y1 =[float(a[1])for a in word_list_1]
y2 =[float(a[1])for a in word_list_2]

fig,ax = plt.subplots()
ax.plot(x,y1,marker='o',color='orange',label="永長")
ax.plot(x,y2,marker='o',color='blue',label="矢野")
ax.legend(fontsize=12) #これで凡例が表示されるらしい
ax.set_xlabel("Difficulty (ID)")
ax.set_ylabel("Time (s)")
fig.suptitle("平均時間")

plt.show()