class Junior_Development():
    def __init__(self,laptop,salory, prog_long):
        self.laptop = laptop
        self.salory = salory
        self.prog_long = prog_long
    def __str__(self):

    def copy_past(self, resoyrse):
        return f'can copy past from-   {resoyrse}'
    def __dir__(self) -> Iterable[str]:



class Middel_development(Junior_Development):
    def __init__(self, laptop,salory, prog_long):

