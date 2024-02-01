label c4s0:

    stop music

    scene bg02:
        zoom 2.0
    with fade

    play music "audio/bgm/kitten.wav"

    centered "Chapter 4 - \"Kitten\""

    jump c4s1

label c4s1:

    stop music

    play music "audio/bgm/rain.wav"

    "It was a cold and monotonous end of the morning."
    "Juliet could really take a walk with Matt and use the umbrella."
    "You start following them."

    show matt_c at right:
        ypos 1.0
        zoom 0.184
    with dissolve
    
    mr "It's the start of the week, why are you going to your dad's house?"

    show juliet_b at left:
        ypos 1.0
        zoom 0.156
    with dissolve

    js "Actually, I was supposed to go to my mother's house, but I guess they won't mind and it should be easier for you."
    js "At worst, I'll take an umbrella from my dad's house and walk to my mom's."

    hide matt_c
    show matt_d at right:
        ypos 1.0
        zoom 0.184

    mr "That's Nice of you."
    js "So, where were you?"

    hide matt_d
    show matt_a at right:
        ypos 1.0
        zoom 0.184

    mr "I... Kinda saw a forgotten face showing up again after a while."

    hide juliet_b
    show juliet_a at left:
        ypos 1.0
        zoom 0.156

    js "Would you mind telling me who it was?"

    hide matt_a
    show matt_b at right:
        ypos 1.0
        zoom 0.184

    mr "Lindsey Pawns."

    hide juliet_a
    show juliet_e at left:
        ypos 1.0
        zoom 0.156

    js "Your first girlfriend?"
    mr "Yeah. It has been a long while since the last time we talked."
    mr "She stayed silent for more than a year."

    hide juliet_e
    show juliet_g at left:
        ypos 1.0
        zoom 0.156

    js "So what exactly have you done?"
    mr "Well, we were hanging around and... Ended up on her house."

    python:
        chance5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    $ chanceevent10 = renpy.random.choice(chance5)

    if chanceevent10 > 0:
        jump ch04_umbrella_rng

    stop music

    js "In her bedroom?"
    
    hide matt_b
    show matt_c at right:
        ypos 1.0
        zoom 0.184

    mr "Yep. Door locked."
    
    play music "audio/bgm/lovers_metal.wav"
    
    js "Will you ever listen to me?"

    hide matt_c
    show matt_a at right:
        ypos 1.0
        zoom 0.184
    
    mr "Wha-?"
    js "Come on, Matt."
    js "This isn't the first time we talk about this."
    js "You know you don't ever give yourself time so you can just breathe!"
    js "You just find another \"Somebody To Love\" again and again to lay your head on their shoulder..."
    js "While you haven't even got over the last \"Love Of My Life\" you had!"
    js "When the fuck will you wake up?!"
    js "I just think..."
    "Juliet's shutted her mouth as soon as she noticed Matt putting the umbrella on her hands and leaving."
    "You could see Matt whispering in her ear."
    
    hide matt_a
    show matt_g at right:
        ypos 1.0
        zoom 0.184

    stop music

    mr "I don't belong to you. Don't act like you know me better than I do."

    hide matt
    with dissolve
    
    "Matt left as the rain kept falling in his hair."

    hide juliet_g
    show juliet_e at left:
        ypos 1.0
        zoom 0.156

    js "Shit. I did that again."

    menu:
        "Matt is already far, and Juliet didn't move."
        "Talk to her":
            jump c4s2
        "Avoid her":
            hide juliet_e
            with dissolve
            jump c4s3

label c4s2:

    play music "audio/bgm/vulture.wav"

    js "Oh, [mcname]! How long have you been there? Did you hear anything?"

    menu:
        "You feel some tension."
        "Tell her the truth":
            pass
        "Lie":
            pass

    js "Heh... Of course you heard it."

    hide juliet_e
    show juliet_f at left:
        ypos 1.0
        zoom 0.156

    js "And yeah... I'm a mess."
    js "A total mess."
    js "Please, keep going."
    js "Not in the mood to talk about it."
    js "You can just go after Matt."
    
    hide juliet_f
    with dissolve
    
    "She left."

    jump c4s3

