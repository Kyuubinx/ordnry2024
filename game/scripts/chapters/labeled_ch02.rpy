label c2s0:

    stop music

    scene bg02:
        zoom 2.0
    with fade

    play music "audio/bgm/a_perfect_portrait.wav"

    centered "Chapter 2 - \"A Perfect Portrait\""

    # gallery image

    scene bg03:
    with fade

    stop music

    play music "audio/bgm/matt_raven.wav"

    "At some moments..."
    "It felt like listening to an angel singing a sweet melody."
    "At other moments..."
    "It felt like listening to an agonizing scream... But emotionally."
    "It felt good..."
    "The lyrics were deep too."
    "Besides they were almost always about teenager themes..."
    "They were full of poetry and metaphors."

    show emily_c at left:
        ypos 1.0
        zoom 0.17
    with dissolve

    es "Did you know that Matt writes all the band's lyrics?"

    show lindsey_b at right:
        ypos 1.0
        zoom 0.168
    with dissolve

    unkf "It's beautiful, isn't it?"
    unkf "You must be a newcomer."
    hide lindsey_b
    show lindsey_a at right:
        ypos 1.0
        zoom 0.168
    unkf "[mcname], right?"
    hide lindsey_a
    show lindsey_c at right:
        ypos 1.0
        zoom 0.168
    unkf "I'm Lindsey Pawns."
    hide emily_c
    show emily_g at left:
        ypos 1.0
        zoom 0.17
    es "Oh, you again."
    hide lindsey_c
    show lindsey_b at right:
        ypos 1.0
        zoom 0.168
    lp "Oh, hi, Emily."
    es "So, do you feel happy observing Matt from far?"
    hide lindsey_b
    show lindsey_e at right:
        ypos 1.0
        zoom 0.168
    lp "What do you mean?"
    hide emily_g
    show emily_h at left:
        ypos 1.0
        zoom 0.17
    es "Yeah, you'll never forget him, right?"
    es "It's been years, and you're like that."
    hide emily_h
    show emily_g at left:
        ypos 1.0
        zoom 0.17
    es "Can't move on, can't let him live his life..."
    lp "What are you talking about?!"
    lp "I literally couldn't say a word to him since we broke up!"
    es "Still, you want him back, right?"
    lp "Apparently, you want him too..."
    es "Shut up, you brat."
    menu:
        "Who will you defend?"
        "I'll stay by Lindsey's side":
            es "Hmpf."
            es "Whatever."
            hide emily_g
            with dissolve
            jump c2s2

        "I'll stay by Emily's side":
            hide lindsey_e
            show lindsey_f at right:
                ypos 1.0
                zoom 0.168
            lp "Yeah... Sorry, then..."
            lp "I shall be going..."
            hide lindsey_f
            with dissolve
            hide emily_g
            show emily_h at left:
                ypos 1.0
                zoom 0.17
            es "Heh... Lindsey's always like that."
            es "It's fucking annoying."
            es "Thanks, by the way."
            jump c2s1

label c2s1:

# TODO gwen's sprite

    stop music

    hide emily_h
    with dissolve

    "And so, after a while, the show ends."
    "No one's around."
    "Everybody left."
    "."
    "Everybody left."
    ".."
    "Everybody left."
    "..."
    "Everybody left."
    ".."
    "Everybody left."
    "."
    show gwen_mask at center:
        ypos 1.0
        zoom 0.174
    with dissolve

    play music "audio/bgm/get_gwened.wav"

    if persistent.gwened == True:
        gf "Hello again."
        gf "We've met before, right?"
        hide gwen_mask
        show gwen_dark at center:
            ypos 1.0
            zoom 0.174
        gf "So... You like to step into others?"
        hide gwen_dark
        show gwen_darker at center:
            ypos 1.0
            zoom 0.174
        gf "You could clearly see that Emily was taking things way too far..."
        hide gwen_darker
        show gwen_yet_darker at center:
            ypos 1.0
            zoom 0.174
        gf "But you'd still put Lindsey down."
        hide gwen_yet_darker
        show gwen_penumbra at center:
            ypos 1.0
            zoom 0.174
        gf "Do you feel pleasured about this?"
        #stop music        
        scene bg06:
            zoom 0.8
            xalign 0.6
        gf "I'll teach you a lesson."

        "Wrong Ending 1/2:\n\"Paranoid\""

        $ persistent.gwened = True
        $ persistent.c2we1 = True

        stop music

        $ renpy.full_restart()

    else:
        unkf "Hello."
        hide gwen_mask
        show gwen_dark at center:
            ypos 1.0
            zoom 0.174
        unkf "So... You like to step into others?"
        hide gwen_dark
        show gwen_darker at center:
            ypos 1.0
            zoom 0.174
        unkf "You could clearly see that Emily was taking things way too far..."
        hide gwen_darker
        show gwen_yet_darker at center:
            ypos 1.0
            zoom 0.174
        unkf "But you'd still put Lindsey down."
        hide gwen_yet_darker
        show gwen_penumbra at center:
            ypos 1.0
            zoom 0.174
        unkf "Do you feel pleasured about this?"
        scene bg06:
            zoom 0.8
            xalign 0.6
        unkf "I'll teach you a lesson."
        unkf "My name is Gwendolyn Forster."
        gf "Be sure not to forget."

        "Wrong Ending 1/2:\n\"Paranoid\""

        $ persistent.gwened = True
        $ persistent.c2we1 = True

        stop music

        $ renpy.full_restart()

