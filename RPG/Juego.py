 
import random 
print ("====== CREADOR DE PERSONAJE ======")
nombre = input ("¿Cual es el nombre de tu personaje? ")
print("Elije una clase entre las siguientes:")
print("1. Guerrero")
print("2. Arquero")
print("3. Mago")
personaje={"Nombre":nombre,"Vida Maxima":0,"Vida":0,"Ataque":0,"Defensa":0,"Oro":0,"Nivel":1,"Experiencia":0,
           "Experiencia Necesaria":100}
while True:
    try:
        clase = int(input("Tu clase:"))
        if clase==1:
            personaje["Clase"]="Guerrero"
            personaje["Vida Maxima"]=120
            personaje["Vida"]=120
            personaje["Ataque"]=20
            personaje["Defensa"]=15
            personaje["Oro"]=45
            break
        elif clase==2:
            personaje["Clase"]="Arquero"
            personaje["Vida Maxima"]=90
            personaje["Vida"]=90
            personaje["Ataque"]=25
            personaje["Defensa"]=8
            personaje["Oro"]=75
            break
        elif clase==3:
            personaje["Clase"]="Mago"
            personaje["Vida Maxima"]=80
            personaje["Vida"]=80
            personaje["Ataque"]=30
            personaje["Defensa"]=5
            personaje["Oro"]=50
            break
        else:
            print ("Esta clase no existe. Por favor, introduce una clase.")
    except ValueError:
        print ("Por favor, introduce un valor valido.")
print ("====== FICHA DE PERSONAJE ======")
print ("====== IDENTIDAD ======")
print ("Nombre:",personaje["Nombre"])
print ("Clase:",personaje["Clase"])
print ("====== PROGRESO ======")
print ("Nivel:",personaje["Nivel"])
print ("Experiencia:",personaje["Experiencia"])
print ("====== ESTADISTICAS ======")
print ("Vida:",personaje["Vida"]) 
print ("Ataque:",personaje["Ataque"])
print ("Defensa:",personaje["Defensa"])
print ("====== ECONOMIA ======")
print ("Oro:", personaje["Oro"])
print ("===============================")
esqueleto = {"Nombre": "Esqueleto","Vida": 50,"Vida Máxima": 50,"Ataque": 15,"Defensa": 20,"Oro": 5,"EXP": 20}
orco = {"Nombre": "Orco","Vida": 75,"Vida Máxima": 75,"Ataque": 35,"Defensa": 30,"Oro": 10,"EXP": 30}
goblin = {"Nombre": "Goblin","Vida": 40,"Vida Máxima": 40,"Ataque": 10,"Defensa": 5,"Oro": 3,"EXP": 10}
enemigos=[esqueleto,orco,goblin] 
def combate(personaje,enemigo):
    print ("====== COMBATE ======")
    while True:
        try:
            print ("Has entrado al combate")
            print ("Elije como actuaras")
            print ("1. Atacar")
            print ("2. Defender")
            print ("3. Huir")
            menu=int(input("¿Que quieres hacer?"))
            print()
            if menu==1: 
                enemigo["Vida"]-=personaje["Ataque"]
                print("Has atacado al",enemigo["Nombre"])
                print ("Daño: ",personaje["Ataque"])
                print ("Vida del",enemigo["Nombre"],":",enemigo["Vida"],"/",enemigo["Vida Máxima"])
                if enemigo["Vida"]<=0:
                    print ("¡Has vencido a tu enemigo!")
                    personaje["Oro"]+=enemigo["Oro"]
                    print ("Acabas de recibir ",enemigo["Oro"],"de oro")
                    personaje["Experiencia"]+=enemigo["EXP"]
                    print("Has obtenido ",enemigo["EXP"],"puntos de experiencia.")
                    if personaje["Experiencia"]>=personaje["Experiencia Necesaria"]:
                        personaje["Experiencia Necesaria"]+=100
                        personaje["Nivel"]+=1 
                        personaje["Vida Maxima"]+=10
                        personaje["Ataque"]+=5
                        personaje["Defensa"]+=2
                        print ("Has subido a nivel",personaje["Nivel"])
                        print ("Vida máxima: ",personaje["Vida Maxima"])
                        print ("Ataque: ",personaje["Ataque"])
                        print ("Defensa: ",personaje["Defensa"])
                    break
                else:
                    personaje["Vida"]-=enemigo["Ataque"]
                    print ("¡Tu enemigo te ha atacado!")
                    print ("Tu vida actual es de",personaje["Vida"],"/",personaje["Vida Maxima"])
                    if personaje["Vida"]<=0:
                        print ("Has muerto.")
                        break
            elif menu==2:
                daño_recibido=enemigo["Ataque"]-personaje["Defensa"]
                if daño_recibido<0:
                    daño_recibido=0
                personaje["Vida"]-=daño_recibido
                if daño_recibido>0:
                    print ("Has sido atacado, pero bloqueaste parte del daño.")
                else:
                    print ("Has sido atacado, pero bloqueaste el daño.")
                print ("Recibiste",daño_recibido,"puntos de daño.")
                print ("Te quedan",personaje["Vida"],"/",personaje["Vida Maxima"])
                if personaje["Vida"]<=0:
                    print ("Has muerto.")
                    break
            elif menu==3:
                resultado_huida=random.randint(1,2)
                if resultado_huida==1:
                    print ("¡Has logrado escapar con exito!")
                    break
                else:
                    print ("No lograste escapar. ahora tendras que pelear.")
                    personaje["Vida"]-=enemigo["Ataque"]
                    print ("¡Tu enemigo te ha atacado!")
                    print ("Tu vida actual es de",personaje["Vida"],"/",personaje["Vida Maxima"])
                    if personaje["Vida"]<=0:
                        print ("Has muerto.")
                        break
            else: 
                print ("Elegiste una opción invalida.")
        except ValueError:
            print ("Elegiste una opcion invalida.") 
while True:
    print ("====== EXPLORACIÓN ======")
    print ("1. Explorar")
    print ("2. Descansar")
    print ("3. Salir")
    menu_expln=int(input("¿Que deseas hacer?"))
    if menu_expln==1:
        print("Has decidido explorar.")
        resultado_expln=random.randint(1,3)
        if resultado_expln==1:
            print("¡Has encontrado un enemigo!")
            print ("¡Preparate para combatir!")
            enemigo=random.choice(enemigos)
            enemigo=enemigo.copy()
            print("====== ESTADISTICAS ======")
            print("Nombre:",enemigo["Nombre"])
            print("Vida:",enemigo["Vida"])
            print("Vida máxima:", enemigo["Vida Máxima"])
            print("Ataque:",enemigo["Ataque"])
            print("Defensa:",enemigo["Defensa"])
            combate(enemigo=enemigo,personaje=personaje)
        elif resultado_expln==2:
            print ("¡Encontraste un tesoro!")
            oro_tesoro=random.randint(10,30)
            personaje["Oro"]+=oro_tesoro
            print("¡Has recibido",oro_tesoro,"lingotes de oro!")
        elif resultado_expln==3:
            print ("No has hallado nada.")
    elif menu_expln==2:
        print("Has decidido descansar.")
    elif menu_expln==3:
        print("Has decidido salir.")
        break
    else:
        print ("Has elegido una opción invalida.")