label c4s3:

    play music "audio/bgm/matt_raven.wav"

    "You keep walking, and eventually end up going towards Matt's direction."
    
    show matt_a at center:
        ypos 1.0
        zoom 0.184
    with dissolve
    show over_wet at center:
        ypos 1.0
        zoom 0.184
    
    "And there he is, all wet"
    
    hide matt_a
    show matt_b at center:
        ypos 1.0
        zoom 0.184
    
    mr "Oh, [mcname]."
    mr "You probably heard it all, right?"
    
    hide matt_b
    show matt_c at center:
        ypos 1.0
        zoom 0.184
    
    mr "You didn't bring an umbrella, huh?"
    
    hide matt_c
    show matt_a at center:
        ypos 1.0
        zoom 0.184
    
    mr "Well, sorry, but I guess you already noticed I left mine with Juliet…"
    
    hide matt_a
    show matt_e at center:
        ypos 1.0
        zoom 0.184

    stop music
    
    mr "Me and Juliet have a dark past, you know?"
    
    play music "audio/bgm/better_than_i_do.wav"
    
    mr "We had some pretty nice memories, it would be wrong to say I didn't like it."
    mr "I was in love with… All the small things."
    mr "But at some point, it felt kinda toxic."
    mr "It was a rainy day, and we were having a fight over the phone."
    mr "Sometimes, I…"
    mr "Remember it, when it rains."
    
    hide matt_e
    show matt_b at center:
        ypos 1.0
        zoom 0.184
    
    mr "Anyways, we're almost there."
    
    hide matt_b
    show matt_c at center:
        ypos 1.0
        zoom 0.184
    
    mr "Oh, right, I didn't even say where we were going."
    
    hide matt_c
    show matt_d at center:
        ypos 1.0
        zoom 0.184
    
    mr "I'll introduce you to my sister."

    jump c4s5

label c4s4:

    stop music

    play music "audio/bgm/raven_tattoo_studio.wav"

    "You keep walking and eventually lose sight of them two."
    "You almost get lost, because it's raining and you don't know this town."
    "Suddenly, you see some flashing lights coming from a big sign."
    "It says \"Raven Tattoo Studio\"."
    "Is Matt a tattoo artist?"
    "You see a girl coming through the door."

    show janis_a at center:
        ypos 1.0
        zoom 0.154
    with dissolve

    unkf "May I help you, [mcprn6]?"
    
    hide janis_a
    show janis_b at center:
        ypos 1.0
        zoom 0.154
    
    unkf "Oh, you got lost, huh?"
    
    hide janis_b
    show janic_c at center:
        ypos 1.0
        zoom 0.154
    
    unkf "No worries, are you a Rainer High student?"
    
    hide janis_c
    show janis_d at center:
        ypos 1.0
        zoom 0.154
    
    unkf "I see. My name is Janis."

    hide janis_d
    show janis_c at center:
        ypos 1.0
        zoom 0.154
    jr "You can stay here for a while, maybe you'll find someone you know."
    jr "Come in, I'll get you a towel."

    hide janis_c
    with dissolve

    $ nomatt = True

    jump c4s6