label c2s2:

    play music "audio/bgm/old_letter_from_june.wav"

    hide lindsey_e
    show lindsey_b at right:
        ypos 1.0
        zoom 0.168
    lp "Thank you..."
    lp "Well, you know..."
    lp "Since you've been so nice to me..."
    hide lindsey_b
    show lindsey_c at right:
        ypos 1.0
        zoom 0.168
    lp "It might be nice to tell you my story with Matt."
    hide lindsey_c
    show lindsey_d at right:
        ypos 1.0
        zoom 0.168
    menu:
        lp "Do you want to hear it?"
        "Yes":
            jump c2s3
        "No":
            hide lindsey_d
            show lindsey_e at right:
                ypos 1.0
                zoom 0.168
            lp "Oh... Okay then..."
            "The show was over."
            lp "Guess I should be going by now..."
            hide lindsey_e
            show lindsey_a at right:
                ypos 1.0
                zoom 0.168
            lp "It was nice to meet you, [mcname]"

            hide lindsey_a
            with dissolve

            jump c2s4

label c2s3:

    hide lindsey_d
    with dissolve
    
    # gallery image

    stop music

    play music "audio/bgm/memoria.wav"

    lp "Well... I was in the school way before Matt got in here..."
    lp "Since his popularity grew so insanely fast, I decided to ask Tina about this \"Matt Raven\" boy everybody was talking about."
    lp "Her answer was short and clear."
    lp "\"Yeah, that dirty Dorian Gray complex brat. Stay away from him\""
    lp "Obviously, that didn't stop me."
    lp "It may seem very strange, but Matt was an introvert."
    lp "Still, he had a massive history with the girls from this school."
    lp "Even though the rumors were horrendous, the facts weren't that bad at all."
    lp "Matt actually avoids hurting people."
    lp "Sometimes he ends up hurting himself more than he should."
    lp "I was probably the first one to notice."
    lp "After all, I was his first girlfriend."
    lp "That's probably why I can have a deep dive into his lyrics, like..."
    lp "\"The lockers are filled with love letters, and I've got no perfume.\""
    lp "I can also recognize the lyrics where he's trying to express anger because of false rumors."
    lp "Probably because sometimes I get way angrier than him."
    lp "Specially when it comes to a ridiculous lie spreaded by Gwendolyn Foster."
    lp "You might've seen her already."
    lp "She always wears some kind of mask."
    lp "She said Matt hurt her face, leaving her with a horrible scar."
    lp "The rumor lasted two weeks, until Tina took her mask off in front of everyone."
    lp "Matt and I always met when we were leaving the school."
    lp "We broke up because of a long story envolving cheating rumors."
    lp "\"It's december..."
    lp "Four hours ago it was a night of november..."
    lp "And I can't find a cure for you, you're my cancer..."
    lp "And as the rain falls, my tears fall too."
    lp "Sorry, I'm just really confused and don't really know who to believe."
    lp "I love you.\""
    lp "That's all he said in a letter he left on my window."
    lp "It was the night we broke up."
    lp "The looks left all even more obvious."
    lp "I'm still enchanted by his charm, specially in a moment like this one."
    lp "The high notes can be pretty unexpected if you've only heard him talking, but not singing."
    lp "I'm obsessed by the way he can bring a thousand emotions using something that many would consider futile."
    lp "A guitar solo."
    lp "Normally, those who think music is something have never actually tried to understand it."
    lp "Others may say it's just poetry with a melody."
    lp "Music is just one of the infinite things that made me fall for Matt."
    lp "We got to know each other very slowly, and we experienced romance more maturely for the first time."
    lp "Matt's kiss with Kate Lynn and silly dates with Tina Mercury and Nigel Weekes got me kinda insecure."
    lp "I admit I was a little toxic when it came to Tina."
    lp "Their relation is extremely undefined."
    lp "It's a very deep friendship, and they always make silly jokes with each other at any opportunity."
    lp "Sometimes it even seems like Tina's trying to protect something."
    
    show lindsey_b at center:
        ypos 1.0
        zoom 0.168
    
    lp "But all of it is in the past."
    lp "It all happened two years ago."
    lp "Oh, the show is ending."
    lp "Sorry, hope I didn't took that long."
    lp "I guess I'll try talking to Matt now."

    hide lindsey_b
    with dissolve

    jump c2s4

