import itertools
import time
start=time.time()
ll=[1,2,5,10,20,50,100,200]
l2=[]
count=0
for a0 in range(0,201):
    for a1 in range(0,101):
        for a2 in range(0,41):
            if ll[0]*a0+ll[1]*a1+ll[2]*a2>200:break
            for a3 in range(0,21):
                if ll[0]*a0+ll[1]*a1+ll[2]*a2+ll[3]*a3>200:break
                for a4 in range(0,11):
                    if ll[0]*a0+ll[1]*a1+ll[2]*a2+ll[3]*a3+ll[4]*a4>200:break
                    for a5 in range(0,5):
                        for a6 in range(0,3):
                            for a7 in range(0,2):
                                if ll[0]*a0+ll[1]*a1+ll[2]*a2+ll[3]*a3+ll[4]*a4+ll[5]*a5+ll[6]*a6+ll[7]*a7==200:
                                    count+=1
                        #l2.append([a0,a1,a2,a3,a4,a5])

print(count)
end=time.time()
print('运行了'+str(end-start))                      