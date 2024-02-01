label ch05_secev_mike:

    "You suddenly find yourself in the Weekes' apartment."
    
    show mike_a at right:
        ypos 1.0
        zoom 0.187
    with dissolve
    
    mw "Oh, [mcname]."
    mw "What are you doing here?"
    mw "Did you… Get lost or something?"
    
    hide mike_a
    show mike_b at right:
        ypos 1.0
        zoom 0.187
    
    mw "I see…"
    mw "I'm actually waiting on someone…"
    
    hide mike_b
    show mike_c at right:
        ypos 1.0
        zoom 0.187
    
    mw "Oh, he's here."

    show taylor_b at left:
        ypos 1.0
        zoom 0.185
    with dissolve

    unkm "Oh, hi Mike."
    mw "[mcname], this is Taylor Lanza."
    
    hide taylor_b
    show taylor_c at left:
        ypos 1.0
        zoom 0.185
    
    tl "Yo."
    mw "You didn't say you were coming over."
    tl "Still, you knew about it."
    mw "Yeah... You're right..."
    tl "I wanted to make a surprise."
    
    hide taylor_c
    show taylor_b at left:
        ypos 1.0
        zoom 0.185
    
    tl "Is Nigel in?"

    hide mike_c
    show mike_b at right:
        ypos 1.0
        zoom 0.187

    mw "Nah, he's getting a new tattoo."
    tl "So you know where he is."
    tl "Impressive."

    hide mike_b
    show mike_e at right:
        ypos 1.0
        zoom 0.187

    mw "We've been... Talking."
    tl "For how long?"
    mw "Some minutes."
    tl "Miraculously."

    hide mike_e
    show mike_b at right:
        ypos 1.0
        zoom 0.187

    mw "Why don't you come in?"
    "You decide to go back to Raven Tattoo Studio."

    hide mike_b, taylor_b
    with dissolve

    $ persistent.turn_on_secev_c5 = False
