import os   #載入作業系統，用於增加權限
products = []          #商品建立空清單

if os.path.isfile('products.csv'):    #利用作業系統權限找電腦中的products.csv檔案
    print('已找到檔案')
    with open('products.csv', 'r', encoding='utf-8') as f:        #讀取檔案 
        for line in f:
            if '商品,價格' in line:
                continue    #跳到下一迴
            name, price = line.strip().split(',')    #找逗點切開，逗點會不見
            products.append([name, price])
    print(products)

else:
    print('未找到檔案')




while True:
    name = input('請輸入商品名稱，離開請按q：')
    if name == 'q':     #離開迴圈(quit)
        break
    price = input('請輸入商品價格：')
    
    p = []              #建立products中的子清單
    p.append(name)      #8、9、10行可縮減為p = [name, price]
    p.append(price)
    products.append(p)
print(products)

products[0][0]          #存取products清單  

for p in products:      #用for迴圈存取
    print(p[0], '的價格是', p[1])         #印出product中子清單的第0個位置

with open('products.csv','w', encoding='utf-8') as f:      #開啟product.csv進寫入模式(若電腦有此檔會覆蓋，無此檔會建立，csv檔可用excel開)
                                                          #encoding='utf-8'解決編碼問題即可輸入中文
    f.write('商品,價格\n')              #加入欄位
    for p in products:      #用for迴圈一個個存取
        f.write(p[0] + ',' + p[1] + '\n') #將資料寫入檔案，用+號合併字串，\n代表換行       



