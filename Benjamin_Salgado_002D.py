#Programa de gestion de entradas rock "Los Fortificados"





def validar_nombre():
    while True:
        esta_repetido=False
        tiene_numeros=False
        try:
            nombre_usuario=input("Ingrese su nombre de usuario")
            if len(nombre_usuario)<3:
                print("El nombre de usuario no puede ser menor a 3 Caracteres.")
            elif len(nombre_usuario.strip())<=0:
                print("No puede ingresar espacios en blanco!")
            else:
                for i in lista_usuarios["usuarios"]:
                    if nombre_usuario.capitalize()==i["Nombre"]:
                        esta_repetido=True
                if esta_repetido==False:
                    print("Nombre de usuario agregado con exito!")
                    return nombre_usuario.capitalize()
                elif esta_repetido==True:
                    print("EL nombre esta repetido, reintente con otro!")
        except ValueError:
            print("Error de valor Reintente!")



            
            
def validar_codigo():
    while True:
        tiene_numero=False
        tiene_mayuscula=False
        tiene_espacio=False
        tiene_minuscula=False
        try:
            codigo_usuario=input("Ingrese su codigo de usuario (6 caracteres)")
        except ValueError:
            print("Error de valor vuelva a ingresar su nombre de usuario")

        if len(codigo_usuario)<6:
            print("El codigo de usuario debe tener minimo 6 caracteres, reintente.")
        elif len(codigo_usuario.strip())<=0:
            print("No puede ingresar espacios vacios!")
        else:
            for i in codigo_usuario:
                if i==i.upper():
                    tiene_mayuscula=True
            for i in codigo_usuario:
                if i==" ":
                    tiene_espacio=True
            for i in codigo_usuario:
                if i==i.lower():
                    tiene_minuscula=True
            for i in codigo_usuario:
                try:
                    int(i)
                except ValueError:
                    tiene_numero=True
            if tiene_minuscula==True and tiene_mayuscula==True and tiene_numero==True and tiene_espacio==False:
                print("CODIGO DE USUARIO AGREGADO CON EXITO!")                 
                return codigo_usuario
            else:
                print("El CODIGO debe tener una mayusucla una minuscula un numero y no tener espacios")

lista_usuarios={
    "usuarios":[
        {
            "Nombre":"pussy",
            "codigo":None
        },
    ]
}
lista_entradas={
    "entradas_conce":[
        {
            "cantidad":500,
        }
    ],
    "entradas_pte":[
        {
            "cantidad":1300
        }
    ],
    "entradas_muelle":[
        {
            "cantidad":100
        }
    ],
    "entradas_vergara":[
        {
            "cantidad":50
        }
    ]
}

def cuanta_quiere_conce():
    while True:
        se_pasa=False
        try:
            cantidad_deseada=int(input("Ingrese la cantidad de entradas que desea comprar!"))
            if cantidad_deseada<=0:
                print("No puede comprar 0 entradas o entradas negativas, Reintente.")
            else:
                for i in lista_entradas["entradas_conce"]:
                    if cantidad_deseada>i["cantidad"]:
                        se_pasa=True
                if se_pasa==True:
                    print("No puede comprar mas entradas de las que hay en stock!")
                    for i in lista_entradas["entradas_conce"]:
                        print("Stock disponible", i["cantidad"])
                else:
                    print("Entradas compradas correctamente!")
                    for i in lista_entradas["entradas_conce"]:
                        i["cantidad"]=i["cantidad"]-cantidad_deseada
                        print("Stock disponible: ", i["cantidad"])
                    return lista_entradas
        except ValueError:
            print("Solo puede ingresar numeros enteros positivos!")


def cuanta_quiere_pte():
    while True:
        se_pasa=False
        try:
            cantidad_deseada=int(input("Ingrese la cantidad de entradas que desea comprar!"))
            if cantidad_deseada<=0:
                print("No puede comprar 0 entradas o entradas negativas, Reintente.")
            else:
                for i in lista_entradas["entradas_pte"]:
                    if cantidad_deseada>3:
                        se_pasa=True
                if se_pasa==True:
                    print("No puede comprar mas de 3 entradas!")
                    for i in lista_entradas["entradas_pte"]:
                        print("Stock disponible", i["cantidad"])
                else:
                    print("Entradas compradas correctamente!")
                    for i in lista_entradas["entradas_pte"]:
                        i["cantidad"]=i["cantidad"]-cantidad_deseada
                        print("Stock disponible: ",i["cantidad"])
                    return lista_entradas
        except ValueError:
            print("Solo puede ingresar numeros enteros positivos!")

