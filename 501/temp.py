import datetime
now = datetime.datetime.now()
a=open('a.txt','w')
a.write('aa    ')
a.write(str(now))
a.close()