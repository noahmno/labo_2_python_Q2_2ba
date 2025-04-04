import re 

text = "noahmanono2443@gmail.com"
#pattern = r'^[a-zA-Z0-9._]+@[a-z]+.[a-z]{2,}$'
#if re.match(pattern,text):
 #   print("c'est ok")

#else:
#    print("c'est ko")

pattern = r"^[a-z]+$"
p = re.compile(pattern, re.IGNORECASE)
print(p.match("bogoss"))
print(p.match("LaTeX") )