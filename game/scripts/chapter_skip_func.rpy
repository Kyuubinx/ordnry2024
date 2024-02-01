init python:
    path = "1"

label chapter_skip:

    menu:
        "Would you like to proceed to the next chapter?"
        "Yes":
            $ renpy.jump ("c" + path + "s0")
        "No":
            $ renpy.full_restart()
