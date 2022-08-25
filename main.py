from re import S


nome = input("Bem vindo ao Dark Monster, por favor, insira seu nome: ")
print(f"{nome}, você está dormindo, e agora são 3 da manhã, o vento assopra perante seu quarto,no qual a janela está aberta, você sente uma brisa gelado, passando por todo")
print("seu corpo, você não se cubriu direito, e você nota algo estranho enquanto dorme: o ar está mais gelado que o comum, aparentemente está nevando, e um silencio toma conta")
print("de tudo. Você de repente escuta um barulho vindo de fora do seu quarto, o que você quer fazer?")

levantar = input("Deseja levantar? S ou N").lower()
if levantar == "N":
    print("você continua dormindo então, em um sono estremamente pesado e agradável, a noite toma conta de você, a escuridão também... até que, você sente um leve calor lhe")
    print("aquecendo... parece confortável. Você deseja verificar o que é? S ou N")
    verificar = input()
    if verificar == "S":
        print("Você abre seus olhos, e então você se depara com enormes chamas tomando conta da sua cama, chamas para todo lado!")
        print("Já é tarde demais, infelizmente as chamas estão tomando conta do seu corpo. Você grita em desespero, tentando pedir ajuda,")
        print("Ninguém aparece. Seu corpo foi totalmente consumido pelas chamas... Apenas sua carne queimada e uma expressão de desespero")
        print("onde costumava ser seu corpo permanecem...")
        print(f"Você está morto, fim de jogo {nome}")
    elif verificar == "N":
        print("Você permanece dormindo, sentindo um quentinho agradável, que aos poucos, começa a ficar desagradável... você está agonizando, tendo um")
        print("pesadelo que reflete a vida real. Sua agonia aumenta de instante em instante. A dor que você está sentindo é indescritivel... ")
        print("mas, idai? é só um pesadelo, certo? você está dormindo um sono bem agradável ainda... infelizmente, é o seu último sono...")
        print(f"Você está morto, fim de jogo {nome}")

elif levantar == "n":
    print("você continua dormindo então, em um sono estremamente pesado e agradável, a noite toma conta de você, a escuridão também... até que, você sente um leve calor lhe")
    print("aquecendo... parece confortável. Você deseja verificar o que é? S ou N")
    verificar = input()
    if verificar == "S":
        print("Você abre seus olhos, e então você se depara com enormes chamas tomando conta da sua cama, chamas para todo lado!")
        print("Já é tarde demais, infelizmente as chamas estão tomando conta do seu corpo. Você grita em desespero, tentando pedir ajuda,")
        print("Ninguém aparece. Seu corpo foi totalmente consumido pelas chamas... Apenas sua carne queimada e uma expressão de desespero")
        print("onde costumava ser seu corpo permanecem...")
        print(f"Você está morto, fim de jogo {nome}")
    elif verificar == "N":
        print("Você permanece dormindo, sentindo um quentinho agradável, que aos poucos, começa a ficar desagradável... você está agonizando, tendo um")
        print("pesadelo que reflete a vida real. Sua agonia aumenta de instante em instante. A dor que você está sentindo é indescritivel... ")
        print("mas, idai? é só um pesadelo, certo? você está dormindo um sono bem agradável ainda... infelizmente, é o seu último sono...")
        print(f"Você está morto, fim de jogo {nome}")

elif levantar == "S":
    print("Você consegue fugir de uma morte certeira")
elif levantar == "s":
    print("Você consegue fugir de uma morte certeira")
