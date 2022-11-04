# Использование JSON - хранение и использование данных
import json

player1 = {
    'PlayerName': 'Donald',
    'Score': 345,
    'awards': ['OR', 'NV', 'NY']
}

player2 = {
    'PlayerName': 'Hillary',
    'Score': 346,
    'awards': ['WT', 'TX', 'MI']
}
myplayers = []
myplayers.append(player1)
myplayers.append(player2)

#_________________SAVE_by_JSON_________________

filename = 'user_settings.txt'
myfile = open(filename, mode='w', encoding='Latin-1')
json.dump(myplayers, myfile)
myfile.close()

#_________________LOAD_by_JSON_________________

myfile = open(filename, mode='r')
json_data = json.load(myfile)

for users in json_data:
    print("Player Name is: " + str(users['PlayerName']))
    print('Player Score is: ' + str(users['Score']))
    print('Player awards N1: ' + str(users['awards'][0]))
    print('Player awards N2: ' + str(users['awards'][1]))
    print('Player awards N3: ' + str(users['awards'][2]))
    print("____________________________\n")

myfile.close()


