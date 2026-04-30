import re
txt="The ra16283in in Sp4a95872i6n"
x=re.findall("[0-9]{3}",txt)
print(x)