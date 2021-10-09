#all meta characters: . ^ * + ? {} [] \ | ()
import re
#s="abc36725abc87367xyzkdhjXYZ3435ABC"
#pattern = re.compile(r".")
#pattern = re.compile(r"/.") #for finding the "." in the string
#pattern=re.compile(r"^abc")
s1="hello iam shabbeir and roll is 18481hello"
pattern=re.compile(r"\Bhello")   #/s /S /w /W /b /B /d /D
#matches=pattern.finditer(s)
matches1=pattern.finditer(s1)
for match in matches1:
    print(match) #prints all except new line
    