# apres la determination du liste du joueurs et la creation du fichiers on doit la remetre dans le variable list_player_spain pour determiner les statistique du joueurs
# cette algorithme créer un fichier csv dont il y a les statistiques des joueurs (par example ici les joueurs marocains)

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException



list_player_spain = ['Bono', 'El Mehdi Benabid', 'Munir', 'Nayef Aguerd ', 'Chadi Riad', 'Romain Saïss', 'Abdel Abqar ',
                     'Yunis Abdelhamid', 'Yahia Attiyat Allah', 'Achraf Hakimi', 'Noussair Mazraoui  ', 'Mohamed Chibi',
                     'Sofyan Amrabat ', 'Oussama El Azzouzi ', 'Azzedine Ounahi', 'Ismael Saibari', 'Amir Richardson',
                     'Bilal El Khannouss', 'Amine Harit', 'Selim Amallah', 'Amine Adli ', 'Abde Ezzalzouli',
                     'Sofiane Boufal ', 'Hakim Ziyech ', 'Youssef En-Nesyri', 'Tarik Tissoudali', 'Ayoub El Kaabi ',
                     'Anas Zniti', 'Ahmed Reda Tagnaouti', 'Youssef El Motie', 'Adam Masina', 'Badr Benoun',
                     'Samy Mmaee', 'Jawad El Yamiq', 'Achraf Dari', 'Ismaël Kandouss', 'Ayoub Amraoui', 'Fahd Moufi',
                     'Yahya Jabrane', 'Imrân Louza', 'Youssef Maleh', 'Benjamin Bouchouari', 'Yassine Kechta',
                     'Ilias Chair', 'Younès Belhanda', 'Abdelhamid Sabiri ', 'Oussama Idrissi', 'Anass Zaroury',
                     'Ibrahim Salah', 'Munir El Haddadi', 'Zakaria Aboukhlal ', 'Abderrazak Hamdallah', 'Ryan Mmaee',
                     'Walid Cheddira']


list_players = []
os.environ['PATH'] += r'C:\Users\ULTRAPC\Downloads\Chrome'

driver = webdriver.Firefox()

driver.get('https://www.sofascore.com/')

driver.implicitly_wait(3)

element = driver.find_element(By.CLASS_NAME, 'sc-30244387-0.bwrEIu')

element.send_keys('youness')

