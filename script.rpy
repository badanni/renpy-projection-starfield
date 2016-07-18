﻿init:
    # Simple black background to show under the stars 
    define space = Solid((0, 0, 0, 255))  

    # Create the starfield displayables. Optional keyword arguments can tweak the default display.
    $starfield = ProjectionStarfield(star_amount=128, depth=16, perspective=128.0, speed=5)

    # Create another with an image used.
    image star:
        "Star Filled-48.png"
        zoom 0.5
        #linear 2.0 rotate 360
        #repeat

    $i_starfield = ProjectionStarfield(star_amount=128, depth=16, perspective=128.0, speed=5, image="star")       
 
# Screens where the displayables are shown 
screen starfield:
    add space
    add starfield

screen starfield_with_image:
    add space
    add i_starfield
 
# The game starts here.
label start:

    show screen starfield
    
    "Space."
    
    "The final frontier."

    "These are the voyages of the starship Enterprise."

    hide screen starfield
    show screen starfield_with_image

    "It's continuing mission, to explore strange new worlds."
    return