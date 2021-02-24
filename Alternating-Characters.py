T = "AAAAA"
for test in range(T): 
    line = input() 
    prev, changes  = line[0], 0
    for ch in line[1:]:
        if prev == ch:
            changes += 1
        prev = ch            
    print(changes)