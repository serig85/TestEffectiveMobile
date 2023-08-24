from random import choice
def gen():
    gens = chr(choice(range(97, 122)))
    return gens

f=open('file.txt','w')

for i in range(100):
    ln=gen()+gen()+gen()+','+gen()+gen()+gen()+'\n'
    f.writelines(ln)