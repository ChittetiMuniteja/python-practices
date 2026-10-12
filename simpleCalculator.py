from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.config(bg="black")

first_num=0
math=' '
math_sign=' '
math_list=['+','-','÷','×','^']
def calc(math_type,ms):
    global first_num,math,math_sign
    math_sign= ms
    math = math_type
    first_num =entry.get()
    for i in math_list:
        if i in first_num:
            first_num= first_num.replace(i,'')
    cleared()
    entry.insert(0,first_num+math_sign)
    
def equal():
    global first_num,math,math_sign
    second_num= entry.get().replace(str(first_num+math_sign),' ')
    cleared()
    if (math=='add'):
        result =int(first_num)+int(second_num)
        first_num=0       
    elif (math=='sub'):
        result =int(first_num)-int(second_num)
        first_num=0
    elif (math=='div'):
        try:
            result =int(first_num)/int(second_num)
            first_num=0
        except:
            exption="INVID"
            entry.insert(0,exption)
    elif (math=='mul'):
        result =int(first_num)*int(second_num)
        first_num=0
    elif (math=='exp'):
        result =int(first_num)**int(second_num)
        first_num=0
    entry.insert(0,result)
        
        
def cleared():
    entry.delete(0,END)
    
def deleted():
    text = entry.get()[:-1]
    entry.delete(0, END)
    entry.insert(0, text)
  
    
def btn_show(num):
    curr_num=entry.get()
    final_num=curr_num+num
    cleared()
    entry.insert(0,final_num)

#Entry ;    
entry= Entry(root,width=24,justify=CENTER,font=('Arial',15),bg="#262624",fg="white")
entry.grid(row=0,column=0,columnspan =4)
#buttons
btn9 = Button(root, text= "9",padx=24,pady=10,bg="#171616",fg='white',command=lambda :btn_show('9'))
btn9.grid(row=1,column=0)
btn8 = Button(root, text= "8",padx=26,pady=10,bg="#171616",fg='white',command=lambda :btn_show('8') )
btn8.grid(row=1,column=1)
btn7= Button(root, text= "7",padx=26,pady=10,bg="#171616",fg='white',command=lambda :btn_show('7') )
btn7.grid(row=1,column=2)

btn6 = Button(root, text= "6",padx=24,pady=10,bg="#171616",fg='white',command=lambda :btn_show('6') )
btn6.grid(row=2,column=0)
btn5 = Button(root, text= "5",padx=26,pady=10,bg="#171616",fg='white',command=lambda :btn_show('5') )
btn5.grid(row=2,column=1)
btn4 = Button(root, text= "4",padx=26,pady=10,bg="#171616",fg='white',command=lambda :btn_show('4') )
btn4.grid(row=2,column=2)

btn3 = Button(root, text= "3",padx=24,pady=10,bg="#171616",fg='white',command=lambda :btn_show('3'))
btn3.grid(row=3,column=0)
btn2 = Button(root, text= "2",padx=26,pady=10,bg="#171616",fg='white',command=lambda :btn_show('2') )
btn2.grid(row=3,column=1)
btn1 = Button(root, text= "1",padx=26,pady=10,bg="#171616",fg='white',command=lambda :btn_show('1'))
btn1.grid(row=3,column=2)

#equal button;
btn_equal = Button(root, text= "=",pady=32,padx=26,bg="#bda746",fg="white",command=equal)
btn_equal.grid(row=3,column=3,rowspan=2)

btn0= Button(root, text= "0",padx=24,pady=10,bg="#171616",fg='white',command=lambda :btn_show('0'))
btn0.grid(row=4,column=0)

#cleared function;
btn_clear= Button(root, text= "C",padx=59,pady=10,bg="#352873",fg='white',command=cleared)
btn_clear.grid(row=4,column=1,columnspan=2)

#dividing;
btn_sub= Button(root, text= "÷",padx=25,pady=10,bg="#a63737",fg="white",command=lambda: calc('div','÷'))
btn_sub.grid(row=5,column=2)

#multiplication;
btn_sub= Button(root, text= "×",padx=26,pady=10,bg="#a63737",fg="white",command=lambda: calc('mul','×'))
btn_sub.grid(row=5,column=3)

#exponential;
btn_sub= Button(root, text= "exp",padx=21,pady=10,bg="#966293",fg="white",command=lambda: calc('exp','^'))
btn_sub.grid(row=2,column=3)

# delete;
btn_sub= Button(root, text= "del",padx=22,pady=10,bg="#1a2233",fg="white",command=deleted)
btn_sub.grid(row=1,column=3)

#subtraction;
btn_sub= Button(root, text= "-",padx=27,pady=10,bg="#a63737",fg="white",command=lambda: calc('sub','-'))
btn_sub.grid(row=5,column=1)

#addition;
btn_add = Button(root, text= "+",padx=24,pady=10,bg="#a63737",fg="white",command=lambda :calc('add','+'))
btn_add.grid(row=5,column=0)

root.mainloop()
