label c3s0:

    stop music

    scene bg02:
        zoom 2.0
    with fade

    play music "audio/bgm/when_it_rains.wav"

    centered "Chapter 3 - \"When It Rains\""

    scene bg03:
    with fade

    show gwen_mask at right:
        ypos 1.0
        zoom 0.174
    with dissolve

    stop music

    play music "audio/bgm/nigels_practice_solo.wav"

    gf "Kitten Deathcore, right?"

    show nigel_b at left:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Creative, isn't it?"

    hide gwen_mask
    show gwen_dark at right:
        ypos 1.0
        zoom 0.174
    with dissolve

    gf "Did Matt give you this name?"

    hide nigel_b

    if persistent.gwened == True:

        python:
            chance20 = [0, 0, 0, 0, 1]
        $ chanceevent4 = renpy.random.choice(chance20)

        show nigel_g at left:
            ypos 1.0
            zoom 0.172

        if chanceevent4 == 1:

            nw "None of your fucking business, you bitch."
            "Nigel has fire in his eyes."

        else:

            nw "None of your business."
        
        hide nigel_g

    else:

        show nigel_a at left:
            ypos 1.0
            zoom 0.172

        nw "Nah, Tina actually did half of it."

        hide nigel_a

    show nigel_b at left:
        ypos 1.0
        zoom 0.172
    hide gwen_dark
    show gwen_darker at right:
        ypos 1.0
        zoom 0.172 

    gf "Come on, I just want to tell you some things about Matt you don't know."

    menu:
        "Listen to Gwen?"
        "Yes":
            hide nigel_b
            show nigel_g at left:
                ypos 1.0
                zoom 0.172
            nw "Are you fucking nuts?!"
            nw "Come on, I'll open your eyes!"
            "Nigel slaps you in the face."
            hide nigel_g
        "No":
            hide nigel_b
            show nigel_d at left:
                ypos 1.0
                zoom 0.172
            nw "Nice!"
            nw "You're learning!"
            hide nigel_d

    stop music

    play music "audio/bgm/be_a_rockstar.wav"

    show nigel_a at left:
            ypos 1.0
            zoom 0.172

    nw "Like if you know Matt better than me, Gwen."
    nw "Every single fucking thing you've said to this very moment have been used against you."
    nw "You're nothing but a liar."
    
    hide gwen_darker
    show gwen_dark at right:
        ypos 1.0
        zoom 0.172
    
    gf "Are you saying you don't actually know his true personality?"
    
    hide gwen_dark
    show gwen_darker at right:
        ypos 1.0
        zoom 0.172
    
    gf "Don't you think his lyrics are just a way to avoid his true se..."

    #gallery image

    "Nigel interrupted the girl's speech by pushing her shirt and headbutting her forehead."
    "After that, he kicked both her shins, leaving her on her knees."

    python:
        chance20 = [0, 0, 0, 0, 1]
    $ chanceevent4 = renpy.random.choice(chance20)

    if chanceevent4 == 1:

        nw "Shut the fuck up, you dirty whore."

    else:

        nw "Why don't you shut your mouth?"

    #gallery image

    hide gwen_darker
    show gwen_mask at right:
        ypos 1.0
        zoom 0.174
    gf "I guess I interpret his poetry in a way different than yours."
    "He put a feet on one of her shoulders."
    nw "Yeah, welcome."
    nw "It's called rock 'n' roll."

    "Nigel left Gwen in the ground and started walking."

    menu:
        nw "So, will you follow me or should I wait for you to catch me later?"
        "Follow him":
            hide nigel
            with dissolve
            jump c3s1
        "Catch him later":
            stop music
            hide nigel
            with dissolve
            jump c3s2

label c3s1:

    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    "As you follow Nigel through the school, you both see a girl sitting in a window."
    nw "Dude!!"
    nw "She's beautiful!!"

    stop music

    play music "audio/bgm/loving_kitten.wav"

    hide nigel_b
    with dissolve

    #gallery image

    $ persistent.enclotus1 = True

    "As you both approach, the girl instantly talks to Nigel."

    unkf "Trouble right in the first day?"
    nw "Yeah, you can say it's my lifestyle."
    unkf "Nice show up there."
    nw "Thanks..."
    nw "Do I... Know you?"
    unkf "Oh, sorry..."
    unkf "I forgot to introduce myself."

    stop music

    play music "audio/bgm/a_flower.wav"

    unkf "Lotus."
    lh "Lotus Heilsie."
    nw "\"Heilsie\"?"
    nw "So you must be the goth freshgirl's older sister."
    lh "Is that how you call Celeste?"
    nw "Heh... You seem to be fun."
    lh "I barely got here, and you're already one of my inspirations."
    nw "Do you want to learn how to play the guitar?"
    lh "Actually, I do already play."
    nw "Ooh... Unexpected..."
    #back to normal
    
    show nigel_c at right:
        ypos 1.0
        zoom 0.172
    with dissolve

    show lotus_b t left:
        ypos 1.0
        zoom 0.169
    with dissolve
    
    lh "You think so?"

    hide lotus_b
    hide nigel_c

    show nigel_a at right:
        ypos 1.0
        zoom 0.172
    with dissolve

    show lotus_a t left:
        ypos 1.0
        zoom 0.169
    with dissolve

    unkm "Lotus, let's go, you'll miss the ride!!"

    hide lotus_a
    hide nigel_a

    show nigel_g at right:
        ypos 1.0
        zoom 0.172
    with dissolve

    show lotus_e at left:
        ypos 1.0
        zoom 0.169
    with dissolve

    lh "Coming, Wade."

    hide nigel_g
    show nigel_h at right:
        ypos 1.0
        zoom 0.172

    nw "Come on!! You're gonna leave me here and go with fucking Fletcher?"
    
    hide lotus_e
    show lotus_c at left:
        ypos 1.0
        zoom 0.172
    
    lh "It's my first day, give me a break."
    
    hide lotus_c
    show lotus_h at left:
        ypos 1.0
        zoom 0.172
    
    "Lotus got down from the window, smiled and winked at Nigel."
    lh "See you around, Kitten."

    hide lotus_h
    with dissolve

    "She left."
    nw "Dude... I think I'm in love..."
    nw "Anyways, let's keep going."

    #hide lotus

    jump c3s10

    return

label c3s2:

    play music "audio/bgm/welcome_to_rainer_high.wav"

    show nigel_b at center:
        ypos 1.0
        zoom 0.172

    nw "Alright, see ya!!"

    hide nigel_b
    with dissolve

    "As you see Nigel leaving, you notice two other people walking by."
    "You also notice they're talking about Matt."

    show colson_g at right:
        ypos 1.0
        zoom 0.173
    with dissolve

    unkm "Dude, I just can't realize why the girls are so obsessed with him."
    unkm "His mouth must taste like blood by the way he scratches his throat."

    show avril_a at left:
        ypos 1.0
        zoom 0.17 
    with dissolve

    unkf "It doesn't."

    hide avril_a

    show avril_h at left:
        ypos 1.0
        zoom 0.17

    unkm "What the actual fuck?!"

    menu:
        "What will you do?"
        "Ask the boy why he hates Matt":
            jump c3s3
        "Ask the girl why she knows Matt doesn't taste like blood":
            jump c3s4
        "Ignore them":
            hide avril_h
            with dissolve

            hide colson_g
            with dissolve
            
            "You decide to ignore them and keep on walking."
            jump c3s5

