N,Q = map(int, input().split())
lastAns=0
seq=[]
for i in range(N):
    seq.append([])
    
for query in range(Q):
    vals= map(int, raw_input().split())
    x,y=vals[1],vals[2] 
    if vals[0]==1:
        index=(x ^ lastAns) % N
        seq[index].append(y)
    else:
        index=(x ^ lastAns) % N
        size=y % len(seq[index])
        lastAns= seq[index][size]