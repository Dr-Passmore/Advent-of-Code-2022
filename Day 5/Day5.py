'''--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
'''

#teststacks
'''
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 '''

stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]

'''stacks = [["L", "N", "W", "T", "D"], 
          ["C", "P", "H"], 
          ["W", "P", "H", "N", "D", "G", "M", "J"],
          ["C", "W", "S", "N", "T", "Q", "L"],
          ["P", "H", "C", "N"],
          ["T", "H", "N", "D", "M", "W", "Q", "B"],
          ["M", "B", "R", "J", "G", "S", "L"],
          ["Z", "N", "W", "G", "V", "B", "R", "T"],
          ["W", "G", "D", "N", "P", "L"]
          ]
'''
print(stacks)
output= ""

#PuzzleStacks
'''
        [J]         [B]     [T]    
        [M] [L]     [Q] [L] [R]    
        [G] [Q]     [W] [S] [B] [L]
[D]     [D] [T]     [M] [G] [V] [P]
[T]     [N] [N] [N] [D] [J] [G] [N]
[W] [H] [H] [S] [C] [N] [R] [W] [D]
[N] [P] [P] [W] [H] [H] [B] [N] [G]
[L] [C] [W] [C] [P] [T] [M] [Z] [W]
 1   2   3   4   5   6   7   8   9 
 '''
def crateMove (numberofCrates, currentStack, newstack):
    while numberofCrates != 0:
        newValue = stacks[currentStack-1]
        newValue.reverse
        newValue = newValue[-1]
        stacks[newstack-1].append(newValue)
        stacks[currentStack-1].pop()
        numberofCrates -= 1
        print(f"The new Value {newValue} has moved from stack {currentStack} to {newstack}")
        print(stacks)

with open(r'Day 5\testInput.txt') as f:
    data = f.read()
moves = [m for m in data.split("\n")]


for i in moves:
    movement = [s for s in i.split(" ")]
    numberofCrates = int(movement[1])
    currentStack = int(movement[3])
    newstack = int(movement[5])
    crateMove(numberofCrates, currentStack, newstack)
    
for i in stacks:
    print(i)
    output = output + str(i[0])

print(output)
