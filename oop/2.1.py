class Acount:
    def __init__(self, login, password,secret_key):
        self.login = login
        self.password = password
        self.sk = secret_key

    def balance(self,summary):
        return f'Summary{summary}'

    def __str__(self):
        return f' login: {self.login}\n'\
            f'pass__{self.password}\n'\
            f' sk__ {self.sk}'

acc = Acount(login='Radomir',password=12345,secret_key=12345)
print(acc.balance(9000)
print(acc.password)
