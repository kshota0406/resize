from tkinter import *
import tkinter
import tkinter.font as font
import os
from PIL import Image


root = Tk()
root.title(u"img_resize")
root.geometry("260x120")
my_font = font.Font(root,family="System",size=20,weight="bold")

#画像ソースディレクトリ
dir_name = "input"
new_dir_name ="output"

#実行ボタンホバー関数
def enter_bg(event):
    event.widget['bg'] = '#CCFFFF'
def leave_bg(event):
    event.widget['bg'] = '#f0e68c'

# ボタンが押されるとここが呼び出される
def resize(event):
  files = os.listdir(dir_name)
  for file in files:
      value = float(var_spinbox.get())/100
      img=Image.open(os.path.join(dir_name,file))
      fx, fy = float(value), float(value)
      size = (round(img.width * fx), round(img.height * fy))
      img_resize=img.resize(size)
      img_resize.save(os.path.join(new_dir_name,file))
  label2 = tkinter.Label(text="outputフォルダを確認してね", font=my_font,bg="yellow")
  label2.grid(
    column=0,
    row=4,
    columnspan=2
)

#inputフォルダに画像を入れてね
label3 = tkinter.Label(text="inputフォルダに画像を入れてね" ,font=my_font)
label3.grid(
    column=0,
    row=0,
    columnspan=2
)

#スピンボックス
var_spinbox = tkinter.StringVar()
var_spinbox.set(10)
spinbox = tkinter.Spinbox(root, from_=5, to=95, increment=5, textvariable=var_spinbox, width=5 ,font=my_font)
spinbox.grid(
    column=0,
    row=1,
)

#%にリサイズ
label4 = tkinter.Label(text="%にリサイズ" ,font=my_font)
label4.grid(
    column=1,
    row=1,
)


#ボタン
#左クリック（<Button-1>）されると，resize関数を呼び出すようにバインド
Button = tkinter.Button(text=u'実行', width=20 ,font=my_font ,bg="#f0e68c")
Button.bind("<Button-1>",resize) 
Button.grid(
    column=0,
    row=2,
    columnspan=2
)
#マウスホバーされると，実行ボタンの色を変える
Button.bind("<Enter>", enter_bg)
Button.bind("<Leave>", leave_bg)

root.mainloop()





