print('Ola mundo')
import random 

opcoes=['uva','limao','caju']

secreta = random.choice(opcoes)
lista =[]

for o in secreta:
    lista.append('_')

c = 5

listacont=[]



while c > 0 and  len(lista) != len(listacont):
    for y in lista:
        print(y)
    letra=input('Escolha uma letra ')
    print(f'Letra escolhida foi {letra}'.upper())
    for n in secreta:
        if letra == n in secreta:
            numerador=secreta.index(n)
            #for k in lista:
            if letra  in lista:
                print('Letra invalida, esta errada ou repetida ')
            else:
                print('Letra aceita, parabens')
                lista.pop(numerador)
                lista.insert(numerador,letra)
                listacont.append(letra)
                if len(lista) == len(listacont):
                    print('Voce venceu'.upper())
                    for y in lista:
                        print(y)
                    
            break
        elif letra not in secreta: ## finalizar o codigo
            print('Letra não pertence a essa palvra')
            c -= 1
            print('O total são 5 chances')
            print(f'Voce agora tem {c} chances'.upper())

            if c == 5:
                print('Voce perdeu'.upper())
            break

  
