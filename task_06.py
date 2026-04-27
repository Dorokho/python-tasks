class WrongNumberOfPlayersError(Exception):
    pass

class NoSuchStrategyError(Exception):
    pass

def rps_game_winner(players):
    if len(players) != 2:
        raise WrongNumberOfPlayersError
    
    player1, player2 = players

    name1, move1 = player1
    name2, move2 = player2

    move1 = move1.upper()
    move2 = move2.upper()
    
    valid_moves = ['R', 'P', "S"]

    if move1 not in valid_moves or move2 not in valid_moves:
        raise NoSuchStrategyError
    
    if move1 == move2:
        return player1
    
    if (
        (move1 == 'R' and move2 == 'S') or
        (move1 == 'S' and move2 == 'P') or
        (move1 == 'P' and move2 == 'R')
    ):
        return player1
    else:
        return player2

# print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))    # => WrongNumberOfPlayersError
# print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))  # => NoSuchStrategyError
# print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  # => 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))    # => 'player1 P'