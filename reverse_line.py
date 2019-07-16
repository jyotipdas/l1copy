pos = 0
new_pos = 0
res = ''
st = 'Hello I am Jyoti'

for d in st:
    if d == st[-1]:
        print new_pos
        res = st[pos:new_pos + 1] + ' ' + res
    elif d == ' ':
        print pos,new_pos
        res = st[pos:new_pos] +' '+ res
        pos = new_pos + 1
        new_pos +=1
    elif d != ' ':
        new_pos +=1

print res
