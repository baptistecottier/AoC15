with open("Day1/input.txt") as f: 
    instructions=f.read()
    print("The instructions take Santa to floor :",instructions.count('(')-instructions.count(')'))

    floor=0
    i=0
    while(floor!=-1):
        floor+=(-1+2*(instructions[i]=='('))
        i+=1
    print("Santa reaches the absement after the "+str(i)+"-th instruction")

    