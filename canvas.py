from tkinter import*
import sys

def angle(n):
    x = n/allmoney/3600
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

Label(screen1, text = "PIE", anchor ="n",width = 20, height = 1,).pack()

canvas = Canvas(screen1, width= 400, height= 400)
canvas.pack()

eat = canvas.create_arc((5, 5, 150, 150), fill = "red", outline ="red",start = (0), extent = angle(eatm))
clothing = canvas.create_arc((5, 5, 150, 150), fill = "yellow", outline ="yellow",start = (eatm), extent = angle(clothingm))
housing = canvas.create_arc((5, 5, 150, 150), fill = "blue", outline ="blue",start = (eatm+clothing), extent = angle(housingm))
entertainment = canvas.create_arc((5, 5, 150, 150), fill = "grey", outline ="gray",start = (eatm+clothing+housingm), extent = angle(entertainmentm))
transportation = canvas.create_arc((5, 5, 150, 150), fill = "green", outline ="green",start = (eatm+clothing+housingm+entertainmentm), extent = angle(transportationm))



screen1.mainloop()