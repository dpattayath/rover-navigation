# Rover Navigation

## Description
Program to deploy and navigate rovers on the defined plateau. Shows final position of the rovers and the plateau grid after all rovers were deployed.

## Instructions
``python3 app.py``

Format:
- first line of input is parsed as plateau coordinates: [x y]
- from second line onwards, instructions will be parsed for rovers.
    - position and direction in the format: `x y direction`
    - nav commands in the format: `LMR`. Available values `L`, `M` and `R`
- instruct `end` to finish the program and print the plateau grid listing all the deployed rovers.