label c3s3:

    play music "audio/bgm/minor_classical.wav"

    $ persistent.encavril1 = True

    unkm "C'mon, I don't even know you, and don't owe you any kind of explanation."
    
    hide colson_g
    with dissolve
    
    "The boy left."

    hide avril_h
    with dissolve
    show avril_a at center:
        ypos 1.0
        zoom 0.17
    with dissolve

    unkf "And that is our ex president."

    hide avril_a
    show avril_b at center:
        ypos 1.0
        zoom 0.17

    unkf "Sorry for that."

    hide avril_b
    show avril_c at center:
        ypos 1.0
        zoom 0.17

    unkf "[mcname], right?"

    hide avril_c
    show avril_d at center:
        ypos 1.0
        zoom 0.17

    unkf "My name is Avril Cosette."

    hide avril_d
    show avril_b at center:
        ypos 1.0
        zoom 0.17

    ac "So..."
    ac "I'm guessing now it's time for me to start telling you the story, right?"
    ac "Come on, will you say you're not curious?"

    hide avril_b
    with dissolve
    show avril_d at center:
        ypos 1.0
        zoom 0.17

    ac "I feel confortable to tell you my story with Matt."
    ac "You're new here, right?"
    ac "That's why I feel like you wouldn't judge me."
    ac "You've found all of us in a moment which Missing Halloween's image is already super well built."
    ac "So, why don't I start?"
    menu:
        "Listen to Avril's story?"
        "Yes":
            jump c3s6
        "No":
            hide avril_d
            show avril_a at center:
                ypos 1.0
                zoom 0.17
            ac "Oh, you don't want it?"
            ac "Okay, then."
            hide avril_a
            show avril_b at center:
                ypos 1.0
                zoom 0.17
            ac "I'll go find that jerk, if you don't mind."
            hide avril_b
            with dissolve
            jump c3s5

    return

label c3s4:

    stop music

    unkf "You know what?"
    unkf "I gotta go."

    hide avril_h
    with dissolve

    "The girl left."

    $ persistent.enccolson1 = True

    hide colson_g
    with dissolve

    play music "audio/bgm/narcisio.wav"

    show colson_a at center:
        ypos 1.0
        zoom 0.173
    with dissolve

    "The boy approached you with a wide grin on his face."
    
    hide colson_a
    show colson_b at center:
        ypos 1.0
        zoom 0.173
    
    unkm "Hey there, buddy!"

    hide colson_b
    show colson_c at center:
        ypos 1.0
        zoom 0.173

    "He slaps your back with a little too much force."
    unkm "What's up?"
    unkm "My name is Colson Vee."
    "Suddenly, you remember what Nigel said."
    "You took a step back, trying to distance yourself from him."
    "Colson followed your gaze and chuckled."
    cv "Don't worry, I'm not gonna bite."
    cv "I just wanted to talk to you about something important."

    menu:
        "What are you gonna do, [mcname]?"
        "Listen to him":
            hide colson_c
            show colson_d at center:
                ypos 1.0
                zoom 0.173
            cv "Good."
        "Leave":
            "You left the boy alone before he could even talk."
            jump c3s5

    stop music

    play music "audio/bgm/narcisio_out_of_tune.wav"

    cv "How do you feel about writing articles?"
    "His eyes gleaming with what you suspected was fake admiration."
    cv "And I know you care about the truth, right?"
    "You hesitate, unsure of where this was going."
    cv "Well, I would like you to join the Journal Club."
    cv "We're all about reporting the truth, no matter how ugly it is."
    cv "And oh, do we have some juicy stories to share."
    cv "Like the Matt Raven's ones..."
    cv "The guy's not as perfect as he seems, you know."
    cv "He's got some skeletons in his closet, and we're gonna expose them."
    cv "Whatever gets the clicks, right?"
    cv "It's not like Matt Raven is a saint."
    cv "He's been getting too much attention lately, and it's time to take him down a peg or two."
    hide colson_d
    show colson_a at center:
        ypos 1.0
        zoom 0.173
    "Colson's expression darkened for a moment."

    menu:
        cv "So... Will you help me?"
        "Yes":
            cv "That's what I thought..."
            jump c3s14
        "No":
            cv "Oh, really?"
            cv "You're missing out on some serious fun."
            cv "And who knows, maybe you'll change your mind later."
            cv "But why not teach you a lesson right away?"
            cv "Heh... Just kidding..."

            hide colson_a
            with dissolve

            jump c3s13

label c3s5:

    python:
        chance25 = [0, 0, 0, 1]
    $ chanceevent5 = renpy.random.choice(chance25)

    if chanceevent5 == 1:

        call ch03_paige_rng

    $ chanceevent6 = renpy.random.choice(chance25)

    if chanceevent6 == 1:

        call ch03_charlie_rng

    $ chanceevent7 = renpy.random.choice(chance25)

    if chanceevent7 == 1:

        call ch03_amy_rng

    jump c3s7

label c3s6:

    show avril_h at center:
        ypos 1.0
        zoom 0.17
    with dissolve

    play music "audio/bgm/memoria.wav"

    ac "It was last year's Christmas break."
    ac "A party organized by Kane Ravat."
    ac "Crazy, noisy, and stink of alcohol."
    ac "Clearly not my type of party, specially with all those drunk faces even outside."
    ac "I could just leave, but I needed Chelsea Yore, a friend of mine to give me a ride."
    ac "And she wouldn't agree on doing that for at least two hours."
    ac "So I saw a tree house, and decided to go there."
    ac "It was a little far from Kane's party room."
    ac "As I went up the stairs and opened the trapdoor, I saw an unexpected face."
    ac "Of course I was still pissed by the talent show."
    ac "Missing Halloween stole all my glamour."
    ac "So I just apologized for the intromission."
    ac "I started going down the stairs again, but he stopped me, by saying..."
    ac "\"Aren't you searching for peace? I wouldn't mind having your company for a while.\""
    ac "So, I stayed at the tree house, sitting by the opposite side of his and enjoying a whole minute of pure silence."
    ac "Until he decided to break it."

    hide avril_h
    show avril_c at center:
        ypos 1.0
        zoom 0.17

    ac "\"Are you still angry?\", he asks."
    ac "I didn't lie."
    ac "We started arguing a bit about both our musical styles, and..."
    ac "At some point, we just gave up and started making out."
    
    hide avril_c
    show avril_e at center:
        ypos 1.0
        zoom 0.17
    
    ac "I don't regret a single thing, but..."
    ac "I'm kinda scared of what my friends might say if I told them about it."
    
    hide avril_e
    show avril_b at center:
        ypos 1.0
        zoom 0.17
    
    ac "And speaking of my friends, I gotta find that jerk."
    ac "Thanks for spending some time with me, [mcname]."

    hide avril_b
    with dissolve

    jump c3s5

label c3s7:

    stop music

    play music "audio/bgm/welcome_to_rainer_high.wav"

    "You start exploring the place, the school is completely new to you."
    "That's the moment where you find the bicycles parking lot."

    #scene bicypark
    #with fade

    "There, you saw two unfamiliar faces."

    show bonnie_b at left:
        ypos 1.0
        zoom 0.158
    with dissolve

    unkf "So... Wanna go to my house?"
    "You notice that was the girl that was playing bass on the stage some minutes ago."
    "Nigel mentioned her name was Bonnie."

    stop music

    play music "audio/bgm/bonbon.wav"

    show andy_e_a at right:
        ypos 1.0
        zoom 0.178
    with dissolve

    unkm "Isn't it kinda far?"

    hide bonnie_b
    show bonnie_c at left:
        ypos 1.0
        zoom 0.158

    bm "We have time, you can even sleep there."
    unkm "Isn't it too soon for us to do it?"
    
    hide bonnie_c
    show bonnie_a at left:
        ypos 1.0
        zoom 0.158
    
    bm "Nope. We're teenage highschoolers in love!! It's super normal!!"
    unkm "I dunno... I wonder what my mom would think about this..."
    "You start to think, and remember that's probably her boyfriend, Andy."
    
    hide bonnie_a
    show bonnie_g at left:
        ypos 1.0
        zoom 0.158

    stop music

    play music "audio/bgm/lovers_metal.wav"

    bm "Dude, come on!!"
    bm "You live for yourself, not for your mom!!"
    bm "You're literally in Rainer High, the school of rock 'n' roll, dating the bassist of Missing Halloween, the band that created all the massive dark scenario here."
    bm "Where's your rebel spirit?!"
    bm "Be a little more rock 'n' roll, dude!!"

    hide bonnie_g
    show bonnie_h at left:
        ypos 1.0
        zoom 0.158

    bm "It would be soooo awesome if you just did it like in the movies..."
    
    hide bonnie_h
    show bonnie_c at left:
        ypos 1.0
        zoom 0.158
    
    "She smiled nicely."
    bm "And knock at my window in the middle of the night..."
    aw "I just think you should be in class... I don't want you to get stuck in the final exams like last year."
    
    hide bonnie_c
    show bonnie_e at left:
        ypos 1.0
        zoom 0.158
    
    bm "Andy, dear... It's literally the first day."
    bm "I bet no one is in the classroom."
    bm "Maybe Ebony, Franz or Mika..."
    aw "I'm pretty sure Damon is in there."

    stop music

    "Suddenly, a really heavy boot hits Andy's shoulder."

    show vicky_g at center:
        ypos 1.0
        zoom 0.177
    with dissolve

    play music "audio/bgm/vickvickvick.wav"

    unktt "I'm not, and it's \"Vicky\" now, don't be such a transphobic."
    vs "Besides, you didn't see that face over there."
    "Vicky pointed at you."
    
    hide vicky_g
    show vicky_b at center:
        ypos 1.0
        zoom 0.177
    
    vs "Come on, buddy, give me a hand over here."
    menu:
        vs "Who do you agree with?"
        "Bonnie":
            bm "See?!"
            bm "I told you, Andy!"
            bm "Love, you're just being too paranoid..."
            bm "[mcname], right?"
            bm "Come on, you will go home with me."

            hide andy_e_a
            with dissolve

            hide vicky_b
            with dissolve

            hide bonnie_e
            with dissolve

            jump c3s9

        "Andy":
            aw "Thank you."
            aw "[mcname]?"
            aw "Quite a nice name, if you don't mind me saying."
            aw "Shall we go to my apartment, then?"

            hide andy_e_a
            with dissolve

            hide vicky_b
            with dissolve

            hide bonnie_e
            with dissolve

            jump c3s8

        "\"I should meet with Nigel, do you know where he is?\"":
            vs "Oh... Yeah... I see..."
            bm "Ooh... Are you friends with Nigel already?!"
            bm "That's sooo niiice!!"
            bm "And quite surprising..."
            bm "So it was you he was talking about, right?"
            bm "He's right there."
            "Bonnie pointed at the street almost outside of the school."
            "There you saw Nigel."
            bm "He seemed pretty excited about it, you should meet him right away!!"
            "So you decided to go after nigel."

            hide andy_e_a
            with dissolve

            hide vicky_b
            with dissolve

            hide bonnie_e
            with dissolve

            jump c3s11

label c3s8:

    stop music

    play music "audio/bgm/stray.wav"

    #scene city
    #with fade

    "As you walk through the streets with Andy, you notice he has sort of an obsession with videogames."
    "You two finally arrive at the door of Andy's apartment, excitement coursing through you."

    show andy_a at center:
        ypos 1.0
        zoom 0.178
    with dissolve

    stop music

    aw "Oh, the earrings?"
    aw "My mom doesn't like them."
    
    hide andy_a
    show andy_b at center:
        ypos 1.0
        zoom 0.178
    with dissolve

    play music "audio/bgm/fake_earrings.wav"
    
    aw "They're fake."
    aw "She doesn't know I wear them."

    #scene andyap
    #with fade

    "He opens the door."

    hide andy_b
    show andy_c at center:
        ypos 1.0
        zoom 0.178

    aw "Come on in!!"
    "You step inside, taking in the small but cozy apartment."
    "The living room is cluttered with video game consoles and controllers, and a TV sits at the center of the room."
    "As you make your way to the living room, you can hear the familiar sounds of games you've played before coming from the TV."
    "You settle in on the couch and pick up a controller, ready to race your way to victory."
    "But before you can even start, Andy's mother appears in the doorway."

    stop music

    andm "Who is this?"
    "Andy introduces you, but his mother seems less than pleased."
    andm "I don't know them"
    "She says it coldly."
    andm "I don't want strangers in my apartment."
    "You feel your face flush with embarrassment as Andy's mother asks you to leave."
    "You quickly gather your things and make your way to the door, feeling disappointed that your videogame session has been cut short."
    
    hide andy_c
    show andy_e at center:
        ypos 1.0
        zoom 0.178
    
    aw "I'm sorry about that..."
    aw "My mom can be a bit overprotective sometimes."
    
    hide andy_e
    with dissolve

    play music "audio/bgm/lost_and_numb.wav"
    
    "You wave goodbye and make your way down the hallway, feeling a little hurt by the rejection."

    #scene city
    #with fade

    "But as you step outside, you can't help but remember this town is also new to you, and you can't remember his apartment number, as well as you don't have his phone number."
    "You're lost in the town, and don't know where to go..."

    "Wrong Ending 3/8: \n\"Lost and Numb\""

    $ persistent.c3we3 = True

    $ renpy.full_restart()

