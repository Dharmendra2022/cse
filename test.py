
import numpy as np;

a=[45,65,78,25,12,6,15,50];
n=len(a);

def insertion(b):
    m=len(b)
    for i in range(m):
        y=b[i];
        j=i-1;
        while j>-1 and y<b[j]:
            b[j+1]=b[j];
            j=j-1;
        b[j+1]=y;
    return b;
s=insertion(a)
print(s)
