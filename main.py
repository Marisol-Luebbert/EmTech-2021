#Las librerías que vamos a usar
import os
#Vamos a importar los datos del documento
import lifestore_file as lf

#Simplificando los nombres de las listas
ls_products = lf.lifestore_products
ls_searches = lf.lifestore_searches
ls_sales = lf.lifestore_sales

#Eliminemos los datos que no pertenecen a las ventas del 2020
for venta in ls_sales:
  if venta[3][6:10] != "2020":
    ls_sales.remove(venta)

#Vamos a crear una lista de administradores con sus contraseñas con el formato: admins= [[usuario, contraseña],...]
admins = [['Marisol','sol3312'],['Javier', 'javi123'],['Gerencia','ventas123']]

print("¡Bienvenid@ a Lifestore!")

#Solicitamos los datos de usuario
usuario = input("Ingresa tu nombre de usuario: ")
contrasena = input("Ingresa tu contraseña: ")

miembro = 0
intentos = 0

#Verifiquemos que los datos son correctos, tiene 3 intentos 
while miembro != 1 and intentos < 2:
  for admin in admins: 
    if admin[0] == usuario and admin[1] == contrasena:
      miembro = 1
  
  if miembro == 0:
    print('Los datos son incorrectos')
    usuario = input("Ingresa de nuevo tu nombre de usuario: ")
    contrasena = input("Ingresa de nuevo tu contraseña: ")
    intentos +=1

#No dejamos acceder a los que no son miembros
if miembro != 1:
  #Vamos a limpiar la consola, para evitar exceso de información
  os.system('clear')
  print("Lo siento, no puedo darte acceso.")
#Si es miembro, le mostramos el menú de opciones
else: 
  os.system('clear')
  print("¡ Hola ", usuario, "!")
  print("Elige alguna de las siguientes opciones: \n \n-Productos más vendidos y rezagados \n a)Los 10 productos más vendidos \n b)Los 20 productos más buscados \n c)Los 5 productos con menores ventas de cada categoría \n d)Los 5 productos menos buscados de cada categoría \n e)Productos devueltos \n\n-Productos por reseña en el servicio \n f)Los 20 productos mejor calificados \n g)Los 10 productos peor calificados \n\n-Ventas e ingresos \n h)Total de ingresos y Venta total anual \n i)Ventas mensuales \n j)Meses con más ventas en el año")