label c4s5:

    stop music

    play music "audio/bgm/raven_tattoo_studio.wav"

    hide matt_d
    show matt_b at center:
        ypos 1.0
        zoom 0.184

    "You keep following Matt until you see some flashing lights coming from a sign."
    "It says \"Raven Tattoo Studio\"."
    
    show raelyn_b at left:
        ypos 1.0
        zoom 0.169
    with dissolve

    show janis_c at right:
        ypos 1.0
        zoom 0.154
    with dissolve
    
    unkf "See ya, Raelyn! I can already see you doing the second one!"

    hide raelyn_b
    with dissolve

    "The other girl leaves, waving goodbye."

    hide matt_b
    show matt_d at center:
        ypos 1.0
        zoom 0.184

    mr "[mcname], this is my sister, Janis."

    hide janis_c
    show janis_h at right:
        ypos 1.0
        zoom 0.154

    jr "Matt?! Why the hell are you so wet?!"

    hide matt_d
    show matt_e at center:
        ypos 1.0
        zoom 0.184

    mr "I was nice to someone who pissed me off."
    
    hide janis_h
    show janis_g at right:
        ypos 1.0
        zoom 0.154
    
    jr "Yeah… You never seem to show your anger the right way."
    
    hide matt_e
    show matt_b at center:
        ypos 1.0
        zoom 0.184
    
    mr "By the way, this is [mcname]."

    hide janis_g
    show janis_b at right:
        ypos 1.0
        zoom 0.154

    jr "Oh, hi. Didn't see you there. Janis Raven."
    jr "Come in, I'll get you two a towel."
    
    hide janis_b
    with dissolve
    
    "She came back after some seconds and got closer to you, to dry your hair."
    
    show janis_g at right:
        ypos 1.0
        zoom 0.154
    with dissolve
    
    jr "Matt, you should really be a nice guy now and give [mcname] some of your clothes."
    
    hide matt_b
    show matt_g at center:
        ypos 1.0
        zoom 0.154
    hide over_wet
    with dissolve
    
    mr "Fine, fine. I'd do that anyway."

    hide matt_g
    with dissolve

    hide janis_g
    with dissolve

    stop music

    play music "audio/bgm/old_violin.wav"

    #gallery image    

    "When she got closer to Matt, you noticed she was around 30 cm shorter than him."

    mr "So, who was the girl?"
    jr "Raelyn Kingslay."
    jr "Parents are funny."
    jr "She's almost twenty five and got her first tattoo today."
    mr "How much drama?"
    jr "Not as much as your friend, Caroline."
    mr "Carol? Well, she tattooed all the phases of the moon in her chest."
    mr "I guess I'd be dramatic as well."
    jr "Liar."
    jr "Whenever I tattoo you, it feels like I'm tattooing a rock."
    jr "You're almost uncapable of feeling pain."
    mr "That's not true."
    mr "I just don't show the pain I'm feeling on the outside."

    show matt_a at right:
        ypos 1.0
        zoom 0.184
    with dissolve

    show janis_a at left:
        ypos 1.0
        zoom 0.154
    with dissolve

    jr "Anyways, you might see some familiar faces today. Be ready."

    jump c4s6

label c4s6:    

    hide janis_a
    with dissolve

    "You suddenly see a familiar face in the studio."

    if nomatt == true:
        show matt_a at right:
            ypos 1.0
            zoom 0.184
        with dissolve

    stop music

    play music "audio/bgm/painful.wav"

    show emily_a at center:
        ypos 1.0
        zoom 0.17
    with dissolve

    es "Yeah, I thought about it because of the studio's name."
    es "You're… Matt Raven, right?"
    mr "I… Am?"

    hide emily_a
    show emily_b at center:
        ypos 1.0
        zoom 0.17

    es "Emily Stamey."

    show kate_b at left:
        ypos 1.0
        zoom 0.174
    with dissolve

    stop music

    unkf "Matt, it's been a while."
    
    hide matt_a
    show matt_g at right:
        ypos 1.0
        zoom 0.184

    play music "audio/bgm/generic_sex_song.wav"
    
    mr "Fuck."
    mr "[mcname], this is Kate Lynn."
    
    hide kate_b
    show kate_c at left:
        ypos 1.0
        zoom 0.174
    
    kl "When will you ask me to hang out with you again, huh?"
    mr "Hang… Out... Ugh…"
    kl "I just came to retouch the last tattoo."

    hide matt_g
    show matt_a at center:
        ypos 1.0
        zoom 0.184

    "Matt looked relieved for some reason."
    mr "Well, you should at least get a new one if you want that to happen again, you know?"
    "Matt took the coffee jar."
    mr "Janis, what happened to the energy drinks?"
    jr "You drank'em all."
    mr "Oh."
    
    hide kate_c
    show kate_d at left:
        ypos 1.0
        zoom 0.174
    
    kl "Come on, honey!"
    kl "I'm so into you…"
    mr "Nope. Had enough."

    hide matt_a
    with dissolve

    hide kate_d
    show kate_a at left:
        ypos 1.0
        zoom 0.174

    hide emily_b
    show emily_c at center:
        ypos 1.0
        zoom 0.17

    "Emily giggled."
    
    menu:
        "What will [mcname] do?"
        "Stick with Matt":
            jump c4s8
        "Leave him alone":
            jump c4s7

