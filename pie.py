import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def angel(percent, allvalues):
    absolute = int((percent) / 100.*np.sum(allvalues)+0.5)
    return "{:.2f}%\n({:d})".format(percent, absolute)

if __name__ == "__main__":
    if len(sys.argv) > 0: 
        while True:
            allmoney = int(input("請輸入總金額"":"))
            balance = 0
            print("按照食衣住樂行輸入金額"":")
            for i in range(5):
                if i == 0:
                    print("請輸入食的金額"":")
                    eatm = int(input())
                elif i == 1:
                    print("請輸入衣的金額"":")
                    clothingm = int(input())
                elif i == 2:
                    print("請輸入住的金額"":")
                    housingm = int(input())
                elif i == 3:
                    print("請輸入樂的金額"":")
                    entertainmentm = int(input())
                elif i == 4:
                    print("請輸入行的金額"":")
                    transportationm = int(input())
            balance = (allmoney - eatm -clothingm -housingm - entertainmentm - transportationm)
            break


x = ["eat", "clothing", "housing", "entertainment", "transportation","balance"]
y = [eatm, clothingm, housingm, entertainmentm, transportationm, balance]
colors = ( "#70C1CF", "#FF9900", "#FF4D40", "#006400", "#FFF345", "#75542B")
explode = (0,0,0,0,0,.1)#炸開
expenditure = [eatm, clothingm, housingm, entertainmentm, transportationm, balance]#支出內容

fig, ax = plt.subplots(figsize = (10, 7))

ax.set_title("Expenditure of Month")
ax.pie(y, labels= x,autopct = lambda percent:angel(percent, expenditure), startangle = 90, colors = colors,shadow = True,explode = explode)
plt.show()



