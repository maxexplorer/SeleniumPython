from random import randint, sample # функция для генерации целых случайных значений в диапазоне [a; b]

# здесь объявляйте класс RandomPassword
class RandomPassword:
    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args, **kwargs):
        return ''.join(sample(self.psw_chars, randint(self.min_length, self.max_length)))

min_length = 9
max_length = 30
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)

password = rnd()
