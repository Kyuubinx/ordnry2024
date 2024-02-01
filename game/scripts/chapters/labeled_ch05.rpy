label c5s0:
    
    centered "Chapter 5 - Soul"
    play music "audio/bgm/soul.wav"

    if persistent.turn_on_secev_c5 == True:
        call ch05_secev_mike

label c5s1:

    show matt_a at center:
        zoom 0.184
        ypos 1.0
    with dissolve

    mr "So… There really isn't much to do in here."

    hide matt_a
    show matt_b at center:
        zoom 0.184
        ypos 1.0

    mr "It stopped raining, why don't you come to the mall with me to kill some time?"

    hide matt_b
    with dissolve

    "You agree and you both start walking."

    show matt_b at center:
        zoom 0.184
        ypos 1.0
    with dissolve

    mr "This parking lot kinda reminds me of my motorbike."
    mr "I still have it, but lately, I have only been driving the car, so I can carry the guitar and the rest of the things…"

    hide matt_b
    show matt_c at center:
        zoom 0.184
        ypos 1.0

    mr "Yeah, kind of a silly thing, feelings for machines, right?"

    menu:
        mr "If I invited you out, would you like to hang out with me and the band tonight?"
        "Yes":
            mr "Good."

        "No":
            
            hide matt_c
            show matt_e at center:
                zoom 0.184
                ypos 1.0

            mr "Oh..."
            mr "Okay..."

            hide matt_e
            with dissolve

            jump c5s5

    menu:
        mr "So, wanna go to the mall now?"
        "Go to the mall":
            hide matt_c
            with dissolve
            jump c5s3

        "Stay at the studio":
            hide matt_c
            with dissolve
            jump c5s6

label c5s2:
    
    show matt_c at left:
        zoom 0.184
        ypos 1.0
    with dissolve
    
    mr "Oh, hey, you're back, [mcname]."
    
    show nigel_c at right:
        zoom 0.182
        ypos 1.0
    with dissolve
    
    nw "Hey."

    hide matt_c
    show matt_b at left:
        zoom 0.184
        ypos 1.0

    mr "Yeah, as you can see, Nigel is back too…"
    mr "So… There really isn't much to do in here."

    hide matt_b
    show matt_c at left:
        zoom 0.184
        ypos 1.0

    mr "It stopped raining, why don't you come to the mall with me to kill some time?"
    nw "Nice."
    
    hide matt_c
    with dissolve

    hide nigel_c
    with dissolve
    
    "You agree and start walking with them."
    
    show matt_b at left:
        zoom 0.184
        ypos 1.0
    with dissolve
    
    mr "This parking lot kinda reminds me of my motorbike."
    
    show nigel_b at right:
        zoom 0.172
        ypos 1.0
    with dissolve
    
    nw "Heh… That's the memory you have?"

    hide matt_b
    show matt_c at left:
        zoom 0.184
        ypos 1.0

    mr "Well, yeah…"

    hide nigel_b
    show nigel_g at right:
        zoom 0.172
        ypos 1.0

    nw "Kinda virgin coming from you."

    hide matt_c
    show matt_d at left:
        zoom 0.172
        ypos 1.0

    mr "Fuck you."

    hide matt_d
    with dissolve

    hide nigel_g
    with dissolve

    $ chance33 = [0,0,1]

    $ chanceevent_c5_1 = renpy.random.choice(chance33)

    if chanceevent_c5_1 == 1:

        call ch05_mika_rng

    jump c5s7

