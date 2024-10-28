# ici on créer un fichier csv pour stocker les valeurs des statistiques des joueurs

import pandas as pd
data_frame_player = pd.DataFrame(columns=['player_name_sofascore','player_name_transfer_market' , 'player_team', 'player_position','player_market_value',
                                                                   'average_rating','total_game_played','started_game_percentage',
                                                                   'minute_per_game', 'goals_per_game', 'assist_per_game',
                                                                   'dribbled_per_game','pourcentage passes',
                                                                    'balls_recovered_per_game',
                                                                   'possession_won', 'tackles_per_game',
                                                                   'interception_per_game', 'clean_sheets',
                                                       'saves','goals_conceded'])

data_frame_player.to_csv('morocco_player_statistique_caf_2023.csv')