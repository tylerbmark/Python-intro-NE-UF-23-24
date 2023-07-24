# gt_ICA7_A.py
# Playing with dictionaries!
# Allows you to view the statistics for a player of a game

# Input: Player Name

# Output: Statistics

# by Gentry Trimble
def dictionary():
    players = {'Aaron': {'Wins':158, 'Losses':85,'Ties': 1 }, 'Justin':{'Wins': 25,'Losses': 25,'Ties': 0 },
               'Kirk': {'Wins': 73,'Losses':66,'Ties':2}}
    return players

def display_players(players):
    player_names = sorted(players.keys())
    for name in player_names:
        print(name)

def display_stats(players,player_name):
    stats = players.get(player_name)
    if stats:
        wins = stats['Wins']
        losses = stats['Losses']
        ties = stats['Ties']
        line = '{:10} {:>5}'
        print(line.format('Wins:', wins))
        print(line.format('Losses:',losses))
        print(line.format('Ties:',ties))
    else: print(f"There is no player named {player_name}.")

def main():
    players = dictionary()
    display_players(players)
    repeat = 'y'
    while repeat.lower() == 'y':
        name = input('Enter a player name: ')
        display_stats(players,name.title())
        repeat = input('Want stats for another player? (y/n):')

main()
