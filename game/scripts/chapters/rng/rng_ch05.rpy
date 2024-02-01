label ch05_lane_rng:
    
    "A green-haired girl was coming upstairs."

    show lane_a at center:
        ypos 1.0
        zoom 0.165
    with dissolve

    unkf "Yo, you guys could've waited two minutes, right?" 
    # "The girl's piercings caught your attention."
    # "Two on the lips, seven on each ear and 3 on the nostril"
    # "There's probably even more in places that aren't visible." 
    
    show janis_b at left:
        zoom 0.154
        ypos 1.0
    with dissolve
    
    jr "Boys, Emily, [mcname], that's Lane."
    jr "She'll be helping me with the studio sometimes from now on."
    
    hide lane_a
    show lane_b at center:
        ypos 1.0
        zoom 0.165
    
    lq "Lane Quincy."
    lq "I watched your show today."
    lq "Pretty welcoming, for someone with my aesthetic, considering I'm new in town."
    
    show matt_c at right:
        zoom 0.184
        ypos 1.0
    with dissolve
    
    mr "Matt Raven."
    mr "I'm glad you liked the show."
    mr "So, what will you be doing here?"
    lq "I'm an expert on piercings, and am also in the tattoo business for some time now."
    
    hide janis_b
    with dissolve

    show nigel_g at left:
        ypos 1.0
        zoom 0.172
    with dissolve
    
    nw "Congrats, broccoli head."
    nw "That's very sexy of you."
    
    hide matt_c
    show matt_g at right:
        zoom 0.184
        ypos 1.0
    
    mr "Nigel?!"
    
    hide lane_b
    show lane_c at center:
        zoom 0.165
        ypos 1.0
    
    lq "Heh."
    lq "It's fine."
    
    hide lane_c
    show lane_d at center:
        zoom 0.165
        ypos 1.0
    
    lq "He's just scared of losing you to me."
    "Nigel grabbed Matt's arm."
    nw "Shut. Your. Fucking. Mouth."

    hide matt_g
    with dissolve

    hide nigel_g
    with dissolve

    hide lane_d
    with dissolve
    
    $ chance33 = [0,0,1]

    $ chanceevent_c5_4 = renpy.random.choice(chance33)

    if chanceevent_c5_4 == 1:

        call ch05_avril_rng

label ch05_mika_rng:

    "You all see two other familiar faces sitting by the food court."

    show matt_c at right:
        ypos 1.0
        zoom 0.184
    with dissolve

    mr "Okay, Oliver and Mika are here."

    show nigel_g at left:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "They were flirting in the classroom some hours ago."
    mr "Let's say \"hi\", I guess."

    hide matt_c
    with dissolve

    hide nigel_g
    with dissolve

    "You all start listening to their conversation."

    show mika_e at right:
        ypos 1.0
        zoom 0.17
    with dissolve

    mn "Tina kind of passes off the limits with us sometimes."

    show oli_a at left:
        ypos 1.0
        zoom 0.186
    with dissolve

    os "Yeah, maybe you're right."

    hide oli_a
    show oli_b at left:
        ypos 1.0
        zoom 0.186

    os "But…"

    hide oli_b
    show oli_c at left:
        ypos 1.0
        zoom 0.186

    os "If it wasn't for her, I wouldn't have asked you out on a date."
    
    hide mika_e
    show mika_b at right:
        ypos 1.0
        zoom 0.17
    
    mn "Maybe I'll thank her later, then."
    
    show matt_b at center:
        ypos 1.0
        zoom 0.184
    with dissolve
    
    mr "Date, huh?"

    hide mika_b
    with dissolve

    show nigel_b at right:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "You two are so cute together."

    hide oli_c
    show oli_a at left:
        ypos 1.0
        zoom 0.186

    os "Oh, fuck."
    os "Matt, Nigel."

    hide oli_a
    with dissolve

    show mika_c at left:
        ypos 1.0
        zoom 0.17
    with dissolve

    mn "And [mcname]."
    mn "How long have you two been in here?"
    mr "A while."
    nw "Enough to see you two flirting up the place."
    mn "So, how about an ice cream?"
    
    hide matt_b
    with dissolve

    show oli_a at center:
        ypos 1.0
        zoom 0.186
    with dissolve
    
    os "Yo, Kane just sent this video to every single group he's in."
    nw "Yeah, I'll take the ice cream."

    jump c5s7

label ch05_oli_rng:

    "You two see two other familiar faces sitting by the food court."

    show matt_c at right:
        ypos 1.0
        zoom 0.184
    with dissolve

    mr "Okay, Oliver and Mika are here."
    mr "Let's say \"hi\", I guess."

    hide matt_c
    with dissolve

    "You start listening to their conversation."

    show mika_e at right:
        ypos 1.0
        zoom 0.17
    with dissolve

    mn "Tina kind of passes off the limits with us sometimes."

    show oli_a at left:
        ypos 1.0
        zoom 0.186
    with dissolve
    
    os "Yeah, maybe you're right."

    hide oli_a
    show oli_b at left:
        ypos 1.0
        zoom 0.186

    os "But…"

    hide oli_b
    show oli_c at left:
        ypos 1.0
        zoom 0.186

    os "If it wasn't for her, I wouldn't have asked you out on a date."

    hide mika_e
    show mika_b at right:
        ypos 1.0
        zoom 0.17

    mn "Maybe I'll thank her later, then."

    show matt_b at center:
        ypos 1.0
        zoom 0.184
    with dissolve

    mr "Date, huh?"

    hide oli_c
    show oli_a at left:
        ypos 1.0
        zoom 0.186

    os "Oh, fuck."
    os "Matt."

    show mika_c at left:
        ypos 1.0
        zoom 0.17
    with dissolve

    mn "And [mcname]."
    mn "How long have you two been in here?"
    mr "A while."
    mn "So, how about an ice cream?"
    os "Yo, Kane just sent this video to every single group he's in."


    jump c5s7

label ch05_avril_rng:

    "As you go out of the studio with Matt and Nigel, you could see someone hiding in their hoodie."
    "They tried to be silent, but failed."
    jr "Yo, first time here?"
    # (if)
    "Suddenly, you recognize the girl."
    # (v1)
    ac "I guess so…"
    ac "I came to do my first tattoo."
    jr "Interesting."
    jr "So, what's it gonna be and where?"
    ac "A… Raven."
    ac "In my chest…"
    "Janis smiled."
    jr "Got inspired by the studio's name?"
    jr "Okay, you're gonna be the new girl's subject number one."
    ac "L-Lane?!"
    lq "Oh, hi Avril."
    # (v2)
    unkf "I guess so…"
    unkf "I came to get my first tattoo."
    jr "Interesting."
    jr "So, what's it gonna be and where?"
    unkf "A… Raven."
    unkf "In my chest…"
    "Janis smiled."
    jr "Got inspired by the studio's name?"
    jr "Okay, you're gonna be the new girl's subject number one."
    unkf "L-Lane?!"
    lq "Oh, hi Avril."
    # ($)


label ch05_bonnie_rng: