# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define adam = Character("Adam")
define johanna = Character("Johanna")
define matilde = Character("Matilde")
define artur = Character("Artur")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show adam_placeholder

    # These display lines of dialogue.

    "*beep beep* *beep beep*"

    adam "*yawn* *groan* Hmm?"

    "I look at the clock next to me. The time reads 07:35."

    adam "Mmh. I've still got time…"

    "…I overslept."

    adam "7:35!?"

    "I jump out of bed, frantically looking for my clothes."

    # This ends the game.

    return
