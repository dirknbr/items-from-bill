
#https://docs.python.org/2/library/itertools.html
#allow max x items
#choose bill with smallest number of items

import itertools

bills=[20,33,24.5,23.6,10,11.1,49]
items=[2,3.3,4.4,5.5,5,4.5,6] #are unique

poss={}
maxitems=max(bills)/min(items)
print maxitems
for i in range(1,maxitems):
    comb=itertools.combinations_with_replacement(items,i)
    for c in comb:
        s=round(sum(c),2) #saw some float errors
        if s not in poss:
            poss[s]=[[c,i]]
        else:
            poss[s].append([c,i])

print len(poss)

for b in bills:
    print '-------------------'
    if b in poss:
        p=poss[b]
        print b,len(p)
        #smallest number of items
        m=min([i[1] for i in p])
        #all sols
        sol=[i for i in p if i[1]==m]
        print b,sol
    else:
        print 'no sol for',b