label c4s7:

    stop music

    play music "audio/bgm/raven_tattoo_studio.wav"
   
    $ katepts = 0

    $ emilyapology = False

    $ talkevent2 = False

    $ switched_once = False

    "You stay downstairs, surrounded by the girls."
    
    while talkevent2 == False:
        if switched_once == True:
            stop music

            play music "audio/bgm/raven_tattoo_studio.wav"

            $ switched_once = True
        
        menu:
            "Will you talk to someone?"
            
            "Talk to Kate" if katepts < 2:

                stop music

                play music "audio/bgm/generic_goth_chick.wav"
            
                if emilyapology == False:
                    hide emily_c
                    with dissolve

                if katepts < 1:
                
                    hide kate_a
                    show kate_b at left:
                        ypos 1.0
                        zoom 0.174
                    
                    kl "So, also interested in Matt?"
                    
                    
                    hide kate_b
                    show kate_g at left:
                        ypos 1.0
                        zoom 0.174
                    
                    kl "Know that I won't let you win."
                    
                    hide kate_g
                    show kate_a at left:
                        ypos 1.0
                        zoom 0.174
                    
                    $ katepts += 1

                    if emilyapology == False:
                        show emily_c at center:
                            ypos 1.0
                            zoom 0.17
                        with dissolve
            
                else:

                    if emilyapology == False:
                        hide emily_c
                        with dissolve
                
                    hide kate_a
                    show kate_g at left:
                        ypos 1.0
                        zoom 0.174
                    
                    kl "Well, you must be confused, right?"
                    
                    hide kate_g
                    show kate_b at left:
                        ypos 1.0
                        zoom 0.174
                    
                    kl "Let's say Matt and I had some spicy fun in the past."
                    
                    hide kate_b
                    show kate_g at left:
                        ypos 1.0
                        zoom 0.174
                    
                    kl "Now be gone, I don't like you."
                    
                    $ katepts += 1

                    hide kate_b
                    with dissolve

                    if emilyapology == False:
                        show emily_c at center:
                            ypos 1.0
                            zoom 0.17
                        with dissolve
            
            
            "Talk to Emily" if emilyapology == False:

                stop music

                play music "audio/bgm/shame.wav"
                
                if katepts < 2:
                    hide kate_a
                    with dissolve

                hide emily_c
                show emily_g at center:
                    ypos 1.0
                    zoom 0.17

                es "Oh, you again."
                es "Still pretending you care about Lindsey?"

                menu:
                    "Apology?"
                    
                    "Yes":
                        es "Hmm..."
                        es "Ok, I guess I can accept your apologies."
                        es "But don't fuck things up with Lindsey, understand?"

                        hide emily_g
                        with dissolve

                        $ emilyapology = True

                    "No":

                        jump c4s9

                if katepts < 2:
                    show kate_a at left:
                        ypos 1.0
                        zoom 0.174
                    with dissolve

            "Go upstairs":

                if katepts < 2:
                    hide kate_a
                    with dissolve

                if emilyapology == False:
                    hide emily_c
                    with dissolve

                $ talkevent2 = True
                
    jump c4s8

label c4s8:

    stop music

    "Someone was coming down the stairs of the studio."

    play music "audio/bgm/ruby_hair.wav"

    show nigel_b_a at right:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Wow, you literally dismissed a girl, Matt Raven."
    "Matt choked with the coffee."
    
    show matt_c at left:
        ypos 1.0
        zoom 0.184
    with dissolve
    
    mr "Dude, did you really just get all this well-dressed just to get a new tattoo?"
    
    hide nigel_b_a
    show nigel_c_a at right:
        ypos 1.0
        zoom 0.172
    
    nw "Yep."

    hide nigel_c_a
    show nigel_d_a at right:
        ypos 1.0
        zoom 0.172

    nw "Oh, hi, [mcname]."
    mr "You're… Marvelous."
    jr "So is the tattoo!"

    hide matt_c
    show matt_g at left:
        ypos 1.0
        zoom 0.184

    mr "Y-Yeah… So is the tattoo…"

    hide nigel_d_a
    show nigel_h_a at right:
        ypos 1.0
        zoom 0.172

    nw "Hehe… What's wrong, Matt? Did I take your breath away?"
    mr "Shut the fuck up."

    hide matt_g
    show matt_a at left:
        ypos 1.0
        zoom 0.184

    mr "Come on, let's go upstairs. I haven't had lunch yet."
    
    hide matt_a
    with dissolve

    hide nigel_h_a
    with dissolve
    
    "You three go upstairs."
    
    show nigel_b_a at right:
        ypos 1.0
        zoom 0.172
    with dissolve

    stop music

    play music "audio/bgm/be_a_rockstar.wav"
    
    nw "So, [mcname], are you here to get your first tattoo?"
    nw "I see."

    show matt_b at left:
        ypos 1.0
        zoom 0.184
    with dissolve

    mr "Well, you can start thinking about getting some piercings too."
    
    hide matt_b
    show matt_c at left:
        ypos 1.0
        zoom 0.184
    
    mr "Janis could do them for a friendly price, I promise."
    
    hide nigel_b_a
    show nigel_c_a at right:
        ypos 1.0
        zoom 0.172

    nw "So, are you into tattoos and piercings?"
    nw "Yeah, I can understand that."
    
    hide nigel_c_a
    show nigel_a_a at right:
        ypos 1.0
        zoom 0.172
    
    nw "So, Matt… What happened between you and the girl?"
    
    hide matt_c
    show matt_a at left:
        ypos 1.0
        zoom 0.184
    
    mr "Which one?"
    
    hide nigel_a_a
    show nigel_g_a at right:
        ypos 1.0
        zoom 0.172
    
    nw "Well, you really are the scum of the earth."
    
    hide matt_a
    show matt_g at left:
        ypos 1.0
        zoom 0.184
    
    mr "Sorry, it's a curse."
    
    hide matt_g
    show matt_a at left:
        ypos 1.0
        zoom 0.184
    
    mr "Actually, this was the very first time I ever talked to Emily."
    
    
    hide nigel_g_a
    show nigel_a_a at right:
        ypos 1.0
        zoom 0.172
    
    nw "I'm talking about the one retouching the tattoo."
    mr "Oh, Kate."
    mr "I thought you knew about her."
    
    hide nigel_a_a
    show nigel_g_a at right:
        ypos 1.0
        zoom 0.172
    
    nw "You have a big collection, buddy."
    mr "Yeah, she…"

    hide matt_a
    show matt_g at left:
        ypos 1.0
        zoom 0.184

    mr "She was a bad choice."
    nw "I'm used to it."
    mr "Yeah, now that I've put my head in place, I know exactly what she wants."
    nw "And what does she want?"
    mr "Status."

    hide matt_g
    show matt_a at left:
        ypos 1.0
        zoom 0.184

    mr "She doesn't seem to actually have any interest in me."
    nw "Yeah, I imagined."
    
    hide matt_a
    show matt_b at left:
        ypos 1.0
        zoom 0.184
    
    mr "Yo, is that guitar yours?"
    
    hide nigel_g_a
    show nigel_c_a at right:
        ypos 1.0
        zoom 0.172

    nw "Mike gave it to me."
    nw "Christmas gift."

    hide matt_a
    show matt_g at left:
        ypos 1.0
        zoom 0.184

    mr "Just in time."

    hide nigel_c_a
    show nigel_a_a at right:
        ypos 1.0
        zoom 0.172

    nw "Better late than never."

    hide matt_g
    show matt_a at left:
        ypos 1.0
        zoom 0.184

    mr "That's what they say."
    
    hide matt_a
    show matt_c at left:
        ypos 1.0
        zoom 0.184
    
    mr "Christmas, huh?"

    hide nigel_a_a
    show nigel_b_a at right:
        ypos 1.0
        zoom 0.172

    mr "This brings back some old memories…"

    jump c4s10

label c4s9:

    stop music
    
    play music "audio/bgm/eaten_alive.wav"

    es "Is that so?"
    es "So yeah, whatever."
    es "Game over for you, [mcname]."
    "She was leaving."

    show janis_h at right:
        ypos 1.0
        zoom 0.154
    with dissolve

    jr "Yo, you still have to pay for the tattoo!"
    es "Get out of my way!"
    jr "What?! The fucking tattoo, Emily!"
    jr "I don't have nothing to do with these things between you both!"
    
    hide emily_g
    with dissolve
    
    "BLAM!"
    "Emily broke the studio's glass door."
    jr "WHAT THE ACTUAL FUCK?!"

    
    "Wrong Ending 1/2:\n\"Studio Scandal\""

    $ persistent.c4we1 = True

    $ renpy.full_restart()