label c5s3:

    "You both decide to enter the mall."
    
    show matt_b at center:
        ypos 1.0
        zoom 0.184
    
    mr "I miss the time when there was a gamer store in here."
    mr "It would be nice if they came back."

    hide matt_b

    $ chance33 = [0,0,1]

    $ chanceevent_c5_2 = renpy.random.choice(chance33)

    if chanceevent_c5_2 == 1:

        call ch05_oli_rng
    
    else:

        $ ch05_matt_talkevent = False
        $ ch05_matt_talkevent_ques1 = False
        $ ch05_matt_talkevent_ques2 = False
        $ ch05_matt_talkevent_ques3 = False
        $ ch05_matt_talkevent_ques_x = 0

        while ch05_matt_talkevent == False && ch05_matt_talkevent_ques_x < 3:

            show matt_b at center:
                ypos 1.0
                zoom 0.184

            menu:
                "So, do you like motorbikes?" if ch05_matt_talkevent_ques1 == False:

                    hide matt_b
                    show matt_c at center:
                        ypos 1.0
                        zoom 0.184

                    mr "Love them."

                    hide matt_c
                    show matt_b at center:
                        ypos 1.0
                        zoom 0.184

                    mr "It's not like I dislike cars, though."
                    mr "I also have a Chevy Impala 1970's."

                    hide matt_b

                    $ ch05_matt_talkevent_ques_x += 1
                    $ ch05_matt_talkevent_ques1 = True
                    
                "Are you a gamer?" if ch05_matt_talkevent_ques2 == False:

                    mr "Not much, really, but I love horror games."

                    hide matt_b

                    $ ch05_matt_talkevent_ques_x += 1
                    $ ch05_matt_talkevent_ques2 = True

                "How do you feel about yourself?" if ch05_matt_talkevent_ques3 == False:

                    hide matt_b
                    show matt_e at center:
                        ypos 1.0
                        zoom 0.184
                    
                    mr "Phew!"
                    mr "Dude, that's the hell of a complicated question right now..."

                    hide matt_e
                    show matt_a at center:
                        ypos 1.0
                        zoom 0.184

                    mr "Okay, let's see..."
                    mr "I mean, the theory is good, right?"
                    mr "And most of it is really good..."

                    hide matt_a
                    show matt_b at center:
                        ypos 1.0
                        zoom 0.184

                    mr "I'm an artist, I can express myself so well, but..."

                    hide matt_b
                    show matt_e at center:
                        ypos 1.0
                        zoom 0.184

                    mr "It's kinda hard sometimes."
                    mr "I know I'm not any kind of celebrity."
                    mr "But sometimes I feel like I understand some of their problems..."
                    mr "Like... If... Hypothetically, you started dating a fan..."
                    mr "How can you be so sure that person loves you for who you are and isn't just obsessed, or just admired?"
                    mr "It's hard..."

                    hide matt_e

                    $ ch05_matt_talkevent_ques_x += 1
                    $ ch05_matt_talkevent_ques3 = True

                "Stop talking":

                    $ ch05_matt_talkevent = True

    jump c5s7

label c5s4:

    "You all enter the mall."
    
    show nigel_a at left:
        zoom 0.172
        ypos 1.0
    with dissolve
    
    nw "Yo, weird paranoia."
    
    show matt_b at right:
        zoom 0.184
        ypos 1.0
    with dissolve
    
    mr "Go on."

    hide nigel_a
    show nigel_e at left:
        zoom 0.172
        ypos 1.0

    nw "Imagine if a bunch of creeps suddenly form another band in Rainer High."
    
    hide matt_b
    show matt_a at right:
        zoom 0.184
        ypos 1.0
    
    mr "Wouldn't be the end of the world."
    mr "But yeah, we're number one for a reason."
    mr "We're literally the only one."
    nw "Gotta be ready for that, though."
    nw "We're probably inspiring the hell out of some people."
    
    hide matt_a
    show matt_d at right:
        zoom 0.184
        ypos 1.0

    mr "Then we'll just need to improve, right?"
    mr "It'll be fun."

    hide matt_d
    with dissolve

    hide nigel_e
    with dissolve

    $ nigel_mall = True

    jump c5s6

label c5s5:

    scene bg02:
        zoom 2.0
    with fade

    "Time passes, and in the end, you don't go to Kane's party."
    "You're home alone now."

    pause 3

    "Your cellphone rings."

    nw "[mcname]."
    nw "We got a huge problem."

    pause 3

    nw "Apparently, some freak made a trap on the street."
    nw "Basically, Matt's car crashed, and he almost got kidnaped."
    nw "He made it to the hospital, but he was stabbed."
    nw "He's pretty bad."
    nw "Just wanted to let you know..."

    "Wrong Ending 2/2:\n\"Matt's Car Crash\""

    $ renpy.full_restart()

