'''
def rem(l, word):
            n = []
            for item in l :
                if not(item == word):
                n.append(item.replace(word, ""))
            return n
l =["sohan", "rohan","mohan", "parveen","anshu"]

print(rem(l, "an"))

'''
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["amrit", "ankit", "amit", "denesh", "suresh", "it", "sh"]
print(rem(l, "sh"))