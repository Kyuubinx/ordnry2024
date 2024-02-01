label ch03_paige_rng:

    show paige_c at center:
        ypos 1.0
        zoom 0.163
    with dissolve

    play music "audio/bgm/cutiepie.wav"

    pt "Oh, hi, cutie pie."
    pt "I'm hanging out with some friends, why don't you come with me?"
    "You decide to go with Paige."
    pt "Anyways, as I was saying..."
    pt "Nigel can be a jerk sometimes, but he's a cutie."

    play music "audio/bgm/1st_grade.wav"

    show amy_a at left:
        ypos 1.0
        zoom 0.165
    with dissolve

    if encamy1 == True:

        ak "Well, I'm still building my opinion about him."

    else:

        unkf "Well, I'm still building my opinion about him."
        
        hide amy_a
        show amy_c at left:
            ypos 1.0
            zoom 0.165

        unkf "Your name is [mcname], right?"
        unkf "Nice to meet you, I'm Amy Kingslay, also a newcomer."

        hide amy_c
        show amy_a at left:
            ypos 1.0
            zoom 0.165

        $ encamy1 = True

        if persistent.unl_amy == False:
            $ persistent.unl_amy = True

    show charlie_a at right:
        ypos 1.0
        zoom 0.167
    with dissolve

    unkf "Guys, I think you're being too harsh..."

    hide charlie_a
    show charlie_c at right:
        ypos 1.0
        zoom 0.167

    unkf "The boy is a rockstar!!"
    unkf "I'm Charlotte Dewbie, by the way."
    cd "You can call me Charlie!!"

    "You sticked with them for a while and kept walking."

    $ enccharlie1 = True

    $ persistent.unl_charlie = True

    hide charlie_c
    with dissolve

    hide amy_a
    with dissolve

    hide paige_c
    with dissolve

    return

label ch03_charlie_rng:

    play music "audio/bgm/1st_grade.wav"

    if enccharlie1 == True:
        "Charlie follows you."

    if chanceevent5 == 1:
        "Suddenly, you find another group."
    else:
        "Suddenly, you find a group of people."

    show dell_b at left:
        ypos 1.0
        zoom 0.174
    with dissolve

    dd "Oh, hi there."

    show charlie_b at right:
        ypos 1.0
        zoom 0.167
    with dissolve

    if enccharlie1 == True:
        cd "Hey, Dell."
    else:
        "Another girl appears out of nothing."
        unkf "Oh, hey Dell."
        unkf "And you're [mcname], right?"
        unkf "I'm Charlotte Dewbie."
        cd "You can call me Charlie!!"
        $ enccharlie1 = True
        if persistent.unl_charlie == False:
            $ persistent.unl_charlie = True

    dd "You see, Missing Halloween's show kinda inspired me."
    dd "Now I wanna start a band."

    play music "audio/bgm/blessed_n_blazed.wav"

    show marie_a at center:
        ypos 1.0
        zoom 0.17
    with dissolve

    unkf "You'd do it pretty well, Dell."
    unkf "You got the spirit."
    cd "Oh, hi Marie."

    hide marie_a
    show marie_b at center:
        ypos 1.0
        zoom 0.17

    mp "Oh, [mcname], right?"
    mp "Forgot to introduce myself."
    mp "I'm Marie Poplar."
    mp "Something like Charlie's best friend."
    cd "So... Yeah, I agree with Marie."
    cd "You just need some chill people to play with."
    "Charlotte moved her arms in a funny way."
    dd "Yeah, but... Who?"

    hide marie_b
    with dissolve

    show celeste_a at center:
        ypos 1.0
        zoom 0.162
    with dissolve

    ch "My sister plays guitar."
    ch "Maybe she could help."

    hide dell_b
    show dell_c at left:
        ypos 1.0
        zoom 0.174

    dd "Perfect."
    dd "Give me her name and number."

    "Dell suddenly bumped into someone."

    dd "B-Bierce?"

    hide celeste_a
    with dissolve

    hide dell_c
    with dissolve

    hide charlie_b
    with dissolve

    #gallery image

    "Charlie whispers in your ear."

    cd "Y-Yeah, they were like... Girlfriends or something like that."

    show bierce_b at center:
        ypos 1.0
        zoom 0.167
    with dissolve

    bg "Yeah... I'm assuming you need someone to play the drums, right?"
    
    show dell_b at left:
        ypos 1.0
        zoom 0.174
    with dissolve
    
    dd "You were listening?"
    bg "You know your voice calls my attention."
    dd "Silly."
    bg "And you must be [mcname]."
    bg "Greetings, I'm Bierce Gambino."

    show leo_a at right:
        ypos 1.0
        zoom 0.168
    with dissolve

    "A boy and a girl were walking by, right behind Bierce."
    unkm "Why don't you call Colson?"

    hide dell_b
    with dissolve

    show marie_a at left:
        ypos 1.0
        zoom 0.17
    with dissolve

    mp "He literally can't play a single instrument, you're just obsessed with him."
    mp "By the way, [mcname], this is Leo Beaurenaire, he's gay."
    lb "Hi."
    bg "What do you say about Roxy, then?"

    hide marie_a
    with dissolve
    
    show roxy_e at left:
        ypos 1.0
        zoom 0.176
    with dissolve

    rr "W-What?"
    rr "Me?!"
    rr "Drums?"

    hide bierce_b

    show dell_c at center:
        ypos 1.0       
        zoom 0.174
    with dissolve

    hide roxy_e
    with dissolve

    hide leo_a
    with dissolve

    python:
        persistent.encbierce1 = True
        persistent.encleo1 = True
        persistent.encroxy1 = True

    dd "Roxy Raymond, huh?"
    dd "Don't think it's such a bad idea, actually."

    hide dell_c
    with dissolve

    "You sticked with them for a while and kept walking."

    return

label ch03_amy_rng:

    show paige_c at right:
        ypos 1.0
        zoom 0.163
    with dissolve

    show amy_a at left:
        ypos 1.0
        zoom 0.165
    with dissolve

    play music "audio/bgm/1st_grade.wav"

    pt "You came back!! Yaaay!!"

    if persistent.encamy1 == False:

        unkf "Hi."
        unkf "Your name is [mcname], right?"
        unkf "Nice to meet you, I'm Amy Kingslay, also a newcomer."

        $ persistent.encamy1 = True

    ak "So... Juliet... Do you feel better about telling me what's your thing with Matt?"

    show juliet_g at center:
        ypos 1.0
        zoom 0.156
    with dissolve

    js "Leave me alone, will you?"

    hide paige_c
    with dissolve

    show carol_b at right:
        ypos 1.0
        zoom 0.168
    with dissolve

    cr "Don't be rude, Juliet."
    cr "It was just a peaceful question."
    js "Ugh."
    js "Okay."
    js "We had a thing."
    js "A very thingy thing."
    js "A little bit more thingy than Jackson."
    js "It's complicated."
    js "You seem too interested."
    js "Are you obsessed with Matt?"

    hide amy_a
    with dissolve

    show paige_c at left:
        zoom 0.6
        yalign 0.1
    with dissolve

    pt "I mean..."
    pt "It's kinda natural..."
    pt "I also had some thingy things with Matt."
    cr "Matt is sweet."
    cr "Never had any thingy things with him, but..."
    cr "He's not like Kane, who plays with people's feelings."
    pt "Matt... Knows how to leave a good memory, and maybe write a song about it."
    pt "His lovely eyes are blue like the sky..."
    cr "Okay, you're getting a little thingy crazy, now."
    cr "He might try not to hurt people, but you can't deny his history is kinda sus."

    "You sticked with them for a while and kept walking."

    hide paige_c
    with dissolve

    hide carol_b
    with dissolve

    hide juliet_g
    with dissolve

    return

