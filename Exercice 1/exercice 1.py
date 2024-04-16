e1=0
e2=0
e3=0
s = bool(~e1&e2 | e3)

print ("la table de vérité :s=(/e1.e2 + e3)\n")
print ("e1 | e2 | e3  | s")
print (  e1, " |" ,  e2," | " , e3," |"  ,int(s));

e1=0
e2=0
e3=1
s = bool(~e1&e2 | e3)
print (  e1, " |" ,  e2," | " , e3," |"  ,int(s));

e1=0
e2=1
e3=0
s = bool(~e1&e2 | e3)
print (  e1, " |" ,  e2," | " , e3," |"  ,int(s));

e1=0
e2=1
e3=1
s = bool(~e1&e2 | e3)
print (  e1, " |" ,  e2," | " , e3," |"  ,int(s));

e1=1
e2=0
e3=0
s = bool(~e1&e2 | e3)
print (  e1, " |" ,  e2," | " , e3," |"  ,int(s));

e1=1
e2=0
e3=1
s = bool(~e1&e2 | e3)
print (  e1, " |" ,  e2," | " , e3," |"  ,int(s));

e1=1
e2=1
e3=0
s = bool(~e1&e2 | e3)
print (  e1, " |" ,  e2," | " , e3," |"  ,int(s));

e1=1
e2=1
e3=1
s = bool(~e1&e2 | e3)
print (  e1, " |" ,  e2," | " , e3," |"  ,int(s));
print ("- la première forme canonique : s=(/e1./e2.e3 + /e1.e2./e3 + /e1.e2.e3 + e1./e2.e3 + e1.e2.e3 )\n")
print ("- la seconde forme canonique : s=(/e1./e2./e3 + e1./e2./e3 + e1.e2./e3)\n") 
