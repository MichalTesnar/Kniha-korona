RECURSION_DEPTH = 23
posts = 0

class ctenar:
    def __init__(self):
        self.counter = 7

    def removeCounter(self):
        self.counter -= 1

    def replicate(self):
        ctenari.append(ctenar())


ctenari = []
ctenari.append(ctenar())

# Replikační cyklus pro rekurzivní tvorbu fraktálu
for k in range(RECURSION_DEPTH):
    for p in range(len(ctenari)):
        if ctenari[p].counter>0:
            ctenari[p].removeCounter()
            posts +=1
            ctenari[p].replicate()

print(posts)