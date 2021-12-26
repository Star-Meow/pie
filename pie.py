from tkinter import*
import sys
import matplotlib.pyplot as plt
#import pandas as pd


def angle(n):
    x = n/allmoney*360
    print(x)
    return (x)

if __name__ == "__main__":
    if len(sys.argv) > 0: 
        while True:
            allmoney = int(input("請輸入總金額"":"))

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
            break

screen1 = Tk()
screen1.geometry
screen1.title("PIE")
screen1.config(bg = "white")
#Label(screen1, text = "PIE", anchor ="n",width = 20, height = 1,).pack()
x = ["食", "衣", "住", "樂", "行"]
y = [eatm, clothingm, housingm, entertainmentm, transportationm]
plt.pie(y, labels= x,autopct = "%2.2f%%", )
plt.show()





screen1.mainloop()