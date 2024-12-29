# ChromaCode 

## Overview

ChromaCode is an esoteric 2d programming language that operates on infinite memory, a stack and a program image. Each instruction is a color on an image that performs operations like moving the program counter, manipulating stack values, and basic arithmetic.

The program counter is always moving, starting out moving to the right and the direction being able to be altered by instructions.


## Usage:
1. Install PIL and Numpy.
2. Create your program or choose one from the example folder.
3. Run the script using `py main.py {path_to_program}.png`
4. The program will be executed and the output will be displayed in the console.


## Instructions:
    #000088 - Load: Put a value from memory onto the stack.
    
    #008800 - Store: Pop a value from the stack, and set the current memory cell to that value.
    
    #add8e6 - IncPtr: Moves the memory pointer to the right.
    
    #5454eb - DecPtr: Moves the memory pointer to the left.
    
    #ad0000 - Pop: Pops the stack.
    
    #ff9100 - Dup: Duplicates the top value on the stack.
    
    #ffd000 - Swap: Swaps two top stack values.
    
    #800080 - Inc: Increments the top value on the stack.
    
    #ffc0cb - Dec: Decrements the top value on the stack.
    
    #ff00ff - Mul: Multiplies the two top values on the stack.
    
    #0000ff - Left: Set the program counter direction to "Left".
    
    #000050 - Right: Set the program counter direction to "Right".
    
    #00ff00 - Up: Set the program counter direction to "Up".
    
    #005000 - Down: Set the program counter direction to "Down".
    
    #c4c4c4 - Mirror: Set the program counter direction to the opposite of the current one.
    
    #40e0d0 - Random Direction: Set the program counter direction to a random one.
    
    #ffffff - Skip: Skip one pixel, useful for crossings.
    
    #1c1b1b - Conditional Skip: Skip one pixel, if the top stack value isnt zero.
    
    #00ffff - PrintNum: Pops the stack and prints a number.
    
    #008080 - PrintStr: Pops the stack and prints the Unicode character of the value.
    
    #4b0082 - Input: Pushes a number inputted by user to the stack if the input is a number, if it's a string, pushes it to the stack in reverse order.
    
    #8b0000 - End: Terminates the program.
    
