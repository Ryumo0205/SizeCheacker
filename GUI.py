from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from tkinter.ttk import Combobox
from turtle import width

#ListBox Ver

# 定義方法_取得輸入欄內路徑


def CHECK_IMG():
    import sizechecker as SC
    MULT_NUM = RADIOVALUE.get()  # 取得要檢查的倍數
    SC.SizeCheck(MULT_NUM)  # 將倍數放入引數執行檢查
    CHECK_TIMES = 0
    for OUTPUT_FALSE in SC.FALSE_LIST:
        MSG_SPACE.insert(tk.END,SC.FALSE_LIST[CHECK_TIMES])
        CHECK_TIMES = CHECK_TIMES + 1
    #SC.FALSE_LIST = []  # 還原成空列表

def CLEAR():
    MSG_SPACE.delete("1.0", "end")
def TEST_OPEN():
    import sizechecker as SC
    SC.ClickOpenFile()

#------------------介面內容-------------------#
# 主視窗設定
MAIN_WINDOW = tk.Tk()
MAIN_WINDOW.geometry("500x500")
MAIN_WINDOW.title("SizeChecker")
# 創造可容納物件的框架
FRAME = tk.Frame(MAIN_WINDOW, width=450, height=450)
FRAME.pack(pady=20)  # 讓框架稍微遠離邊界
# 把各部件放入 Frame
WORD_1 = tk.Label(FRAME, text='圖片尺寸檢查器', font=(
    "微軟正黑體", 18)).place(x=30, y=10)  # 第一行文字
WORD_2 = tk.Label(FRAME, text="檢查下列路徑的圖片  支援格式 : jpg , png", font=(
    "微軟正黑體", 10)).place(x=30, y=50)  # 第二行文字
WORD_3 = tk.Label(FRAME, text="選擇想要檢查的倍數", font=(
    "微軟正黑體", 10)).place(x=30, y=100)  # 倍數選擇文字
WORD_4 = tk.Label(FRAME, text="下列圖片不符合倍數", font=(
    "微軟正黑體", 12)).place(x=30, y=125)
ENTRY_SPACE = tk.Entry(FRAME, width=55)  # 創造輸入欄
ENTRY_SPACE.place(x=30, y=75)  # 輸入欄位置
# 創造倍數選項
RADIOVALUE = tk.IntVar()  # 倍數單選項內的變數型態
MULTIPLE_NUM_1 = tk.Radiobutton(
FRAME, text="2倍", variable=RADIOVALUE, value=2)  # 倍數選單定義
MULTIPLE_NUM_2 = tk.Radiobutton(FRAME, text="4倍", variable=RADIOVALUE, value=4)

MULTIPLE_NUM_1.place(x=150, y=100)
MULTIPLE_NUM_2.place(x=200, y=100)
# 文字顯示欄位，用來顯示被檢查出有問題的圖片
#MSG_SPACE = ScrolledText(FRAME, width=53, height=20)
#MSG_SPACE.place(x=30, y=150)
MSG_SPACE = tk.Listbox(FRAME, width=53, height=18)
MSG_SPACE.place(x=30, y=150)
SCROLL_BAR = tk.Scrollbar(FRAME, command=MSG_SPACE.yview)
MSG_SPACE.config(yscrollcommand=SCROLL_BAR.set)
SCROLL_BAR.place(x=421, y=150, height=293, anchor='ne')

CHECK_BTN = tk.Button(FRAME, text="Get",font=("微軟正黑體", 14), command=CHECK_IMG)
CHECK_BTN.place(x=300, y=100)
CLEAR_BTN = tk.Button(FRAME, text="Clear",font=("微軟正黑體", 14), command=CLEAR)
CLEAR_BTN.place(x=370, y=100)
TEST_BTN = tk.Button(FRAME, text="OPEN",font=("微軟正黑體", 14), command=TEST_OPEN)
TEST_BTN.place(x=370, y=200)

MAIN_WINDOW.mainloop()
