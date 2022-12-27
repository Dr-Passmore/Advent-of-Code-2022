import time
#stacksPart2 = [["Z", "N"], ["M", "C", "D"], ["P"]]

stacksPart2 = [["L", "N", "W", "T", "D"], 
          ["C", "P", "H"], 
          ["W", "P", "H", "N", "D", "G", "M", "J"],
          ["C", "W", "S", "N", "T", "Q", "L"],
          ["P", "H", "C", "N"],
          ["T", "H", "N", "D", "M", "W", "Q", "B"],
          ["M", "B", "R", "J", "G", "S", "L"],
          ["Z", "N", "W", "G", "V", "B", "R", "T"],
          ["W", "G", "D", "N", "P", "L"]
          ]

output = ""
with open(r'Day 5\puzzleInput.txt') as f:
    data = f.read()
moves = [m for m in data.split("\n")]

def createMovePart2 (numberofCrates, currentStack, newstack):
    print(stacksPart2)
    #newValue2 = stacksPart2
    #print(newValue2)
    stackrange = -abs(int(numberofCrates))
    
    cratesToMove = stacksPart2[currentStack]
    #cratesToMove = cratesToMove[-1]
    print(cratesToMove)
    cratesToMove = cratesToMove[stackrange:]
    
    list(cratesToMove).reverse
    
    print(cratesToMove)
   
    #print(f"{targetstack} is the target stack" )
    for i in range(numberofCrates):
    
        print(cratesToMove[i])
        print(stacksPart2[newstack])
        print(stacksPart2[currentStack])
        stacksPart2[newstack].append(cratesToMove[i])
        stacksPart2[currentStack].pop()
    print(f"The new Value {cratesToMove[i]} has moved from stack {currentStack} to {newstack}")
    print(stacksPart2)
    

for i in moves:
    movement = [s for s in i.split(" ")]
    numberofCrates = int(movement[1])
    currentStack = int(movement[3])-1
    newstack = int(movement[5])-1
    createMovePart2(numberofCrates, currentStack, newstack)
    

answer = []
for i in stacksPart2:
    if i != []:
        answer.append(i[-1])
        
        #print(i[-1], end="")

answer = [item.replace("[","").replace("]","") for item in answer]
answer = "".join(answer)
print(answer)