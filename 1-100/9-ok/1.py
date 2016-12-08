for u in range(1,35):
    for v in range(1,35):
        a=u*u-v*v;b=2*u*v;c=u*u+v*v
        if(a+b+c==1000) and (a*a+b*b==c*c):
            print(a,b,c,a*b*c)
				
			#200,275,425
			