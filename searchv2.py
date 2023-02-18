cf = [7,8,9,10,8,7,6,7,8,10,12,8,10,11,7,9,8,7,6,5,6,7,7,6]
len = 20

scale = {}

scale[0] = 0
scale[1] = 2
scale[2] = 4
scale[3] = 5
scale[4] = 7
scale[5] = 9
scale[6] = 11
scale[7] = 12

def downstep(a):
 if a%12 == 0:
  b = a-1
 if a%12 == 2:
  b = a-2
 if a%12 == 4:
  b = a-2
 if a%12 == 5:
  b = a-1
 if a%12 == 7:
  b = a-2
 if a%12 == 9:
  b = a-2
 if a%12 == 11:
  b = a-2
 return b


seventh = {}

seventh[1] = [0,4,7,11]
seventh[2] = [2,5,9,0]
seventh[3]  = [4,7,11,2]
seventh[4] = [5,9,0,4]
seventh[5] = [7,11,2,5]
seventh[6] = [9,0,4,7]
seventh[7] = [11,2,5,9]

triad = {}

triad[1] = [0,4,7]
triad[2] = [2,5,9]
triad[3]  = [4,7,11]

triad[4] = [5,9,0]
triad[5] = [7,11,2]
triad[6] = [9,0,4]
triad[7] = [11,2,5]


scale = [0,2,4,5,7,9,11]

conv = {}
conv[0] = "c"
conv[2] = "d"
conv[4] = "e"
conv[5] = "f"
conv[7] = "g"
conv[9] =  "a"
conv[11] = "b"

lily = {}
lily[0] = ","
lily[1] = " "
lily[2] = "'"
lily[3] = "''"
lily[4] = "'''"

def lil(a):
 b = scale[a%7]+ (a/7)*12
 return conv[b%12]+lily[b/12]


def next(a,b,c):
 if c < 28:
  return (a,b,c+1)
 else:
  if b < 28:
   return (a,b+1,0)
  else:
   if a < 28:
    return (a+1,0,0)
   else:
    return False

music =  []


def lprint(k,s,c,t,b):
 if k <9:
  print k+1,
  print "  ->",
  print lil(b)+", " + lil(t)+", "+ lil(c)+", "+ lil(s)
 else:
  print k+1,
  print " ->",
  print lil(b)+", " + lil(t)+", "+ lil(c)+", "+ lil(s)
 return


sp ={}
cn ={}
tn ={}
bs ={}

bs[0] = lil(cf[0])

def wdata(k,s,c,t,b):
 sp[k] = lil(s)
 cn[k] = lil(c)
 tn[k] = lil(t)
 bs[k] = lil(b)


def path(k,u,v,w):
 if k == len:
  return True
 (s,c,t) = (0,0,0)
 while(not(next(s,c,t)== (28,28,28))):
  if check(k,u,v,w,s,c,t) and path(k+1,s,c,t):
   #lprint(k,s,c,t,cf[k+1])
   wdata(k+1, s,c,t,cf[k+1])
   print ("["+ str(k+1) + "](" + str(s) + " , " + str(c) + " , " + str(t) + " , "+ str(cf[k+1]) +")"),   
   return True
  (s,c,t) = next(s,c,t) 
 return False

def check(k,u,v,w,s,c,t):
 val = cor(k,u,v,w) and cor(k+1,s,c,t) and tran(k,u,v,w,s,c,t)
 return val


def cor(k,s,c,t):
 sop = scale[s%7]+ (s/7)*12
 con = scale[c%7]+ (c/7)*12
 ten = scale[t%7]+ (t/7)*12 
 bas = scale[cf[k]%7] + (cf[k]/7)*12
 val = tri(sop,con,ten,bas) or sev(sop,con,ten,bas) 
 return val

