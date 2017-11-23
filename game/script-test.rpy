##This is an example scene
##It teaches you about making mods, and is also a code example itself!

#Each section needs a label, this is how we will call the scene in or parts of the script
label test_chapter_1:
    stop music fadeout 2.0
	$ s_name = glitchtext(10)

    #This set's up the scene with a background and music
    #scene bg club_day
    #with dissolve_scene_full
    #play music t3

    # Most of the story will be told using "Say" statements
    # They take the form of a short nickname, follow by their statement in quotes.
    s "[player]..."

	show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
	
	
    #You will also want to show characters of other images
    show sayori 1 at t11 zorder 2
    s "holy shit im dead af"
	s "im a ghost or something"
	s "OOOooooooOOOOOOO"
	
	mc "omg"

    #Character images are their name followed by a number and letters
    #The trailing letter is generally the facial expression

    #The number is the pose

    #Faces and poses can be changed inline if you are not changing positions of the character(s).
    #For face reference, view the image files of the character you are trying to manipulate,
    #and choose the face image letter that most accurately displays the emotion you are trying to convey.

    #Refer to the Character Pose Cheat Sheet(This doesn't exist yet!) to find out which number corresponds to which pose!

    

    scene white
    with Dissolve(1.0)
	
	"You awaken in a puddle of your own sweat"
	mc "Wow, I really need to lay off the drugs"

    return

label test_chapter_2:
	stop music fadeout 2.0
	
	#TODO transparent
	show sayori 1 at t11 zorder 2
	s "You don't stand... a GHOST of a chance xD"
	stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "NORMIES GET OUT\"{space=5000}{w=0.75}{nw}"
    m 1g "REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\"{space=5000}{w=1.5}{nw}"
	
	window hide(None)
    window auto
    hide black onlayer front

    return
	
label test_chapter_3:

	show sayori 1 at t11 zorder 2
	s "so like, do you want to catch a movie later or something?"
	
	show monika 2 at t12 zorder 20
	m "rejected!"
	
	"Monika proceeds to beat the shit out of Sayori"
	
	mc "nice"
	
	return
