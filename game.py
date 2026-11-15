import random
secret = random.randint(1, 100)
print("欢迎来到猜数字游戏！数字范围1~100")
while True:
    guess = int(input("请输入你的猜测："))
    if guess == secret:
        print("恭喜猜对！游戏结束")
        break
    elif guess > secret:
        print("猜大了，再试试")
    else:
        print("猜小了，再试试")


