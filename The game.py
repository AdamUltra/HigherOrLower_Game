import DataBase
import Art
import random
Score = 0
lose = False
print(Art.logo)
a = random.choice(DataBase.data)
while lose is False:
    b = random.choice(DataBase.data)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(Art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    Guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    def check():
        if a['follower_count'] > b['follower_count']:
            return True

        else:
            return False


    def win_lose(more):
        global Score, lose
        if more:
            if Guess == 'a':
                Score += 1
                return f'You win!!\n Your score now is {Score}\n'
            else:
                lose = True
                return f'You lose\n Your final score is {Score}'

        else:
            if Guess == 'a':
                lose = True
                return f'You lose\n Your final score is {Score}'
            else:
                Score += 1
                return f'You win!!\n Your score now is {Score}\n'


    if check():
        print(win_lose(True))

    else:
        print(win_lose(False))

    a = b

