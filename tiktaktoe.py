import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("Krestiki Noliki")

playera = tk.StringVar()
playerb = tk.StringVar()
p1 = tk.StringVar()
p2 = tk.StringVar()


player1_name = tk.Entry(window, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = tk.Entry(window, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)


bclick = True
flag = 0


def disableButton():
    button1.configure(state="disabled")
    button2.configure(state="disabled")
    button3.configure(state="disabled")
    button4.configure(state="disabled")
    button5.configure(state="disabled")
    button6.configure(state="disabled")
    button7.configure(state="disabled")
    button8.configure(state="disabled")
    button9.configure(state="disabled")


def btnclick(buttons):
    global bclick, flag, player1_name, player2_name, playerb, playera

    if buttons["text"] == " " and bclick==True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " wins!"
        playera = p1.get() + " wins!"
        checkForWin()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "Ｏ"
        bclick = True
        checkForWin()
        flag += 1

    else:
        tkinter.messagebox.showinfo("Krestiki Noliki","Button already clicked")


def checkForWin():
    global flag
    if(button1['text']=='X' and button2['text']=='X' and button3['text']=='X' or
            button4['text']=='X' and button5['text']=='X' and button6['text']=='X' or
            button7['text']=='X' and button8['text']=='X' and button9['text']=='X' or
            button1['text']=='X' and button4['text']=='X' and button7['text']=='X' or
            button2['text']=='X' and button5['text']=='X' and button8['text']=='X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text']=='X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text']=='X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text']=='X'):
        #disableButton()
        tkinter.messagebox.showinfo(playera , "Let's play again!")

        button1['text'] = " "
        button2['text'] = " "
        button3['text'] = " "
        button4['text'] = " "
        button5['text'] = " "
        button6['text'] = " "
        button7['text'] = " "
        button8['text'] = " "
        button9['text'] = " "

        flag = -1

    elif flag == 8:
        print("flag 8")
        tkinter.messagebox.showinfo("It's a tie", "Let's play again!")

        button1['text'] = " "
        button2['text'] = " "
        button3['text'] = " "
        button4['text'] = " "
        button5['text'] = " "
        button6['text'] = " "
        button7['text'] = " "
        button8['text'] = " "
        button9['text'] = " "
        flag = -1


    elif(button1['text']=='Ｏ' and button2['text']=='Ｏ' and button3['text']=='Ｏ' or
            button4['text']=='Ｏ' and button5['text']=='Ｏ' and button6['text']=='Ｏ' or
            button7['text']=='Ｏ' and button8['text']=='Ｏ' and button9['text']=='Ｏ' or
            button1['text']=='Ｏ' and button4['text']=='Ｏ' and button7['text']=='Ｏ' or
            button2['text']=='Ｏ' and button5['text']=='Ｏ' and button8['text']=='Ｏ' or
            button3['text']=='Ｏ' and button6['text']=='Ｏ' and button9['text']=='Ｏ' or
            button1['text']=='Ｏ' and button5['text']=='Ｏ' and button9['text']=='Ｏ' or
            button3['text']=='Ｏ' and button5['text']=='Ｏ' and button7['text']=='Ｏ'):
        #disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)

        button1['text'] = " "
        button2['text'] = " "
        button3['text'] = " "
        button4['text'] = " "
        button5['text'] = " "
        button6['text'] = " "
        button7['text'] = " "
        button8['text'] = " "
        button9['text'] = " "
        flag = -1



label = tk.Label(window, text=" player 1:", font='Helvetica 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=1, column=0)

label = tk.Label(window, text=" player 2:", font='Helvetica 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=2, column=0)

button1 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button1))
button1.grid(row=3, column=0)

button2 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button2))
button2.grid(row=3, column=1)

button3 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button3))
button3.grid(row=3, column=2)

button4 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button4))
button4.grid(row=4, column=0)

button5 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button5))
button5.grid(row=4, column=1)

button6 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button6))
button6.grid(row=4, column=2)

button7 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button7))
button7.grid(row=5, column=0)

button8 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button8))
button8.grid(row=5, column=1)

button9 = tk.Button(window, text=" ", font="Helvetica 20 bold", bg="blue", fg="white", height=4, width=8, command=lambda: btnclick(button9))
button9.grid(row=5, column=2)

window.mainloop()
