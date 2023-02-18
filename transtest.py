from autotransv2 import *

#atoms

Enoun = Word("noun","English")
#with open("Enounroot.txt") as f:#
#    input = f.readlines()#
#Enoun.root = [x.strip() for x in input]


#still must distinguish between persons and things neuters
Enoun.root = ["cat","mouse","book","table","dog","sausage","milk"]
Enoun.irreg = {}
Enoun.irreg["mouse"] = ["number","plu","mice"]

for c in case:
   for g in gender:
    Enoun.morph[("sing",g,"3rd",c)] = ""
    Enoun.morph[("plu", g,"3rd",c)] = "s"

Epronoun = Word("pronoun","English")
Epronoun.root = [""]
for g in gender:
    Epronoun.morph[("sing",g,"1st","subj")] = "I"
    Epronoun.morph[("sing",g,"2nd","subj")] = "you"
    Epronoun.morph[("plu",g,"1st","subj")] = "we"
    Epronoun.morph[("plu",g,"2nd","subj")] = "you"
    Epronoun.morph[("plu",g,"3rd","subj")] = "they"
Epronoun.morph[("sing","masc","3rd","subj")] = "he"      
Epronoun.morph[("sing","fem","3rd","subj")] = "she"
Epronoun.morph[("sing","neut","3rd","subj")] = "it"


for g in gender:
    Epronoun.morph[("sing",g,"1st","obj")] = "me"
    Epronoun.morph[("sing",g,"2nd","obj")] = "you"
    Epronoun.morph[("plu",g,"1st","obj")] = "us"
    Epronoun.morph[("plu",g,"2nd","obj")] = "you"
    Epronoun.morph[("plu",g,"3rd","obj")] = "them"

Epronoun.morph[("sing","masc","3rd","obj")] = "him"      
Epronoun.morph[("sing","fem","3rd","obj")] = "her"
Epronoun.morph[("sing","neut","3rd","obj")] = "it"



for g in gender:
    Epronoun.morph[("sing",g,"1st","gen")] = "me"
    Epronoun.morph[("sing",g,"2nd","gen")] = "you"
    Epronoun.morph[("plu",g,"1st","gen")] = "us"
    Epronoun.morph[("plu",g,"2nd","gen")] = "you"
    Epronoun.morph[("plu",g,"3rd","gen")] = "them"

Epronoun.morph[("sing","masc","3rd","gen")] = "him"      
Epronoun.morph[("sing","fem","3rd","gen")] = "her"
Epronoun.morph[("sing","neut","3rd","gen")] = "it"


  
Earticle = Word("article","English")
Earticle.root = ["the"]
for c in case:
   for g in gender:
     Earticle.morph[("sing",g,"3rd",c)] =""
     Earticle.morph[("plu",g,"3rd",c)] = ""

  
EIarticle = Word("indarticle","English")
EIarticle.root = [""]
for c in case:
   for g in gender:
     EIarticle.morph[("sing",g,"3rd",c)] ="a"
     EIarticle.morph[("plu",g,"3rd",c)] = "some"

verb0 = Word("verb0","English")
verb0.root = ["run","eat","play","talk"]
for c in case:
   for g in gender:
     verb0.morph[("sing",g,"1st",c)] =""
     verb0.morph[("sing",g,"2nd",c)] =""
     verb0.morph[("sing",g,"3rd",c)] ="s"
     verb0.morph[("plu",g,"1st",c)] =""
     verb0.morph[("plu",g,"2nd",c)] =""
     verb0.morph[("plu",g,"3rd",c)] =""

verb1 = Word("verb1","English")
verb1.root = ["like","take","drop","love"]
for c in case:
   for g in gender:
     verb1.morph[("sing",g,"1st",c)] =""
     verb1.morph[("sing",g,"2nd",c)] =""
     verb1.morph[("sing",g,"3rd",c)] ="s"
     verb1.morph[("plu",g,"1st",c)] =""
     verb1.morph[("plu",g,"2nd",c)] =""
     verb1.morph[("plu",g,"3rd",c)] =""

Art = OSynt("article","English")
Art.alter =[Earticle,EIarticle]

NounPhrase = ASynt("noun phrase","English")
NounPhrase.twolist = [Art, Enoun]
NounPhrase.constraint = ["number","gender","person"]

Subject = OSynt("subject","English")
Subject.alter = [Epronoun,NounPhrase]
Subject.impose = [["case","subj"]]

Object = OSynt("subject","English")
Object.alter = [Epronoun,NounPhrase]
Object.impose = [["case","obj"],["case","gen"]]

S3 = ASynt("S3","English")
S3.twolist = [Subject,verb1]
S3.constraint = ["number","person"]

S2 = ASynt("S2","English")
S2.twolist = [S3,Object]

S1 = ASynt("S1","English")
S1.twolist = [Subject,verb0]
S1.constraint = ["number","person"]

Sen = OSynt("sentence","English")
Sen.alter = [S1,S2]

def P(s):
 return Sen.parse(s)

