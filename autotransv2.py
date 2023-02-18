
number = ["sing","plu"]
gender = ["fem","masc","neut"]
person = ["1st","2nd","3rd"]
case =   ["subj","gen","obj"]


categories = [] 
for n in number:
 for g in gender:
  for p in person:
   for c in case:
     categories.append((n,g,p,c))


type={}
type["number"] = [cat[0] for cat in categories]
type["gender"] = [cat[1] for cat in categories]
type["person"] = [cat[2] for cat in categories]
type["case"] = [cat[3] for cat in categories]

sym = {"number":0,"gender":1,"person":2,"case":3}


def sandhi(s):
 aux = "" 
 intron = -1
 exon = -1   
 for k in range(len(s)):
   if s[k]=="(":
     intron = k  
     for m in range(k, len(s)):
       if s[m]==")":
         exon = m  
         aux = s[intron+1:exon]
 if intron!=-1:         
  if s[intron-int(aux[1])] == aux[0] and aux[2]=="+" :
    return s[0:intron]+aux[3]+s[exon+1:]
  else:
    return s[0:intron]+s[exon+1:]
 else:
    return s
   

def sandhicomb(s):
 aux = "" 
 intron = -1
 exon = -1   
 for k in range(len(s)):
   if s[k]=="(":
     intron = k  
     for m in range(k, len(s)):
       if s[m]==")":
         exon = m  
         aux = s[intron+1:exon]
 if intron!=-1:         
    return [s[0:intron]+aux[3]+s[exon+1:], s[0:intron]+s[exon+1:]]
 else:
  return [s]
        

def group(h,l):
 aux = []
 for a in l:    
  if a[0]== h:
    if not a in aux:
      aux.append(a[1])
 return aux

def kind(l):
 aux = []
 for a in l:
  if not a[0] in aux:
      aux.append(a[0])
 return aux

def fix(l):
 c = l[0][0]
 aux = []
 for n in range(len(l)):
  if l[n][0]==c:
    aux.append(l[n][1])
  else:
   return [aux]+fix(l[n:]) 
 return [aux]
 

def fix2(l):
 c = l[0][0]
 aux = []
 for n in range(len(l)):
  if l[n][0]==c:
    aux.append(l[n])
  else:
   return [aux]+fix2(l[n:]) 
 return [aux] 
 
 
def doublemap(f,l):
 return map(lambda s:map(f,s), l) 

def tensor(l):
 if len(l) == 1:
  return [[x] for x in l[0]]
 aux = []
 for x in l[0]:
    for y in tensor(l[1:]):  
     aux.append([x] + y)        
 return aux


def intersection(a,b):
 val = []
 for x in a:
  if x in b:
   val.append(x)
 return val

def intersection3(a,b,c):
  return intersection(intersection(a,b),c)

def intersection4(a,b,c,d):
  return intersection(intersection3(a,b,c),d)


def listproj1(list, constraint1):
 return [lex[sym[constraint1]] for lex in list]

def listproj2(list, constraint2):
 return [(lex[sym[constraint2[0]]], lex[sym[constraint2[1]]]) for lex in list]

def comp2(element, constraint2):
 return (element[sym[constraint2[0]]], element[sym[constraint2[1]]])

def prepverb(x):
 for n in range(len(x)):
  if x[n]=="|":
   return [x[:n],x[n+1:]]         
 return False

      
class Word:
  def __init__(self,data,lang):
   self.name = data
   self.lang = lang
   self.root = []
   self.morph= {}
   self.irreg = {}
 
   for cat in categories:
    self.morph[cat] = "*"
 
  def flex(self,root,cat):
   if self.morph[cat]!="*" and root in self.irreg.keys() and cat[sym[self.irreg[root][0]]] == self.irreg[root][1]:
    return self.irreg[root][2] 
   else:
    if self.morph[cat]!="*":
     if prepverb(root)!= False:
      return prepverb(root)[0] + self.morph[cat]+"|"+prepverb(root)[1]
     else:
      return root + self.morph[cat]    
    else:
     return "*"
 #will need another flex for translation that returns ""#
  def flexcheck(self,string,root,cat):
   if string == self.flex(root,cat):
     return True
   else:
     return False
 

  def parse(self,s):
      val = []
      for lex in self.root:
       for cat in categories:
        if s in sandhicomb(self.flex(lex,cat)):
         val.append((self.name,lex,cat))
      return val 
 
  def parsecat(self,s):
   return [par[2] for par in self.parse(s)]

  def parsecheck(self,s):
   if self.parse(s)!=[]:
    return True
   else:
    return False

  def permuparse(self,s,dictionary):
   return s

Nullword = Word("false","none")



