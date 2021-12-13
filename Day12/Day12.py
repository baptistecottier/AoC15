import re

with open("Day12/input.txt") as f:
    s=f.read()
    numbers = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)
    value=0
    for number in numbers:
        value+=sum([int(item) for item in number.split(',')])
    print("Part I : ",value)


    pattern="{(.*?)}"
    to_test= re.findall(pattern, s)
    value_bis=0
    s=re.sub("""{^[^{]+$"[a-z]":"red"^[^}]+$}""",'0',s)
    numbers = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)
    value=0
    for number in numbers:
        value+=sum([int(item) for item in number.split(',')])
    print("Part II : ",value)



    # 104046 34786