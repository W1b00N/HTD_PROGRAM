#ให้เขียนโปรแกรมที่นับจำนวนแต่ละตัวอักษร จาก user ที่ input เข้ามา
# output
# hello
# {'h': 1', 'e': 1, 'l': 2, 'o': 1}

def charFreq(userinput):
    dictx = {}
    for char in userinput:
        keys = dictx.keys()
        if char in keys:
            dictx[char] += 1
        else:
            dictx[char] = 1
    return dictx

Uinput = input('ใส่คำตัวอักษร : ')
print(charFreq(Uinput))