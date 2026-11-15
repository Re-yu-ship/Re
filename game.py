import random
secret = random.randint(1, 100)
print("欢迎来到猜数字游戏！数字范围1~100")
guess = int(input("请输入你的猜测："))
if guess == secret:
    print("恭喜猜对！")
elif guess > secret:
    print("大了")
else:
    print("小了")

