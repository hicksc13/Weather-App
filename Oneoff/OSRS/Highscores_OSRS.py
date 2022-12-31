from osrs_api.const import AccountType
from osrs_api import Hiscores


player = input("Who would you like to look up?: ")
input_player = Hiscores(player)
print(input_player)


