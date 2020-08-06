print("¿Que operacion quieres hacer A)Suma B)Resta C)Multiplicacion o D)Division?")
print("Escribe un inciso, ya sea A B C o D: ")

inc=input()
if inc == "A":
    print("¿Cuantos valores quieres sumar?")
    lst=[]
    suma=0
    num=int(input())
    for number in range(num):
        print("Dame un valor: ")
        A=int(input())
        lst.append(A)
    for i in range(0,len(lst)):
        suma=suma+lst[i]
    print(f"answer: {suma}")
    
elif inc == "B":
    print("¿Cuantos valores quieres restar?")
    lst=[]
    resta=0
    num=int(input())
    for number in range(num):
        print("Dame un valor (No es necesario poner signo): ")
        A=int(input())
        lst.append(A)
    for i in range(0,len(lst)):
        resta=lst[i]-resta
    print(f"answer: {resta-resta-resta}")

elif inc == "C":
    print("Dame un valor a multiplicar: ")
    A=int(input())
    print("¿Por cuanto lo vas a multiplicar?")
    B=int(input())
    RESU=A*B
    print(f"answer: {RESU}")

elif inc == "D":
    print("Dame un dividendo (El valor que dividiras): ")
    A=int(input())
    print("Dame el divisior (Cuanto le dividiras): ")
    B=int(input())
    RESU=A/B
    print(f"answer: {RESU}")

else:
    print("Solo leo incisos con este formato: A B C o D")
