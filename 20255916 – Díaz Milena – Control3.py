# CONFIGURACION INICIAL

agente= "encargado"
platillo= []
precios= []

# INGRESO A LA APLICACIÓN
g=True
while g:
    nombre= input("Favor ingrese el nombre del agente: ")
    if nombre==agente:
        g=False
    else: print("Agente no registrado")

# MENÚ PRINCIPAL 
i= True
while i:
    print("1. Creación de platillos")
    print("2. Consulta de platillo ")
    print("3. Colocar un pedido")
    print("4. Salir")
    lo= int(input("Ingrese número"))
    if lo ==1:
        p=input("Ingrese el nombre del platillo a crear: ")
        o=float(input("Ingrese el precio del platillo a crear: "))
        platillo.append(p)
        precios.append(o)
    if lo==2:
        if len(platillo)==0:
            print("Actualmente no hay platillos ingresados")
        else:
            for x in range(len(platillo)):
                print(f"{platillo[x]}: ${precios[x]}")
    if lo==3:
        e=input("Indique el nombre del platillo para su orden: ")
        k=False
        for d in range(len(platillo)):
            if e == platillo[d]:
                print(f"Usted ha elegido {platillo[d]} con un precio de ${precios[d]}")
                k=True
        if k==False: print("No es un platillo valido")
    if lo==4:
        i=False
    


    