label c2s4:

    stop music

    play music "audio/bgm/welcome_to_rainer_high.wav"

    "The members of the band slowly went out of the stage."
    "Lindsey was talking to Matt."
    "The drummer, the bassist and Tina tried to run between the crowd, escaping smoothly from the fans."
    "Nigel was laughing while being thrown up and down by part of the crowd while they screamed the name \"Kitten\"."
    "After a while, it all has stopped."

    show nigel_a at center:
        ypos 1.0
        zoom 0.172
    with dissolve

    "People went away, and the only thing you could see was Nigel, sitting on a bench."
    menu:
        "Go talk to him?"
        "Yes":
            "You walk in his direction, and greet him nicely."
            jump c2s6
        "No":
            "You decide not to talk with him, and after a while, he leaves."

            hide nigel_a
            with dissolve

            jump c2s5

label c2s5:

    stop music

    "You start feeling lonely and alone."
    "Shouldn't you... Be with your friends?"
    "Shouldn't you..."
    "Have friends?"

    show gwen_mask at center:
        ypos 1.0
        zoom 0.174
    with dissolve

    play music "audio/bgm/get_gwened.wav"

    if persistent.gwened == True:

        gf "Feeling depressed all by yourself, handsome?"
        hide gwen_mask
        show gwen_dark at center:
            ypos 1.0
            zoom 0.174
        gf "You need to learn... That every time that you're alone..."
        hide gwen_dark
        show gwen_darker at center:
            ypos 1.0
            zoom 0.174
        gf "You can't escape me..."
        hide gwen_darker
        show gwen_yet_darker at center:
            ypos 1.0
            zoom 0.174
        gf "Now we're all alone, right?"
        hide gwen_yet_darker
        show gwen_penumbra at center:
            ypos 1.0
            zoom 0.174
        gf "I'll make sure you do not to forget this, [mcname]."

        scene bg06:
            zoom 0.8
            xalign 0.6

        gf "I'll become your worst nightmare."
        gf "Game over for you."
        "Wrong Ending 2/2:\n\"Gwen's Game Over\""

        $ persistent.c2we2 = True

        stop music

        $ renpy.full_restart()

    else:

        unkf "Feeling depressed all by yourself, handsome?"
        hide gwen_mask
        show gwen_dark at center:
            ypos 1.0
            zoom 0.174
        unkf "I believe we haven't met yet..."
        hide gwen_dark
        show gwen_darker at center:
            ypos 1.0
            zoom 0.174
        unkf "Allow me to introduce myself..."
        hide gwen_darker
        show gwen_yet_darker at center:
            ypos 1.0
            zoom 0.174
        unkf "My name is Gwendolyn Forster."
        hide gwen_yet_darker
        show gwen_penumbra at center:
            ypos 1.0
            zoom 0.174
        gf "You need to learn... That every time that you're alone..."
        gf "You can't escape me..."
        gf "Now we're all alone, right?"
        gf "I'll make sure you do not to forget this, [mcname]."

        scene bg06:
            zoom 0.8
            xalign 0.6

        gf "I'll become your worst nightmare."
        gf "Game over for you."

        "Wrong Ending 2/2:\n\"Gwen's Game Over\""

        $ persistent.gwened = True
        $ persistent.c2we2 = True

        stop music

        $ renpy.full_restart()