Particle = Word("Particle","Portuguese")
Particle.root = [""]
for p in person:
 for c in case:
  Particle.morph[("sing","fem",p, c)] = "a"
  Particle.morph[("sing","masc",p,c)] = "o"
  Particle.morph[("plu","fem",p,c)] = "as"
  Particle.morph[("plu","masc",p,c)] = "os"
 
PIarticle = Word("PIarticle","Portuguese")
PIarticle.root = [""]
for p in person:
 for c in case:
  PIarticle.morph[("sing","fem",p, c)] = "uma"
  PIarticle.morph[("sing","masc",p, c)] = "um"
  PIarticle.morph[("plu","fem",p, c)] = "umas"
  PIarticle.morph[("plu","masc",p, c)] = "uns"
 
Ppronoun = Word("Ppronoun","Portuguese")
Ppronoun.root = [""]
for g in gender:
    Ppronoun.morph[("sing",g,"1st","subj")] = "eu"
    Ppronoun.morph[("sing",g,"2nd","subj")] = "tu"
    Ppronoun.morph[("plu",g,"1st","subj")] = "nos"
    Ppronoun.morph[("plu",g,"2nd","subj")] = "vos"
    
Ppronoun.morph[("plu","masc","3rd","subj")] = "eles"
Ppronoun.morph[("plu","fem","3rd","subj")] = "elas"
Ppronoun.morph[("sing","masc","3rd","subj")] = "ele"      
Ppronoun.morph[("sing","fem","3rd","subj")] = "ela"
Ppronoun.morph[("sing","neut","3rd","subj")] = "ele"


for g in gender:
    Ppronoun.morph[("sing",g,"1st","obj")] = "-me"
    Ppronoun.morph[("sing",g,"2nd","obj")] = "-te"
    Ppronoun.morph[("plu",g,"1st","obj")] = "-nos"
    Ppronoun.morph[("plu",g,"2nd","obj")] = "-vos"
Ppronoun.morph[("plu","masc","3rd","obj")] = "-(m3+n)os"
Ppronoun.morph[("plu","fem","3rd","obj")] = "-(m3+n)as"

Ppronoun.morph[("sing","masc","3rd","obj")] = "-(m3+n)o"      
Ppronoun.morph[("sing","fem","3rd","obj")] = "-(m3+n)a"
Ppronoun.morph[("sing","neut","3rd","obj")] = "-(m3+n)o"  
# phonetic laws amam -no - sandhi post-processor


for g in gender:
    Ppronoun.morph[("sing",g,"1st","gen")] = "mim"
    Ppronoun.morph[("sing",g,"2nd","gen")] = "ti"
    Ppronoun.morph[("plu",g,"1st","gen")] = "nOs"
    Ppronoun.morph[("plu",g,"2nd","gen")] = "vOs"
Ppronoun.morph[("plu","masc","3rd","gen")] = "eles"
Ppronoun.morph[("plu","fem","3rd","gen")] = "elas"

Ppronoun.morph[("sing","masc","3rd","gen")] = "ele"      
Ppronoun.morph[("sing","fem","3rd","gen")] = "ela"
Ppronoun.morph[("sing","neut","3rd","gen")] = "ele"  



Pfnoun = Word("fem-noun","Portuguese")
Pfnoun.root = ["mesa"]
for c in case:
    Pfnoun.morph[("sing","fem","3rd",c)] = ""
    Pfnoun.morph[("plu", "fem","3rd",c)] = "s"


Pmnoun = Word("masc-noun","Portuguese")
Pmnoun.root = ["gato","rato","livro"]
for c in case:
    Pmnoun.morph[("sing","masc","3rd",c)] = ""
    Pmnoun.morph[("plu", "masc","3rd",c)] = "s"

Pnoun = OSynt("Pnoun","Portuguese")
Pnoun.alter =[Pmnoun,Pfnoun]

Averb0 = Word("a-verb0","Portuguese")
Averb0.root = ["cant"]
for c in case:
   for g in gender:
    Averb0.morph[("sing",g,"1st",c)] ="o"
    Averb0.morph[("sing",g,"2nd",c)] ="as"
    Averb0.morph[("sing",g,"3rd",c)] ="a"
    Averb0.morph[("plu",g,"1st",c)] ="amos"
    Averb0.morph[("plu",g,"2nd",c)] ="ais"
    Averb0.morph[("plu",g,"3rd",c)] ="am"

Everb0 = Word("e-verb0","Portuguese")
Everb0.root = ["corr"]
for c in case:
   for g in gender:
    Everb0.morph[("sing",g,"1st",c)] ="o"
    Everb0.morph[("sing",g,"2nd",c)] ="es"
    Everb0.morph[("sing",g,"3rd",c)] ="e"
    Everb0.morph[("plu",g,"1st",c)] ="emos"
    Everb0.morph[("plu",g,"2nd",c)] ="eis"
    Everb0.morph[("plu",g,"3rd",c)] ="em"


Pverb0 = OSynt("Pverb","Portuguese")
Pverb0.alter = [Averb0,Everb0]