label c5s6:

    if nigel_mall:

        show nigel_a at left:
            zoom 0.172
            ypos 1.0
        with dissolve
        
        nw "Hey, I got something to show you at my home."
        "Matt's cellphone begins to ring."

        show matt_a at right:
            zoom 0.184
            ypos 1.0
        with dissolve

        mr "Sis."
        jr "Need you to do a piercing."
        jr "Can you come over?"
        mr "Fine."
        "Matt hung up."
        mr "Okay… Let me just finish this."
        
        hide nigel_a
        show nigel_g at legt:
            zoom 0.172
            ypos 1.0
        
        nw "Right."
        "You all get back in the studio and go upstairs."
        #scene changes

        hide nigel_g 
        with dissolve

        hide matt_a
        with dissolve

    show emily_a at center:
        zoom 0.17
        ypos 1.0
    with with dissolve

    "After some seconds, Emily went up the stairs."

    show matt_d at right:
        zoom 0.184
        ypos 1.0
    with dissolve

    mr "Oh, it's you."
    
    show janis_a at left:
        zoom 0.154
        ypos 1.0
    with dissolve
    
    jr "Industrial on the left ear, get your hands clean."

    hide matt_d
    show matt_g at right:
        zoom 0.184
        ypos 1.0

    mr "On my way."

    hide matt_g
    show matt_a at right:
        zoom 0.184
        ypos 1.0

    mr "So, what did you tattoo?"
    
    hide emily_a
    show emily_c at center:
        zoom 0.17
        ypos 1.0
    
    es "Here, take a look."
    
    hide janis_a
    with dissolve

    hide emily_c
    with dissolve

    hide matt_a
    with dissolve

    #gallery image
    
    "Emily shows her wrist, now tattooed with the word \"Karma\"."
    
    show matt_d at right:
        zoom 0.184
        ypos 1.0
    with dissolve
    
    mr "It fits you."
    mr "I like that, it's a nice tattoo."
    
    show janis_b at left:
        zoom 0.154
        ypos 1.0
    with dissolve
    
    jr "Of course."
    jr "I did it."

    hide janis_b
    with dissolve

    show emily_b at left:
        zoom 0.17
        ypos 1.0
    with dissolve

    "Emily layed down and started getting ready for the piercing."
    
    hide matt_d
    show matt_a at right:
        zoom 0.184
        ypos 1.0
    
    mr "Won't lie, it'll hurt a bit."

    hide matt_a
    show matt_b at right:
        zoom 0.184
        ypos 1.0

    mr "But I promise to make it fast."

    hide emily_b
    show emily_e at left:
        zoom 0.17
        ypos 1.0

    es "Okay…"
    mr "Trust me?"
    es "I guess so…"

    hide matt_b
    with dissolve

    hide emily_e
    with dissolve

    "In less than a minute, Matt's job was done."

    $ chance33 = [0,0,1]

    $ chanceevent_c5_3 = renpy.random.choice(chance33)

    if chanceevent_c5_3 == 1:

        call ch05_lane_rng

label c5s7:

    #gallery image

    kr "Boys and girls from Rainer High…"
    kr "I know, it's monday, but…"
    kr "Who cares, right?"
    kr "I'm doing a party at my home, you are all invited."
    kr "Missing Halloween will be there playing!!"
    sm "Dude, did you at least ask them to pl-"
    "The video ended."

    pause 3

    show matt_a at right:
        zoom 0.184
        ypos 1.0
    with dissolve

    mr "Yeah, he didn't."
    
    if nigel_mall:
    
        show nigel_g at left:
            zoom 0.172
            ypos 1.0
        with dissolve

        nw "I just hope we get paid."
        mr "Oh, do you?"

label c5s8:

    "You all arrived at Nigel's building."
    "When the elevator opens, you both see Mike and Taylor hugging each other."
    "Matt and Nigel had the same exact reaction."
    both "I'll take the stairs."
    "So you three take the stairs for 10 floors."

label c5s9:

    nw "Fuck."
    nw "I'm done with stairs."
    "Nigel threw himself on the ground, still not opening the door for the 10th floor."
    mr "Remember when we used to skip class here?"
    nw "We used to spend hours here… Throwing our shit at the world…"
    mr "You threw your shit at the world."
    mr "I threw my shit at Gwen."
    mr "You used to lay your head on my lap."
    mr "Wanna do it again?"
    nw "Nope."
    nw "Stop being cute."
    nw "We gotta go fast, not to find Mike again."

label c5s10:

    "Matt and Nigel finally got into the apartment, where Nigel guided you two to his bedroom."
    nw "You know…"
    nw "Bonnie gave me something…"
    nw "I was thinking about using it…"
    mr "Oh, yeah?"
    mr "What is it?"
    "Nigel took down a blanket in the middle of the room, revealing an empty canvas."
    mr "A canvas? You're gonna paint something?"
    nw "Not \"something\"."
    nw "You."
    mr "How romantic."
    nw "There's literally no romance in this."
    mr "If you say so…"
    nw "Well, truth is…"
    nw "Tina always says you got a Dorian Gray complex."
    nw "Her words have been kinda echoing in my head lately."
    mr "So you decided to paint The Picture of Matt Raven?"
    nw "Exactly."
    nw "And you do have the two only things that matter for dumb and reckless teenagers."
    nw "Youth and beauty."
    mr "Fabulous."
    mr "Are you gonna ask if I'd sell my soul to the painting, now?" 
    nw "Would you?"
    mr "Yes. Without thinking twice."
    nw "What a filthy soul then, Mister Raven."
    nw "What about you, [mcname]?"
    
    #($)
    
    "As time passes, Nigel slowly creates a perfect portrait."
    "He took a photo of Matt, to use as a reference when the boy couldn't be with him."
    "But it was already time to get ready for the party."
    "Nigel would use the same clothes, even after taking a bath, just to show his tattoo."
    "His eyeliner was now forming hearts around his eyes."
    mr "Can I borrow your eyeliner?"
    "Matt was wearing a leather jacket and a fishnet shirt."
    nw "Sure."
    nw "Come here. I'll make that spikey one that you like."

