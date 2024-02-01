init python:
    if persistent.definitions != None:
        mcname = persistent.name
        mcprn1 = persistent.prn1
        mcprn2 = persistent.prn2
        mcprn3 = persistent.prn3
        mcprn4 = persistent.prn4
        mcprn5 = persistent.prn5
        mcprn6 = persistent.prn6

label start:

    stop music

    menu:
        "Would you like to start a new game?"
        "Yes":
            play music "audio/bgm/be_yourself.wav"
            jump intro
        "No":
            play music "audio/bgm/playlist_shuffler.wav"
            jump selector

label selector:

    menu:
        "Please, select your chapter."
        "Chapter 1":
            if persistent.definitions == True:
                jump c1s0
            else:
                centered "You need to pass through the intro first."
                $ renpy.full_restart()
        "Chapter 2":
            if persistent.unlockch2 == True:
                jump c2s0
            else:
                centered "You haven't unlocked this chapter yet."
                $ renpy.full_restart()
        "Chapter 3":
            if persistent.unlockch3 == True:
                jump c3s0
            else:
                centered "You haven't unlocked this chapter yet."
                $ renpy.full_restart()
        "Chapter 4":
            if persistent.unlockch4 == True:
                jump c4s0
            else:
                centered "You haven't unlocked this chapter yet."
                $ renpy.full_restart()
        "Chapter 5":
            if persistent.unlockch5 == True:
                jump c5s0
            else:
                centered "You haven't unlocked this chapter yet."
                $ renpy.full_restart()
        "Next Page":
            jump selector
        "Check Endings":
            "You have done [counter] of the 19 possible endings in this game."
            jump selector

label intro:

    "Welcome, player."
    "This game is a visual novel."
    "You will pass through many story events which will request you to make a choice."
    "Each one of your choices will impact in the progress of your game, and in the ending you will get."
    "Know that there are also some events that has a certain chance of happening or not."
    "We hope you enjoy this journey of love, sex and rock and roll."
    "This is where it starts."
    "You're 15 years old, and you were transfered to Rainer High, where you'll spend your whole highschooler life."

    if persistent.definitions == None:
        jump intro_2
    else:
        "It seems like you've played this game before."
        menu:
            "Would you like to change your name and pronouns?"
            "Yes":
                jump intro_2
            "No":
                $ mcname = persistent.name
                jump c1s0

label intro_2:


    if persistent.gwennamed == True:
        if persistent.gwencounter < 5:
            $ renpy.input("Tell me, what's your name?")
            "Error."
            $ persistent.gwencounter += 1
            $ renpy.full_restart()
        else:
            gf "So you want to change it this much, huh?"
            gf "Alright, I'll let you do it."
            gf "[persistent.name]."
            gf "Have fun, asshole."

    python:
        mcname = renpy.input("Tell me... What's your name?")
    if mcname == "":
        "Please, input your name, and after that, press Enter or Space."
        while mcname == "":
            python:
                mcname = renpy.input("Tell me... What's your name?")
    $ persistent.name = mcname

    call anti_name_repeat

label intro_3:

    menu:
        "What are your pronouns?"
        "He/him":
            python:
                persistent.prn1 = "he"
                mcprn1 = "he"
                persistent.prn2 = "him"
                mcprn2 = "him"
                persistent.prn3 = "his"
                mcprn3 = "his"
                persistent.prn4 = "is"
                mcprn4 = "is"
                persistent.prn5 = "guy"
                mcprn5 = "guy"
                persistent.prn6 = "sir"
                mcprn6 = "sir"
        "She/her":
            python:
                persistent.prn1 = "she"
                mcprn1 = "she"
                persistent.prn2 = "her"
                mcprn2 = "her"
                persistent.prn3 = "her"
                mcprn3 = "her"
                persistent.prn4 = "is"
                mcprn4 = "is"
                persistent.prn5 = "girl"
                mcprn5 = "girl"
                persistent.prn6 = "miss"
                mcprn6 = "miss"
        "They/them":
            python:
                persistent.prn1 = "they"
                mcprn1 = "they"
                persistent.prn2 = "them"
                mcprn2 = "them"
                persistent.prn3 = "their"
                mcprn3 = "their"
                persistent.prn4 = "are"
                mcprn4 = "are"
                persistent.prn5 = "kid"
                mcprn5 = "kid"
                persistent.prn6 = "kid"
                mcprn6 = "kid"

    "Very well, [mcname]. Let's get it started!"

    $ persistent.definitions = True
    
    call first_play

    jump c1s0
