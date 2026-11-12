class Hayvon:
    pass

class It(Hayvon):
    pass

it = It()

print(isinstance(it, It))        # ?
print(isinstance(it, Hayvon))    # ?
print(isinstance(it, str))       # ?

print(type(it) == It)            # ?
print(type(it) == Hayvon)        # ?