print("\t\tConsulta sobre su salario");
print("\n\nDatos: ");


def calcularImpuestos(nombre):
  #Preguntas
  dui=(input("Ingrese el numero de su DUI: "));
  nit=(input("Ingrese el numero de su NIT: "));

  sueldo=float(input("Ingrese su salario mensual $: "));
  bono=float(input("Ingrese el bono que se le ha otorgado $: "));
  if sueldo<300:
    print("\nA su sueldo no se le puede aplicar isss ya, que esta por debajo minimo");
    isss=0
  elif sueldo>1000:
    print("ISSS: $30.00 Dolares");
    isss=30;
  else:
    isss=sueldo*0.03 
  if sueldo<300:
    print("\nA su sueldo no se le puede aplicar afp ya, que esta por debajo minimo");
    afp=0
  elif sueldo>6500:
    print("AFP: 471.25 Dolares");
    afp=471.25;
  else:
    afp=sueldo*0.0725;
  renta=sueldo*0.1;
  

  print("\t\tDatos");
  print("Nombre: ",nombre);
  print("DUI: ",dui);
  print("NIT: ",nit);
  print("Sueldo $: ",sueldo);
  print("\nDescuentos");
  print("ISSS: ",isss,"Dolares");
  print("AFP: ",round(afp,2),"Dolares");
  print("Renta: ",round(renta,2)," Dolares");
  print("\n\t\tBonos");
  print("Bono $: ",bono,"Dolares");
  resultado=sueldo-isss-renta-afp+bono;
  
  print("Salario neto a recibir es: ",round(resultado,2),"Dolares");
 
while True:
  opcion=int(input("1.llenar datos \n2.Salir \n-->"));
  if opcion == 1:
    calcularImpuestos(nombre=input("Cual es su nombre: "));
  else:
    False
    print("Fin del programa....");
    break  
