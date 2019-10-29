PRI=0
SEG=1
SIG=0
for I in range(3,1,180):
    SIG=PRI+SEG
    PRI=SIG
    SEG=SIG
    I=I+1
print(SIG)