label ch03_nigel_rng:

    hide nigel_h
    show nigel_a at center:
        ypos 1.0
        zoom 0.172

    nw "Come with me, there's something I gotta do."

    if persistent.encamy1 == True:

        "Nigel walks through the school with you until he finds Amy."

    else:

        "Nigel walks through the school with you until he finds a girl."
        "[mcname], that's Amy Kingslay, and you can say I owe her my apologies."

        $ encamy1 = True

    show amy_g at right:
        ypos 1.0
        zoom 0.165
    with dissolve

    ak "You, again."
    nw "Hi, Amy."
    nw "Sorry for the way I treated you a while ago."
    nw "Can I do something for you to accept my apologies?"

    hide amy_g
    show amy_a at right:
        ypos 1.0
        zoom 0.165

    ak "Go on."
    "Nigel removes the shoelace from amy's left shoe."

    hide amy_a
    show amy_g at right:
        ypos 1.0
        zoom 0.165

    ak "Come on, dude!! I trusted you!!"

    hide nigel_a
    show nigel_g at center:
        ypos 1.0
        zoom 0.172

    nw "Just wait, dammit!! I'm not done yet..."

    hide nigel_g
    show nigel_a at center:
        ypos 1.0
        zoom 0.172

    "Nigel puts it back in a way that the shoelace would form an inverted pentagram."
    
    hide amy_g
    hide nigel_a
    show amy_a at right:
        ypos 1.0
        zoom 0.165
    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    
    nw "So, what did you think?"
    nw "Pretty rock 'n' roll, right?"
    nw "Feeling more emo now?"
    
    hide amy_a
    show amy_b at right:
        ypos 1.0
        zoom 0.165
    
    ak "Thanks..."

    hide amy_a
    with dissolve

    hide nigel_b
    with dissolve

    return

label ch03_matt_rng:

    stop music

    #scene lindseyhouse

    show nigel_d at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    play music "audio/bgm/rockstar_hangout.wav"

    nw "Hey, we're passing through Lindsey's house now."
    nw "I bet Matt is here."
    nw "They were talking to each other after the show."
    nw "Come on, a little peek won't kill us."

    hide nigel_d
    with dissolve

    #scene lindseyhouse2

    "As you both get close to the window, you can hear them talking inside Lindsey's bedroom."

    stop music

    #gallery image

    play music "audio/bgm/memoria.wav"

    lp "I... Took over a year to say a single word to you."
    mr "Well, you didn't waited forever, right?"
    lp "So many things have happened in the last two years, right?"
    mr "Yeah, the band, the formation changing all the time..."
    mr "That was kinda tiring."
    mr "But honestly, I couldn't be more satisfied with every single member of Missing Halloween at this moment."
    mr "Me and Oliver were actually the point of start."
    mr "Bonnie adds a cute side to the band, which is also nice."
    mr "Tina's stage energy is absurdely crazy."
    mr "Heh, and of course..."
    mr "That fucking fire head."
    mr "Missing Halloween would never be the same without Nigel."
    nw "*giggles*"
    lp "I wasn't talking about the band, actually."
    nw "Pfffft..."
    mr "Oh, sorry."
    lp "You see, I've heard a lot of rumors..."
    mr "Yeah, I've got a collection of them."
    lp "Seems like your reputation never decreases."
    mr "Rumors are rumors."
    mr "They don't last more than ninety days."
    mr "But... Yeah..."
    mr "I guess a few of them might be true..."
    lp "I wouldn't mind checking if they are..."
    mr "What exactly will you do to me?"
    lp "The worst things, honey..."

    stop music

    "You hear some noises, assuming that Lindsey was taking off her clothes."
    mr "Sorry, Lindsey..."
    mr "I don't want to hurt you again..."
    lp "Trust me..."
    "You hear kiss noises."
    lp "I just wanna have some fun."
    mr "Come on, you're cheating."
    "Bed noises."

    play music "audio/bgm/blush_flush_crush.wav"

    #gallery image

    "Nigel was blushing more than usual."
    nw "O...Kay..."
    nw "Things got kinda hot in here, huh?"
    nw "How about we go to the school already?"

    return