label c4s10:

    stop music

    play music "audio/bgm/missing_christmas.wav"

    hide nigel_b_a
    with dissolve

    hide matt_c
    with dissolve

    #gallery images switch

    #show
    nw "You wanna know, [mcname]?"
    mr "Yeah, I guess there's no big deal telling [mcprn4]."
    nw "True."
    nw "Last Christmas…"
    nw "Mom couldn't come to see me and Mike, she had some work to do."
    nw "Mike wouldn't care much about it, so I asked Matt if I could spend the night with them."
    #switch
    mr "Dad doesn't care much about his children, and mom is always busy with work…"
    mr "Just like Nigel's."
    mr "So, it has been me and Janis for a long time now."
    mr "Nine years, to be more specific. I was 8 and she was 16."
    nw "My dad passed away when I was 10, so, basically, it would be me, Matt and Janis."
    mr "Nigel's Christmas gift to me was a necklace."
    mr "A rose quartz necklace."
    mr "I'm always wearing it, but I keep it hidden."
    mr "I feel safer this way."
    nw "We had a simple dinner."
    mr "Yeah, we ordered pizza."
    #switch
    nw "So, after we were finished, Matt and I decided to take a walk outside."
    nw "And Matt took his acoustic guitar with him."
    nw "A classical Wade-like act."
    mr "Shut up."
    mr "We went to the park, and there we found some familiar faces."
    nw "Kaelyn and Jackson were playing some music around a campfire."
    nw "Jackson was playing his acoustic bass guitar, Kaelyn was playing an acoustic guitar."
    #switch
    mr "For some reason it was the same model as mine."
    mr "As we got closer, we all started playing together."
    nw "Fun fact: Kane never knew Kaelyn was hanging out with Jackson at that time."
    nw "He'd fucking freak out."
    mr "Well, after a while, Carol showed up, playing ukulele."
    nw "As we all sticked together, Matt taught them how to play a song he wrote."
    nw "I improvised it."
    mr "~Are we both just scarecrows~"
    mr "~Searching for a way to move?~"
    #switch
    nw "Stop. You're gaying up the place."
    mr "Yeah, keep pretending you don't like it."
    nw "Sh."
    nw "Well, when we reached the solo…"
    nw "Janis randomly showed up and started playing the violin."
    nw "It was…"
    #switch
    mr "Beautiful."
    mr "Well, after that, we came back home and Nigel stayed the night."
    mr "That was the moment I told him the name of the song."
    mr "I called it \"Kit-"
    #hide
    
    show matt_d at left:
        ypos 1.0
        zoom 0.184
    with dissolve

    show nigel_g_a at right:
        ypos 1.0
        zoom 0.172
    with dissolve
    
    nw "You don't have to mention that part!"

    hide nigel_g_a
    show nigel_a_a at right:
        ypos 1.0
        zoom 0.172

    nw "Well, I gotta go somewhere."
    
    menu:
        nw "[mcname], wanna come with me?"
        "Go with Nigel":
            hide nigel_a_a
            with dissolve
            jump c4s11
        "Stick with Matt":
            jump c4s12


