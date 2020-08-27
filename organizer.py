file = open('fruits.txt','r',encoding='utf_8')
easy = open('easy.txt','w',encoding='utf_8')
normal = open('normal.txt','w',encoding='utf_8')
hard = open('hard.txt','w',encoding='utf_8')

for c in file:
    fruit = file.readline()
    letters =len(fruit)
    if letters <= 4:
        easy.write(fruit)
    elif letters > 4 and letters <= 8:
        normal.write(fruit)
    elif letters > 8:
        hard.write(fruit)
    else:
        pass
easy.close()
normal.close()
hard.close()