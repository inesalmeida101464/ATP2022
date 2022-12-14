import csv

def leficheiro(filename):
    file=open(filename,encoding="UTF8")
    csv_file=csv.reader(file,delimiter=",")
    file.readline()

    listalunos=[]
    for aluno in csv_file:
        listalunos.append(tuple(aluno))
    return listalunos
listalunos=leficheiro("alunos.csv")

def distribCurso(listalunos):
    dici={}
    for _,_,curso,*_ in listalunos:
        if curso in dici.keys():
            dici[curso]=dici[curso]+1
        else:
            dici[curso]=1
    return dici

def datasetMedia(listalunos):
    listaMedia=[]
    for aluno in listalunos:
        if len(aluno )> 7:
            id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media=aluno
        else:
            id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4=aluno
        media= (int(aluno[3])+int(aluno[4])+int(aluno[5])+int(aluno[6]))/4
        alunoMedia=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media
        listaMedia.append(alunoMedia)
    return listaMedia
listaMedia=datasetMedia(listalunos)

def escalaoMedia(listaMedia):
    listaEscalao=[]
    for alunoMedia in listaMedia:
        if len(alunoMedia)>8:
            id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao=alunoMedia
        else:
            id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media=alunoMedia
            
        if int(media) in range (1,5):
            escalao="E"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            listaEscalao.append(alunoEscalao)
        
        elif int(media) in range (5,9):
            escalao="D"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            listaEscalao.append(alunoEscalao)

        elif int(media) in range (9,13):
            escalao="C"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            listaEscalao.append(alunoEscalao)

        elif int(media) in range (13,16):
            escalao="B"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            listaEscalao.append(alunoEscalao)
        
        elif int(media) in range (16,21):
            escalao="A"
            alunoEscalao=id_aluno,nome,curso,tpc1,tpc2,tpc3,tpc4,media,escalao
            listaEscalao.append(alunoEscalao)

    return listaEscalao

listaEscalao=escalaoMedia(listaMedia)

def distribEscalao(listalunos):
    diciDistrib={}
    for _,_,_,_,_,_,_,_,escalao in listalunos:
        if escalao in diciDistrib.keys():
            diciDistrib[escalao] += 1
        else:
            diciDistrib[escalao] = 1
    return diciDistrib

def grafico(listalunos):
    import matplotlib.pyplot as plt
    print("""    1-Distribui????o por curso
    2-Distribui????o por escal??o

    Escolha uma das op????es acima""")

    opcao=input("Escolha uma distribui????o")

    if opcao=="1":
            distrib=distribCurso(listalunos)
            eixoXx=distrib.keys()
            eixoXy=distrib.values()
            plt.plot(eixoXx,eixoXy,color = "red",linewidth = 1)
            plt.title("Distribui????o de alunos por Curso")
            plt.xlabel("Cursos", color ="blue")
            plt.ylabel("N??mero de alunos", color = "blue")
            plt.show()

    elif opcao=="2":
            distrib=distribEscalao(listalunos)
            eixoXx=distrib.keys()
            eixoXy=distrib.values()
            plt.plot(eixoXx,eixoXy,color = "red",linewidth = 1)
            plt.title("Distribui????o de alunos por Escal??es")
            plt.xlabel("Escal??es", color ="blue")
            plt.ylabel("N??mero de alunos", color = "blue")
            plt.show()
    else:
        print("Op????o inv??lida")


def tabela(listalunos):
    print("""    1- Distribui????o de alunos por curso
    2- Distribui????o de alunos por escal??o
    
    Escolha uma das op????es acima""")

    opcao=input("Escolha uma distribui????o")
    
    if opcao=="1":
        distrib=distribCurso(listalunos)
        print("Tabela distribui????o de alunos por curso")
        print("")
        print(f" Curso   |  Alunos")
        for i in distrib:
            print(f" {i:7} | {distrib[i]:7} ")

    elif opcao == "2":
        distrib = distribEscalao(listalunos) 
        print(" Tabela distribui????o de alunos por escal??o:")
        print("")
        print(f" Escal??o |  Alunos")
        for i in distrib:
            print(f" {i:7} | {distrib[i]:7} ")

    else:
        print("Op????o inv??lida")

def menu(listalunos,listaMedia,listaEscalao):
    
    opcao=-1
    while opcao !=0:
        print(""" Menu:
                    1- Ver informa????o do dataset 
                    2- Ver informa????o do dataset com m??dia das notas de cada aluno
                    3- Ver informa????o do dataset com m??dia e escal??o dos alunos
                    4- Ver distribui????o dos alunos por curso
                    5- Ver distribui????o dos alunos pelos seguintes escal??es: 
                        E [1-4], D [5-8], C [9-12], B [13-16], A [17-20]
                    6- Ver distribui????es na forma de gr??fico 
                    7- Ver distribui????es na forma de uma tabela
                    0- Sair.
                Escolha uma das op????es acima.""")
        opcao=int(input("Escolha uma op????o do menu"))
   
        if opcao==1:
           
            print(listalunos)
        elif opcao==2:
        
            datasetMedia(listaMedia)
    
        elif opcao==3:
           
            escalaoMedia(listaEscalao)

        elif opcao==4:
            distribCurso(listalunos)
    
        elif opcao==5:
            distribEscalao(listalunos)
    
        elif opcao==6:
            grafico(listalunos)

        elif opcao==7:
            tabela(listalunos)
        









            



