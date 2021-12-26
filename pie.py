import sys
import matplotlib.pyplot as plt

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


expenditure = [eatm, clothingm, housingm, entertainmentm, transportationm, balance]#支出內容
x = ["eat", "clothing", "housing", "entertainment", "transportation","balance"]
y = [eatm, clothingm, housingm, entertainmentm, transportationm, balance]
colors = ( "#70C1CF", "#FF9900", "#FF4D40", "#006400", "#FFF345", "#75542B")
explode = (0,0,0,0,0,.1)#炸開
plt.pie(y, labels= x,autopct = "%2.2f%%", colors = colors,shadow = True,explode = explode)
plt.show()

#ax.legend(expenditure, title ="expenditure", loc ="center left", bbox_to_anchor =(1, 0, 0.5, 1))


#import pandas as pd
#from tkinter import*
#screen1 = Tk()
#screen1.geometry
#screen1.title("PIE")
#screen1.config(bg = "white")
#Label(screen1, text = "PIE", anchor ="n",width = 20, height = 1,).pack()
#screen1.mainloop()