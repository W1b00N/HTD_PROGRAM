# ให้เขียน function สุ่มตัวเลขเพื่อใช้สำหรับการทายตัวเลข
# 1. สุ่มตัวเลข random
import random


# 2.สร้าง function
def guess(x):
    random_number = random.randint(1, x)
    userguess = 0
    while userguess != random_number:
        userguess = int(input(f"ให้ใส่ตัวเลขระหว่าง 1-{x} : "))
        if userguess < random_number:
            print("ขอโทษ ทายใหม่อีกที เพราะว่ามัน น้อยกว่า")
        elif userguess > random_number:
            print("ขอโทษ ทายใหม่อีกที เพราะว่ามัน มากกว่า")
    print(f"ยินดีด้วย ในที่สุดก็ทายตัวเลขถูก {random_number}")


# 3.เรียกใช้ function
userinput = int(input("ใส่จำนวนสูงสุดที่ใช้สำหรับทาย : "))
guess(userinput)
