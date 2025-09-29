print("\033c\033[43;30m\nfile to load?")
def loads(files):
    a=[]
    aa=[]
    s=""
    f1=open(files,"r")
    s=f1.read()
    f1.close()
    arr=s.split("\n")
    for n in arr:
        n=n.strip()
        arr2=n.split(",")
        aa=[]
        for nn in arr2:
            nn=nn.strip()
            if nn!="":
                aa=aa+[nn]
        if aa!=[]:
            a=a+[aa]    
    return a

files=input()
aa=loads(files)
print(aa)