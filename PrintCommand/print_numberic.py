a = 2
b = 3
print('1. 'f"{a} * {b} = ",str (a+b))


a = 2
b = 3
print('2. 'f"{a} + {b} = {b} + {a} = 6" )


a = 2
b = 3 
c = 5
print('3. 'f"{a} * ({a} + {c}) = {a} * {3} + {a} * {c}")

a = 2.4
b = 2.5
c = a + b
print('4. 'f"{a} + {b} = " "%.4f" % c)

a = 5 
b = 2 
c = a+b
print('5. 'f"{a:.2f} + {b:.2f} = {c:.3f}")

birthday = 25
print('6. 'f"ฉันเกิดวันที่ {birthday} ธันวาคม")

a = 5
b = 100
print('7. 'f"{a} เท่าของ {b} มีเท่ากับ {(a * b)}")

a = 3.5
print('8. 'f"เขามีเงินเยอะกว่าฉัน {a:.2f} บาท")

a = 5 
print('9. 'f'ฉันได้กำไร {a}% หรือ {(a * .01)}')

a = 5 
b = 3.5
print('10. 'f'เมื่อวานฉันขาดทุน {a - int(b)}% วันนี้ฉันได้กำไร {b:.2f}%')