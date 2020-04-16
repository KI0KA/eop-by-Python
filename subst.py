# eop program for python

### subst関数 ###
def subst(s, c1, c2):
    return s.replace(c1, c2)
#################

str1 = "apple"
print(str1)

str1 = subst(str1, "p", "q")
print(str1)