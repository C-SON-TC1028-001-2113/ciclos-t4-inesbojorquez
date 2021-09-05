
def main():
    a = int(input("Valor 1: "))
    b = int(input("Valor 2: "))
    if  a>0 and b>0 :
        if a!=b :
            if a > b:
                for i in range(b,a+1):
                    if i%2 ==0 :
                        print(i)
            elif b > a :
                for i in range(a,b+1):
                    if i%2==0:
                        print(i)   
        else:
            print( "No hay pares")                         

if __name__=='__main__':
    main()
