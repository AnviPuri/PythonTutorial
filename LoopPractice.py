picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

fill="*"
blank=" "
for i in picture:
    for j in i:
        if(j):
            print(fill,end="")
        else:
            print(blank,end="")
    print(blank)