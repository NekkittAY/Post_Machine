start = list(input().split()) # 0 0 0
position = int(input()) # 1
rules = ["V","R","V","R","L","X","!"]
PM = Post_Machine(start,position,rules)
PM.tape()
PM.Machine()