def tran(k,u,v,w,s,c,t):
 s1 = scale[u%7]+ (u/7)*12
 c1 = scale[v%7]+ (v/7)*12
 t1 = scale[w%7]+ (w/7)*12 
 b1 = scale[cf[k]%7] + (cf[k]/7)*12
 s2 = scale[s%7]+ (s/7)*12
 c2 = scale[c%7]+ (c/7)*12
 t2 = scale[t%7]+ (t/7)*12 
 b2 = scale[cf[k+1]%7] + (cf[k+1]/7)*12
 val = parallel(s1,c1,t1,b1,s2,c2,t2,b2) and resolve(s1,c1,t1,b1,s2) and coveroctave(s1,c1,t1,b1,s2,c2,t2,b2) and jump(s1,c1,t1,s2,c2,t2) and law(s1,c1,t1,b1,s2,c2,t2,b2)
 return val

#isolated harmony laws

def full(s,c,t,b):
 val = not((s%12 == c%12 and t%12 == b%12) or (s%12 == t%12 and c%12 == b%12) or (s%12 == b%12 and c%12 == t%12)) and leading(s,c,t,b)
 return val

def tria(j,s,c,t,b):
 val =  b%12 in triad[j] and not(b%12 == triad[j][2]) and t%12 in triad[j] and c%12 in triad[j] and s%12 in triad[j] and full(s,c,t,b) and ord(s,c,t,b) and range(s,c,t,b) 
 return val

def tri(s,c,t,b):
 val = (tria(1,s,c,t,b) or tria(2,s,c,t,b) or tria(3,s,c,t,b) or tria(4,s,c,t,b) or tria(4,s,c,t,b) or tria(6,s,c,t,b) or tria(7,s,c,t,b)) and doublesixth(s,c,t,b) and dimsixth(s,c,t,b)
 return val


def ord(s,c,t,b):
 val = (s>c) and (c>t) and (t>b) and triple(s,c,t,b) 
 return val

def range(s,c,t,b):
 val = (s-t) < 13
 return val


def triple(s,c,t,b):
 val = not(s%12 == t%12 == c%12) and not(s%12 == t%12 == b%12) and not(s%12 == c%12 == b%12) and not(c%12 == t%12 == b%12)
 return val

def leading(s,c,t,b):
 val = not(s%12== t%12 == 11) and not(s%12 == c%12 == 11) and not(s%12 == b%12 == 11) and not(c%12 == t%12 == 11) and  not(c%12 == b%12 == 11) and not(t%12 == b%12 == 11)
 return val

def presixth(j,s,c,t,b):
 val = tria(j,s,c,t,b) and b%12 ==triad[j][1]
 return val

def sixth(s,c,t,b):
 val = presixth(1,s,c,t,b) or presixth(2,s,c,t,b) or presixth(3,s,c,t,b) or presixth(4,s,c,t,b) or presixth(5,s,c,t,b) or presixth(6,s,c,t,b)
 return val

def doublesixth(s,c,t,b):
 val = not(sixth(s,c,t,b) and b%12 in [s%12, c%12,t%12])
 return val

def dimsixth(s,c,t,b):
 val = not(presixth(7,s,c,t,b) and not(b%12 in [s%12,c%12,t%12]))
 return val


#transition laws

def para(u,v,a,b):
 same = u == a and v == b 
 up = a > u and b > v 
 down = a < u and b < v
 fifth = (abs(u-v)== 7 or abs(u-v) == 6) and  (abs(a-b)== 7 or abs(a-b) == 6)
 octave =(abs(a-b))%12 == 0  and (abs(u-v))%12 == 0
 val = (up and fifth) or (down and fifth) or (up and octave) or (down and octave) or(same and octave)
 return val

def parallel(u,v,w,x,s,c,t,b):
 val = not(para(u,v,s,c)) and not(para(u,w,s,t)) and not(para(u,x,s,b)) and not(para(v,w,c,t)) and not(para(v,x,c,b)) and not(para(w,x,t,b))
 return val

def resolve(u,v,w,x,s):
 val = not(not(tria(3,u,v,w,x)) and (u%12 == 11 and not(s == u +1)) )    
 return val


def cover(u,v,a,b):
 up = a > u and (b > v or v == b)  
 down = a < u and ( b < v or b == v)
 octave = abs(a-b)%12 == 0 and abs(a-u) > 1
 val = (up and octave) or (down and octave)
 return val