label c3s9:

    stop music

    play music "audio/bgm/bonbon.wav"

    #scene city
    #with fade

    "As you walk out of the school gates with Bonnie, you feel a rush of excitement."
    "She's Andy's girlfriend, and yet she asked you to come over to her house."
    "You can't help but feel flattered to hang out with a Missing Halloween member."
    "The two of you chat about your favorite TV shows and music on the way to her house."
    "Bonnie's house is almost like a giant cube."

    #scene bonhouse
    #with fade

    show todd_a at left:
        ypos 1.0
        zoom 0.187
    with dissolve

    stop music
    
    play music "audio/bgm/kickstarted.wav"

    "As you walk up the path, you notice a boy around your age, some years older sitting on the front porch, looking at you with a scowl on his face."

    show bonnie_g at center:
        ypos 1.0
        zoom 0.158
    with dissolve

    "Bonnie looks at him and rolls her eyes."
    bm "That's my annoying big brother, Todd."
    bm "Don't mind him."

    hide todd_a
    with dissolve

    #scene bonhousein
    #with fade

    "You follow Bonnie inside, and she leads you to the living room."
    "You sit down on the couch and start chatting about school and your plans for the weekend."

    show todd_h at left:
        ypos 1.0
        zoom 0.187
    with dissolve

    "That's when Todd walks in."
    "He looks you up and down with a sneer on his face."
    to "So, who's the loser?"
    "Bonnie rolls her eyes."
    bm "Todd, this is my friend."
    bm "[mcprn1] [mcprn4] here to hang out with me."
    "Todd walks over to you and towers over you."
    to "Well, you're not welcome here."
    to "You should leave."
    "Bonnie tries to intervene."
    bm "Todd, leave him alone."
    bm "He's my friend."
    "But Todd doesn't listen."
    "He grabs you by the collar of your shirt and starts to push you towards the door."
    to "I said leave! And don't come back unless you want me to throw you to the hellfire!"
    "You try to resist, but Todd is much stronger than you."
    "He shoves you out the door, and you stumble down the steps, almost falling over."

    stop music

    play music "audio/bgm/painful.wav"

    hide todd_h
    with dissolve

    "You can hear Todd and Bonnie arguing inside as you make your way down the street, feeling humiliated and confused."
    "You can't believe what just happened."
    "You were just trying to hang out with Bonnie."
    "You can't help but feel angry and frustrated, but also sad that you won't be able to hang out with Bonnie anymore."

    #scene bonhouse
    #with fade

    "You still feel dizzy because Todd thrown you to the ground."
    "You start to go down the stairs, but stumbles to the ground again, and starts falling over the stairs."
    "It's a neverending horrible pain, and you eventually hit your head in the ground, and passes over."

    "Wrong Ending 4/8: \n\"To The Hellfire\""

    $ persistent.c3we4 = True

    $ renpy.full_restart()

label c3s10:

    stop music

    play music "audio/bgm/be_a_rockstar.wav"

    python:
        chance20 = [0, 0, 0, 0, 1]
    $ chanceevent8 = renpy.random.choice(chance20)

    if chanceevent8 == 1:

        call ch03_nigel_rng

    jump c3s12

label c3s11:

    stop music

    play music "audio/bgm/ruby/hair.wav"

    #scene schoolexit
    #with fade

    show nigel_d at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Oh, hi there."
    nw "I was waiting for you."
    nw "Ready to keep going?"

    hide nigel_d

    jump c3s15

label c3s12:

    stop music

    play music "audio/bgm/ruby/hair.wav"

    #scene schoolexit
    #with fade

    show nigel_d at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Enjoying our little date, are we?"
    
    hide nigel_d
    show nigel_c at center:
        ypos 1.0
        zoom 0.172
    with dissolve
    
    nw "Hehe... Just kidding."
    
    hide nigel_c
    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "But seriously, are you feeling happy?"

    hide nigel_b

    jump c3s15

label c3s13:

    stop music

    "As soon as Colson Vee was out of sight, you breathed a sigh of relief and started to walk away."
    "But before you could take more than a few steps, you felt a sudden force push you forward."
    "Your arms flailed as you stumbled, and then you realized that you had been shoved into a locker."

    #play metal sound
    #scene locker
    #with fade

    "You tried to push the door open, but it wouldn't budge."
    "You were trapped, and you had no idea how to get out."
    "Panic rose in your chest as you heard Colson's voice on the other side."

    #scene lockerwcolson
    #with fade

    play music "audio/bgm/narcisio_detuned.wav"

    cv "Hey there, little journalist,"
    "He taunted, his voice echoing in the small space."
    cv "How's it going?"
    "You gritted your teeth, feeling angry and scared at the same time."
    "Colson laughed, a cold, cruel sound."
    cv "Oh, I'm not laughing..."
    cv "I'm serious."
    cv "You're not getting out of there until you see things my way."
    "You glared at the door, realizing that Colson was going to try to convince you to join the Journal Club again."
    "You braced yourself for the worst, knowing that he wasn't going to give up easily."
    "Colson's voice turned deadly serious."
    cv "You don't get it, do you?"
    cv "You can't just walk away from me."
    cv "You're going to do what I say, or else."
    "Your heart skipped a beat as you realized that Colson was not playing around."
    "You didn't know what he was capable of, but you knew that you had to get out of the locker before things got worse."
    cv "Think about it, kiddo..."
    cv "You could be part of something big."
    cv "Something important."
    cv "And all you have to do is tell a few lies."

    pause 3

    cv "You're not even listening to me, right?"
    cv "Great."
    "You hear the sound of a padlock closing, and his footsteps were becoming more quiet at every single second."
    "Wrong Ending 1/8: \n\"Colson's Trap\""

    $ persistent.c3we1 = True

    $ renpy.full_restart()

label c3s14:

    scene bg02:
        zoom 2.0
    with fade

    stop music

    "You accepted the journal club deal."

    pause 3

    "Some days have passed."
    "You've written the most cruel lies about not only Matt, but all the members of the band."

    #scene bandexecution
    #with fade

    play music "audio/bgm/eaten_alive.wav"

    "They don't look very happy about it."
    tm "You know... I like to call this... A manual expulsion."
    nw "I trusted you... Now get ready to not recognize your own self when you look in the mirror."
    mr "\"Don't mess with a Raven if you don't want the vultures to devour your corpse\", it's what my sister says... But I... A Raven myself... Wouldn't mind to do a vulture's job..."

    #play sound punch_rain

    scene bg02:
        zoom 2.0
    with fade

    "Wrong Ending 2/8: \n\"Fake News Club\""

    $ persistent.c3we2 = True

    $ renpy.full_restart()

