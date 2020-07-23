nome=input("Caro aluno, digite seu nome: ")
matricula=input("Digite o número da sua matrícula, por favor: ")
P1=float(input("Digite a nota da P1: "))
P2=float(input("Digite a nota da P2: "))
P3=float(input("Digite a nota da P3: "))
P4=float(input("Digite a nota da P4: "))
media=(P1+P2+P3+P4)/4
print("Sua média é de " + str(media))
if media>=7.0:
    print("Você foi aprovado! ")
else:
    print(" Você foi reprovado! ")