def coveroctave(u,v,w,x,s,c,t,b):
 val =  not(cover(u,v,s,c)) and not(cover(u,w,s,t)) and not(cover(u,x,s,b)) and not(cover(v,w,c,t)) and not(cover(v,x,c,b)) and not(cover(w,x,t,b))
 return val

def jump(u,v,w,s,c,t):
 val =  abs(s-u) <13 and abs(c-v) <13 and abs(t-w) <13
 return val

def prep(j,u,v,w,x,s,c,t,b):
 val = not(seven(j,s,c,t,b) and s%12 == seventh[j][3] and u != s)and not(seven(j,s,c,t,b) and c%12 == seventh[j][3] and v != c) and  not(seven(j,s,c,t,b) and t%12 == seventh[j][3] and w != t)and not(seven(j,s,c,t,b) and b%12 == seventh[j][3] and x != b)

 return val

def preparation(u,v,w,x,s,c,t,b):
 v=prep(1,u,v,w,x,s,c,t,b) and prep(2,u,v,w,x,s,c,t,b) and prep(3,u,v,w,x,s,c,t,b) and prep(4,u,v,w,x,s,c,t,b) and prep(5,u,v,w,x,s,c,t,b) and prep(6,u,v,w,x,s,c,t,b) and prep(7,u,v,w,x,s,c,t,b)
 return v

def resol(j,u,v,w,x,s,c,t,b):
 val = not(seven(j,u,v,w,x) and u%12 == seventh[j][3] and s!= downstep(u))and not(seven(j,u,v,w,x) and v%12 == seventh[j][3] and c!= downstep(v))and  not(seven(j,u,v,w,x) and w%12 == seventh[j][3] and t!= downstep(w)) 
 return val

def resolution(u,v,w,x,s,c,t,b):
 val= resol(1,u,v,w,x,s,c,t,b) and resol(2,u,v,w,x,s,c,t,b) and resol(3,u,v,w,x,s,c,t,b) and resol(4,u,v,w,x,s,c,t,b) and resol(5,u,v,w,x,s,c,t,b) and resol(6,u,v,w,x,s,c,t,b) and resol(7,u,v,w,x,s,c,t,b)
 return val

def law(u,v,w,x,s,c,t,b):
 val =  preparation(u,v,w,x,s,c,t,b) and resolution(u,v,w,x,s,c,t,b)
 return val

#seventh

def seven(j,s,c,t,b):
 val = t%12!=s%12!=c%12!=t%12!=b%12!=s%12!=b%12!=c%12 and  s>c>t>b and t >30 and (s-t)< 13 and s%12 in seventh[j] and c%12 in seventh[j] and t%12 in seventh[j] and b%12 in seventh[j]
 return val

def sev(s,c,t,b):
 val = seven(1,s,c,t,b) or seven(2,s,c,t,b) or  seven(3,s,c,t,b) or  seven(4,s,c,t,b) or  seven(5,s,c,t,b) or  seven(6,s,c,t,b) or  seven(7,s,c,t,b) 
 return val


def harmonize(s,a,t):
    path(0,s,a,t)
    print "[0]("+str(s)+","+str(a)+","+str(t)+","+str(cf[0])+")"
#main

#path(0, 18 ,16 , 14)
#print "[0](18,16,14,7)",



#sp[0] = lil(18)
#cn[0] = lil(16)
#tn[0] = lil(14)

#print 0,
#print "  ->",
#print lil(cf[0])+", "+lil(14)+", "+lil(16)+", "+lil(18)

#output lily file

#prog = []
#prog.append("<<{")
#prog.append(sp[0]+"2 ")
#k = 1
#while k < len:
# prog.append(sp[k])
# k = k+1
#prog.append("}{")
#k = 0
#while k <len:
# prog.append(cn[k])
# k = k+1
#prog.append("}{")
#k = 0
#while k <len:
# prog.append(tn[k])
# k = k+1
#prog.append("} >>    ")
#prog.append("} lower = {\clef bass\key c \major ")
#k = 0
#while k <len:
# prog.append(bs[k])
# k = k+1
#output = ''.join(prog)
#print output