label c3s15:

    stop music

    play music "audio/bgm/ruby_hair.wav"

    show nigel_a at center:
        ypos 1.0
        zoom 0.172

    nw "Good."
    nw "I need to go to my house now."
    nw "Come with me."

    #scene city
    #with fade

    "You and Nigel start talking about guitars along the way."

    menu:
        nw "So, what's your favourite guitar model?"
        "Les Paul":
            hide nigel_a
            show nigel_c at center:
                ypos 1.0
                zoom 0.172
            nw "Classics [mcprn5], aren't you?"
            hide nigel_c
            with dissolve

        "Stratocaster":
            hide nigel_a
            show nigel_g at center:
                ypos 1.0
                zoom 0.172
            nw "Either you own one single guitar, or you don't own a guitar."
            hide nigel_g
            with dissolve

        "Telecaster":
            hide nigel_a
            show nigel_g at center:
                ypos 1.0
                zoom 0.172
            nw "What?! Blues?! Kinda outdated, huh?"
            hide nigel_g
            with dissolve

        "SG":
            hide nigel_a
            show nigel_b at center:
                ypos 1.0
                zoom 0.172
            nw "You're old."
            hide nigel_b
            with dissolve

        "Star":
            hide nigel_a
            show nigel_d at center:
                ypos 1.0
                zoom 0.172
            nw "Nice, if you want to be a star, why not buy a guitar that's a star too, right?"
            hide nigel_d
            with dissolve

        "Explorer":
            hide nigel_a
            show nigel_b at center:
                ypos 1.0
                zoom 0.172
            nw "Yeah, they're nice, but I feel like something's always missing something."
            hide nigel_b
            with dissolve

        "Flying V":
            hide nigel_a
            show nigel_g at center:
                ypos 1.0
                zoom 0.172
            nw "I don't like those."
            hide nigel_g
            with dissolve

        "Warlock":
            hide nigel_a
            show nigel_h at center:
                ypos 1.0
                zoom 0.172
            nw "NICE!! THOSE ARE THE FUCKING BEST!!"
            hide nigel_h
            with dissolve

        "Razorback":
            hide nigel_a
            show nigel_h at center:
                ypos 1.0
                zoom 0.172
            nw "Other words, you're absurdely hot."
            hide nigel_h
            with dissolve

    #scene nigelblock
    #with fade

    "Finally, you both arrive."
    "Actually, Nigel's apartment was just three blocks away from the school."

    #scene nigelap
    #with fade

    show nigel_c at left:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "So, here we are."
    "He pressed the button to call the elevator."
    "It opened instantly."

    #gallery image

    stop music

    pause 3

    nw "..."
    unkm "..."

    pause 3

    play music "audio/bgm/elev.wav"

    nw "I'll take the stairs."

    #scene nigelstairs
    #with fade

    "As you two suffer from fatigue to arrive at the 10th floor through the stairs, Nigel sits in the ground before you two could leave the stairs."

    show nigel_a at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Wow... That was quite torturing."
    nw "Anyways, that's my brother, Mike."
    nw "We don't really talk much."
    nw "*sigh*"
    nw "Time to face him, I guess..."
    "You couldn't help but notice Nigel has a key in his hand."
    nw "Oh, yeah, we have these keys for each floor of the stairways here."
    nw "Security thing, you know?"
    nw "I used the other one before."

    hide nigel_a
    with dissolve

    jump c3s16

label c3s16:

    #scene nigelapin
    #with fade

    stop music

    play music "audio/bgm/ruby_hair.wav"

    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Sooo... I came here just to leave my things..."

    menu:
        nw "What do you wanna do after that?"
        "\"I really want to stay at your house.\"":
            hide nigel_b
            show nigel_d at center:
                ypos 1.0
                zoom 0.172            
            nw "Whatever you say..."
            hide nigel_d
            with dissolve
            jump c3s17

        "\"Let's go to the park!!\"":
            hide nigel_a
            show nigel_d at center:
                ypos 1.0
                zoom 0.172
            nw "Awesome idea!!"
            nw "You're a genius!!"
            nw "Let me just leave my things at my bedroom."
            hide nigel_d
            with dissolve
            jump c3s18

label c3s17:

    #scene nigelbedroom
    #with fade

    stop music

    play music "audio/bgm/rockstar_bedroom.wav"

    "Nigel leads you to his bedroom, chatting excitedly about his music."
    "As you reach his room, Nigel opens the door, and you step inside."
    "Suddenly, Mike appears in the doorway of his own bedroom across the hall."
    "He looks at you with disgust."

    show mike_a at right:
        ypos 1.0
        zoom 0.187
    with dissolve

    stop music

    play music "audio/bgm/pseudo_hiki.wav"

    mw "What are you doing here?"

    show nigel_g at left:
        ypos 1.0
        zoom 0.172
    with dissolve

    "Nigel tries to defuse the situation."
    nw "What the actual fuck, this is probably the first time you take a step close to me in a fucking year."
    nw "We were just going to hang out in my room."
    "But Mike is having none of it."

    hide mike_a
    show mike_h at left:
        ypos 1.0
        zoom 0.187

    mw "I don't want [mcprn2] in my house."
    "He pushes his way past Nigel and into the room."
    "Mike starts messing with you, making fun of your clothes, your hair, your hobbies."
    "You try to ignore him, but it's hard to do with him standing right in front of you."
    "Nigel looks uncomfortable, but he doesn't say anything."
    "Finally, Mike gets fed up and says."
    mw "That's it, you need to leave."
    "He grabs your arm and starts pulling you towards the door."
    "Nigel grabs his arm."
    nw "Try anything weird and I will fuck you up."
    mw "Oh, really?"

    hide nigel_g
    with dissolve

    "Mike fastly grabs the key to Nigel's room, and closes the door, locking Nigel inside his own room."
    nw "FUCK YOU, MIKE!!"

    #scene nigelapin
    #with fade

    stop music

    play music "audio/bgm/painful.wav"

    "Mike grabs you by the arm and starts pushing you outside of the apartment."

    #scene nigelap
    #with fade

    "He doesn't stop at the door, though."

    #scene nigelstairs
    #with fade
    
    hide mike_h
    show mike_g at center:
        ypos 1.0
        zoom 0.187
        
    mw "Rot in hell."

    hide mike_g
    with dissolve

    "He closes the door."
    "Locked."
    "You don't have the keys."
    "You're trapped."

    "Wrong Ending 5/8: \n\"No Way Out\""

    $ persistent.c3we5 = True

    $ renpy.full_restart()

