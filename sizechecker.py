from ast import Pass
import sys
sys.path.append("modules")  # 新增根目錄下資料夾的模組搜尋路徑
import GUI
from pathlib import Path
from PIL import Image

""" 檢查資料夾路境內的圖片能否被設定的數字整除 """
#PATH_STR = GUI.ENTRY_SPACE.get()
#IMGS_PATH = list(Path(PATH_STR).glob("*"))  # 定義圖片路徑為列表
FALSE_LIST = []  # 儲存不合倍數的空列表

#------------列出所有要檢查的檔名(檢查用不向使用者開放)-----------------#

def AllCheck():
    PATH_STR = str()  #路徑字串
    IMGS_PATH = list(Path(PATH_STR).glob("*"))  # 定義圖片路徑為列表
    IMGS_NAME = []  # 儲存所有檔名的空列表
    x = 0  # 用於紀錄取得路徑列表中的第幾個參數
    for GET_NAME in IMGS_PATH:
        PURENAME = Path(IMGS_PATH[x].stem)  # 取得不含路徑檔名
        NAME = str(PURENAME)    # 將該路徑從路徑物件轉成字串
        IMGS_NAME.append(NAME)  # 放至空列表
        x = x + 1
    for PRINT_ALL in IMGS_PATH:
        print("圖片名稱:", PRINT_ALL)

#------------檢查圖片是否符合倍數---------------#


def SizeCheck(mult=int):
    PATH_STR = GUI.ENTRY_SPACE.get()
    IMGS_PATH_JPG = list(Path(PATH_STR).glob("*.jpg"))  # 定義圖片路徑為列表
    IMGS_PATH_PNG = list(Path(PATH_STR).glob("*.png"))  # 定義圖片路徑為列表
    print("檢查路徑:",PATH_STR)
    SET_NUM = mult  # 設定除數
    # 檢查JPG用迴圈
    CHECK_TIMES_JPG = 0 #jpg檔檢查迴圈次數
    CHECK_TIMES_PNG = 0 #png檔檢查迴圈次數
    CHECK_BOOL_JPG = 0  #判斷jpg是否有不符合的檔案
    CHECK_BOOL_PNG = 0  #判斷png是否有不符合的檔案
    for CHECk_IMGS_JPG in IMGS_PATH_JPG:
        IMG_NOW = Image.open(CHECk_IMGS_JPG)  # 開啟該迴圈的圖片
        GETSIZE = IMG_NOW.size  # 取得圖片尺寸tuple放至變數
        IMG_STATE = bool(True)  # 判斷是否被該倍數整除
        for SizeCheck in GETSIZE:  # 迴圈判斷該尺寸tuple是否能被設定的值整除
            if SizeCheck % SET_NUM == 0:
                pass
            else:
                IMG_STATE = False
                GET_FALSENAME = Path(IMGS_PATH_JPG[CHECK_TIMES_JPG].stem)  # 取得不含路徑檔名
                FALSENAME = str(GET_FALSENAME)  # 路徑物件轉成字串
                FALSE_LIST.append(FALSENAME + ".jpg")    # 加入不符合倍數的空列表
                CHECK_BOOL_JPG = CHECK_BOOL_JPG + 1 #計算不符合的數量
                break
        CHECK_TIMES_JPG = CHECK_TIMES_JPG + 1   #換到下個路徑
    if CHECK_BOOL_JPG == 0:
        FALSE_LIST.append("★★★★★★★★JPG檔案全數通過★★★★★★★★")
        FALSE_LIST.append("\n")
    else:
        FALSE_LIST.append("----------以上為有問題的JPG檔案-----------")
        FALSE_LIST.append("\n")

    for CHECk_IMGS_PNG in IMGS_PATH_PNG:
        IMG_NOW = Image.open(CHECk_IMGS_PNG)  # 開啟該迴圈的圖片
        GETSIZE = IMG_NOW.size  # 取得圖片尺寸tuple放至變數
        IMG_STATE = bool(True)  # 判斷是否被該倍數整除
        for SizeCheck in GETSIZE:  # 迴圈判斷該尺寸tuple是否能被設定的值整除
            if SizeCheck % SET_NUM == 0:
                pass
            else:
                IMG_STATE = False
                GET_FALSENAME = Path(IMGS_PATH_PNG[CHECK_TIMES_PNG].stem)  # 取得不含路徑檔名
                FALSENAME = str(GET_FALSENAME)  # 路徑物件轉成字串
                FALSE_LIST.append(FALSENAME + ".png")    # 加入不符合倍數的空列表
                CHECK_BOOL_PNG = CHECK_BOOL_PNG + 1 #計算不符合的數量
                break
        CHECK_TIMES_PNG = CHECK_TIMES_PNG + 1
    if CHECK_BOOL_PNG == 0:
        FALSE_LIST.append("★★★★★★★★PNG檔案全數通過★★★★★★★★")
    else:
        FALSE_LIST.append("----------以上為有問題的PNG檔案-----------")

    print("---------不合", SET_NUM, "倍數的圖片-----------")

    for PRINT_FALSE in FALSE_LIST:
        print(PRINT_FALSE)
    

    #Git Test
    #Git Test3