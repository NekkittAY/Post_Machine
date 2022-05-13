class Post_Machine:
    def __init__(self,sTape,sPos,rules):
        self.sTape = sTape
        self.sPos = sPos
        self.rules = rules

    def tape(self):
        self.blank = ["#"]
        self.Tape = self.blank+self.sTape+self.blank

    def Machine(self):
        self.endTape = self.Tape
        pos=self.sPos
        i=0
        while True:
            elem = self.rules[i]
            if elem == "L":
                pos-=1
            elif elem == "R":
                pos+=1
            elif elem == "V":
                self.endTape[pos]="1"
            elif elem == "X":
                self.endTape[pos]="0"
            elif elem[0]=="?":
                if self.endTape=="0":
                    i=elem[1]-1
                else:
                    i=elem[2]-1
            elif elem == "!":
                print("result:")
                print(self.endTape)
                break
            else:
                print(self.endTape)
                break
            i+=1
            print(self.endTape)
            