label c3s18:

    stop music

    play music "audio/bgm/rockstar_bedroom.wav"

    #scene nigelbedroom
    #with fade

    "Nigel leads you to his bedroom, chatting excitedly about his music."
    "As you reach his room, Nigel opens the door, and you step inside."
    "Suddenly, Mike appears in the doorway of his own bedroom across the hall."

    show nigel_a at left:
        ypos 1.0
        zoom 0.172
    with dissolve

    show mike_b at right:
        ypos 1.0
        zoom 0.187
    with dissolve

    stop music

    mw "W-Welcome home..."
    "Nigel faced him like he has seen a ghost."

    play music "audio/bgm/ghostboy.wav"

    mw "You... Played really well today."
    
    hide nigel_a
    show nigel_g at left:
        ypos 1.0
        zoom 0.172
    
    nw "Dude... What the fuck is going on?"
    nw "You literally don't talk to me."
    nw "You actually don't even leave your bedroom when I'm home."
    nw "Sometimes I feel like you don't exist."
    
    hide mike_b
    show mike_h at right:
        ypos 1.0
        zoom 0.187
    
    mw "I... Guess I owe you a Christmas gift, don't I?"
    mw "I guess now it's a good time."
    nw "Okay, will you give me some candy or what?"
    nw "Come on, I don't have all day."
    mw "*sigh*"
    mw "..."
    nw "Okay, then I'll enter my bedroom."

    hide nigel_g
    with dissolve

    stop music

    #scene nigelbedroomin
    #with fade

    #show eagleegp10:
        #zoom 0.2
        #yalign 0.3
        #xalign 0.7
    #with dissolve

    pause 3

    show nigel_d at left:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "YOU GOTTA BE FUCKING KIDDING ME!!"

    play music "audio/bgm/i_hate_pink.wav"

    "Before Mike could open the door, Nigel opened it aggressively himself."
    
    hide mike_h
    show mike_d at right:
        ypos 1.0
        zoom 0.187
    
    mw "Did you... Like it?"
    nw "An eternity without saying a single word and that's how you say \"hello\"?"
    nw "Dude, I absolutely love you."
    nw "Did you see it, [mcname]?"
    nw "It's an PinKrow 25 Stratocaster guitar!!"
    mw "[mcname], huh?"
    mw "I'm Mike."
    mw "Anyways, Nigel, I'm glad you liked it."
    mw "I was just... Thinking about how much you like pink, and..."
    nw "I hate pink."

    hide mike_d
    show mike_e at right:
        ypos 1.0
        zoom 0.187

    mw "Oh..."
    mw "I see."

    hide mike_e
    show mike_a at right:
        ypos 1.0
        zoom 0.187

    stop music

    mw "By the way, how long is that cat living here?"

    play music "audio/bgm/nyaigel.wav"

    #show muffin:
        #zoom 0.2
        #yalign 0.3
        #xalign 0.5
    #with dissolve

    hide nigel_d
    show nigel_a at left:
        ypos 1.0
        zoom 0.172

    nw "Oh, Muffin?"
    nw "It was Matt's Christmas gift to me."
    mw "You've been really close to Matt lately, right?"
    nw "Yeah... We're in the same band... What exactly did you expect?"
    mw "Anything but a cat."
    nw "Technically, I was the one who found Muffin, but he liked Matt better."
    
    hide nigel_a
    show nigel_c at left:
        ypos 1.0
        zoom 0.172
    
    nw "It just happened that he got tired of Matt and now he is destined to live with me."
    mw "O...Kay... I'll... Go back to my bedroom and... Never come back again... It was good to see you, though."

    hide mike_a
    with dissolve

    hide nigel_c
    show nigel_b at left:
        ypos 1.0
        zoom 0.172
    
    nw "I guess now it's the time we go out to the park."

    jump c3s19

label c3s19:

    stop music

    play music "audio/bgm/ruby_hair.wav"
    
    scene bg02:
        zoom 2.0
    with fade

    "You and Nigel went to the park and saw two faces you were beggining to feel familiar with."

    #scene park
    #with fade

    show nigel_a at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    show jackson_b at right:
        ypos 1.0
        zoom 0.178
    with dissolve

    show kaelyn_b at left:
        ypos 1.0
        zoom 0.168
    with dissolve

    stop music

    nw "Okay, should I say this is unexpected or the most expectable thing ever?"
    
    hide kaelyn_b
    show kaelyn_c at left:
        ypos 1.0
        zoom 0.178

    play music "audio/bgm/childhood_friends.wav"
    
    ka "Oh, hi Nigel, hi [mcname]."
    jn "What brings you guys here?"
    
    hide nigel_a
    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    
    nw "Just hanging around, I guess."
    ka "Oh, I see..."

    hide kaelyn_c
    show kaelyn_d at left:
        ypos 1.0
        zoom 0.168

    ka "Hey, Jackson, why don't you come with me to the rollercoaster?"

    hide jackson_b
    show jackson_h at right:
        ypos 1.0
        zoom 0.178

    jn "You didn't bring your wallet, I know you're gonna make me pay for it."
    jn "What about the ferris wheel?"
    jn "The tickets are cheaper."
    ka "I looove it when you pay things for me."
    jn "Nice. Now I really wouldn't be surprised if you agree on joining me in the love tunnel."
    
    hide kaelyn_d
    show kaelyn_b at right:
        ypos 1.0
        zoom 0.168
    
    ka "You never tried to ask me, right?"
    jn "Yeah, and today will not be different."

    stop music

    jn "Well, Nigel, we actually got a favor to ask..."
    
    hide nigel_a
    show nigel_g at center:
        ypos 1.0
        zoom 0.172
    
    nw "Bring it on."
    
    play music "audio/bgm/evil_thoughts.wav"
    
    ka "Well, we kinda left our backpacks in the classroom..."
    jn "Could you guys like... Get them for us?"
    nw "Hmm..."
    menu:
        nw "So, what do you say?"
        "Yes":
            jump c3s21
        "No":
            hide kaelyn_b
            show kaelyn_g at left:
                ypos 1.0
                zoom 0.168
            ka "Oh, really?"

    if enckane1 == True:
        ka "You know, Kane was about to call everyone out for a party today..."
    else:
        ka "You know, my brother was about to call everyone out for a party today..."

    ka "He would ask Missing Halloween for a show..."
    ka "But if your choice is this... I can really make him cancel it..."
    menu:
        nw "Shit... I don't wanna miss a show opportunity... I don't mind it... Will you come with me?"
        "Yes":
            jump c3s21
        "No":
            menu:
                nw "Come on!! The backpacks are too heavy for me to carry them all the way here, won't you give me a little help?"
                "Yes":
                    jump c3s21
                "No":
                    jump c3s20

label c3s20:

    if enckane1 == True:
        ka "What a shame... Then I'll call Kane and ask him to cancel it."
    else:
        ka "What a shame... Then I'll call my brother and ask him to cancel it."

    nw "Shit!! Come on, dude!!"
    nw "This happened because of you, [mcname]!!"

    #gallery image

    nw "I lost the fucking show because you chose not to help me out on a simple task!!"
    nw "Fuck you."

    "Wrong Ending 6/8: \n\"Kaelyn's Blackmail\""

    $ persistent.c3we6 = True

    $ renpy.full_restart()