label c2s6:

    play music "audio/bgm/be_a_rockstar"

    hide nigel_a
    show nigel_b at center:
        ypos 1.0
        zoom 0.172

    nw "Well, hello there."

    menu:
        nw "What brings you here, [mcname]?"
        "\"I liked the music\"":
            hide nigel_b
            show nigel_d at center:
                ypos 1.0
                zoom 0.172
            nw "Oh, really?"
            nw "Thank you."
        "\"Didn't really have anywhere else to go\"":
            hide nigel_b
            show nigel_d at center:
                ypos 1.0
                zoom 0.172
            nw "Heh... So you followed the current, right?"
    hide nigel_d
    show nigel_c at center:
        ypos 1.0
        zoom 0.172
    nw "You know what?"
    nw "I'm gonna tell you the band's story."
    hide nigel_c
    show nigel_a at center:
        ypos 1.0
        zoom 0.172
    nw "But before that..."
    hide nigel_a
    show nigel_g at center:
        ypos 1.0
        zoom 0.172
    nw "Have you seen a masked person somewhere?"

    if persistent.gwened == True:
        nw "Oh, so you did, huh?"
        nw "Then you probably know that's Gwen."
        nw "Now, tell me... [mcname]..."
        menu:
            nw "Are you scared of her?"
            "\"She scares the living shit out of me.\"":
                nw "Ok, first of all, fuck you."
                nw "You don't need to be fucking scared of her."
                nw "She's nothing but a victimist who likes to scare people and tear them apart."

            "\"Does she think she's a ghost or something?\"":
                nw "Good."
                nw "Yeah, it's ridiculous."
                nw "She's completely pathetic."

    else:
        nw "No?"
        nw "Okay, that's even better."
        nw "If you ever see her, that's Gwen."
        nw "Don't be scared of her."
        nw "She's nothing but a victimist who likes to scare people and tear them apart."

    hide nigel_g
    show nigel_a at center:
        ypos 1.0
        zoom 0.172

    nw "Anyways, the band."

    hide nigel_a
    show nigel_b at center:
        ypos 1.0
        zoom 0.172

    stop music
    
    play music "audio/bgm/nigels_practice_solo"

    nw "Let's start with the basics..."
    nw "Matt and Oliver, the drummer."
    nw "Matt Raven and Oliver Shaw have been playing together since they met each other in a Halloween party about five years ago, both of them were twelve."
    
    hide nigel_b
    show nigel_c at center:
        ypos 1.0
        zoom 0.172
    
    nw "That's how the band came to be called \"Missing Halloween\"."
    nw "Also, I'm not the first guitar player the band has played with."
    nw "Besides Matt, of course, they had another guitarrist called Chester."
    
    hide nigel_c
    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    
    nw "Chester Lindemann."
    nw "He didn't last too long because he was too insecure with his abilities with a guitar."

    hide nigel_b
    show nigel_c at center:
        ypos 1.0
        zoom 0.172

    nw "Bonnie Mee came some time after he left the band, she's the bassist."
    nw "Matt and Bonnie know each other since kindergarten."
    nw "Her brother had just given up his interest in music, leaving behind two guitars, a flute, a ukulele and a melodica for the girl."
    nw "But nothing seems to be more important to her than the gorgeous bass got on her sixteenth birthday."
    
    hide nigel_c
    show nigel_d at center:
        ypos 1.0
        zoom 0.172
    
    nw "She played that same bass today."
    nw "She came back to school last year, that's when she found Matt again."
    nw "You see... The band can be old, but we actually started playing together only last year's december."
    nw "Anyways, they got closer again really quick."

    hide nigel_d
    show nigel_c at center:
        ypos 1.0
        zoom 0.172

    nw "She only started hanging out with us a little less when she started dating Andy Williams."
    nw "Not that Andy's a bad guy, I don't dislike him or whatever."
    
    hide nigel_c
    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    
    nw "But facts are facts, you know?"
    nw "Andy's completely obsessed with Bonnie and all her cute way of living that kinda fits with her being a 5'2."
    
    hide nigel_b
    show nigel_c at center:
        ypos 1.0
        zoom 0.172

    nw "Bonnie has a cute energy and is frequently jumping nicely while on stage, slapping that bass of hers."
    
    hide nigel_c
    show nigel_d at center:
        ypos 1.0
        zoom 0.172
    
    nw "The band stood a while with a formation of just Matt, Oliver and Bonnie."
    
    hide nigel_d
    show nigel_h at center:
        ypos 1.0
        zoom 0.172
    
    nw "That's when I came in."

    hide nigel_h
    show nigel_a at center:
        ypos 1.0
        zoom 0.172

    nw "At first, my role was just to replace Chester."
    
    hide nigel_a
    show nigel_b at center:
        ypos 1.0
        zoom 0.172
    
    nw "But I guess I ended up impressing them a little too much."
    
    hide nigel_b
    show nigel_c at center:
        ypos 1.0
        zoom 0.172
    
    nw "I could do many things that Chester couldn't."
    
    hide nigel_c
    show nigel_d at center:
        ypos 1.0
        zoom 0.172
    
    nw "Bend, tapping, pinch harmonics, sweep..."

    hide nigel_d
    show nigel_c at center:
        ypos 1.0
        zoom 0.172

    nw "But it all started slowly, when I met Matt for the first time."

    hide nigel_c

    # gallery image

    nw "First of all, it's nice to know that my big brother, Michael, is in the 3rd grade, same class as Matt."
    nw "But that's not the actual point."
    nw "On a normal sunny day, I was taking a walk outside of my apartment's building."
    nw "Suddenly, I found a cat walking through the park."
    nw "I was obsessed."
    nw "I tried to get closer, until..."
    nw "At a certain moment..."
    nw "The cat ran into a boy's lap, and started to purr."
    nw "The boy was alone."
    nw "\"Hey, Kitten.\", he said."
    nw "He started to play with the cat, as I tried to silently go away."
    nw "That's when..."
    nw "He looked at me and said..."
    nw "\"Hey, I'm talking to you.\""
    nw "Confused, I answered, \"What? Me? \'Kitten\'?\""
    nw "And he said..."
    nw "\"Yeah... Nice haircut.\""
    nw "I... Guess I got too embarassed and went home at that very second."
    nw "Some weeks after that, I was helping my uncle out with the instrument store."
    nw "Matt came in and asked for a pedal for his guitar."
    nw "That's when he told me his name and I told him mine."
    nw "Before he could test the pedal, I picked up a guitar and checked if it was well tuned."
    nw "I mean... Not in a normal way."
    nw "I played the very beggining of the solo in The Drug In Me Is You, by Falling In Reverse."
    nw "We started talking."
    nw "I told him I had a red Stratocaster and a black Warlock guitar."
    nw "He told me he had a black Stratocaster and a red Telecaster."
    nw "He also told me he kept the cat, and named him \"Muffin\"."
    nw "He... kept calling me \"Kitten\" and asked me to join the band."
    nw "That's basically how it all started."
    nw "The insanely overexpressive Missing Halloween solos..."
    nw "Not that I want to brag or anything, of course."
    nw "I also started doing the rasping and distorted backing vocals for the songs."
    nw "And at some point, we decided we needed a keyboard player."
    nw "We thought about Avril Cosette at first, but it was just... Not her vibe."
    nw "Avril plays the piano and likes soft songs, classical songs, it wouldn't work out."
    nw "That's when we got determined to start a fucking revolution to take Colson Vee out of the student council."
    nw "And the perfect way to start it was asking Tina Mercury to play the Keytar, keeping in mind she was the vice president at that time."
    nw "She was the one who started calling me \"Deathcore\", and that's how my stage name came to be..."
    nw "\"Kitten Deathcore\"."
    nw "The band was ready, we only needed an ocasion to play..."
    nw "And the school's talent show was the perfect ocasion."
    nw "So there we were, ready to make our empire rise."
    nw "The fact that Avril had just played Moonlight Sonata was so comic."
    nw "Colson, who was the student council's president in that time, didn't like us that much."
    nw "He's actually a brat who begs for attention."
    nw "He tried to make fun of us in front of everyone before we were on stage."
    nw "But everyone ended up laughing when I silenced him with a noisy pinch harmonic, right after saying \"Muted\"."
    nw "It was last year's december."
    nw "That's when we played our first song together, \"BAD BLOOD\"."
    nw "I savoured every single note of it with my Warlock."
    nw "That wasn't the only song we played, though."
    nw "I also played \"june\" in my Stratocaster."
    nw "It's something totally different."
    nw "It's a slow romantic song."
    nw "And our second show for the school was today."
    nw "We played two brand new songs, \"happy valentine's death\" and \"when it rains\"..."
    nw "It felt good."
    nw "People love us."

    show nigel_g at center:
        ypos 1.0
        zoom 0.172

    nw "Oh, wait a minute."
    nw "Isn't that..."

    show gwen_mask at right:
        ypos 1.0
        zoom 0.174
    with dissolve

    nw "Gwen."
    nw "[mcname], stay back. I'll take care of this."

    scene bg02:
        zoom 2.0
    with fade

    stop music

    play music "audio/bgm/my_soft_side.wav"

    centered "CHAPTER CLEAR!!"
    $ persistent.c2te = True
    $ persistent.unlockch3 = True
    centered "You unlocked \'Chapter 3\'!!"

    $ path = "3"

    call chapter_skip
