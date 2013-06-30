import sys

def main():
    
    if(len(sys.argv) > 1):
        print 'abrir: ' + sys.argv[1]
        nombrearchivo=sys.argv[1]
    else:
        print 'archivo cargado por defecto'
        nombrearchivo="hola.txt"

    print '*************************'
    
    archivo=open(nombrearchivo,'r')    
    completo=archivo.read()
    print completo

    print '*************************'

    archivo=open(nombrearchivo,'r')    
    linea=archivo.readline()
    print linea
    linea=archivo.readline()
    print linea
    linea=archivo.readline()
    print linea

    print '*************************'

    archivo=open(nombrearchivo,'r')    
    vector=archivo.readlines()
    print vector

    print '*************************'


    


if __name__ == "__main__":
    main()
