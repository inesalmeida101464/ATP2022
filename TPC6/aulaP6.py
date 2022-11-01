#modelo : obras=[(nome,descriçao,ano.período, compositor,duraçao,id)]

import csv 

def lerObras(filename):
    file=open(filename,encoding="UTF8")
    csv_file= csv.reader(file, delimiter=";") #delimiter informar qual é o separdor de campos do csv
    file.readline() #le a primeira linha e passa à frente, o ciclo começa na proxima linha

    lista=[]
    for obra in csv_file:
        lista.append(tuple(obra))
    return (lista)

def tamanhoObras(obras):
    return len(obras)

def imprimeObras(obras):
    print(f"| {'Nome':20} | {'Descrição':25} | {'Ano':8} | {'Compositor':15} |")
    for nome,desc,ano,_,comp,*_ in obras:
        print(f"| {nome[:20]:20} | {desc[:25]:25} | {ano:8} | {comp[:15]:15} |") #partir a string da descriçao, fazer slice

def ordem1(tuplo):
    return tuplo[0]

def ordem2(tuplo):
    return tuplo[1]

def ordemtitAno(obras):
    lista=[]
    for nome,_,ano,*_ in obras:
        lista.append((nome,ano))

    lista.sort(key=ordem1) #faz se a funçao ordem pq eu apenas quero ordenar o tuplo[0] que é o primeiro elemento do tuplo, o titulo
    return lista

def ordemtitAno_2(obras):
    lista=[]
    for nome,_,ano,*_ in obras:
        lista.append((nome,ano))
    
    lista.sort(key=ordem2) #ou lista.sort(keu=lambda tuplo:tuplo[1])
    return lista

def titporAno(obras):
    dici={}
    for nome,_,ano,*_ in obras:
        if ano in dici.keys():
            dici[ano].append(nome)
        else:
            dici[ano]=[nome] #se nao estiver no dicionario crio uma lista e meto o nome la dentro
    return dici

def ordemcomp(obras):
    listacomp=[]
    for nome,*_ in obras:
        listacomp.append(nome)
    
    listacomp.sort()
    return listacomp


def distribperiodo(obras): #dicionario vazio, percorre os periodos, se ele existir acrescenta 1 se nao existe tem de se inserir essa chave
    diciperiodo={}
    for _,_,_,periodo,*_ in obras:
        if periodo in diciperiodo.keys():
            diciperiodo[periodo]=diciperiodo[periodo]+1
        else:
            diciperiodo[periodo]=1
    return diciperiodo

def distribano(obras):
    diciano={}
    for _,_,ano,*_ in obras:
        if ano in diciano.keys():
            diciano[ano]=diciano[ano]+1
        
        else:
            diciano[ano]=1
    return diciano

def distribcomp(obras):
    dicicomp={}
    for _,_,_,_,comp,*_ in obras:
        if comp in dicicomp.keys():
            dicicomp[comp]=dicicomp[comp]+1
        else:
            dicicomp[comp]=1
    return dicicomp

def distribgraf(obras):
    import matplotlib.pyplot as plt
    print(""""1-Distribuição por período
    2-Distribuição por ano
    3- Distribuição por compositor""")
    dist=input("Qual o gráfico que pretende visualizar?")

    if dist=="1":
        distribperiodos = distribperiodo(obras)
        x = [x for x in range(1, len(distribperiodos)+1)]
        periodos = list(distribperiodos.keys())
        y=[]
        for i in periodos:
            y.append(distribperiodos[i])
        plt.bar( x, y, tick_label = periodos, color = ['red'])
        plt.xticks(rotation = 90)
        plt.title('Distribuição da obras por Período') 
        plt.xlabel('Períodos')
        plt.ylabel('Número de Obras')
        plt.show()    

    if dist=="2":
        distribanos = distribano(obras)
        x=[x for x in range(1, len(distribanos)+1)]
        anos=list(distribanos.keys())
        y=[]
        for i in anos:
            y.append(distribanos[i])
        plt.bar( x, y, tick_label = anos, width=0.5,color = ['green'])
        plt.title('Distribuição da obras por Ano') 
        plt.xlabel('Anos')
        plt.ylabel('Número de Obras')
        plt.show()
    
    if dist=="3":
        distribcomps = distribcomp(obras)
        x = [x for x in range(1, len(distribcomps)+1)]
        comps = list(distribcomps.keys())
        y = []
        for i in comps:
            y.append(distribcomps[i])
        plt.bar( x, y, tick_label = comps, width=0.5,color = ['blue'])
        plt.xticks(rotation = 90)
        plt.title('Distribuição da obras por Compositores') 
        plt.xlabel('Compositores')
        plt.ylabel('Número de Obras')
        plt.show()
    return

def titcomp(obras):
    lista=[]
    dici={}
    for nome,_,_,_,comp,*_ in obras:
        if comp in dici.keys():
            dici[comp].append(nome)
        else:
            dici[comp]=[nome]
    lista.append(dici)
    return lista

def menu(obras):
    
    opçao = -1
        
    while opçao != 0:
        print("""Menu:
                1- Ver número de obras;
                2- Ver tabela estruturada das obras;
                3- Ver lista de tuplos (título, ano), ordenada alfabeticamente por título;
                4- Ver lista de tuplos (título, ano), ordenada crescentemente por ano;
                5- Ver obras organizadas por ano de criação
                6- Ver lista ordenada dos compositores;
                7- Ver distribuição das obras por período;
                8- Ver distribuição das obras por ano;
                9- Ver distribuição das obras por compositor;
                10- Desenhar um gráfico das distribuições anteriores;
                11- Ver lista de obras por compositor; 
                0- Sair 
                 
                """)

        opçao = int(input("Escolha uma das opções apresentadas no menu:"))

        if opçao==1:
            print("O número de obras é ", tamanhoObras(obras))

        if opçao==2:
            print("--------------------------------------------------------------------")
            imprimeObras(obras)
        
        if opçao==3:
            print("--------------------------------------------------------------------")
            print(ordemtitAno(obras))

        if opçao==4:
            print("---------------------------------------------------------------------")
            print(ordemtitAno_2(obras))

        if opçao==5:
            print("---------------------------------------------------------------------")
            print(titporAno(obras))

        if opçao==6:
            print("---------------------------------------------------------------------")
            print(ordemcomp(obras))

        if opçao==7:
            print("---------------------------------------------------------------------")
            print(distribperiodo(obras))

        if opçao==8:
            print("---------------------------------------------------------------------")
            print(distribano(obras))

        if opçao==9:
            print("---------------------------------------------------------------------")
            print(distribcomp(obras))

        if opçao==10:
            print("---------------------------------------------------------------------")
            print(distribgraf(obras))

        if opçao==11:
            print("---------------------------------------------------------------------")
            print(titcomp(obras))

    print("Saiu do programa.")
    return