class ASynt:
 def __init__(self, data, language):
  self.name =data
  self.language = language
  self.twolist = []
  self.constraint = []
  self.impose = []
  self.switch = "off"
  
 
 def impcheck(self, x):
  for i in self.impose:
    if x[2][sym[i[0]]] == i[1]:
     return True
  return False
 
 def parse(self,s):
  s= s.replace(" ","")
  l = len(s)
  val = [n for n in range(l) if self.twolist[0].parsecheck(s[0:n]) and self.twolist[1].parsecheck(s[n:l])]
  if val!=[]:
   m = val[0]
   v = self.twolist[0].parse(s[0:m]) + self.twolist[1].parse(s[m:l])
   if self.constraint!=[]:
    con =  intersection( listproj2(self.twolist[0].parsecat(s[0:m]), self.constraint),  listproj2(self.twolist[1].parsecat(s[m:l]),self.constraint))
    if con!=[]:
     v = [a for a in self.twolist[0].parse(s[0:m])+ self.twolist[1].parse(s[m:l]) if comp2(a[2],self.constraint) in con]
    else:
     v = []
   if self.impose!=[] and v!=[]:
     v = [a for a in v if self.impcheck(a)]
   return v
  return []
 def parsecheck(self,s):
  val = self.parse(s)
  if val!=[]:
   return True
  else:
   return False
 def parsecat(self,s):
  val = []
  list = self.parse(s)
  for lex in list:
     val.append(lex[2])
  return val
 
 def parsefilter(self,s, con):
  return list(set(listproj2(self.parsecat(s),con)))

 def permuparse(self,s,switchlist):
  s= s.replace(" ","")
  l = len(s)
  val = [n for n in range(l) if self.twolist[0].parse(s[0:n]) and self.twolist[1].parse(s[n:l])]
  if val!=[]:
   m = val[0]
   if switchlist[self]=="":
    return self.twolist[0].permuparse(s[0:m],switchlist)+" "+ self.twolist[1].permuparse(s[m:l],switchlist)
   else:
    return self.twolist[1].permuparse(s[m:l],switchlist)+" "+ self.twolist[0].permuparse(s[0:m],switchlist)


class OSynt:
 def __init__(self, data, language):
  self.name =data
  self.language = language
  self.alter = []
  self.impose =[]
 #def flex(self,root, cat):
  #if self.alter[0].flex(root,cat)!= "*":
   #  return self.alter[0].flex(root,cat)
  #else:
   #  return self.alter[1].flex(root,cat)     
 
 
 
 def impcheck(self, x):
  for i in self.impose:
    if x[2][sym[i[0]]] == i[1]:
     return True
  return False
 
 def parse(self,s):
  a =[]
  if self.alter[0].parsecheck(s) == True: 
   a = self.alter[0].parse(s)
  if self.alter[1].parsecheck(s) == True: 
   a = self.alter[1].parse(s)
  w = a
  if self.impose!=[] and a is not None and a!=[]:
    w = [x for x in a if self.impcheck(x)]
  return w


 def parsecheck(self,s):
  if self.parse(s)!=[]:
   return True
  else:
   return False





 def parsecat(self,s):
  val = []
  list = self.parse(s)
  for lex in list:
     val.append(lex[2])
  return val

 def flex(self,root,cat):
   if root in self.alter[0].root:
    return self.alter[0].flex(root,cat)
   if root in self.alter[1].root:
    return self.alter[1].flex(root,cat)

 def permuparse(self,s,switchlist):
  if self.alter[0].parsecheck(s) == True: 
    return self.alter[0].permuparse(s,switchlist)
  if self.alter[1].parsecheck(s) == True: 
   return self.alter[1].permuparse(s,switchlist)
 
 def parsefilter(self,s, con):
  return list(set(listproj2(self.parsecat(s),con)))



 
class Dictionary:
 def __init__(self,source,target):
   self.source = source
   self.target = target
   self.dictionary = {}
   self.word ={}
   self.switchlist = {}
#i.e. {"prenoun":"switch",}
 def pretrans(self, a):
   return (self.word[a[0]].name, self.word[a[0]].flex( self.dictionary[(a[0],a[1])],a[2]),a[2])
 
 def trans1(self,l):
  return [ x for x in map(self.pretrans,self.source(l)) if x[1]!="*"]  
  
 def trans2(self,l):
  return map(lambda x: x.replace("  "," "), list(set(map(lambda x: " ".join(x),  tensor(fix(self.trans1(l)))))))
   
 def trans(self,l):
   aux = self.trans2(l)
   return map (lambda x: x.replace("|"," "), map(lambda x: x.replace(" -","-"), [sandhi(s) for s in aux if self.target(sandhi(s))!=[] and not '*' in s]) ) 

def organize1(list,keys):
 col = {}
 for typ in keys:
  col[typ] = []
  for lex in list:
   if lex[0] == typ:
    col[typ].append(lex)
 return col


