from tkinter import*

def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
    
def btn_clear_display():
    global operator
    operator=" "
    text_input.set(" ")
    
def btn_equals_input():
    global operator
    sum_op=(eval(operator))
    text_input.set(sum_op)
    operator=" "


cal = Tk()
cal.title('Calculator')
operator =""
text_input = StringVar()


txtDisplay = Entry(cal,font=('arial', 20, 'bold'), textvariable = text_input, bd=30, insertwidth=4, 
                    bg='#8fb996', highlightcolor="#415d43",  justify='right').grid(columnspan=4)

#==========================
btn7=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='8',bg='#8fb996', command=lambda:btn_click(7)).grid(row=1,column=0)

btn8=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='8',bg='#8fb996', command=lambda:btn_click(8)).grid(row=1,column=1)

btn9=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='9',bg='#8fb996', command=lambda:btn_click('9')).grid(row=1,column=2)

division=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='/',bg='#8fb996', command=lambda:btn_click('/')).grid(row=1,column=3)
#===========================
btn4=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='4',bg='#8fb996', command=lambda:btn_click(4)).grid(row=2,column=0)

btn5=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='5',bg='#8fb996', command=lambda:btn_click(5)).grid(row=2,column=1)

btn6=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='6',bg='#8fb996', command=lambda:btn_click(6)).grid(row=2,column=2)

multiplication=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='*',bg='#8fb996', command=lambda:btn_click('*')).grid(row=2,column=3)
#===========================
btn1=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='1',bg='#8fb996', command=lambda:btn_click(1)).grid(row=3,column=0)

btn2=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='2',bg='#8fb996', command=lambda:btn_click(2)).grid(row=3,column=1)

btn3=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='3',bg='#8fb996', command=lambda:btn_click(3)).grid(row=3,column=2)

subtraction=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='-',bg='#8fb996', command=lambda:btn_click('-')).grid(row=3,column=3)
#===========================
btn0=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='0',bg='#8fb996', command=lambda:btn_click(0)).grid(row=4,column=0)

btn_clear=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='C', bg='#8fb996', command=btn_clear_display).grid(row=4,column=1)

btn_equal=Button(cal,padx=16,bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='=',bg='#8fb996', command=btn_equals_input).grid(row=4,column=2)

addition=Button(cal,padx=16, bd=8, fg='black', font=('arial', 20, 'bold'), 
            text='+',bg='#8fb996', command=lambda:btn_click('+')).grid(row=4,column=3)


cal.mainloop()