def cuanta_quiere_muelle():
    while True:
        se_pasa=False
        try:
            cantidad_deseada=int(input("Ingrese la cantidad de entradas que desea comprar!"))
            if cantidad_deseada<=0:
                print("No puede comprar 0 entradas o entradas negativas, Reintente.")
            else:
                for i in lista_entradas["entradas_muelle"]:
                    if cantidad_deseada>i["cantidad"]:
                        se_pasa=True
                if se_pasa==True:
                    print("No puede comprar mas entradas de las que hay en stock!")
                    for i in lista_entradas["entradas_muelle"]:
                        print("Stock disponible", i["cantidad"])
                else:
                    print("Entradas compradas correctamente!")
                    for i in lista_entradas["entradas_muelle"]:
                        i["cantidad"]=i["cantidad"]-cantidad_deseada, "G"
                        print("Stock y tipo de entrada:",i["cantidad"])
                    return lista_entradas
        except ValueError:
            print("Solo puede ingresar numeros enteros positivos!")

def cuanta_quiere_vergara():
    while True:
        se_pasa=False
        try:
            cantidad_deseada=int(input("Ingrese la cantidad de entradas que desea comprar!"))
            if cantidad_deseada<=0:
                print("No puede comprar 0 entradas o entradas negativas, Reintente.")
            else:
                for i in lista_entradas["entradas_vergara"]:
                    if cantidad_deseada>i["cantidad"]:
                        se_pasa=True
                if se_pasa==True:
                    print("No puede comprar mas entradas de las que hay en stock!")
                    for i in lista_entradas["entradas_vergara"]:
                        print("Stock disponible", i["cantidad"])
                else:
                    tipo=input("Ingrese el tipo de entrada que desea (Sun o Ni)")
                    if tipo.lower()=="ni":
                        for i in lista_entradas["entradas_vergara"]:
                            print("Entradas compradas correctamente!")
                            i["cantidad"]=i["cantidad"]-cantidad_deseada,"Ni"
                            print("Stock restante y tipo de entrada!",i["cantidad"])
                        return lista_entradas
                    elif tipo.lower()=="sun":
                        for i in lista_entradas["entradas_vergara"]:
                            print("Entradas compradas correctamente!")
                            i["cantidad"]=i["cantidad"]-cantidad_deseada,"Sun"
                            print("Stock restante y tipo de entrada!",i["cantidad"])
                        return lista_entradas
                    else:
                        print("Solo puede ingresar 2 tipos de entradas Ni o Sun")
        except ValueError:
            print("Solo puede ingresar numeros enteros positivos!")



def comprar_conce():
    nombre=validar_nombre()
    codigo=validar_codigo()
    lista_usuarios["usuarios"].append(
                        {
                            "Nombre":nombre,
                            "codigo":codigo
                        },
                    )
    desea=cuanta_quiere_conce()
    print("Nombre de usuario: ",nombre)
    return lista_usuarios, lista_entradas

def comprar_pte():
    nombre=validar_nombre()
    codigo=validar_codigo()
    lista_usuarios["usuarios"].append(
                        {
                            "Nombre":nombre,
                            "codigo":codigo
                        },
                    )
    desea=cuanta_quiere_pte()
    print("Nombre de usuario: ",nombre)
    return lista_usuarios, lista_entradas

def comprar_muelle():
    nombre=validar_nombre()
    codigo=validar_codigo()
    lista_usuarios["usuarios"].append(
                        {
                            "Nombre":nombre,
                            "codigo":codigo
                        },
                    )
    desea=cuanta_quiere_muelle()
    print("Nombre de usuario: ",nombre)
    return lista_usuarios, lista_entradas

def comprar_vergara():
    nombre=validar_nombre()
    codigo=validar_codigo()
    lista_usuarios["usuarios"].append(
                        {
                            "Nombre":nombre,
                            "codigo":codigo
                        },
                    )
    desea=cuanta_quiere_vergara()
    print("Nombre de usuario:",nombre)
    return lista_usuarios, lista_entradas


#AHORA CREAMOS EL MENU!
while True:
    print("TOTEM AUTOSERVICIO GIRA LOS FORTIFICADOS ROCK AND CHILE IN CHILE")
    print("1.- Comprar entrada a “los Fortificados” en Concepción")
    print("2.- Comprar entrada a “los Fortificados” en Puente Alto")
    print("3.- Comprar entrada a “los Fortificados” en Muelle Barón en Valparaíso")
    print("4.- Comprar entrada a “los Fortificados” en Muelle Vergara en Viña del Mar")
    print("5.- Salir")
    try:
        opc_user=int(input("Ingrese una opcion: "))
        if opc_user==1:
            compra_entradas=comprar_conce()
        elif opc_user==2:
            comprar_entradas=comprar_pte()
        elif opc_user==3:
            comprar_entradas=comprar_muelle()
        elif opc_user==4:
            comprar_entradas=comprar_vergara()
        elif opc_user==5:
            print("Saliendoo!!!")
            break
        else:
            print("ingrese una opcion valida!!")
    except ValueError:
        print("Solo se pueden ingresar numeros enteros positivos!")