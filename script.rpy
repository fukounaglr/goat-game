# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("EGG")


# The game starts here.

label start:

    "uh... hello?"

    "oh wait..."

    scene bg room
    with Dissolve(.5)

    show goat home normal
    with Dissolve(.5)

    "Better? ..."

    window hide
    "Oh. I should ask your name..."

    "You don't want to tell?\nIt's ok, i understand."

    "My name? right..."

    "You can call me... EGG.\nDon't think too much about it."

    window hide
    with Dissolve(.5)

    window show
    with Dissolve(.5)
    show goat home paw

    "It's pretty early, isn't it?"

    "We used to wake up late..."

    window hide
    with Dissolve(.5)
    show goat home normal

    "...\nAnyway."

    "I still have some time before the classes.\nMight do something."

    "What do you think?"

menu:
    "have a breakfast":
        jump choice1_yes

    "do nothing":
        jump choice1_no

label choice1_yes:

    $ menu_flag1 = True

    "Oh, yeah. i probably should."

    window hide
    hide goat
    with Dissolve(.5)

    pause .5

    scene bg kitchen
    show goat home normal
    with Dissolve(.5)

    "Hmm... what should i eat?"

    menu:
        "ramen":
            $menu_flag2 = False

            "Yeah, i dont really wanna cook anything"
            "Just ramen and sandwich. that'll be enough."

        "pasta":
            $menu_flag2 = True

            "Ohh. i usually cook it every day.\ntricolour pasta with nugget sticks."
            "Though lately i dont have enough energy to cook every day."
            "But today will be different, i guess!"


    window hide
    hide goat home normal
    scene bg none
    with Dissolve(.5)

    pause .5

    scene bg kitchen
    show goat home thinking
    with Dissolve(.5)

    "Mmm. fueled."

    "There's still time left... I'm gonna do stuff on PC."

    jump choice1_done

label choice1_no:

    $ menu_flag1 = True

    "Mm. yeah."

    "I'm not really supposed to be awake anyway."

    "Guess i'll just lie in bed til its time to go."

    jump choice1_done


label choice1_done:

    window hide
    hide goat
    with Dissolve(.5)

    pause .3

    scene bg none
    with Dissolve(.5)

    pause 1.5

    scene bg room
    show goat home normal
    with Dissolve(.5)

    "ok, i should get going now."
    "Wait, i need to change..."

    window hide
    hide goat
    with Dissolve(.5)



    pause .5

    show goat skirt normal
    with Dissolve(.5)

    "what do you think?..."

menu:
    "cute":
        "really? yeah... it's cute..."

        window hide
        show goat skirt unsure
        with Dissolve(.5)

        "but i dont know... i'm scared..."

        menu:
            "it's okay":
                $ menu_flag3 = True

                show goat skirt normal
                with Dissolve(.5)

                "..."

                "what?..."

                "you really think so?"

                "..."

                "you dont say nice things very often..."

                "... thanks..."
                window hide
                jump choice2_done



            "...":

                jump choice2_done

    "...":
        $ menu_flag3 = False
        "...?"
        menu:
            "what even are you.":
                show goat skirt unsure
                with Dissolve(.5)

                "..."
                menu:
                    "abomination.":
                        "..."
                        pause 1

                        jump choice2_done



label choice2_done:

    pause .5
    "it's too cold anyway"


    window hide
    hide goat
    with Dissolve(.5)

    pause .5

    show goat home school
    with Dissolve(.5)

    "ok we can go now."

    window hide
    hide goat
    scene bg none
    with Dissolve(.5)

    pause 1

    scene bg outside

    show goat outside going:
        xalign 0.8
        yalign 1.0

    with Dissolve(.5)

    pause .5

    "it's spring..."

    "and it's getting warmer..."


    window hide
    pause 0.5

    "I dont like cold."

    "Heat is not great too, but at least you're not freezing."

    window hide
    pause 1

    "I thought that with the spring my seasonal depression would end."

    "well, i guess it's just no longer seasonal."

    "..."

    window hide
    scene bg none
    hide goat
    with Dissolve(.5)

    pause 2

    scene bg school enterance
    show goat school eyesclosed
    with Dissolve(.5)

    "of course i'm late again"

    window hide

    show goat school normal

    "i need to find the classroom tho."

    show goat school eyesclosed
    "3-0-1... third floor. sigh."

    window hide

    scene bg none
    hide goat
    with Dissolve(.5)

    pause .5

    scene bg school classroom
    show goat school normal:
        xalign 0.2
        yalign 1.5
    with Dissolve(.5)

    "teacher isn't here yet."

    "(classmates wave to egg)"

    e "..."














    # return
