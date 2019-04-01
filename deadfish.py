"""
Deadfish Programming Language Interpreter
Programmed by Jonathan Todd Skinner
This code is hereby released into the public domain
Harry eased the mess
"""

# Initialization
accumulator = 0
instructions="iisiiiisiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiodddoiiiiiiiooiiiodddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddoiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiioddddddddoiiioddddddoddddddddo"
asciicode=[]
# Main program loop
for instruction in instructions:
    # Get user input
    if accumulator == 256 or accumulator == -1:
        # Overflow, reset accumulator
        accumulator = 0
    # Process input
    if instruction == 'i':
        accumulator += 1 # Increment
    elif instruction == 'd':
        accumulator += -1 # Decrement
    elif instruction == 'o':
        asciicode.append(accumulator) # Output
    elif instruction == 's':
        accumulator *= accumulator # Square
    else:
        print 'Unrecognized command.'

output = "".join([chr(c) for c in asciicode])
print output