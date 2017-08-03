def ransom_note(magazine, ransom):
    # Build a dictionary of the magazine words, and 
    # check to see if that dictionary contains the 
    # random note words.
    
    # Watch out for cases where a word may appear 
    # twice in the ransom note, but only once in 
    # the magazine (so keep a running count!).
    d = {}
    for i in magazine:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    thesum = 0
    for j in ransom:
        if j in d:
            if d.get(j) > 0:
                d[j] -= 1
                thesum+=1
            
    return thesum==len(ransom)

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if(answer):
    print "Yes"
else:
    print "No"
