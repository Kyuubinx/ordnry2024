label ch01_franz_rng:

    "You observe a misterious boy wearing headphones."
    show franz_a at center:
        ypos 1.05
        zoom 0.188
    with dissolve
    menu:
        "Say 'hi'?"
        "Yes":
            $ encfranz1=True
            "You approach with a smile and say 'hi'."
            unkm "Oh... Are you talking to me?"
            hide franz_a
            show franz_b at center:
                ypos 1.05
                zoom 0.188
            unkm "Like... Really? Me?"
            hide franz_b
            show franz_c at center:
                ypos 1.05
                zoom 0.188
            unkm "Oh... I see... You just moved to Rainer High, right?"
            hide franz_c
            show franz_d at center:
                ypos 1.05
                zoom 0.188
            unkm "Nice, I'm Franz Momsen."
            hide franz_d
            show franz_b at center:
                ypos 1.05
                zoom 0.188
            fm "Not really the type who actually talks, but... Yeah... Whatever. You can call me if you'd like to."
            hide franz_b
            with dissolve
            "The metro stopped at the station that was close to Rainer High."
            "Franz went straight to his classroom, and you noticed he's in the 3rd grade."

        "No":
            "You've decided to keep your mouth shut."
            "The metro stopped at the station that was close to Rainer High."

    return

label ch01_paige_rng:

    "As you look through the wagon behind you, you see a girl with the school's uniform."
    menu:
        "Go to the other wagon?"
        "Yes":
            scene bg02:
                zoom 2.0
                xalign 0.8
            with dissolve

            "You hear your metallic footsteps as you walk to the other wagon."

            scene bg01
            with dissolve

            show paige_a at center:
                ypos 1.0
                zoom 0.163
            with dissolve

            "Now that you're in the other wagon, you can see the girl more clearly."
            menu:
                "Talk to her?"
                "Yes":
                    $ encpaige1 = True
                    $ ttp = True
                    "You calmly say 'hello' with a comforting smile."
                    hide paige_a
                    
                    play music "audio/bgm/cutiepie.wav"
                    
                    show paige_c at center:
                        ypos 1.0
                        zoom 0.163
                    unkf "Oh, hi!! Going to Rainer High, too?"
                    hide paige_c
                    show paige_a at center:
                        ypos 1.0
                        zoom 0.163
                    unkf "I see... You must be new..."
                    hide paige_a
                    show paige_d at center:
                        ypos 1.0
                        zoom 0.163
                    unkf "I'm Paige Tyshe, by the way."
                    pt "It is a pleasure to meet you, [persistent.mcname]."
                    hide paige_d
                    show paige_c at center:
                        ypos 1.0
                        zoom 0.163
                    pt "Really? You're in 1st grade?"
                    hide paige_c
                    show paige_d at center:
                        ypos 1.0
                        zoom 0.163
                    pt "This means we're gonna be classmates, cutie pie."
                    hide paige
                    with dissolve
                    "The metro stopped at the station that was close to Rainer High."

                "No":
                    "The girl seems pretty nice, but you've decided not to say a word."
                    "The metro stopped at the station that was close to Rainer High."


        "No":
            "The girl might be a good first friend in your highschool experience, but you've decided to stay in your wagon."
            "The metro stopped at the station that was close to Rainer High."

    return

label ch01_amy_rng:

    $ encamy1 = True
    $ persistent.unl_amy = True
    "As you walk through the halls of the entrance of the school, you see a school monitor seated and writing some names in a paper."
    "That's when you realize you're late on your first day."

    show amy_a at center:
        ypos 1.0
        zoom 0.165
    with dissolve

    "There's a girl talking to the school monitor."
    sm "What's your name, miss?"
    unkf "It's Amy Kingslay."
    sm "It seems you're not the only late one."
    hide amy_a
    show amy_b at center:
        ypos 1.0
        zoom 0.165
    ak "Oh, hi there."
    ak "So, you're also new, right?"
    ak "We're both new to the school and to the class."
    hide amy_b
    show amy_c at center:
        ypos 1.0
        zoom 0.165
    ak "Yeah, I'm also in the 1st grade."
    ak "So, why don't we walk together to the classroom?"
    hide amy_c
    show amy_b at center:
        ypos 1.0
        zoom 0.165
    ak "Oh, you have to sign your name here first, right?"
    ak "Don't feel bad, we're in the same boat, late in the first day."
    "You signed your name in the paper, and walked with amy to your classroom."
    hide amy_b
    with dissolve

    return