for z in range(len(list_player_spain)):

    list_player = []

    time.sleep(0.2)

    element3 = driver.find_element(By.CLASS_NAME, 'sc-fXSgeo.bRCkiq')

    time.sleep(0.2)

    element3.click()

    element = driver.find_element(By.CLASS_NAME, 'sc-30244387-0.bwrEIu')

    time.sleep(0.2)

    element.send_keys(list_player_spain[z])

    time.sleep(0.2)

    element.send_keys(Keys.RETURN)

    time.sleep(0.5)

    try:

        element2 = driver.find_element(By.CLASS_NAME, 'sc-fqkvVR.sc-dcJsrY.fdFbZo.fFmCDf')

    except NoSuchElementException:

        continue

    time.sleep(0.2)

    try:

        element2.click()

    except StaleElementReferenceException:

        z=z-1
        continue

    time.sleep(0.2)

    season_button = driver.find_elements(By.CLASS_NAME, 'sc-fUnMCh.etLKqo')

    time.sleep(0.2)

    try:

        season_button[0].click()

    except IndexError:

        continue

    except StaleElementReferenceException:

        z = z - 1
        continue

    time.sleep(1)

    championship = driver.find_elements(By.CLASS_NAME,'sc-fqkvVR.sc-dcJsrY.gBgQbz.dTIlke')

    time.sleep(0.2)

    list_player_performance = []

    for i in range(0, len(championship)):

        time.sleep(1)

        try:
            season_button[0].click()

        except StaleElementReferenceException:
            z=z-1
            continue

        time.sleep(1)

        championship1 = driver.find_elements(By.CLASS_NAME, 'sc-fqkvVR.sc-dcJsrY.gBgQbz.dTIlke')

        time.sleep(0.2)

        try:

            championship1[i].click()

        except ElementClickInterceptedException:

            z = z-1

            continue

        time.sleep(0.2)

        try:
            season_button[1].click()
        except IndexError:
            continue
        except StaleElementReferenceException:
            z=z-1
            continue

        time.sleep(0.2)

        seasons = driver.find_elements(By.CLASS_NAME,'sc-jEACwC.kxciLR')

        L = []

        for season in seasons:
            L.append(season.text)

        if '' in L:
            time.sleep(0.5)
            seasons[-1].click()
            season_button[1].click()
            time.sleep(0.2)
            seasons = driver.find_elements(By.CLASS_NAME, 'sc-jEACwC.kxciLR')
            L = []

            for season in seasons:
                L.append(season.text)

        if '23/24' in L:
            j = L.index('23/24')
            time.sleep(0.5)
            seasons[j].click()
            A = []
            try:
                my_element3 = driver.find_element(By.CLASS_NAME, 'sc-fqkvVR.sc-dcJsrY.jQVEMT.eFJwJL')
                time.sleep(0.2)
                A.append(my_element3.text.split('\n'))

            except NoSuchElementException:
                A.append(['Average Sofascore rating', '7.00'])

            my_element = driver.find_elements(By.CLASS_NAME, 'sc-fqkvVR.sc-dcJsrY.litZes.eFJwJL')

            time.sleep(0.2)

            for element in my_element:
                A.append(element.text.split('\n'))

            if A not in list_player_performance and not A[0][1] == '-':
                list_player_performance.append(A)

        elif '2023' in L:
            j = L.index('2023')
            time.sleep(0.5)
            seasons[j].click()
            A = []
            try:
                my_element3 = driver.find_element(By.CLASS_NAME, 'sc-fqkvVR.sc-dcJsrY.jQVEMT.eFJwJL')
                time.sleep(0.2)
                A.append(my_element3.text.split('\n'))

            except NoSuchElementException:
                A.append(['Average Sofascore rating', '7.00'])

            my_element = driver.find_elements(By.CLASS_NAME, 'sc-fqkvVR.sc-dcJsrY.litZes.eFJwJL')

            time.sleep(0.2)

            for element in my_element:
                A.append(element.text.split('\n'))

            if A not in list_player_performance and not A[0][1] == '-':
                list_player_performance.append(A)



    L = list_player_performance
    a = len(L)

    print(L)

    started = 0
    total_played = 0
    average_rating = 0
    minute_per_game = 0

    for i in range(a):
        average_rating = average_rating + float(L[i][0][1]) * float(L[i][1][1])
        total_played = total_played + float(L[i][1][1])
        started = started + float(L[i][2][1])
        minute_per_game += float(L[i][3][1]) * float(L[i][1][1])

    if total_played == 0:
        continue

    started_percentage = started / total_played
    average_rating = round(average_rating / total_played, 2)
    minute_per_game = minute_per_game/total_played

    player_name = list_player_spain[z]
    player_position = driver.find_elements(By.CLASS_NAME, 'sc-jEACwC.hJlaNd')[4].text

    player_team = driver.find_element(By.CLASS_NAME, 'sc-fqkvVR.sc-dcJsrY.gAJgeg.eOzYQf').text
    player_name_sofascore = driver.find_element(By.CLASS_NAME, 'sc-jEACwC.iLVhST').text

    print(player_name_sofascore)

    i = player_team.split('\n')
    player_team = i[0]
    print(player_team)

    try:

        player_market_value = driver.find_element(By.CLASS_NAME, 'sc-jEACwC.jdfxsp')

        a = 0
        for i in player_market_value.text:
            if i == 'M':
                player_market_value = float(player_market_value.text[:a])
                break
            if i == 'K':
                player_market_value = float(player_market_value.text[:a]) * 0.001
                break
            a = a + 1
    except NoSuchElementException:
        player_market_value = 0

    a = len(L)

    if player_position == 'F':

        goals = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Goals':
                    goals = goals + int(L[j][i][1])
                    break

        goals_scored_per_game = goals / total_played

        assist = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Assists':
                    assist = assist + float(L[j][i][1])
                    break

        assist_per_game = assist / total_played

        dribble_per_game = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Dribbled past per game':
                    dribble_per_game = dribble_per_game + float(L[j][i][1]) * float(L[j][1][1])
                    break

        dribble_per_game = dribble_per_game / total_played

        pourcentage_passes = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Accurate per game':
                    pourcentage_passes = pourcentage_passes + float(L[j][i][1][-4:-2]) * float(L[j][1][1])
                    print(float(L[j][i][1][-4:-2]))
                    print(pourcentage_passes)
                    break

        pourcentage_passes = pourcentage_passes / total_played

        balls_recovered_per_game = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Balls recovered per game':
                    balls_recovered_per_game = balls_recovered_per_game + float(L[j][i][1]) * float(L[j][1][1])
                    break

        balls_recovered_per_game = balls_recovered_per_game / total_played

        possession_won = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Possession won':
                    possession_won = possession_won + float(L[j][i][1]) * float(L[j][1][1])
                    break

        possession_won = possession_won / total_played

        tackle_per_game = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Tackles per game':
                    tackle_per_game = tackle_per_game + float(L[j][i][1]) * float(L[j][1][1])
                    break

        tackle_per_game = tackle_per_game / total_played

        interception = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Interceptions per game':
                    interception = interception + float(L[j][i][1]) * float(L[j][1][1])
                    break

        interception = interception / total_played

        clean_sheet = 0.0
        saves = 0.0
        goals_conceded = 0.0

        list_player = []

        list_player.append(player_name_sofascore)
        list_player.append(player_name)
        list_player.append(player_team)
        list_player.append(player_position)
        list_player.append(player_market_value)
        list_player.append(round(average_rating, 2))
        list_player.append(total_played)
        list_player.append(round(started_percentage, 2))
        list_player.append(round(minute_per_game, 2))
        list_player.append(round(goals_scored_per_game, 2))
        list_player.append(round(assist_per_game, 2))
        list_player.append(round(dribble_per_game, 2))
        list_player.append(round(pourcentage_passes, 2))
        list_player.append(round(balls_recovered_per_game, 2))
        list_player.append(round(possession_won, 2))
        list_player.append(round(tackle_per_game, 2))
        list_player.append(round(interception, 2))
        list_player.append(clean_sheet)
        list_player.append(saves)
        list_player.append(goals_conceded)

        list_players.append(list_player)

    if player_position == 'M':

            goals = 0
            for j in range(a):
                for i in range(len(L[j])):
                    if L[j][i][0] == 'Goals':
                        goals = goals + int(L[j][i][1])
                        break

            goals_scored_per_game = goals / total_played

            assist = 0
            for j in range(a):
                for i in range(len(L[j])):
                    if L[j][i][0] == 'Assists':
                        assist = assist + float(L[j][i][1])
                        break

            assist_per_game = assist / total_played

            dribble_per_game = 0
            for j in range(a):
                for i in range(len(L[j])):
                    if L[j][i][0] == 'Dribbled past per game':
                        dribble_per_game = dribble_per_game + float(L[j][i][1]) * float(L[j][1][1])
                        break

            dribble_per_game = dribble_per_game / total_played

            balls_recovered_per_game = 0
            for j in range(a):
                for i in range(len(L[j])):
                    if L[j][i][0] == 'Balls recovered per game':
                        balls_recovered_per_game = balls_recovered_per_game + float(L[j][i][1]) * float(L[j][1][1])
                        break

            balls_recovered_per_game = balls_recovered_per_game / total_played

            possession_won = 0
            for j in range(a):
                for i in range(len(L[j])):
                    if L[j][i][0] == 'Possession won':
                        possession_won = possession_won + float(L[j][i][1]) * float(L[j][1][1])
                        break

            possession_won = possession_won / total_played

            tackle_per_game = 0
            for j in range(a):
                for i in range(len(L[j])):
                    if L[j][i][0] == 'Tackles per game':
                        tackle_per_game = tackle_per_game + float(L[j][i][1]) * float(L[j][1][1])
                        break

            tackle_per_game = tackle_per_game / total_played

            interception = 0
            for j in range(a):
                for i in range(len(L[j])):
                    if L[j][i][0] == 'Interceptions per game':
                        interception = interception + float(L[j][i][1]) * float(L[j][1][1])
                        break

            interception = interception / total_played

            pourcentage_passes = 0
            for j in range(a):
                for i in range(len(L[j])):
                    if L[j][i][0] == 'Accurate per game':
                        pourcentage_passes = pourcentage_passes + float(L[j][i][1][-4:-2]) * float(L[j][1][1])
                        print(float(L[j][i][1][-4:-2]))
                        print(pourcentage_passes)
                        break

            pourcentage_passes = pourcentage_passes / total_played

            clean_sheet = 0
            saves = 0
            goals_conceded = 0

            list_player = []

            list_player.append(player_name_sofascore)
            list_player.append(player_name)
            list_player.append(player_team)
            list_player.append(player_position)
            list_player.append(player_market_value)
            list_player.append(round(average_rating, 2))
            list_player.append(total_played)
            list_player.append(round(started_percentage, 2))
            list_player.append(round(minute_per_game, 2))
            list_player.append(round(goals_scored_per_game, 2))
            list_player.append(round(assist_per_game, 2))
            list_player.append(round(dribble_per_game, 2))
            list_player.append(round(pourcentage_passes, 2))
            list_player.append(round(balls_recovered_per_game, 2))
            list_player.append(round(possession_won, 2))
            list_player.append(round(tackle_per_game, 2))
            list_player.append(round(interception, 2))
            list_player.append(clean_sheet)
            list_player.append(saves)
            list_player.append(goals_conceded)

            list_players.append(list_player)

    if player_position == 'D':
                goals = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Goals':
                            goals = goals + int(L[j][i][1])
                            break

                goals_scored_per_game = goals / total_played

                assist = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Assists':
                            assist = assist + float(L[j][i][1])
                            break

                assist_per_game = assist / total_played

                dribble_per_game = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Dribbled past per game':
                            dribble_per_game = dribble_per_game + float(L[j][i][1]) * float(L[j][1][1])
                            break

                dribble_per_game = dribble_per_game / total_played

                balls_recovered_per_game = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Balls recovered per game':
                            balls_recovered_per_game = balls_recovered_per_game + float(L[j][i][1]) * float(L[j][1][1])
                            break

                balls_recovered_per_game = balls_recovered_per_game / total_played

                possession_won = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Possession won':
                            possession_won = possession_won + float(L[j][i][1]) * float(L[j][1][1])
                            break

                possession_won = possession_won / total_played

                tackle_per_game = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Tackles per game':
                            tackle_per_game = tackle_per_game + float(L[j][i][1]) * float(L[j][1][1])
                            break

                tackle_per_game = tackle_per_game / total_played

                interception = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Interceptions per game':
                            interception = interception + float(L[j][i][1]) * float(L[j][1][1])
                            break

                interception = interception / total_played

                clean_sheet = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Clean sheets':
                            clean_sheet = clean_sheet + float(L[j][i][1])
                            break

                clean_sheet = clean_sheet

                pourcentage_passes = 0
                for j in range(a):
                    for i in range(len(L[j])):
                        if L[j][i][0] == 'Accurate per game':
                            pourcentage_passes = pourcentage_passes + float(L[j][i][1][-4:-2]) * float(L[j][1][1])
                            print(float(L[j][i][1][-4:-2]))
                            print(pourcentage_passes)
                            break

                pourcentage_passes = pourcentage_passes / total_played

                saves = 0.0
                goals_conceded = 0.0

                list_player = []

                list_player.append(player_name_sofascore)
                list_player.append(player_name)
                list_player.append(player_team)
                list_player.append(player_position)
                list_player.append(player_market_value)
                list_player.append(round(average_rating, 2))
                list_player.append(total_played)
                list_player.append(round(started_percentage, 2))
                list_player.append(round(minute_per_game, 2))
                list_player.append(round(goals_scored_per_game, 2))
                list_player.append(round(assist_per_game, 2))
                list_player.append(round(dribble_per_game, 2))
                list_player.append(round(pourcentage_passes, 2))
                list_player.append(round(balls_recovered_per_game, 2))
                list_player.append(round(possession_won, 2))
                list_player.append(round(tackle_per_game, 2))
                list_player.append(round(interception, 2))
                list_player.append(round(clean_sheet, 2))
                list_player.append(saves)
                list_player.append(goals_conceded)

                list_players.append(list_player)

    if player_position == 'G':

        clean_sheet = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Clean sheets':
                    clean_sheet = clean_sheet + float(L[j][i][1])
                    break

        clean_sheet = clean_sheet

        goals_conceded = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Goals conceded per game':
                    goals_conceded = goals_conceded + float(L[j][i][1]) * float(L[j][1][1])
                    break

        goals_conceded = goals_conceded / total_played

        saves = 0
        for j in range(a):
            for i in range(len(L[j])):
                if L[j][i][0] == 'Saves per game':
                    saves = saves + float(L[j][i][1][:3]) * float(L[j][1][1])
                    break

        saves = saves / total_played

        goals_scored_per_game = 0.0
        assist_per_game = 0.0
        dribble_per_game = 0.0
        balls_recovered_per_game = 0.0
        possession_won = 0.0
        tackle_per_game = 0.0
        interception = 0.0
        pourcentage_passes = 0.0


        list_player = []

        list_player.append(player_name_sofascore)
        list_player.append(player_name)
        list_player.append(player_team)
        list_player.append(player_position)
        list_player.append(player_market_value)
        list_player.append(round(average_rating, 2))
        list_player.append(total_played)
        list_player.append(round(started_percentage, 2))
        list_player.append(round(minute_per_game, 2))
        list_player.append(goals_scored_per_game)
        list_player.append(assist_per_game)
        list_player.append(dribble_per_game)
        list_player.append(pourcentage_passes)
        list_player.append(balls_recovered_per_game)
        list_player.append(possession_won)
        list_player.append(tackle_per_game)
        list_player.append(interception)
        list_player.append(round(clean_sheet, 2))
        list_player.append(round(saves, 2))
        list_player.append(round(goals_conceded, 2))

        list_players.append(list_player)

    list_p = [list_player]

    data_frame_player = pd.DataFrame(list_p)

    data_frame_player.to_csv('morocco_player_statistique_caf_2023.csv',mode='a',header=False)