label c1s0:

    stop music

    scene bg02:
        zoom 2.0
    with fade

    play music "audio/bgm/ordinary.wav"

    centered "Chapter 1 - \"Ordinary\""

    #Here's where the chapter starts. When the game is played for the first time, this is the first point of effective gameplay.

    "It was a calm autumn morning, and you were leaving home and taking the metro to start your first day at Rainer High."

    scene bg01:
        zoom 0.4
    with dissolve

    "There's almost not a single person around, but the thing is still noisy."

    #Chance of 5% of a RNG event to happen

    python:
        chance5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    $ chanceevent1 = renpy.random.choice(chance5)

    if chanceevent1==1:

        call ch01_franz_rng
        jump c1s1

    #Same thing, this time 20% chance

    $ chance20 = [0, 0, 0, 0, 1]
    $ chanceevent2 = renpy.random.choice(chance20)

    if chanceevent2==1 and chanceevent1==0:

        call ch01_paige_rng
        jump c1s1

    stop music

    if chanceevent1 == 0 and chanceevent2 == 0:
            "You wait some minutes, observing the buildings of the city, which is completely new to you."
            "The metro stopped at the station that was close to Rainer High."
            jump c1s1

label c1s1:

    #Chapter 1 - Scene 1

    play music "audio/bgm/welcome_to_rainer_high.wav"

    scene bg03:
    with dissolve

    "Welcome to Rainer High, [mcname]."
    "Are you ready to start your highschool experience?"

    # "ttp" means "talked to paige"

    if ttp == True:
        show paige_d at center:
            ypos 1.0
            zoom 0.163
        with dissolve
        pt "We'll be great friends, [mcname]!!"
        hide paige_d
        with dissolve

    scene bg04
    with dissolve

    #These initial RNG events can't be triggered if another one was already triggered before.

    python:
        chance10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    $ chanceevent3 = renpy.random.choice(chance10)

    if chanceevent3==1 and chanceevent2 == 0 and chanceevent1 == 0:

        call ch01_amy_rng

    if chanceevent3 == 0 and ttp == 0:
        show matt_c at center:
            ypos 1.035
            zoom 0.184
        with dissolve

    if chanceevent3 == 1:
        show amy_b at left:
            ypos 1.0
            zoom 0.165
        with dissolve
        show matt_c at right:
            ypos 1.035
            zoom 0.184
        with dissolve

    if ttp == True:
        show paige_c at left:
            ypos 1.0
            zoom 0.163
        with dissolve
        show matt_a at right:
            ypos 1.035
            zoom 0.184
        with dissolve

    stop music

    play music "audio/bgm/matt_raven.wav"

    "As you walk to the classroom, you notice a pretty boy walking by."
    "He was wearing earphones, and you noticed he was also wearing makeup."

    if ttp == True:
            "The boy makes direct contact with you and Paige."
            hide matt_a
            show matt_e at right:
                ypos 1.035
                zoom 0.184
            "His look turns a bit sad when he sees Paige."
            "He fastly walked to his classroom, the 3rd grade one."
            hide paige_c
            with dissolve
            hide matt_e
            with dissolve

    elif chanceevent3 == 1:
        "The boy makes direct contact with you and Amy."
        "He seems more focused on Amy, though."
        unkm "Nice shoe."
        ak "T-Thanks..."
        "He fastly walked to his classroom, the 3rd grade one."
        hide amy_b
        with dissolve
        hide matt_c
        with dissolve


    else:
        "The boy makes direct eye contact with you."
        "He smiles."
        unkm "Welcome to Rainer High, newcomer."
        "He fastly walked to his classroom, the 3rd grade one."
        if chanceevent1 == 1:
            "It's the same classroom as Franz."
            hide matt_c
            with dissolve

    scene bg05:
    with dissolve

    stop music

    play music "audio/bgm/1st_grade.wav"

    #Entering the classroom

    if ttp == True:
        pt "Welcome to our classroom, cutie pie!!"
        pt "Oh, no... The two only free seats are kinda distant..."

    elif chanceevent3 == 1:
        ak "So... Is it here?"
        ak "Oh, there's two free seats, and they're side-to-side, what a great coincidence!"

    else:
        "You walk alone through a quiet corridor, until you find the door to the 1st grade classroom."
        "As you walk in, you walk straight to a single seat that attracts you the most."

    "As you sit, an unknown girl suddenly talks to you."
    show carol_c at left:
        ypos 1.0
        zoom 0.168
    with dissolve
    unkf "Good morning, person in pink. Or black. Or pink. Whatever, dark magenta."
    if chanceevent3==1:
        show amy_c at center:
            ypos 1.0
            zoom 0.165
        with dissolve
        unkf "Oh, and hi, second person in dark magenta."
        ak "Eh... Hi..."
    hide carol_c
    show carol_a at left:
        ypos 1.0
        zoom 0.168
    unkf "It's kinda curious that the only uniform rules in Rainer High are like..."
    hide carol_a
    show carol_b at left:
        ypos 1.0
        zoom 0.168
    unkf "Wear the school's black social shirt, and whatever you want to wear over it must be black or pink."
    hide carol_b
    show carol_c at left:
        ypos 1.0
        zoom 0.168
    unkf "I'm Caroline Rustman, by the way. You can call me Carol."
    show juliet_g at right:
        ypos 1.0
        zoom 0.156
    with dissolve
    if chanceevent3==1:
        unkf "Carol, you're alarming them."
    else:
        unkf "Carol, you're alarming [persistent.mcprn2]."
    hide carol_c
    show carol_e at left:
        ypos 1.0
        zoom 0.168
    cr "Stop being annoying!"
    unkf "Hello, my name is Juliet Sinkoon."
    hide juliet_g
    show juliet_b at right:
        ypos 1.0
        zoom 0.156
    js "I will protect you from the unreliable people in this class."
    if chanceevent3==1:
        ak "Amy Kingslay, nice to meet you."
    js "[mcname]? That's a pretty name..."
    hide juliet_b
    show juliet_c at right:
        ypos 1.0
        zoom 0.156
    cr "Could you stop ignoring me, Juliet?"
    hide juliet_c
    show juliet_a at right:
        ypos 1.0
        zoom 0.156
    js "I'm not ignoring you, I just don't think you're being like... normal."
    hide carol_g
    show carol_e at left:
        ypos 1.0
        zoom 0.168
    cr "This is me!! Isn't this the reason why I'm your best friend?"
    if chanceevent3==1:
        js "Yeah, but I can tell you made Amy and [mcname] unconfortable."
        cr "Amy... Did I made you unconfortable?"
        ak "A little bit..."
        js "See? And I'm pretty sure [mcname] will give you the same answer."
        cr "That's not true..."
        hide amy_c
        with dissolve
    menu:
        js "[mcname], did you feel unconfortable with Carol's attitude?"
        "Yes":
            $jsev1=True
            js "That's what I thought..."
            #Because of a logic error that would affect the code entirely, some variables are called "alternative resources".
            $alternative_resource1 = True
        "No":
            $crev1=True
            $alternative_resource2 = True
            hide carol_e
            show carol_c at left:
                ypos 1.0
                zoom 0.168
            cr "See?! It was perfectly fine!"
        "I'm gonna grab some water...":
            if chanceevent3==1:
                ak "I think I'm gonna go with you..."
            js "Oh... Sorry... Guess I'm the one who made you unconfortable..."
            cr "Sorry, [mcname]..."
            #Mina's alternative event
            hide juliet_a
            with dissolve

            if alternative_resource2 == True:
                hide carol_c
                with dissolve
            else:
                hide carol_e
                with dissolve

            # If Mina's event isn't triggered, the player is already on a bad ending route.

            stop music

            hide amy_c
            with dissolve
            scene bg04
            with dissolve
            "As you walk to the drinking fountain and take a plastic cup, you feel like you're being observed."
            menu:
                "Look back?"
                "Yes":
                    $ persistent.enckane1=True
                    $ lookback = True
                    show kane_b at center:
                        ypos 1.0
                        zoom 0.181
                    with dissolve
                    "You notice there was a boy looking at you, inside the 3rd grade's classroom, which's door is open."
                    "It's not the same boy you saw earlier, despite they share some things in common."
                    if chanceevent3 == 1:
                        show amy_b at left:
                            ypos 1.0
                            zoom 0.165
                        with dissolve
                        ak "I mean, he's kinda pretty..."
                "No":
                    "You decide not to look."

            play music "audio/bgm/are_you_ogay.wav"

            if lookback == True:
                misv "Got lost in someone's eyes?"
                hide kane_b
                with dissolve
                show mina_b at center:
                    ypos 1.0
                    zoom 0.175
                with dissolve
                if chanceevent3==1:
                    "A girl suddenly appears in front of you and Amy."
                    unkf "So, you two must be the newcomers from 1st grade."
                    ak "That's right. My name is Amy Kingslay, this is [mcname]."
                    hide mina_b
                    show mina_h at center:
                        ypos 1.0
                        zoom 0.175
                    unkf "You're both so beautiful..."
                    "Mina bites her lips."
                    if lookback==True:
                        hide mina_h
                        show mina_c at center:
                            ypos 1.0
                            zoom 0.175
                        unkf "So... who were you looking at?"
                        hide mina_c
                        show mina_g at center:
                            ypos 1.0
                            zoom 0.175
                        unkf "Eww... Kane Ravat? Ugh... He's... Gross. He'll play with your feelings and then throw you away. Just stop looking."
                        hide mina_g
                        show mina_c at center:
                            ypos 1.0
                            zoom 0.175
                        unkf "By the way, my name is Mina Jackish, I'm in 2nd grade. You can find me there whenever you want."
                    else:
                        hide mina_h
                        show mina_c at center:
                            ypos 1.0
                            zoom 0.175
                        unkf "My name is Mina Jackish, I'm in 2nd grade. You can find me there whenever you want."
                    hide mina_c
                    show mina_a at center:
                        ypos 1.0
                        zoom 0.175
                    mj "But, for now, I guess it might be a good idea to go back to class..."
                    hide amy_b
                    show amy_c at left:
                        ypos 1.0
                        zoom 0.175
                    ak "You're right. Nice to meet you, Mina!"
                    "Mina blinked."
                    hide amy_c
                    with dissolve
                    hide mina_a
                    with dissolve
                    
                else:
                    "A girl suddenly appears in front of you."
                    show mina_b at center:
                        ypos 1.0
                        zoom 0.175
                    with dissolve
                    unkf "Relax, I'm just messing around with you."
            else:
                "After filling half of the cup, a girl suddenly appears in front of you."
                show mina_b at center:
                    ypos 1.0
                    zoom 0.175
                with dissolve
                unkf "Well, hi there..."

            if chanceevent3==0:
                unkf "You're new here, right?"
                unkf "[mcname]... My name is Mina Jackish, I'm in 2nd grade."
                $persistent.encmina1=True
                hide mina_b
                show mina_h at center:
                    ypos 1.0
                    zoom 0.175
                mj "If you don't mind me saying, I think you're very pretty..."
                "She bites her lips."
                if lookback==True:
                    hide mina_h
                    show mina_c at center:
                        ypos 1.0
                        zoom 0.175
                    mj "So... who were you looking at?"
                    hide mina_c
                    show mina_g at center:
                        ypos 1.0
                        zoom 0.175
                    mj "Eww... Kane Ravat? Ugh... He's... Gross. He'll play with your feelings and then throw you away. Just stop looking."

            if chanceevent3==0:
                hide mina_g
                show mina_a at center:
                    ypos 1.0
                    zoom 0.175
                mj "Might be a good idea to go back to class right now..."
                mj "See you around, [mcname]..."
                "She blinked."
            $persistent.encmina1=True
            # "Boo" is the variable that represents that mina showed up.
            $ boo = True
            hide mina_a
            with dissolve

    if boo==False:
        if jsev1==True:
            if chanceevent3==True:
                hide amy_c
                with dissolve

            if alternative_resource2 == True:
                hide carol_c
                with dissolve
            else:
                hide carol_e
                with dissolve
            
            js "So, as I was saying, you must be careful with some people in this class..."

            # gallery image

            js "We can start with the blue-eyed rich girl in the front, Kaelyn Ravat."
            show kaelyn_a at left:
                ypos 1.0
                zoom 0.168
            with dissolve
            hide juliet_a
            show juliet_g at right:
                ypos 1.0
                zoom 0.156
            js "She's the most spoiled person you'll see here."
            hide juliet_g
            show juliet_a at right:
                ypos 1.0
                zoom 0.156
            hide kaelyn_a
            with dissolve
            js "And the boy to her right..."
            show jackson_a at left:
                ypos 1.0
                zoom 0.178
            with dissolve
            js "That is Jackson Nyrock."
            hide juliet_a
            show juliet_g at right:
                ypos 1.0
                zoom 0.156
            js "He's kind of a failed replica of Matt Raven from 3rd grade."
            js "Stay away from him too."
            hide jackson_a
            with dissolve
            show carol_c at left:
                ypos 1.0
                zoom 0.168
            with dissolve
            cr "Ooh... Looks like someone still holds a grudge, huh?"
            js "Carol... Shut up..."
            if chanceevent3==True:
                show amy_a at center:
                    ypos 1.0
                    zoom 0.165
                with dissolve
                ak "What about him?"
                js "We... Had a... Thing..."
                hide carol_c
                show carol_a at left:
                    ypos 1.0
                    zoom 0.168
                cr "A very thing thing..."
                js "Don't make it such a big deal... It was casual... He was the one who got attached."
                hide carol_a
                show carol_d at left:
                    ypos 1.0
                    zoom 0.168
                cr "What did you expect? You'd treat him like a puppy!!"
                hide juliet_g
                show juliet_e at right:
                    ypos 1.0
                    zoom 0.156
                js "It's not like that..."
                ak "What about Matt Raven? You've mentioned him before..."
                $persistent.mentmatt1=True
                hide carol_d
                show carol_a at left:
                    ypos 1.0
                    zoom 0.168
                cr "Oh, the story gets worst."
                ak "Why would you say that?"
                hide juliet_e
                show juliet_g at right:
                    ypos 1.0
                    zoom 0.156
                js "Carol, if you open your mouth, I'll break that pretty face of yours."
                "Carol smiled in despair, and kept her mouth shut."
                ak "Okay... I guess..."

            else:
                menu:
                    "Ask about Jackson":
                        hide juliet_g
                        show juliet_a at right:
                            ypos 1.0
                            zoom 0.156
                        js "So... You wanna know, [mcname]?"
                        cr "Hehe..."
                        js "Fine..."
                        js "We... Had a... Thing..."
                        hide carol_c
                        show carol_a at left:
                            ypos 1.0
                            zoom 0.168
                        cr "A very thing thing..."
                        hide juliet_a
                        show juliet_g at right:
                            ypos 1.0
                            zoom 0.156
                        js "Don't make it such a big deal... It was casual... He was the one who got attached."
                        hide carol_a
                        show carol_d at left:
                            ypos 1.0
                            zoom 0.168
                        cr "What did you expect? You'd treat him like a puppy!!"
                        hide juliet_g
                        show juliet_e at right:
                            ypos 1.0
                            zoom 0.156
                        js "It's not like that..."
                        hide carol_d
                        show carol_a at left:
                            ypos 1.0
                            zoom 0.168
                        
                        hide juliet_e
                        show juliet_a at right:
                            ypos 1.0
                            zoom 0.156
                        while infoev1==False:
                            menu:
                                "Matt Raven?":
                                    cr "Oh, the story gets worst."
                                    hide juliet_e
                                    show juliet_g at right:
                                        ypos 1.0
                                        zoom 0.156
                                    js "Carol, if you open your mouth, I'll break that pretty face of yours."
                                    "Carol smiled in despair, and kept her mouth shut."
                                    $persistent.mentmatt1=True
                                    hide juliet_g
                                    show juliet_a at right:
                                        ypos 1.0
                                        zoom 0.156
                                "Paige Tyshe?" if ttp==true:
                                    hide juliet_e
                                    show juliet_a at right:
                                        ypos 1.0
                                        zoom 0.156
                                    js "Paige is... Cute, I guess..."
                                    js "I don't know her super well, but... She seems nice."
                                    hide carol_a
                                    show carol_c at left:
                                        ypos 1.0
                                        zoom 0.168
                                    cr "She is."
                                    hide carol_c
                                    show carol_a at left:
                                        ypos 1.0
                                        zoom 0.168
                                    
                                "Franz Momsen?" if chanceevent1 == 1:
                                        hide juliet_a
                                        show juliet_e at right:
                                            ypos 1.0
                                            zoom 0.156
                                        js "Well... He kinda scares me a bit."
                                        hide carol_a
                                        show carol_e at left:
                                            ypos 1.0
                                            zoom 0.168
                                        cr "That's rude, he's just a quiet boy."
                                        js "Maybe... Never actually talked to him."
                                        hide carol_e
                                        show carol_a at left:
                                            ypos 1.0
                                            zoom 0.168
                                        hide juliet_e
                                        show juliet_a at right:
                                            ypos 1.0
                                            zoom 0.156

                                "End conversation":
                                    $infoev1=True
                                    "You decide to end the conversation."

                    "Better not to insist":
                        "You decide to end the conversation."
                hide juliet_a
                with dissolve
                hide carol_a
                with dissolve
                if chanceevent3==1:
                    hide amy_a
                    with dissolve
                "As the teacher walks in, all the students sit on their respective places, and the class starts."
                jump c1s3

        if crev1==True:
            hide juliet_a
            with dissolve
            show dell_b at center:
                ypos 1.0
                zoom 0.174
            with dissolve
            "Another girl suddenly aproaches you."
            unkf "Another new face in here?"
            hide carol_c
            show carol_d at left:
                ypos 1.0
                zoom 0.168
            cr "Dell!! You're back!!"
            hide dell_b
            show dell_c at center:
                ypos 1.0
                zoom 0.174
            unkf "Hi, Carol."
            hide carol_d
            show carol_c at left:
                ypos 1.0
                zoom 0.168
            cr "This is [mcname]."
            hide dell_c
            show dell_b at center:
                ypos 1.0
                zoom 0.174
            unkf "I see... Pleasured to meet you. My name is Delana."
            show celeste_a at right:
                ypos 1.0
                zoom 0.162
            with dissolve
            "Another girl appears right behind Delana."
            unkf "Please, don't ask her full name."
            hide dell_b
            show dell_a at center:
                ypos 1.0
                zoom 0.174
            dd "It's Delana Diem Cardinal von Cranenbroek."
            hide dell_a
            show dell_c at center:
                ypos 1.0
                zoom 0.174
            dd "Don't worry, you can call me Dell."
            hide dell_c
            show dell_b at center:
                ypos 1.0
                zoom 0.174
            dd "This is Celeste Heilsie."
            hide celeste_a
            show celeste_b at right:
                ypos 1.0
                zoom 0.162
            ch "Hi, [mcname]. I'm also a newcomer."
            hide dell_b
            show dell_a at center:
                ypos 1.0
                zoom 0.174
            dd "Besides I'm not new here, I've been away for two years now."
            hide carol_c
            with dissolve
            show nigel_b at left:
                ypos 1.0
                zoom 0.172
            with dissolve
            "Now, a boy appears, putting his arm around Dell's shoulders."
            hide nigel_b
            show nigel_c at left:
                ypos 1.0
                zoom 0.172
            unkm "And as you can see, she likes to entertain the juniors."
            hide dell_a
            show dell_c at center:
                ypos 1.0
                zoom 0.174
            dd "Hi, Nigel."
            hide nigel_c
            show nigel_b at left:
                ypos 1.0
                zoom 0.172
            unkm "[mcname], right? I'm Nigel Weekes. You'll probably hear my name a lot from now on."
            hide nigel_b
            show nigel_a at left:
                ypos 1.0
                zoom 0.172
            nw "Now, if you don't mind, I need to go to the cafeteria."
            hide dell_c
            show dell_e at center:
                ypos 1.0
                zoom 0.174
            dd "So soon?"
            hide nigel_a
            show nigel_c at left:
                ypos 1.0
                zoom 0.172
            nw "The more I'm out of the class, the better."
            hide dell_e
            show dell_c at center:
                ypos 1.0
                zoom 0.174
            dd "Reckless like always."
            hide nigel_c
            show nigel_b at left:
                ypos 1.0
                zoom 0.172
            nw "See you around, [mcname]."
            hide nigel_b
            with dissolve
            hide dell_c
            with dissolve
            hide celeste_b
            with dissolve
            "As the teacher walks in, all the students sit on their respective places, and the class starts."
            jump c1s3
    else:

        stop music

        play music "audio/bgm/be_a_rockstar.wav"

        scene bg05:
        with dissolve
        "You're back in the classroom."
        show nigel_a at center:
            ypos 1.0
            zoom 0.172
        with dissolve

        # gallery image

        "There is a boy at your chair."
        "You kindly ask him to leave, because that was the place you chose in the classroom."
        hide nigel_a
        show nigel_c at center:
            ypos 1.0
            zoom 0.172
        unkm "Nah, I'm too confortable to leave now."
        unkm "It's not my fault, I thought you went home."
        hide nigel_c
        show nigel_g at center:
            ypos 1.0
            zoom 0.172
        unkm "You should actually thank me. I did you a favor and didn't throw your things in trash."
        menu:
            "Stay quiet and avoid a fight":
                $ alternative_resource3 = True
                hide nigel_g
                with dissolve

            "Be rock 'n' roll and roll and put the boy in his place":
                hide nigel_g
                show nigel_c at center:
                    ypos 1.0
                    zoom 0.172
                "You act confident and strongly ask him to leave, with an angry face."
                show juliet_e at right:
                    ypos 1.0
                    zoom 0.156
                with dissolve
                js "[mcname]."
                "Juliet takes you by the hand and whispers in your ear."
                hide nigel_c
                with dissolve
                js "If I were you, I wouldn't fight Nigel right now."
                js "He can be a lot worse if he doesn't like you."
                hide juliet_e
                show juliet_a at right:
                    ypos 1.0
                    zoom 0.156
                js "It's just the beggining. At the second he gets used to have you around, he'll treat you nicely."
                hide juliet_a
                show juliet_e at right:
                    ypos 1.0
                    zoom 0.156
                js "I know it feels like shit, but please, just try, for now. I'll talk to him later."
                "And then, you decide to stop, with fire in your eyes."
                hide juliet_e
                with dissolve

        stop music

        "You went to the seat the boy was sitting before."
        show paige_c at right:
            ypos 1.0
            zoom 0.168
        with dissolve

        play music "audio/bgm/cutiepie.wav"

        if ttp==True:
            pt "And so, here we are again, cutie pie."
            hide paige_c
            show paige_a at right:
                ypos 1.0
                zoom 0.168
            pt "Thanks, if I spent more time with Nigel, I'd freak out."
            hide paige_a
            show paige_e at right:
                ypos 1.0
                zoom 0.168
            pt "It's not like I'm transphobic or something like that, but DUDE! He's SO annoying!!"
            hide paige_e
            show paige_a at right:
                ypos 1.0
                zoom 0.168
            pt "Oh, so you didn't notice."
            pt "Nigel's a transgender."
            hide paige_a
            show paige_b at right:
                ypos 1.0
                zoom 0.168
            pt "He's kinda cute, though."
            hide paige_b
            show paige_c at right:
                ypos 1.0
                zoom 0.168
        else:
            hide paige_c
            show paige_a at right:
                ypos 1.0
                zoom 0.168
            unkf "Thanks, if I spent more time with Nigel, I'd freak out."
            hide paige_a
            show paige_e at right:
                ypos 1.0
                zoom 0.168
            unkf "It's not like I'm transphobic or something like that, but DUDE! He's SO annoying!!"
            hide paige_e
            show paige_a at right:
                ypos 1.0
                zoom 0.168
            unkf "Oh, so you didn't notice."
            unkf "Nigel's a transgender."
            hide paige_a
            show paige_b at right:
                ypos 1.0
                zoom 0.168
            unkf "He's kinda cute, though."
            hide paige_b
            show paige_c at right:
                ypos 1.0
                zoom 0.168
            unkf "Pleasured to meet you, cutie pie. My name is Paige Tyshe."
        hide paige_c
        with dissolve
        "You noticed Juliet and Carol whispering something you couldn't hear, until you could actually hear Nigel saying something."
        nw "Oh no..."
        js "What?"
        nw "Ugh... The fucking eraser trick."
        menu:
            "Before you could even notice, the boy sitting by your left side left his eraser fall to the ground."
            "Pick the eraser up":
                show jackson_c at center:
                    ypos 1.0
                    zoom 0.178
                with dissolve

                $ jnev1 = True

                # gallery image

                "The boy followed your lead to the ground, and looked at you, making direct eye contact."
            "Let the boy pick it up":
                show jackson_h at center:
                    yalign 1.0
                    zoom 0.178
                with dissolve

                $ jnev1 = False

        play music "audio/bgm/childhood_friends.wav"

        unkm "Oh, you're the newcomer."
        unkm "I'm Jackson Nyrock. Nice to meet you."
        if jnev1 != True:
            hide jackson_h
        else:
            hide jackson_c
        show jackson_b at center:
            ypos 1.0
            zoom 0.178
        jn "[mcname]... Your name is so beautiful... Just like the stars..."
        "He began to sing 'Yellow', by Coldplay."
        show kaelyn_a at left:
            ypos 1.0
            zoom 0.168
        with dissolve
        unkf "You're out of tune."
        hide jackson_b
        show jackson_g at center:
            ypos 1.0
            zoom 0.178
        jn "Shut up."
        jn "It's just because I lowed my voice."
        jn "And I'm not even singing for you!!"
        hide kaelyn_a
        show kaelyn_c at left:
            ypos 1.0
            zoom 0.168
        unkf "Actually, it's because you know this is a cheap trick and you can't sing."
        hide kaelyn_c
        show kaelyn_b at left:
            ypos 1.0
            zoom 0.168
        menu:
            unkf "So, [mcname]. My name is Kaelyn Ravat. Don't listen to this jerk."
            "Agree with Kaelyn and make fun of Jackson's trick":
                "You told Jackson Kaelyn was right and that was a cheap trick."
                "He made a disgusted face, looking at Kaelyn."
                "The girl blinked and showed her tongue."
            "Tell Kaelyn to calm down and listen to Jackson":
                jn "Seems like I won this time."
        ka "Don't mind us. We're best friends since elementary school."
        hide jackson_g
        with dissolve
        "Another girl suddenly aproaches you."
        show dell_a at center:
            ypos 1.0
            zoom 0.174
        with dissolve
        unkf "Another new face in here?"
        ka "This is [mcname]."
        unkf "I see... Pleasured to meet you. My name is Delana."
        show celeste_a at right:
            ypos 1.0
            zoom 0.162
        with dissolve
        "Another girl appears right behind Delana."
        unkf "Please, don't ask her full name."
        hide dell_b
        show dell_a at center:
            ypos 1.0
            zoom 0.174
        dd "It's Delana Diem Cardinal von Cranenbroek."
        hide dell_a
        show dell_c at center:
            ypos 1.0
            zoom 0.174
        dd "Don't worry, you can call me Dell."
        hide dell_c
        show dell_b at center:
            ypos 1.0
            zoom 0.174
        dd "This is Celeste Heilsie."
        hide celeste_a
        show celeste_b at right:
            ypos 1.0
            zoom 0.162
        ch "Hi, [mcname]. I'm also a newcomer."
        hide dell_b
        show dell_a at center:
            ypos 1.0
            zoom 0.174
        dd "Besides I'm not new here, I've been away for two years now."
        hide kaelyn_b
        with dissolve
        show nigel_b at left:
            yalign 1.0
            zoom 0.172
        with dissolve
        "Suddenly, Nigel appears, putting his arm around Dell's shoulders."
        hide nigel_b
        show nigel_c at left:
            ypos 1.0
            zoom 0.172
        nw "And as you can see, she likes to entertain the juniors."
        hide dell_a
        show dell_c at center:
            ypos 1.0
            zoom 0.174
        dd "Hi, Nigel."
        hide nigel_c
        show nigel_b at left:
            ypos 1.0
            zoom 0.172
        nw "[mcname], right? I like your attitude. Seems like I didn't introduce myself properly. I'm Nigel Weekes. You'll probably hear my name a lot from now on."
        hide nigel_b
        show nigel_a at left:
            ypos 1.0
            zoom 0.172
        nw "Now, if you don't mind, I need to go to the cafeteria."
        hide dell_c
        show dell_e at center:
            ypos 1.0
            zoom 0.174
        dd "So soon?"
        hide nigel_a
        show nigel_c at left:
            ypos 1.0
            zoom 0.172
        nw "The more I'm out of the class, the better."
        hide dell_e
        show dell_c at center:
            ypos 1.0
            zoom 0.174
        dd "Reckless like always."
        hide nigel_c
        show nigel_a at left:
            ypos 1.0
            zoom 0.172
        nw "See you around, [mcname]."
        hide nigel_a
        with dissolve
        dd "Actually, he's pretty fun."
        ch "He seems pretty fun."
        hide dell_c
        with dissolve
        hide celeste_b
        with dissolve
        "As the teacher walks in, all the students sit on their respective places, and the class starts."
        jump c1s3

