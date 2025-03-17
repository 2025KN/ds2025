import random
win = False
answer = random.randrange(1, 101)
guess = 0


for i in range (8):
    print(f"{7 - i}번의 기회가 남았습니다.")
    guess = int(input("정수를 입력하시오 :"))
    if answer == guess:
        print("정답입니다.")
        win = True
        break
    elif answer > guess:
        print("입력한 수는 답보다 작은 수")
    else:
        print("입력한 수는 답보다 큰 수")