label c3s21:

    hide kaelyn_g
    with dissolve

    hide jackson_h
    with dissolve

    hide nigel_g
    show nigel_c at center:
        ypos 1.0
        zoom 0.172

    stop music

    nw "Then I guess we gotta get going."

    play music "audio/bgm/ruby_hair.wav"

    pause 3

    #scene city

    nw "Soooo..."
    nw "Since we're hanging out..."

    menu:
        nw "Wanna take a look at a few things at the shopping mall? Don't think they'll mind the time."
        "Yes":
            jump c3s23
        "No":
            jump c3s22

label c3s22:

    nw "Okay then, guess we'll just keep walking and..."

    hide nigel_c
    with dissolve

    stop music

    pause 3

    "..."

    #gallery image

    "A overspeeded car hits both of you, hurting you both badly."

    play music "audio/bgm/emergency.wav"

    if persistent.enckane1 == True:
        "The driver was..."
        pause 3
        "Kane Ravat."

    "Wrong Ending 7/8:\n\"Call an Ambulance!!\""

    $ persistent.c3we7 = True

    $ renpy.full_restart()

label c3s23:

    scene bg02:
        zoom 2.0
    with fade

    hide nigel_c
    show nigel_d at center:
        ypos 1.0
        zoom 0.172

    nw "Awesome!"

    #scene shopping
    #with fade

    pause 3

    hide nigel_d
    show nigel_h at center:
        ypos 1.0
        zoom 0.172

    nw "Hey, that car nearly killed us, right?"
    nw "Well, at least we managed to not get hit."

    stop music

    "You and Nigel took a seat, and you notice two boys talking near to you."

    hide nigel_h
    with dissolve

    show dom_b at right:
        ypos 1.0
        zoom 0.179
    with dissolve

    show chester_b at left:
        ypos 1.0
        zoom 0.18
    with dissolve

    "You recognize their faces from school, they're both from 3rd grade."

    nw "Yo, the one with the black hair, that's Chester, the old guitar player from Missing Halloween."
    nw "I wouldn't be surprised if he hates me."
    "You start to listen to the conversation."

    play music "audio/bgm/fluster.wav"

    unkm "Dude, don't you miss the good times with the band?"
    
    hide chester_b
    show chester_e at left:
        ypos 1.0
        zoom 0.18
    
    cl "Of course I do, but..."
    cl "I feel like... I'm not good enough for them."
    cl "They're doing way better with Nigel, you know?"
    "You hear a little giggle from Nigel."
    unkm "Well, still, you could join the band again as a rhythm guitarrist."
    cl "I guess Matt would be kinda out of place without a guitar."
    
    hide dom_b
    show dom_g at right:
        ypos 1.0
        zoom 0.179
    
    unkm "Bullshit, you should be more confident."
    
    hide chester_e
    show chester_a at left:
        ypos 1.0
        zoom 0.18
    
    cl "Anyways, what's up with you and Heather?"

    hide dom_g
    show dom_e at right:
        ypos 1.0
        zoom 0.179

    unkm "We've been kinda... Distant."
    unkm "She kinda wears me out sometimes, you know?"
    cl "What about Matt, do you feel better?"

    hide dom_e
    show dom_g at right:
        ypos 1.0
        zoom 0.179

    unkm "That never existed, and you know that."
    
    hide chester_a
    show chester_d at left:
        ypos 1.0
        zoom 0.18
    
    cl "If you say so..."

    hide dom_g
    show dom_a at right:
        ypos 1.0
        zoom 0.179

    stop music

    unkm "Hey, Kane's calling me."

    if enckane1 == False:
        "Nigel whispers in your ear."
        nw "Oh, yeah, I forgot to mention, Kaelyn's brother's name is Kane."

    "Kane talks too loud, and that allows you to hear him through the phone."

    play music "audio/bgm/evil_thoughts.wav"

    kr "Wassup, young men."

    hide dom_a
    show dom_g at right:
        ypos 1.0
        zoom 0.179

    unkm "You're literally the same age."
    kr "And I consider myself a young man."
    kr "Come on, get the fuck out of there and join me and Scott in the car outside."

    hide dom_g
    with dissolve

    hide chester_d
    with dissolve

    "The boys left."

    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    stop music

    nw "So, how about we leave too?"
    nw "We still have to take those backpacks, right?"

    hide nigel_b
    with dissolve

    jump c3s24

label c3s24:

    #scene city

    "You and Nigel start walking through the city."

    $ chance15 = [0, 0, 0, 0, 0, 1]
    $ chanceevent9 = renpy.random.choice(chance15)

    if chanceevent9 == 1:
        jump c3s25
    else:
        jump c3s26

label c3s25:

    call ch03_matt_rng
    jump c3s27

label c3s26:

    play music "audio/bgm/ruby_hair.wav"

    show nigel_a at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Yeah, we've been kinda silent in the last few minutes, right?"

    python:
        talkevent1 = False
        ques1 = False
        ques2 = False
        ques3 = False

    while talkevent1 == False:
        menu:
            "What would you like to ask?"
            "Favorite Missing Halloween song" if ques1 == False:
                hide nigel_a
                show nigel_d at center:
                    ypos 1.0
                    zoom 0.172
                nw "Oh, of course it's \"KITTEN\"."
                nw "Heheh..."
                nw "It has my name on it."
                hide nigel_d
                show nigel_a at center:
                    ypos 1.0
                    zoom 0.172
                $ ques1 = True
            "Favourite kind of music to play" if ques2 == False:
                nw "I guess I don't have a favourite type."
                hide nigel_a
                show nigel_b at center:
                    ypos 1.0
                    zoom 0.172
                nw "They're just different vibes, you know?"
                hide nigel_b
                show nigel_c at center:
                    ypos 1.0
                    zoom 0.172
                nw "Like... Epic songs make it easier for me to make people pay attention to me with an absurd solo."
                hide nigel_c
                show nigel_b at center:
                    ypos 1.0
                    zoom 0.172
                nw "As well as romantic songs make the crowd completely gay."
                hide nigel_b
                show nigel_c at center:
                    ypos 1.0
                    zoom 0.172
                nw "And... Heheh... Of course..."
                hide nigel_c
                show nigel_d at center:
                    ypos 1.0
                    zoom 0.172
                nw "The sex songs."
                hide nigel_d
                show nigel_h at center:
                    ypos 1.0
                    zoom 0.172
                nw "They're quite the performance, you know?"
                hide nigel_h
                show nigel_a at center:
                    ypos 1.0
                    zoom 0.172
                $ ques2 = True
            "Sexuality" if ques3 == False:
                hide nigel_a
                show nigel_h at center:
                    ypos 1.0
                    zoom 0.172
                nw "I'm bisexual, and I'm an average goth enjoyer."
                nw "Could you tell? Heheh..."
                nw "Also, anyone who plays guitar increases their chances a lot."
                hide nigel_h
                show nigel_a at center:
                    ypos 1.0
                    zoom 0.172
                $ ques3 = True
            "Stop talking":
                $ talkevent1 = True

    hide nigel_a
    with dissolve

    jump c3s27

