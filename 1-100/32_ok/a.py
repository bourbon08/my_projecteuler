def QPL(m_list):
    if len(m_list) == 1:
        yield m_list
    for i in range(len(m_list)):
        restlist = m_list[0:i]+m_list[i+1:]
        for subres in QPL(restlist):
            yield [m_list[i]]+subres;
 
def cal(ml):
    a = 10*ml[0]+ml[1];
    b = 100*ml[2]+10*ml[3]+ml[4];
    c = 1000*ml[5]+100*ml[6]+10*ml[7]+ml[8];
    return a*b == c
 
def cal2(ml):
    a = ml[0];
    b = 1000*ml[1]+100*ml[2]+10*ml[3]+ml[4];
    c = 1000*ml[5]+100*ml[6]+10*ml[7]+ml[8];
    return a*b == c
 
sum = 0;
prolist = [];
for pql in QPL([1,2,3,4,5,6,7,8,9]):
    if cal(pql) == True:
        t = 1000*pql[5]+100*pql[6]+10*pql[7]+pql[8];
        if t not in prolist:
            sum += t;
            prolist.append(t)
    if cal2(pql) == True:
        sum += 1000*pql[5]+100*pql[6]+10*pql[7]+pql[8];
        if t not in prolist:
            sum += t;
            prolist.append(t)
print(sum)