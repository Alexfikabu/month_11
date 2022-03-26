class CompareCards:
    def __init__(self,player_list,computer_list):
        self.player_list = player_list
        self.computer_list = computer_list
    def compare_result(self):
        if sum(self.player_list) > 20 and sum(self.computer_list )<20:
            print(f'Our cards:{sum(self.player_list)} Computer WIN! Result_c{sum(self.computer_list)}')
            retern True

        elif sum(self.player_list) < 20 and sum(self.computer_list )>20:
            print(f'Our cards:{sum(self.player_list)} You WIN! Result_c{sum(self.computer_list)}')
            retern True

        elif sum(self.player_list) > 20 and sum(self.computer_list )>20:
            print(f'Our cards:{sum(self.player_list)} DRAW! Result_c{sum(self.computer_list)}')
            retern True