label c5s11:

    mr "So… You're coming to the party, right?"
    mr "Nice."
    mr "I can take you there."
    mr "Come on, I want to show you my motorbike."
    "You went with Matt to the party in his motorbike."

    if soul:
        
        $ chance33 = [0,0,1]

        $ chanceevent_c5_5 = renpy.random.choice(chance33)

        if chanceevent_c5_5:

            call ch05_bonnie_rng

label c5s12:

    "Matt gave you his helmet and only wore his glasses."
    mr "Feeling okay over there?"
    mr "That's good."
    mr "Yo, there's some weird people ahead."
    mr "I'll go fast, hold on to me."
    "As you held on, you couldn't see the faces of the people, but felt they were dangerous."
    "Finally, you two arrive at Kane's house."

label c5s13:

    "You chose not to go to the party, and started receiving a lot of videos."
    "Suddenly, you start to feel bad for not being there."
    "Should you have gone?"
    "Wrong Ending 1/2:\n\"Party Missed\""

label c5s14:

    "You notice Kane had a giant saloon."
    kr "Well, well."
    kr "The two biggest rockstars in Rainer High..."
    mr "Yo."
    nw "Just for you to know, this is gonna be expensive."
    kr "Don't worry, I got you the instruments."
    kr "My dad has some nice contacts and money to his bones."
    kr "You can play whenever you're up to."
    nw "Double neck, huh?"
    nw "Never played one before."
    nw "Seems like a nice challenge."
    bm "You're not the only one."
    nw "Bon."
    bm "Six stringed bass."
    bm "Nice."
    kr "Are you really ok to play?"
    kr "I mean, you can say no..."
    tm "Where's my fucking keytar?"
    kr "Okay... Only Oli left."
    mn "I got one of those earlier."
    kr "What?"
    mn "An Oli."
    os "Yo."
    kr "Nice."
    kr "Stage's yours."
    "Time for the second show to start."

label c5s15:

    "As you walk outside, you see Dominic."
    "You notice someone is walking towards him."
    dh "Oh, hi Heather."
    dh "Didn't expect to see you here so soon."
    dh "Oh shit."
    hs "What's wrong?"
    hs "And don't call me Heather."
    dh "Babe, your hair."
    hs "Oh, yeah, I cut it."
    dh "But... With no occasion or whatever?"
    hs "Do I need to have one?"
    hs "Look, it's blue inside."
    dh "You... Dyed it too..."
    
label c5s16:

    "An old car blasting rock 'n' roll was coming."
    kr "Weird."
    kr "I don't recognize that car."
    kr "Either someone bought a car, or it's someone I didn't invite."
    kr "By the way, you're [mcname], right?"
    "The car stopped, making some tire noises."
    "Faye came out of the passenger seat, revealing the driver..."
    "Todd."
    kr "What's up with this guy?"
    kr "I hope he just brought Faye here and then he's gonna disappear."
    
    #(menu, tell him he's bonnie's brother)
    
    "Todd entered the saloon and walked towards Scott, who was smoking some weed."
    sm "Yo, old man."
    sm "Party's highschool only."
    sm "Get lost."
    to "Scotty, huh?"
    to "Listen, we can do this the easy way..."
    to "Which is..."
    to "You simply let me stay here..."
    to "Or..."
    to "We can do it MY way..."
    to "Which means..."
    to "I'll break each one of your faces..."
    "He took the weed to himself."
    to "And report good old Mary Jane here."
    "He unlit the joint in Scott's jacket."
    sm "Yo, this guy's nearly challenging me to a duel..."
    fr "Yeah, my boyfriend."
    fr "There's not much else to expect..."
    kr "This is gonna be so fucked up..."

label c5s17:

    mr "Okay… Let's make some fucking noise…"

    centered "CHAPTER CLEAR!!"

