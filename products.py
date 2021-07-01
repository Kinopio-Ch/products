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


