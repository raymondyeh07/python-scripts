class Static(object):
    num = 0.

s1 = Static()
s2 = Static()

s1.__class__.num += 1
print s1.num, s2.num
