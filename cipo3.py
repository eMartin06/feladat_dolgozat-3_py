class Cipő:
    def __init__(self,ciporingli,cipoanyag, cipoméret, tulnév):
        self.ringli = ciporingli
        self.anyag = cipoanyag
        self.méret = cipoméret
        self.név = tulnév
        
    # def nemész(self,ringli,anyag, méret, nem):    
    #     if self.méret >= 35 and self.méret <= 41:
    #         return "női" 
    #     else:
    #         return "férfi"        
# http://www.cipeszmester.hu/cipofuzok/cipofuzo
    def ringlivalt(self):
        if self.ringli == "2":
            return(f'Kicsi: 45,Közepes: 75,Nagy: 75')
        elif self.ringli == "3":
            return(f'Kicsi: 60,Közepes: 75,Nagy: 90')
    def anyagválszt(self):
        if self.anyag=='b':
            return 'bőr'
        elif self.anyag =='m':
            return 'mesterséges anyag'

cipolista=[]
for _ in range(1):
    név=input('Add meg a cipő tulajdonosát! ')
    ringli=input('Add meg egy cipő ringli számát! ')
    anyag=input('Add meg a cipő anyagát (bőr -b; Mesterséges anyag -m)! ')
    méret=int(input('Add meg a cipő méretét! '))
    lista = Cipő(név,ringli, anyag, méret)
    cipolista.append(lista)
for cipolistak in cipolista:
    print(cipolistak.név,cipolistak.ringli(),'az anyaga',cipolistak.anyag(),'.')
