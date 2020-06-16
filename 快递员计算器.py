#快递员计算器
city=str(input("请输入快递到达的省份："))
weight=float(input("请输入快递重量（公斤）："))
a,b,c,d,e,f='东三省','宁夏','青海','海南','新疆','西藏'
if weight<=3:
    if city==a or city==b or city==c or city==d:
        price=12
    elif city==e or city==f:
        price=20
    else:
        price=10
elif weight>3:
    if city==a or city==b or city==c or city==d:
        price=12
        price=price+(weight-3)*10
    elif city==e or city==f:
        price=20
        price = price + (weight - 3) * 20
    else:
        price=10
        price=price+(weight-3)*5
print("你邮寄%s的快递费用为%d元,重量为%.1f公斤" % (city, price,weight))

