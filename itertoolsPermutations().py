from itertools import permutations
s,t=map(str,input().split())
t=int(t) 
res=[''.join(tups) for tups in permutations(s,t)]
print(*res,sep='\n')
