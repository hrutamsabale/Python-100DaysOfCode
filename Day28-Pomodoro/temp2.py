from time import sleep

def a():
    print("Before")
    b(5)
    print("after")

def b(count):
    if count>0:
        sleep(1)
        print(count)
        b(count-1)
        print("coming out")
    # else:
    #     return

a()