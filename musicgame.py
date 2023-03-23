# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:40:37 2023

@author: blues
"""

# Python code to search .mp3 files in current
# folder (We can change file type/name and path
# according to the requirements.
import os
import vlc
import random

kevin_songs=0
dan_songs=0
chris_songs=0
george_songs=0
connor_songs=0
maxkev=0
maxdan=0
maxchris=0
maxgeorge=0
maxconnor=0
rounds=1
repeats=[]
songlist=os.listdir("C:\Video\MUSICQUIZ")
songlist.sort()
for i in range(0,len(songlist)):
    ele=songlist[i]
    if("Kevin" in ele):
        maxkev=maxkev+1
    if("Danny" in ele):
        maxdan=maxdan+1
    if("Chris" in ele):
        maxchris=maxchris+1
    if("George" in ele):
        maxgeorge=maxgeorge+1
    if("Connor" in ele):
        maxconnor=maxconnor+1
playerlist=[]


# Define a function to display the quiz questions and get the player's answer
def ask_question(question):
    print(question)
    answer = input("Enter your answer: ")


        
# Define a function to play a single round of the quiz game
def play_round(players):
    global kevin_songs
    global dan_songs
    global chris_songs
    global george_songs
    global connor_songs
    global maxkev
    global maxdan
    global maxchris
    global maxgeorge
    global maxconnor
    global rounds
    global songlist
    global playerlist
    global num_rounds
    global typegame
    
    weigh=[]
    for i in range(0,len(playerlist)):
        ele=playerlist[i]
        if("Kevin" in ele):
            weigh.append(["kevin_songs",kevin_songs])
        if("Danny" in ele):
            weigh.append(["dan_songs",dan_songs])
        if("Chris" in ele):
            weigh.append(["chris_songs",chris_songs])
        if("George" in ele):
            weigh.append(["george_songs",george_songs])
        if("Connor" in ele):
            weigh.append(["connor_songs",connor_songs])
            
    names=["Kevin","Danny","Chris","George","Connor"]
    weigh.sort(key=lambda l:l[1])
    
    value=weigh[0][0]
    if(value == "kevin_songs"):
        song=names[0]
        if(kevin_songs>=maxkev):
            kevin_songs=0
            for i in list(repeats):
                if(song in i):
                    repeats.remove(i)
    elif(value == "dan_songs"):
        song=names[1]
        if(dan_songs>=maxdan):
            dan_songs=0
            for i in list(repeats):
                if(song in i):
                    repeats.remove(i)
    elif(value == "chris_songs"):
        song=names[2]
        if(chris_songs>=maxchris):
            chris_songs=0
            for i in list(repeats):
                if(song in i):
                    repeats.remove(i)
    elif(value == "george_songs"):
        song=names[3]
        if(george_songs>=maxgeorge):
            george_songs=0
            for i in list(repeats):
                if(song in i):
                    repeats.remove(i)
    else:
        song=names[4]
        if(connor_songs>=maxconnor):
            connor_songs=0
            for i in list(repeats):
                if(song in i):
                    repeats.remove(i)
    root="C:\Video\MUSICQUIZ"
    pick=random.choice(os.listdir("C:\Video\MUSICQUIZ"))
    if(len(repeats)!=0):
        repeats.sort()
        if(repeats==songlist):
            repeats.clear()
            
    while(song not in pick or pick in repeats):
        pick=random.choice(os.listdir("C:\Video\MUSICQUIZ"))
    if(pick not in repeats):
        repeats.append(pick)
    path=root+'/'+pick
    # creating vlc media player object
    media_player = vlc.MediaPlayer()
     
    # media object
    media = vlc.Media(path)
    media.add_option('start-time=0.0')
    media.add_option('run-time=10.0')
    # setting media to the media player
    media_player.set_media(media)
                 
    # setting video scale
    media_player.video_set_scale(0.6)
                 
                
    # setting volume
    media_player.audio_set_volume(50) 
    # start playing video
    media_player.play()
    
    
    print("Round "+str(rounds))
    question = "What song is this?"
    correct_answer = pick

    # Ask the question to all players
    for player in players:
        print(f"{player['name']}: {player['score']}")
        answer = ask_question(question)
    
    print("The correct answer was "+correct_answer)
    if("Kevin" in correct_answer):
        kevin_songs=kevin_songs+1
    if("Danny" in correct_answer):
        dan_songs=dan_songs+1
    if("Chris" in correct_answer):
        chris_songs=chris_songs+1
    if("George" in correct_answer):
        george_songs=george_songs+1
    if("Connor" in correct_answer):
        connor_songs=connor_songs+1
    # Display the scores for each player
    print("\nCurrent Scores:")
    rounds=rounds+1
    for player in players:
        print(f"{player['name']}: {player['score']}")

# Define a function to let the user add or subtract points for each player
def adjust_score(players):
    for i, player in enumerate(players):
        print(f"\n{i+1}. {player['name']}: {player['score']}")
        choice = input("Do you want to adjust this player's score? (y/n) ")
        if choice == "y":
            adjustment = int(input("Enter the amount to adjust the score by: "))
            player["score"] += adjustment

# Define a function to play the game
def play_game():
    # Ask the user whether they want to play singleplayer or multiplayer
    num_players = int(input("How many players? (1-5) "))
    for i in range(0,num_players):
        ele = input("Enter player library: ")
        playerlist.append(ele)
    num_rounds=int(input("How many rounds?"))
    if num_players == 1:
        name1=input("What is your name, Player 1? ")
        players = [{"name": name1, "score": 0}]
    elif num_players==2:
        name1=input("What is your name, Player 1? ")
        name2=input("What is your name, Player 2? ")
        players = [{"name": name1, "score": 0}, {"name": name2, "score": 0}]
    elif num_players ==3:
        name1=input("What is your name, Player 1? ")
        name2=input("What is your name, Player 2? ")
        name3=input("What is your name, Player 3? ")
        players = [{"name": name1, "score": 0}, {"name": name2, "score": 0}, {"name": name3, "score": 0}]
    elif num_players==4:
        name1=input("What is your name, Player 1? ")
        name2=input("What is your name, Player 2? ")
        name3=input("What is your name, Player 3? ")
        name4=input("What is your name, Player 4? ")
        players = [{"name": name1, "score": 0}, {"name": name2, "score": 0}, {"name": name3, "score": 0}, {"name": name4, "score": 0}]
    else:
        name1=input("What is your name, Player 1? ")
        name2=input("What is your name, Player 2? ")
        name3=input("What is your name, Player 3? ")
        name4=input("What is your name, Player 4? ")
        name5=input("What is your name, Player 5? ")
        players = [{"name": name1, "score": 0}, {"name": name2, "score": 0}, {"name": name3, "score": 0}, {"name": name4, "score": 0}, {"name": name5, "score": 0}]

    

    # Play rounds of the quiz game until the user decides to quit
    while True:
        play_round(players)
        # Allow the user to adjust the scores if playing in multiplayer mode
        if num_players > 1:
            adjust_score(players)
        if rounds>num_rounds:
            print("Thanks for playing!")
            print("\nFinal Scores:")
            for player in players:
                print(f"{player['name']}: {player['score']}")
            break
        choice = input("\nDo you want to play again? (y/n) ")
        if choice == "n":
            break
        

   

# Start the game
play_game()










         

