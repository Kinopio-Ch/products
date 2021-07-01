products = []          #商品建立空清單
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

with open('product.txt','w') as f:      #開啟product.txt進寫入模式(若電腦有此檔會覆蓋，無此檔會建立)
    for p in products:      #用for迴圈一個個存取
        f.write(p[0] + ',' + p[1] + '\n') #將資料寫入檔案，用+號合併字串，\n代表換行       