#Para asegurarnos que quien está viendo la información pertenece al equipo
intento = 0 #Vamos a poner la condición para que el bucle se detenga cuando no quiera seguir en el sistema
while miembro == 1 and intento == 0:
  opcion = input("\nEscribe la letra de la opción que te interesa: ")

  #En caso de no haber puesto una opcion
  if opcion == "":
    print("\nLo siento no entendí.")
    opcion = input("Escribe la letra de la opción que te interesa: ")

  #Los más vendidos
  elif opcion == "a":
    os.system('clear')
    aop = "Los 10 productos más vendidos"
    print (aop.center(50," "))
    sol = 1
    if sol == 1:
      contador = 0
      ventas_prod = []
      for producto in ls_products:
        for venta in ls_sales:
          #Veamos los productos que se vendieron
          if producto[0] == venta[1]:
            contador += 1
            #Veamos si los productos se devolvieron
            if venta[4] == 1:
              contador -= 1
        #En caso de que sí hayan ventas, se van a reunir los datos del producto
        if contador != 0:
          ventas_prod.append([producto[0],producto[1], contador])
          #Para que empiece el ciclo para el siguiente producto
          contador = 0

    mas_vendidos = []
    while ventas_prod: #Vamos a vaciar la lista
	    maximo = ventas_prod[0][2] #Establecemos un máximo cualquiera
	    lista_max = ventas_prod[0]
	    for totalventa in ventas_prod:
      #Si hay un valor más grande se reasigna el máximo
		    if totalventa[2] > maximo:
		    	maximo = totalventa[2]
		    	lista_max = totalventa
	    mas_vendidos.append(lista_max)
	    ventas_prod.remove(lista_max)
    print(["ID","Nombre del producto","Total vendidos"])
    print(*mas_vendidos[0:10], sep="\n")

  #Los más buscados
  elif opcion == "b":
    os.system('clear')
    bop = "Los 20 productos más buscados"
    print(bop.center(50," "))
    holi = 1
    if holi == 1:
      contador = 0
      busquedas = []
      #Se obtiene la cantidad de búsquedas de cada producto 
      for producto in ls_products:
        for busqueda in ls_searches:
         if producto[0] == busqueda[1]:
            contador +=1
        if contador != 0:
          busquedas.append([producto[0],producto[1],contador])
          contador = 0
    mas_buscados = []
    #Se acomodan de mayor a menor cantidad de búsquedas
    while busquedas:
      maximo = busquedas[0][2]
      lista_max = busquedas[0]
      for elemento in busquedas:
       if elemento[2] > maximo:
          maximo = elemento[2]
          lista_max = elemento
      mas_buscados.append(lista_max)
      busquedas.remove(lista_max)
    print(["ID","Nombre del producto","# búsquedas"])
    print(*mas_buscados[0:20],sep = "\n")

  #Los menos vendidos
  elif opcion == "c":
    os.system('clear')
    cop = "Los 5 productos con menores ventas de cada categoría"
    print(cop.center(50," "))
    holis = 1
    if holis == 1:
      contador = 0
      ventas_prod=[]
      #Se buscan las ventas totales de cada producto
      for producto in ls_products:
        for venta in ls_sales:
         if producto[0] == venta[1]:
           contador += 1
           if venta[4] == 1:
             contador-=1
        if contador != 0:
          ventas_prod.append([producto[0],producto[1],producto[3], contador])
          contador=0
    menos_vendidos = []
    #Se acomodan de menor a mayor cantidad de ventas
    while ventas_prod:
	    minimo = ventas_prod[0][3]
	    lista_min = ventas_prod[0]
	    for totalventa in ventas_prod:
		    if totalventa[3] < minimo:
			    minimo = totalventa[3]
			    lista_min = totalventa
	    menos_vendidos.append(lista_min)
	    ventas_prod.remove(lista_min)
    
    #Como se hará el acomodo por categoría, se hará una lista para cada categoria de producto
    procesadores = []
    tarjetas_video = []
    tarjetas_madre = []
    discos_duros = []
    memorias_usb = []
    pantallas = []
    bocinas = []
    audifonos = []

    for vendido in menos_vendidos:
      #Se busca el nombre de la categoría, para agregar los productos a las listas
      if vendido[2] == "procesadores":
       vendido.remove("procesadores")
       procesadores.append(vendido)
      elif vendido[2] == "tarjetas de video":
       vendido.remove("tarjetas de video")
       tarjetas_video.append(vendido)
      elif vendido[2] == "tarjetas madre":
       vendido.remove("tarjetas madre")
       tarjetas_madre.append(vendido)
      elif vendido[2] == "discos duros":
       vendido.remove("discos duros")
       discos_duros.append(vendido)
      elif vendido[2] == "memorias usb":
        vendido.remove("memorias usb")
        memorias_usb.append(vendido)
      elif vendido[2] == "pantallas":
        vendido.remove("pantallas")
        pantallas.append(vendido)
      elif vendido[2] == "bocinas":
        vendido.remove("bocinas")
        bocinas.append(vendido)
      else:
        vendido.remove("audifonos")
        audifonos.append(vendido)
    #Vamos a imprimir los 5 menos vendidos de cada categoria
    proc = "Los procesadores menos vendidos"
    print(proc.center(50,"="))
    print(["ID","Nombre del producto","Total vendidos"])
    print(*procesadores[0:5], sep="\n")
    print("\n")
    video = "Las tarjetas de video menos vendidas"
    print(video.center(50,"="))
    print(["ID","Nombre del producto","Total vendidos"])
    print(*tarjetas_video[0:5], sep="\n")
    print("\n")
    madre = "Las tarjetas madre menos vendidas"
    print(madre.center(50,"="))
    print(["ID","Nombre del producto","Total vendidos"])
    print(*tarjetas_madre[0:5], sep="\n")
    print("\n")
    discos = "Los discos duros menos vendidos"
    print(discos.center(50,"="))
    print(["ID","Nombre del producto","Total vendidos"])
    print(*discos_duros[0:5], sep="\n")
    print("\n")
    usb = "Las memorias USB menos vendidas"
    print(usb.center(50,"="))
    print(["ID","Nombre del producto","Total vendidos"])
    print(*memorias_usb[0:5], sep="\n")
    print("\n")
    pant = "Las pantallas menos vendidas"
    print(pant.center(50,"="))
    print(["ID","Nombre del producto","Total vendidos"])
    print(*pantallas[0:5], sep="\n")
    print("\n")
    boc = "Las bocinas menos vendidas"
    print(boc.center(50,"="))
    print(["ID","Nombre del producto","Total vendidos"])
    print(*bocinas[0:5], sep="\n")
    print("\n")
    audi = "Los audífonos menos vendidos"
    print(audi.center(50,"="))
    print(["ID","Nombre del producto","Total vendidos"])
    print(*audifonos[0:5], sep="\n")

  #Los productos menos buscados 
  elif opcion == "d":
    os.system('clear')
    dop = "Los 5 productos menos buscados de cada categoría"
    print(dop.center(50," "))
    real = 1
    if real == 1:
      contador = 0
      busquedas = []
      #Se hace una lista por búsquedas
      for producto in ls_products:
        for busqueda in ls_searches:
          if producto[0] == busqueda[1]:
            contador +=1
        if contador != 0:
          busquedas.append([producto[0],producto[1],producto[3],contador])
          contador = 0
    menos_buscados = []
    #Se acomodan de menor a mayor buscados
    while busquedas:
      minimo = busquedas[0][3]
      lista_min = busquedas[0]
      for elemento in busquedas:
        if elemento[3] < minimo:
          minimo = elemento[3]
          lista_min = elemento
      menos_buscados.append(lista_min)
      busquedas.remove(lista_min)
  #Para acomodarlos por categoría se meten a listas específicas
    procesadores = []
    tarjetas_video = []
    tarjetas_madre = []
    discos_duros = []
    memorias_usb = []
    pantallas = []
    bocinas = []
    audifonos = []

    for buscado in menos_buscados:
      #Se busca la categoría y se clasifican
      if buscado[2] == "procesadores":
        buscado.remove("procesadores")
        procesadores.append(buscado)
      elif buscado[2] == "tarjetas de video":
        buscado.remove("tarjetas de video")
        tarjetas_video.append(buscado)
      elif buscado[2] == "tarjetas madre":
        buscado.remove("tarjetas madre")
        tarjetas_madre.append(buscado)
      elif buscado[2] == "discos duros":
        buscado.remove("discos duros")
        discos_duros.append(buscado)
      elif buscado[2] == "memorias usb":
        buscado.remove("memorias usb")
        memorias_usb.append(buscado)
      elif buscado[2] == "pantallas":
        buscado.remove("pantallas")
        pantallas.append(buscado)
      elif buscado[2] == "bocinas":
        buscado.remove("bocinas")
        bocinas.append(buscado)
      else:
        buscado.remove("audifonos")
        audifonos.append(buscado)
    
    #Se imprimen los 5 menos buscados de cada categoria
    proc = "Los procesadores menos buscados"
    print(proc.center(50,"="))
    print(["ID","Nombre del producto","Total búsquedas"])
    print(*procesadores[0:5], sep="\n")
    print("\n")
    video = "Las tarjetas de video menos buscadas"
    print(video.center(50,"="))
    print(["ID","Nombre del producto","Total búsquedas"])
    print(*tarjetas_video[0:5], sep="\n")
    print("\n")
    madre = "Las tarjetas madre menos buscadas"
    print(madre.center(50,"="))
    print(["ID","Nombre del producto","Total búsquedas"])
    print(*tarjetas_madre[0:5], sep="\n")
    print("\n")
    discos = "Los discos duros menos buscados"
    print(discos.center(50,"="))
    print(["ID","Nombre del producto","Total búsquedas"])
    print(*discos_duros[0:5], sep="\n")
    print("\n")
    usb = "Las memorias USB menos buscadas"
    print(usb.center(50,"="))
    print(["ID","Nombre del producto","Total búsquedas"])
    print(*memorias_usb[0:5], sep="\n")
    print("\n")
    pant = "Las pantallas menos buscados"
    print(pant.center(50,"="))
    print(["ID","Nombre del producto","Total búsquedas"])
    print(*pantallas[0:5], sep="\n")
    print("\n")
    boc = "Las bocinas menos buscadas"
    print(boc.center(50,"="))
    print(["ID","Nombre del producto","Total búsquedas"])
    print(*bocinas[0:5], sep="\n")
    print("\n")
    audi = "Los audífonos menos buscados"
    print(audi.center(50,"="))
    print(["ID","Nombre del producto","Total búsquedas"])
    print(*audifonos[0:5], sep="\n")

  #Sección de productos devueltos
  elif opcion == "e":
    os.system('clear')
    kop = "Productos devueltos"
    print(kop.center(50," "))
    contador=0
    devueltos=[]
    for producto in ls_products:
      for venta in ls_sales:
        #Buscamos los productos en la lista de ventas
        if producto[0] == venta[1]:
          #Se cuenta el número de devoluciones por producto
          if venta[4]==1:
            contador+=1
            devueltos.append([producto[0],producto[1],contador])
            contador=0
    print(["ID","Nombre del producto","# devoluciones"])
    print(*devueltos,sep="\n")
  
  #Los mejor calificados
  elif opcion == "f":
    os.system('clear')
    eop = "Los 20 productos mejor calificados"
    print(eop.center(50," "))
    mar = 1
    if mar == 1:
      contador = 0
      calificacion = 0
      calificaciones = []
      for producto in ls_products:
        for venta in ls_sales:
          #Se buscan los productos vendidos
          if producto[0] == venta[1]:
            contador += 1
            #Se suman las calificaciones obtenidas de los productos
            calificacion += venta[2]
        if contador!=0:
          #Obtenemos el promedio de calificación
          promedio = calificacion/contador
          calificaciones.append([producto[0],producto[1],promedio])
          calificacion = 0
          contador=0
    #Haremos una lista de mayor a menor calificación de los productos
    mejor_calificados = []
    while calificaciones:
	    maxima = calificaciones[0][2]
	    lista_max = calificaciones[0]
	    for calificacion in calificaciones:
		    if calificacion[2] > maxima:
			    maxima = calificacion[2]
			    lista_max = calificacion
	    mejor_calificados.append(lista_max)
	    calificaciones.remove(lista_max)
    print(["ID","Nombre del producto","Calificación promedio"])
    print(*mejor_calificados[0:20],sep="\n")

  #Los peor calificados
  elif opcion == "g":
    os.system('clear')
    fop = "Los 10 productos peor calificados"
    print(fop.center(50," "))
    mar = 1
    if mar == 1:
      contador = 0
      calificacion = 0
      calificaciones = []
      for producto in ls_products:
        for venta in ls_sales:
          #Vemos los productos que se vendieron
          if producto[0] == venta[1]:
            contador += 1
            #Hacemos una suma de calificaciones
            calificacion += venta[2]
        if contador!=0:
          #Promediamos las calificaciones
          promedio = calificacion/contador
          calificaciones.append([producto[0],producto[1],promedio])
          calificacion = 0
          contador=0

    #Vamos a acomodar los productos de menor a mayor calificación
    peor_calificados = []
    while calificaciones:
	    minima = calificaciones[0][2]
	    lista_min = calificaciones[0]
	    for calificacion in calificaciones:
		    if calificacion[2] < minima:
			    minima = calificacion[2]
			    lista_min = calificacion
	    peor_calificados.append(lista_min)
	    calificaciones.remove(lista_min)

    print(["ID","Nombre del producto","Calificación promedio"])
    print(*peor_calificados[0:10],sep="\n")

  #Total de ingresos y ventas anuales
  elif opcion == "h":
    os.system('clear')
    gop = "Total de ingresos y Venta total anual"
    print(gop.center(50," "))
    cuentas = 0
    gastos = []
    for producto in ls_products:
      for venta in ls_sales:
        #Vamos a ver el dinero invertido en el stock
        stock = producto[4] * producto[2]
        if producto[0] == venta[1]:
        #Contamos los productos vendidos
          cuentas += 1
      if cuentas != 0 or stock != 0:
        #Vemos lo gastado en productos vendidos
        cuentas *= producto[2]
        #Hacemos la cuenta total de gastos por producto
        total_gasto = stock + cuentas
        gastos.append(total_gasto)
        cuentas=0
        stock=0
    #Vamos a sumar los gastos realizados por todos los productos, vendidos  y de stock
    total_gastos = sum(gastos)
    print("En todo el año el total de ingresos tiene un monto igual a: \n$",total_gastos,"(pesos)")
    #Vamos a hacer listas de ventas de cada mes
    cuentas = 0
    mensuales = []
    enero=[]
    febrero=[]
    marzo=[]
    abril=[]
    mayo=[]
    junio=[]
    julio=[]
    agosto=[]
    septiembre=[]
    octubre=[]
    noviembre=[]
    diciembre=[]
    enerito=0
    febrerito=0
    marzito=0
    abrilito=0
    mayito=0
    junito=0
    julito=0
    agostito=0
    septembrito=0
    octubrito=0
    novembrito=0
    dicembrito=0
    for producto in ls_products:
      for venta in ls_sales:
      #Vamos a identificar las ventas por mes, usando la fecha, por mes
        if venta[3][3:5] == "01":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              #Se hace la cuenta de ventas totales, considerando las devoluciones 
              cuentas-=1
          if cuentas  != 0:
            #Se saca el dinero obtenido por ventas por producto
            cuentas*=producto[2]
            enero.append(cuentas)
            cuentas = 0
            #Se hace la suma de ventas de todo el mes
            enerito=sum(enero)
        
        elif venta[3][3:5] == "02":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            febrero.append(cuentas)
            cuentas = 0
            febrerito=sum(febrero)
    
        elif venta[3][3:5] == "03":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            marzo.append(cuentas)
            cuentas = 0
            marzito=sum(marzo)

        elif venta[3][3:5] == "04":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            abril.append(cuentas)
            cuentas = 0
            abrilito=sum(abril)
    
        elif venta[3][3:5] == "05":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            mayo.append(cuentas)
            cuentas = 0
            mayito=sum(mayo)
    
        elif venta[3][3:5] == "06":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            junio.append(cuentas)
            cuentas = 0
            junito=sum(junio)
      
        elif venta[3][3:5] == "07":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            julio.append(cuentas)
            cuentas = 0
            julito=sum(julio)

        elif venta[3][3:5] == "08":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            agosto.append(cuentas)
            cuentas = 0
            agostito=sum(agosto)

        elif venta[3][3:5] == "09":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            septiembre.append(cuentas)
            cuentas = 0
            septembrito=sum(septiembre)
    
        elif venta[3][3:5] == "10":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            octubre.append(cuentas)
            cuentas = 0
            octubrito=sum(octubre)
    
        elif venta[3][3:5] == "11":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            noviembre.append(cuentas)
            cuentas = 0
            novembrito=sum(noviembre)

        elif venta[3][3:5] == "12":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            diciembre.append(cuentas)
            cuentas = 0
            dicembrito=sum(diciembre)
      #Vamos a hacer la suma para obtener el dinero obtenido en el año
      total_anual = enerito + febrerito + marzito + abrilito + mayito + junito + julito + agostito + septembrito + octubrito + novembrito + dicembrito

    print("\nEn todo el año el total de ganancias tiene un monto igual a\n$",total_anual,"(pesos)")

  #Visualicemos las ventas mensuales
  elif opcion == "i":
    os.system('clear')
    hop = "Ventas mensuales"
    print(hop.center(50," "))
    cuentas = 0
    #Nuevamente hagamos una lista para cada mes
    mensuales = []
    enero=[]
    febrero=[]
    marzo=[]
    abril=[]
    mayo=[]
    junio=[]
    julio=[]
    agosto=[]
    septiembre=[]
    octubre=[]
    noviembre=[]
    diciembre=[]
    enerito=0
    febrerito=0
    marzito=0
    abrilito=0
    mayito=0
    junito=0
    julito=0
    agostito=0
    septembrito=0
    octubrito=0
    novembrito=0
    dicembrito=0
    for producto in ls_products:
      for venta in ls_sales:
      #Identificamos las ventas mensuales usando el dato de la fecha en la venta
        if venta[3][3:5] == "01":
          if producto[0] == venta[1]:
            cuentas += 1
            #Consideramos las devoluciones
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            enero.append(cuentas)
            cuentas = 0
            enerito=sum(enero)
        
        elif venta[3][3:5] == "02":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            febrero.append(cuentas)
            cuentas = 0
            febrerito=sum(febrero)
    
        elif venta[3][3:5] == "03":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            marzo.append(cuentas)
            cuentas = 0
            marzito=sum(marzo)

        elif venta[3][3:5] == "04":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            abril.append(cuentas)
            cuentas = 0
            abrilito=sum(abril)
    
        elif venta[3][3:5] == "05":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            mayo.append(cuentas)
            cuentas = 0
            mayito=sum(mayo)
    
        elif venta[3][3:5] == "06":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            junio.append(cuentas)
            cuentas = 0
            junito=sum(junio)
      
        elif venta[3][3:5] == "07":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            julio.append(cuentas)
            cuentas = 0
            julito=sum(julio)

        elif venta[3][3:5] == "08":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            agosto.append(cuentas)
            cuentas = 0
            agostito=sum(agosto)

        elif venta[3][3:5] == "09":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            septiembre.append(cuentas)
            cuentas = 0
            septembrito=sum(septiembre)
    
        elif venta[3][3:5] == "10":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            octubre.append(cuentas)
            cuentas = 0
            octubrito=sum(octubre)
    
        elif venta[3][3:5] == "11":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            noviembre.append(cuentas)
            cuentas = 0
            novembrito=sum(noviembre)

        else:
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            diciembre.append(cuentas)
            cuentas = 0
            dicembrito=sum(diciembre)
    #Vamos a mostrar la ganancia por cada mes    
    print("\nEn Enero se tuvo una ganancia de: \n$",enerito,"(pesos) de las ventas realizadas.")
    print("\nEn Febrero se tuvo una ganancia de: \n$",febrerito,"(pesos) de las ventas realizadas.")
    print("\nEn Marzo se tuvo una ganancia de: \n$",marzito,"(pesos) de las ventas realizadas.")
    print("\nEn Abril se tuvo una ganancia de: \n$",abrilito,"(pesos) de las ventas realizadas.")
    print("\nEn Mayo se tuvo una ganancia de: \n$",mayito,"(pesos) de las ventas realizadas.")
    print("\nEn Junio se tuvo una ganancia de: \n$",junito,"(pesos) de las ventas realizadas.")
    print("\nEn Julio se tuvo una ganancia de: \n$",julito,"(pesos) de las ventas realizadas.")
    print("\nEn Agosto se tuvo una ganancia de: \n$",agostito,"(pesos) de las ventas realizadas.")
    print("\nEn Septiembre se tuvo una ganancia de: \n$",septembrito,"(pesos) de las ventas realizadas.")
    print("\nEn Octubre se tuvo una ganancia de: \n$",octubrito,"(pesos) de las ventas realizadas.")
    print("\nEn Noviembre se tuvo una ganancia de: \n$",novembrito,"(pesos) de las ventas realizadas.")
    print("\nEn Diciembre se tuvo una ganancia de: \n$",dicembrito,"(pesos) de las ventas realizadas.")

  #Los seis meses con más ventas
  elif opcion == "j":
    os.system('clear')
    jop = "Los 6 meses con más ventas en el año"
    print(jop.center(50," "))
    cuentas = 0
    #Haremos un análisis de ventas por mes
    mensuales = []
    enero=[]
    febrero=[]
    marzo=[]
    abril=[]
    mayo=[]
    junio=[]
    julio=[]
    agosto=[]
    septiembre=[]
    octubre=[]
    noviembre=[]
    diciembre=[]
    enerito=0
    febrerito=0
    marzito=0
    abrilito=0
    mayito=0
    junito=0
    julito=0
    agostito=0
    septembrito=0
    octubrito=0
    novembrito=0
    dicembrito=0
    for producto in ls_products:
      for venta in ls_sales:
      #Hacemos búsquedas por mes
        if venta[3][3:5] == "01":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            enero.append(cuentas)
            cuentas = 0
            enerito=sum(enero)
        
        elif venta[3][3:5] == "02":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            febrero.append(cuentas)
            cuentas = 0
            febrerito=sum(febrero)
    
        elif venta[3][3:5] == "03":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            marzo.append(cuentas)
            cuentas = 0
            marzito=sum(marzo)

        elif venta[3][3:5] == "04":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            abril.append(cuentas)
            cuentas = 0
            abrilito=sum(abril)
    
        elif venta[3][3:5] == "05":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            mayo.append(cuentas)
            cuentas = 0
            mayito=sum(mayo)
    
        elif venta[3][3:5] == "06":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            junio.append(cuentas)
            cuentas = 0
            junito=sum(junio)
      
        elif venta[3][3:5] == "07":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            julio.append(cuentas)
            cuentas = 0
            julito=sum(julio)

        elif venta[3][3:5] == "08":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            agosto.append(cuentas)
            cuentas = 0
            agostito=sum(agosto)

        elif venta[3][3:5] == "09":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            septiembre.append(cuentas)
            cuentas = 0
            septembrito=sum(septiembre)
    
        elif venta[3][3:5] == "10":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            octubre.append(cuentas)
            cuentas = 0
            octubrito=sum(octubre)
    
        elif venta[3][3:5] == "11":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            noviembre.append(cuentas)
            cuentas = 0
            novembrito=sum(noviembre)

        elif venta[3][3:5] == "12":
          if producto[0] == venta[1]:
            cuentas += 1
            if venta[4]==1:
              cuentas-=1
          if cuentas  != 0:
            cuentas*=producto[2]
            diciembre.append(cuentas)
            cuentas = 0
            dicembrito=sum(diciembre)
    #Hacemos una lista del mes con las ventas correspondientes en el mismo
    meses = [["Enero",enerito],["Febrero",febrerito],["Marzo",marzito],["Abril",abrilito],["Mayo",mayito],["Junio",junito],["Julio",julito],["Agosto",agostito],["Septiembre",septembrito],["Octubre",octubrito],["Noviembre",novembrito],["Diciembre",dicembrito]]

    top_meses=[]
    while meses:
    #Vamos a acomodar de mayor a menor la cantidad de ventas
      maximo = meses[0][1]
      lista_max = meses[0]
      for elemento in meses:
        if elemento[1] > maximo:
          maximo = elemento[1]
          lista_max = elemento
      top_meses.append(lista_max)
      meses.remove(lista_max)

    toptop = []
    #Con lo siguiente, vamos a considerar únicamente los meses con ventas diferentes a cero (tomamos los meses donde si hubo venta)
    for mes in top_meses:
      if mes[1] != 0:
        toptop.append(mes)

    print(["Mes","# de ventas"])
    print(*toptop[0:6],sep="\n")

  #Damos la opción de que se muestre un mensaje en caso de que se equivoquen de letra en la entrada
  else:
    print("La letra que ingresaste no se encuentra en las opciones")
  
  #Vamos a preguntarle al usuario si quiere ver otra cosa en el programa o si se quiere retirar
  decidir = input("\n¿Quieres verificar otra opción?(Si/No) ")
  #Si se queda, puede ver de nuevo el menú y elegir otra entrada
  if decidir == "Si":
    os.system('clear')
    intento = 0
    print("Elige alguna de las siguientes opciones: \n \n-Productos más vendidos y rezagados \n a)Los 10 productos más vendidos \n b)Los 20 productos más buscados \n c)Los 5 productos con menores ventas de cada categoría \n d)Los 5 productos menos buscados de cada categoría \n e)Productos devueltos \n\n-Productos por reseña en el servicio \n f)Los 20 productos mejor calificados \n g)Los 10 productos peor calificados \n\n-Ventas e ingresos \n h)Total de ingresos y Venta total anual \n i)Ventas mensuales \n j)Meses con más ventas en el año")
    #En caso de que se quiera ir, se ve un mensaje de despedida
  else:
    intento = 1
    os.system('clear')
    print("Gracias por tu visita a LifeStore ", usuario, ". \nEsperamos la información te haya sido útil, adiós")