label c1s3:

    stop music

    "The class didn't take so long to end, and now, it was time for the break."
    
    play music "audio/bgm/welcome_to_rainer_high.wav"
    
    if alternative_resource1==True:
        scene bg04
        with dissolve
        "You went out of your classroom, together with Juliet."

        # gallery image

        "As you look around the corridor, you saw the seniors walking by."
        "The boys walked in a stylish way and the girls were all awesomely pretty."
        if lookback==True:
            "Kane was walking next to Matt."
            "Unlike Matt, he seemed to be trying to desperately call any girl's attention."
        show tina_b at left:
            ypos 1.0
            zoom 0.165
        with dissolve
        show faye_b at right:
            ypos 1.0
            zoom 0.173
        with dissolve
        while infoev2==False:

            # gallery image

            menu:
                js "Can you guess which one of them is the student council's president?"
                "The girl to the left":
                    $ infoev2=True

                "The girl to the right":
                    $ mentfaye1 = True
                    js "Well, that is Faye."
                    js "Faye Ruby."
                    js "She's Matt's ex girlfriend."
                    js "They don't seem to talk much nowadays."
        hide faye_b
        with dissolve
        show juliet_b at right:
            ypos 1.0
            zoom 0.156
        with dissolve
        js "That's right."
        hide juliet_b
        show juliet_a at right:
            ypos 1.0
            zoom 0.156
        js "That is our president, Tina Mercury."
        hide juliet_a
        show juliet_a at right:
            ypos 1.0
            zoom 0.156
        js "You should go talk to her."
        "You decide to follow her outside of the school."
        hide juliet_a
        with dissolve
        hide tina_b
        with dissolve
        scene bg03:
        with dissolve
        show tina_c at center:
            ypos 1.0
            zoom 0.165
        with dissolve
        
        stop music

        tm "Oh, the new student."
        hide tina_c
        show tina_a at center:
            ypos 1.0
            zoom 0.165 
        tm "What are you doing alone, junior?"
        tm "You couldn't make friends on your first day?"
        
        play music "audio/bgm/president.wav"
        
        while infoev3==False:
            menu:
                "It's been kinda confusing and full of emotions...":
                    hide tina_a
                    show tina_e at center:
                        ypos 1.0
                        zoom 0.165
                    tm "Aww... Don't you worry, junior. Tina Mercury's here to make your day!!"
                    hide tina_e
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                "I like your makeup.":
                    hide tina_a
                    show tina_c at center:
                        ypos 1.0
                        zoom 0.165 
                    tm "Thank you... I did it myself. Wait some minutes and you'll understand why."
                    hide tina_c
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                "Faye Ruby?" if mentfaye1==True:
                    hide tina_a
                    show tina_b at center:
                        ypos 1.0
                        zoom 0.165
                    tm "You can say Faye and I are kinda close. She's pretty nice, actually."
                    hide tina_b
                    show tina_c at center:
                        ypos 1.0
                        zoom 0.165
                    tm "She can do lots of things, like skating and playing the drums."
                    hide tina_c
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                "Matt Raven?":
                    hide tina_a
                    show tina_h at center:
                        ypos 1.0
                        zoom 0.165
                    tm "Oh, that boy..."
                    hide tina_h
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                    tm "He's kinda complicated, but we're something like besties, even though he's more intimate with Nigel."
                    hide tina_a
                    show tina_c at center:
                        ypos 1.0
                        zoom 0.165
                    tm "You'll be impressed when you see him singing."
                    hide tina_c
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                "Are you Matt's girlfriend?":
                    $infoev3=True

        # gallery image
        hide tina_a
        show tina_g at center:
            ypos 1.0
            zoom 0.165

        stop music

        "Tina broke her happy face."
        tm "Ugh... I should've imagined."
        tm "Great. Another one in Matt's web."
        tm "Seriously, what the fuck makes him so special?"
        tm "What makes you believe you might be special to him, [mcname]?"
        tm "That's your name, right?"
        tm "Go ahead and try. He might even use you a bit."
        tm "Welcome to your highschool romantic comedy."
        tm "Or will it be a tragedy?"
        tm "Oh, I know."
        tm "Welcome to your highschool thunderstorm."
        tm "And what about Juliet?"
        tm "You got close to her, right?"
        tm "Was she a strategy?"
        tm "Are you trying to get close to me just so you can be close to Matt?"
        tm "Listen to me, [mcname]."
        tm "You better stay away from Matt."
        tm "You better stay away from me."
        tm "You better stay away from anyone related to us, if there's a single person who's not."
        tm "I can ruin your school life if I want to."
        hide tina_g
        with dissolve
        scene bg02:
            zoom 2.0
        with dissolve
        "Tina's speech scared you to death."
        "It scared you so much, you really got away from everyone."
        "It scared you so much, you really got away from the school."
        "Wrong Ending 1/3:\n\"Tina's Evil Side\""

        $ persistent.c1we1 = True

        $renpy.full_restart()

    if alternative_resource2 == True:
        "You're walking alone through the corridor and..."
        "You're alone."
        "Nobody likes you."
        "You're alone."
        "You made no friends."
        "You're alone."

        play music "audio/bgm/get_gwened.wav"

        "You're ridiculous."
        "You're alone."
        "What a shame."
        "You're alone."
        "You should leave."
        "You're alone."
        "Something's wrong."
        scene bg06:
            zoom 0.8
            xalign 0.6
        unktt "You don't seem to realize."
        unktt "You don't belong here."
        unktt "My name is Gwendolyn Foster."
        gf "If you choose to stay, I'll be sure make your life living hell."
        gf "If you make it, great."
        gf "Today, seems like you didn't."
        scene bg02:
            zoom 2.0
        with dissolve
        "Wrong Ending 2/3:\n\"Gwen.\""
        $ persistent.gwened = True
        $ persistent.c1we2 = True

        $ renpy.full_restart()

    else:
        scene bg04
        with dissolve
        "You went out of your classroom, together with Paige."

        # gallery image

        "As you look around the corridor, you saw the seniors walking by."
        "The boys walked in a stylish way and the girls were all awesomely pretty."
        if lookback==True:
            "Kane was walking next to Matt."
            "Unlike Matt, he seemed to be trying to desperately call any girl's attention."
        with dissolve
        show tina_b at left:
            ypos 1.0
            zoom 0.165
        with dissolve
        show faye_b at right:
            ypos 1.0
            zoom 0.173
        with dissolve
        while infoev2==False:

            # gallery image

            menu:
                pt "Can you guess which one of them is the student council's president?"
                "The girl to the left":
                    $ infoev2=True

                "The girl to the right":
                    $ mentfaye1 = True
                    pt "No, no, that is Faye."
                    pt "Faye Ruby."
                    pt "She's my skating teacher."
                    pt "Yeah, she got the job really soon."
        hide faye_b
        with dissolve
        show paige_c at right:
            ypos 1.0
            zoom 0.163
        with dissolve
        pt "Well done, cutie pie."
        hide paige_c
        show paige_b at right:
            ypos 1.0
            zoom 0.163
        pt "That is our president, Tina Mercury."
        hide paige_b
        show paige_a at right:
            ypos 1.0
            zoom 0.163
        pt "You should go talk to her."
        "You decide to follow her outside of the school."
        hide paige_a
        with dissolve
        hide tina_b
        with dissolve
        scene bg03:
        with dissolve
        show tina_c at center:
            ypos 1.0
            zoom 0.165
        with dissolve
        tm "Oh, the new student."
        hide tina_c

        stop music

        show tina_a at center:
            ypos 1.0
            zoom 0.165 
        tm "What are you doing alone, junior?"
        tm "You couldn't make friends on your first day?"
        
        play music "audio/bgm/president.wav"
        
        while infoev3==False:
            menu:
                "It's been kinda confusing and full of emotions...":
                    hide tina_a
                    show tina_e at center:
                        ypos 1.0
                        zoom 0.165
                    tm "Aww... Don't you worry, junior. Tina Mercury's here to make your day!!"
                    hide tina_e
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                "I like your makeup.":
                    hide tina_a
                    show tina_c at center:
                        ypos 1.0
                        zoom 0.165 
                    tm "Thank you... I did it myself. Wait some minutes and you'll understand why."
                    hide tina_c
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                "Faye Ruby?" if mentfaye1==True:
                    hide tina_a
                    show tina_b at center:
                        ypos 1.0
                        zoom 0.165
                    tm "You can say Faye and I are kinda close. She's pretty nice, actually."
                    hide tina_b
                    show tina_c at center:
                        ypos 1.0
                        zoom 0.165
                    tm "She can do lots of things, like skating and playing the drums."
                    hide tina_c
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                "Matt Raven?":
                    hide tina_a
                    show tina_h at center:
                        ypos 1.0
                        zoom 0.165
                    tm "Oh, that boy..."
                    hide tina_h
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                    tm "He's kinda complicated, but we're something like besties, even though he's more intimate with Nigel."
                    hide tina_a
                    show tina_c at center:
                        ypos 1.0
                        zoom 0.165
                    tm "You'll be impressed when you see him singing."
                    hide tina_c
                    show tina_a at center:
                        ypos 1.0
                        zoom 0.165
                "Are you Matt's girlfriend?":
                    $infoev3=True

        # gallery image
        
        hide tina_a
        show tina_g at center:
            ypos 1.0
            zoom 0.165

        stop music

        "Tina broke her happy face."
        tm "Ugh... I should've imagined."
        tm "Great. Another one in Matt's web."
        tm "Seriously, what the fuck makes him so special?"
        tm "What makes you believe you might be special to him, [mcname]?"
        tm "That's your name, right?"
        tm "Go ahead and try. He might even use you a bit."
        tm "Welcome to your highschool romantic comedy."
        tm "Or will it be a tragedy?"
        tm "Oh, I know."
        tm "Welcome to your highschool thunderstorm."
        hide tina_g
        with dissolve

        stop music

        show matt_c at center:
            ypos 1.0
            zoom 0.184
        with dissolve
        mr "Relax, Tina kinda makes a fuss when it's about me."
        hide matt_c

        play music "audio/bgm/matt_raven.wav"

        show matt_a at center:
            ypos 1.0
            zoom 0.184
        mr "Gotta go now, sorry."
        hide matt_a
        show matt_b at center:
            ypos 1.0
            zoom 0.184
        mr "It was a pleasure to meet you, [mcname]."
        hide matt_b
        with dissolve
        "A random girl approaches you."
        show emily_a at center:
            ypos 1.0
            zoom 0.17
        with dissolve
        unkf "Yeah, it's about time for you to find out why everyone's obsessed with Matt."
        hide emily_a
        show emily_b at center:
            ypos 1.0
            zoom 0.17
        unkf "[mcname], right? My name is Emily Stamey, from 2nd grade."
        hide emily_b
        with dissolve
        "Matt was at a stage, adjusting the volume of some amplifiers."
        "He suddenly went close to a microphone."
        show matt_c at center:
            ypos 1.0
            zoom 0.184
        with dissolve

        # gallery image

        mr "Did you miss us?"
        "The crowd went crazy, specially the girls."
        show tina_c at right:
            ypos 1.0
            zoom 0.165
        with dissolve
        tm "Well, I would like to wish you a very good school year, full of new experiences."
        tm "If you need anything, you know I'm here."
        tm "But you know formality doesn't last too much in this school, right?"
        "Matt was now holding a guitar."
        mr "We're Missing Halloween, and this song is called \"happy valentine's death\"!!"
        if alternative_resource3 == True:
            show nigel_g at left:
                ypos 1.0
                zoom 0.172
            with dissolve

            # gallery image

            stop music

            nw "Hold up!!"
            "Nigel was also holding a guitar and speaking through a microphone."
            nw "Just wanted a moment to talk about a specific newcomer, [mcname]."
            hide matt_c
            show matt_e at center:
                ypos 1.0
                zoom 0.184
            mr "Oh, there you go again..."
            hide nigel_g
            show nigel_b at left:
                ypos 1.0
                zoom 0.172
            nw "So, I stole [mcprn3] place in the classroom, just to tease."
            nw "And guess what."
            nw "[mcprn1] surrendered. Without a single word."
            hide nigel_b
            show nigel_g at left:
                ypos 1.0
                zoom 0.172
            nw "No attitude makes people what?"
            "\"ORDINARY!!\", the crowd screamed."
            nw "And does this school has any place for ordinary people?!"
            "\"NO!!\", they screamed repeatedly."
            nw "Get outta here, [mcname]."
            hide nigel_g
            with dissolve
            hide matt_e
            with dissolve
            hide tina_c
            with dissolve
            scene bg02:
                zoom 2.0
            with dissolve
            "Nigel's speech and the crowd's reaction ashamed you to death."
            "It ashamed you you so much, you got away from everyone."
            "It ashamed you so much, you got away from the school."
            "Wrong Ending 3/3:\n\"Ordinary\""
            $ persistent.c1we3 = True

            $ renpy.full_restart()

        stop music

        "The show was only beginning."

        scene bg02:
            zoom 2.0
        with fade

        play music "audio/bgm/happy_valentines_death.wav"

        centered "CHAPTER CLEAR!!"
        $ persistent.unlockch2 = True
        $ persistent.c1te = True

        $ path = "2"

        stop music

        call chapter_skip