label c3s27:

    scene bg03:
    with fade

    show nigel_c at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "So, here we are."

    stop music

    play music "audio/bgm/welcome_to_rainer_high.wav"

    scene bg04
    with fade

    show nigel_d at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Oh, Oli and Mika are in the 3rd grade classroom."
    
    hide nigel_d
    show nigel_a at center:
        ypos 1.0
        zoom 0.172
    
    menu:
        nw "Wanna say \"hi\"?"
        "Yes":
            jump c3s29
        "No":
            jump c3s28

label c3s28:

    stop music


    hide nigel_a
    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    
    nw "Okay, then let's just grab those backpacks."

    scene bg05:
        zoom 1.2
    with fade

    nw "Nigel got the backpacks and you both went to your own houses after giving them back to Kaelyn and Jackson."

    scene bg02:
        zoom 2.0
    with fade

    "*Phone Ringing*"
    nw "Hey... It's me."

    play music "audio/bgm/ring.wav"

    nw "You see... I'm kinda feeling like shit..."
    nw "You know that time when Oli and Mika were standing in the 3rd grade classroom?"
    nw "We should've gone in."
    nw "Tina was locked inside one of the lockers."
    nw "So... Nobody noticed and... When she noticed the night was falling, she had a panic attack."
    nw "She's at the hospital right now."
    nw "Sorry, just wanted to let you know."
    "*Beep*"

    "Wrong Ending 8/8:\n\"ultra!p4niK\""

    $ persistent.c3we8 = True

    $ renpy.full_restart()

label c3s29:

    stop music

    scene bg05:
        zoom 1.2
    with fade

    show nigel_c at right:
        ypos 1.0
        zoom 0.172
    with dissolve

    nw "Yooo, you guys are still here."

    play music "audio/bgm/handshakers.wav"

    show oli_b at center:
        ypos 1.0
        zoom 0.186
    with dissolve
    
    show mika_b at left:
        ypos 1.0
        zoom 0.17
    with dissolve

    os "Oh, hi Nigel."
    os "And you... Are you new here?"
    os "Oh, [mcname]?"
    os "I'm Oliver Shaw."
    os "I play the drums in Missing Halloween."
    mn "New student?"
    mn "I'm Mikaella Nicolette."
    
    stop music

    hide oli_b
    show oli_a at center:
        ypos 1.0
        zoom 0.186
    
    hide mika_b
    show mika_a at left:
        ypos 1.0
        zoom 0.17

    hide nigel_c
    show nigel_a at right:
        ypos 1.0
        zoom 0.172

    "BAM"
    "POW"
    "BLAM"
    tm "Hey, since you stopped the lovey dovey dudes I didn't wanna interrupt, could you please get me out of this fucking locker?"
    
    hide oli_a
    show oli_d at center:
        ypos 1.0
        zoom 0.186
    
    play music "audio/bgm/thats_our_keytarist.wav"

    os "How the fuck did you get stuck in there?"
    tm "I was... Hiding from the crowd... They went after me like crazy."
    mn "And they..."
    mn "Locked you here?"
    tm "Nah, I accidentally locked myself."
    
    hide mika_a
    show mika_h at left:
        ypos 1.0
        zoom 0.17
    
    mn "Nice, president."

    "Suddenly, it started to rain."

    hide nigel_a
    show nigel_g at right:
        ypos 1.0
        zoom 0.172

    nw "Ah, shit."

    hide nigel_g
    show nigel_b at right:
        ypos 1.0
        zoom 0.172

    nw "Come on, I won't make you catch a cold on your first day."
    nw "I'll get those fuckers the backpacks."
    nw "You can stay here until the rain stops, and maybe..."
    
    hide nigel_b
    show nigel_h at right:
        ypos 1.0
        zoom 0.172
    
    nw "You can meet me at Raven Tattoo Studio."

    hide nigel_h
    with dissolve

    "Nigel was gone in less than one second, and Oliver managed to open the locker."

    stop music

    play music "audio/bgm/president.wav"

    show tina_b at right:
        ypos 1.0
        zoom 0.165
    with dissolve

    tm "So..."
    tm "[mcname]..."

    hide tina_b
    show tina_c at right:
        ypos 1.0
        zoom 0.165

    tm "Turns out you may not be as shitty as you seem, huh?"
    tm "Hanging out with Nigel?"

    hide tina_c
    show tina_d at right:
        ypos 1.0
        zoom 0.165

    tm "Pretty nice fucking start, I'd say."
    tm "Let me introduce myself properly."
    tm "I'm Tina Mercury, student council's president and I play the keytar in Missing Halloween."
    
    hide tina_d
    show tina_a at right:
        ypos 1.0
        zoom 0.165
    
    tm "Sorry for earlier, I was not in the best mood."
    tm "I mean... It's not like I didn't expect it already."
    
    hide tina_a
    show tina_c at right:
        ypos 1.0
        zoom 0.165
    
    tm "So yeah."
    tm "Maybe we can hang out some time."
    tm "Up to you."

    hide tina_c
    with dissolve

    hide oliver_d
    with dissolve
    
    hide mika_g
    with dissolve

    jump c3s30

label c3s30:

    stop music

    play music "audio/bgm/rain.wav"

    scene bg04
    with fade

    "As you leave the classroom, you see Matt and Juliet from far."

    show matt_b at left:
        ypos 1.0
        zoom 0.184
    with dissolve

    show juliet_e at right:
        ypos 1.0
        zoom 0.156
    with dissolve

    if chanceevent9 == 1:
        "You start to wonder how Matt got here so fast."

    js "I don't wanna go home."
    mr "Forgot your umbrella?"
    
    hide juliet_e
    show juliet_b at right:
        ypos 1.0
        zoom 0.156

    stop music
    
    js "Oh, it's you."
    js "You really know how to show up in peculiar situations..."
    
    hide juliet_b
    show juliet_c at right:
        ypos 1.0
        zoom 0.156
    
    play music "audio/bgm/matt_raven.wav"

    js "When it rains."
    mr "Let's go."
    mr "Don't want you to catch a cold."

    hide juliet_c
    with dissolve

    hide matt_b
    with dissolve

    scene bg02:
        zoom 2.0
    with fade

    centered "CHAPTER CLEAR!!"
    $ persistent.c3te = True
    $ persistent.unlockch4 = True
    centered "You unlocked \'Chapter 4\'!!"

    $ path = "4"

    call chapter_skip
