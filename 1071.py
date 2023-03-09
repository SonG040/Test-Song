x = int(input())
y = int(input())
inicio = min(x,y)+1
fim = max(x,y)

if inicio %2 == 0:
    inicio += 1

i = 0 
for loop in range(inicio,fim,2):
    i += loop

print(i)
