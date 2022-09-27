import random
vibor1=0
vibor2=0
for c in range(0,100000):
    dver = random.randrange(1, 4)
    zritel = random.randrange(1, 4)
    if(dver==zritel):
        vibor1+=1
    if ((zritel==1) and (dver==1)) or ((zritel==1) and (dver==3)) or ((zritel==3) and (dver==1)):
        shoy=2
    elif ((zritel==1) and(dver==2)) or ((zritel==2) and (dver==1)) or ((zritel==2) and (dver==2)):
        shoy=3
    elif ((zritel==3)and(dver==2)) or ((zritel==2) and (dver==3)) or ((zritel==3) and (dver==3)):
        shoy=1
    if ((shoy==1) and (zritel==2)):
        zritel=3
    elif ((shoy==2) and (zritel==3)):
        zritel=1
    elif ((shoy==1) and (zritel==3)):
        zritel=2
    if(zritel==dver):
        vibor2+=1
print(vibor1, vibor2)