Averb1 = Word("a-verb1","Portuguese")
Averb1.root = ["am","apanh"]
for c in case:
   for g in gender:
    Averb1.morph[("sing",g,"1st",c)] ="o"
    Averb1.morph[("sing",g,"2nd",c)] ="as"
    Averb1.morph[("sing",g,"3rd",c)] ="a"
    Averb1.morph[("plu",g,"1st",c)] ="amos"
    Averb1.morph[("plu",g,"2nd",c)] ="ais"
    Averb1.morph[("plu",g,"3rd",c)] ="am"

Everb1 = Word("e-verb1","Portuguese")
Everb1.root = ["quer","com"]
for c in case:
   for g in gender:
    Everb1.morph[("sing",g,"1st",c)] ="o"
    Everb1.morph[("sing",g,"2nd",c)] ="es"
    Everb1.morph[("sing",g,"3rd",c)] ="e"
    Everb1.morph[("plu",g,"1st",c)] ="emos"
    Everb1.morph[("plu",g,"2nd",c)] ="eis"
    Everb1.morph[("plu",g,"3rd",c)] ="em"


Pverb1 = OSynt("Pverb1","Portuguese")
Pverb1.alter = [Averb1,Everb1]
Pverb1.root = Averb1.root + Everb1.root


AIverb1 = Word("ai-verb1","Portuguese")
AIverb1.root = ["gost|de"]
for c in case:
   for g in gender:
    AIverb1.morph[("sing",g,"1st",c)] ="o"
    AIverb1.morph[("sing",g,"2nd",c)] ="as"
    AIverb1.morph[("sing",g,"3rd",c)] ="a"
    AIverb1.morph[("plu",g,"1st",c)] ="amos"
    AIverb1.morph[("plu",g,"2nd",c)] ="ais"
    AIverb1.morph[("plu",g,"3rd",c)] ="am"

EIverb1 = Word("ei-verb1","Portuguese")
EIverb1.root = ["mex|em"]
for c in case:
   for g in gender:
    EIverb1.morph[("sing",g,"1st",c)] ="o"
    EIverb1.morph[("sing",g,"2nd",c)] ="es"
    EIverb1.morph[("sing",g,"3rd",c)] ="e"
    EIverb1.morph[("plu",g,"1st",c)] ="emos"
    EIverb1.morph[("plu",g,"2nd",c)] ="eis"
    EIverb1.morph[("plu",g,"3rd",c)] ="em"


PIverb1 = OSynt("PIverb1","Portuguese")
PIverb1.alter = [AIverb1,EIverb1]
PIverb1.root = AIverb1.root + EIverb1.root


All1 = OSynt("all1","Portugese")
All1.alter = [Pverb1,PIverb1]
All1.root = Pverb1.root + PIverb1.root



PArt = OSynt("Particle","Portuguese")
PArt.alter =[Particle,PIarticle]

PNounPhrase = ASynt("Pnoun phrase","Portuguese")
PNounPhrase.twolist = [PArt, Pnoun]
PNounPhrase.constraint = ["number","gender","person"]

PSubject = OSynt("Psubject","Portuguese")
PSubject.alter = [Ppronoun,PNounPhrase]
PSubject.impose = [["case","subj"]]

PObject = OSynt("Psubject","Portuguese")
PObject.alter = [Ppronoun,PNounPhrase]
PObject.impose = [["case","obj"]]


PIObject = OSynt("PIsubject","Portuguese")
PIObject.alter = [Ppronoun,PNounPhrase]
PIObject.impose = [["case","gen"]]


PS3 = ASynt("PS3","Portuguese")
PS3.twolist = [PSubject,Pverb1]
PS3.constraint = ["number","person"]


PS3I = ASynt("PS3I","Portuguese")
PS3I.twolist = [PSubject,PIverb1]
PS3I.constraint = ["number","person"]



PS2D = ASynt("PS2D","Portuguese")
PS2D.twolist = [PS3,PObject]


PS2I = ASynt("PS2I","Portuguese")
PS2I.twolist = [PS3I,PIObject]



PS2 = OSynt("PS2","Portuguese")
PS2.alter = [PS2D,PS2I]

PS1 = ASynt("PS1","Portuguese")
PS1.twolist = [PSubject,Pverb0]
PS1.constraint = ["number","person"]

PSen = OSynt("Psentence","Portuguese")
PSen.alter = [PS1,PS2]

def PP(s):
 return PSen.parse(s)


Dic = Dictionary(P,PP)
Dic.dictionary = {("noun","cat"):"gato", ("noun","table"):"mesa", ("article","the"):"", ("indarticle",""):"", ("pronoun",""):"",("verb1","love"):"am",("verb1","like"):"gost|de",("verb0","run"):"corr"}
Dic.word = {"noun":Pnoun, "pronoun":Ppronoun, "article":Particle, "indarticle": PIarticle, "verb0": Pverb0, "verb1": All1}

#it is nice how we do not need to deal with parsing sandhi in the target and can still generate it correctly in translation...




