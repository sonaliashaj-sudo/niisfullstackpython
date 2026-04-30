import re
txt="The ra16283in in Spain"
x=re.findall("[^a-z]",txt)
print(x)