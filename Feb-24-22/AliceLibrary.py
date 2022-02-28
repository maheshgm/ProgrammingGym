# Problem Link : https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/katrina-and-library-c2ed51f3/

library = input()

while library[0] == "/":
    i = 0
    pos = 0
    while library[i] != '\\':
        if library[i] == '/':
            pos = i
        i += 1
    library = library[:pos] + library[i-1:pos:-1]+library[i+1:]
print(''.join(library))

