# 出租车收费计算
time=str(input("请输入坐车时间："))
a=int(time[:2])
dis=float(input("请输入坐车距离（公里）："))
if 6<=a<=22:
    if dis<=3:
      price=12
    if 15>dis>3:
      price = round(float(dis * 2.6))
    if 15<=dis<=25:
      price = float(dis * 2.6)
      price=round(dis*2.6*0.2+price)
    if 25<dis:
      price = float(dis * 2.6)
      price =round (dis * 2.6 * 0.5+price)
else:
    if dis<=3:
      price=12
      price=round(price+price*0.3)
    if 15>dis>3:
      price = float(dis * 2.6)
      price =round (dis * 2.6*0.3+price)
    if 15<=dis<=25:
      price = float(dis * 2.6)
      price=round(price+(dis*2.6*0.2)+(dis * 2.6*0.3))
    if 25<dis:
      price = float(dis * 2.6)
      price =round(price+ (dis * 2.6 * 0.5)+(dis * 2.6*0.3))

print("坐车费用的金额为%.2f元" % (price))