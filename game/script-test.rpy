##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label test_chapter_1:

    #This set's up the scene with a background and music
    stop music fadeout 2.0
    scene bg residential_day
    show noise at noise_alpha zorder 100
    with dissolve_scene_full
    play music t2

    $ s_name = "???"

    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."

    show sayori 1 at t11 zorder2


    "That girl is {space=5000}{nw}"

    #wat dis
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00

    pause 0.75
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)

    "That girl is... I don't know."
    "What is this feeling? Do I recognize her from somewhere?"

    scene white
    with Dissolve(1.0)
    
    "You awaken"
    mc "Just a dream. Who was that girl? (needs work)"

    hide noise

    return

label test_chapter_2:

    #This set's up the scene with a background and music
    stop music fadeout 2.0
    scene bg residential_day
    show noise at noise_alpha zorder 100
    with dissolve_scene_full
    play music t2
    
    #TODO transparent
    show sayori 1 at t11 zorder 2
    s "You don't stand... a GHOST of a chance xD"
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    s "NORMIES GET OUT\"{space=5000}{w=0.75}{nw}"
    s 1g "REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\"{space=5000}{w=1.5}{nw}"
    
    window hide(None)
    window auto
    hide black onlayer front
    
    scene white
    with Dissolve(1.0)
    
    mc "mom it happened again"

    return
    
label test_chapter_3:

    #This set's up the scene with a background and music
    stop music fadeout 2.0
    scene bg residential_day
    show noise at noise_alpha zorder 100
    with dissolve_scene_full
    play music t2

    s "Heeeeeeeyyy!!"
    "I see a pretty girl waving at me from the distance, smiling sweetly something descriptive that actually fits."
    "That girl is Monika, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today because they're so far out of your league, but it just kind of works out because you've known each other for so long?"
    show monika 4p at t11 zorder 2

    scene white
    with Dissolve(1.0)
    
    "You awaken"
    mc "I have nothing interesting to say"
    
    return
