def get_number_of_teams():
    while True: # if the amount of teams is not at least 2 repeat
        amt_teams = int(input("Enter the number of teams in the tournament: "))
        if amt_teams < 2:
            print("The minimum number of teams is 2, try again.")
        else:
            break
        
    return amt_teams

def get_team_names(num_teams):
    team_list = []
    for _ in range(num_teams): # Go through teams and input name except for edge cases
        while True:
            team_name = input("Please input the name of the team: ")
            if len(team_name) < 2:
                print("Team names must have at least 2 characters, try again.")
                team_name = input("Please input the name of the team: ")
            if team_name.count(" ") > 1:
                print("Team names must have at most 2 words, try again.")
                team_name = input("Please input the name of the team: ")
            else:
                break
        team_list.append(team_name)
    return team_list
    

def get_number_of_games_played(num_teams):
    while True:
        games_played = int(input("Enter the number of games played by each team: "))
        if games_played < num_teams-1: # Cover the fact that each team must play each other once
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
        else:
            break
    return games_played

def get_team_wins(team_names, games_played):
    tour = []
    for team in team_names:
        while True:
            team_win = int(input(f"Enter the number of wins Team {team} had: "))
            if team_win < 0:
                print("The minimum number of wins is 0, try again.")
                team_win = int(input(f"Enter the number of wins Team {team} had: "))
            if team_win > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")
                team_win = int(input(f"Enter the number of wins Team {team} had: "))
            else:
                break
        tour.append((team, team_win)) #append both team name to their associated wins for easy pairing later
        
    return tour

# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")

game_pairing = []

win_sorted = sorted(team_wins, key=lambda x: x[1], reverse=True) #Use the sorted function to sort the teams and wins
games_to_make = len(win_sorted) // 2

for game_num in range(games_to_make): # Grab the most/least pairing of teams to play
    home = win_sorted[game_num][0]
    away = win_sorted[num_teams - 1 - game_num][0]
    game_pairing.append([home, away])
    
for pairing in game_pairing: # print out the resulting pairing giving the losing team the home advantage
    home_team, away_team = pairing
    print(f"Home: {home_team} VS Away: {away_team}")
