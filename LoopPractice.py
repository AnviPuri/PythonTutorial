picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

length=len(picture)
for i in range(0,length):
    for j in picture[i]:
        if(j==0):
            print(" ",end="")
        else:
            print("*",end="")
    print(" ")