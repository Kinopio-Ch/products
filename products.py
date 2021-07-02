import os   #載入作業系統，用於增加權限

def read_file(filename):
    products = []
    with open(filename,'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products


def user_input(products):
    while True:
        name = input('請輸入商品名稱，離開請按q：')
        if name == 'q':     #離開迴圈(quit)
            break
        price = input('請輸入商品價格：')
        price = int(price)
        products.append([name, price])
    print(products)
    return products


def print_products(products):
    for p in products:      #用for迴圈存取
        print(p[0], '的價格是', p[1])         #印出product中子清單的第0個位置

def write_file(filename, products):
    with open(filename,'w', encoding='utf-8') as f:      #開啟product.csv進寫入模式(若電腦有此檔會覆蓋，無此檔會建立，csv檔可用excel開)
                                                            #encoding='utf-8'解決編碼問題即可輸入中文
        f.write('商品,價格\n')              #加入欄位
        for p in products:      #用for迴圈一個個存取
            f.write(p[0] + ',' + str(p[1]) + '\n') #將資料寫入檔案，用+號合併字串，\n代表換行       


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):    #利用作業系統權限找電腦中的products.csv檔案
        print('已找到檔案')
        products = read_file(filename)
    else:
        print('未找到檔案')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()

    