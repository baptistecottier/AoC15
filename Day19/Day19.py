def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s

with open("Day19/input") as f:
    input=f.read().splitlines()
    transformations=input[:-2]
    molecule=input[-1]

created_molecules=[]
for transformation in transformations:
    atom_a, atom_z=transformation.split(' => ')
    for i in range(molecule.count(atom_a)):
        created_molecules+=[nth_repl(molecule,atom_a,atom_z,i+1)]

count=len(list(set(created_molecules)))
print(count)
