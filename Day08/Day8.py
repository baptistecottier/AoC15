with open("Day8/input.txt") as f:
    lines=f.read().splitlines()
    text=0
    for line in lines:
        text=line.replace('\"')
        if len(line)-len(eval(line)) != text :
            print(text, len(line), len(eval(line)))
            print(line)
            print(eval(line))
    


    # Tentatives : 1342