label c4s11:

    stop music

    "You choose to stick with Nigel."

    show nigel_a_a at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Okay, let's go."

    play music "audio/bgm/rockstar_hangout.wav"

    #Interactive Dialogue
    python: 
        talkevent3 = False
        chanceevent11 = 0
        ques1 = False
        ques2 = False
        ques3 = False
        ques4 = False
        ques5 = False
        chance5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

    while talkevent3 == False and chanceevent11 == 0:
        $ chanceevent11 = renpy.random.choice(chance5)

        menu:
            "You're having a chat with Nigel."
            "First day" if ques1 == False:
                nw "I guess it was okay."
                nw "I was kind of a jerk to that newcomer, Amy Kingslay..."
                nw "But I guess she'd accept my apologies."
                $ ques1 = True
            "Relationships" if ques2 == False:
                hide nigel_a_a
                show nigel_g_a at center:
                    ypos 1.0
                    zoom 0.172
                nw "Nope."
                hide nigel_g_a
                show nigel_h_a at center:
                    ypos 1.0
                    zoom 0.172
                nw "Got a lot of people I want to..."
                nw "You know..."
                hide nigel_h_a
                show nigel_a_a at center:
                    ypos 1.0
                    zoom 0.172
                $ ques2 = True
            "Today's tattoo" if ques3 == False:
                hide nigel_a_a
                show nigel_c_a at center:
                    ypos 1.0
                    zoom 0.172
                nw "Oh, did you like it?"
                nw "It's an asian dragon."
                hide nigel_c_a
                show nigel_a_a at center:
                    ypos 1.0
                    zoom 0.172
                $ ques3 = True
            "Other tattoos" if ques4 == False:
                hide nigel_a_a
                show nigel_b_a at center:
                    ypos 1.0
                    zoom 0.172
                nw "Well, I got a small bunch of them."
                nw "But I'd say my favorite one is the snake I got on my chest."
                hide nigel_b_a
                show nigel_d_a at center:
                    ypos 1.0
                    zoom 0.172
                nw "It's a matching tattoo that I have with Matt."
                $ ques4 = True
                hide nigel_d_a
                show nigel_a_a at center:
                    ypos 1.0
                    zoom 0.172
            "Name of the song" if ques5 == False:
                hide nigel_a_a
                show nigel_g_a at center:
                    ypos 1.0
                    zoom 0.172
                nw "You'll have to find that one out for yourself."
                nw "I've mentioned it before, but the story behind it makes it kind of embarassing."
                hide nigel_a_a
                show nigel_g_a at center:
                    ypos 1.0
                    zoom 0.172
                hide nigel_g_a
                show nigel_a_a at center:
                    ypos 1.0
                    zoom 0.172
                $ ques5 = True
            "Stop Talking":
                $ talkevent3 = True

    hide nigel_a_a
    show nigel_d_a at center:
        ypos 1.0
        zoom 0.172
                
    nw "Oh, a cat!!"

    hide nigel_d_a
    with dissolve

    "He desperately runs after the animal, and you eventually lose sight of him."

    $ chanceevent12 = renpy.random.choice(chance5)

    if chanceevent12 == 1:
        jump ch04_bonnie_rng
    else:
        jump c4s13

label c4s12:

    stop music

    play music "audio/bgm/matt_raven.wav"

    hide matt_d
    show matt_b at left:
        ypos 1.0
        zoom 0.184
    with dissolve

    
    mr "Oh, so you wanna stick with me, huh?"
    nw "Then I'll be going. Be right back."
    
    hide nigel_a_a
    with dissolve

    "Nigel left."

    hide matt_b
    show matt_c at left:
        ypos 1.0
        zoom 0.184

    mr "Yeah, so we're alone now, [mcname]..."

    jump c4s14

label c4s13:
    
    stop music

    play music "audio/bgm/lost_and_numb.wav"

    "Wrong Ending 2/2:\n\"Lost (Again, maybe)\""

    $ persistent.c4we2 = True

    $ renpy.full_restart()

label c4s14:

    stop music

    play music "audio/bgm/how_i_met_your_cat.wav"

    hide matt_c
    show matt_a at left:
        ypos 1.0
        zoom 0.184
    
    mr "So, telling you a bit more about the song…"

    hide matt_a
    show matt_b at left:
        ypos 1.0
        zoom 0.184
    
    mr "It's about how scary love can be."
    mr "Don't you think love can be scary sometimes?"
    mr "Sometimes I just want that person to know that I'm scared of losing them."
    mr "Despite that, I still want more."
    mr "Why does it have to be so fatal and brutal?"
    mr "Sometimes I just wish this fucking mess in my head stops."
    mr "But still, I try to hang on."
    mr "One day, it will be different."
    
    hide matt_a
    show matt_b at left:
        ypos 1.0
        zoom 0.184
    
    mr "Oh, the name of the song?"
    mr "It's…"
    mr "It's called.."

    
    hide matt_b
    show matt_d at left:
        ypos 1.0
        zoom 0.184

    mr "\"Kitten\"."

    hide matt_d
    with dissolve

    jump c4s15

label c4s15:

    stop music
    play music "audio/bgm/chemical_romance.wav"

    scene bg02:
        zoom 2.0
    with fade

    centered "CHAPTER CLEAR!!"
    $ persistent.c4te = True
    $ persistent.unlockch5 = True
    centered "You unlocked \'Chapter 5\'!!"

    $ renpy.full_restart()
