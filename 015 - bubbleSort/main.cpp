#include <iostream>
#include <vector>
#include "customLibrary.h"

int main()
{

    // declarar el vector que contiene la lista de numeros:
    std::vector<float> numberList;

    // almacenar algunos valores en el vector:
    numberList.push_back( 6.0 );
    numberList.push_back( 8.0 );
    numberList.push_back( 1.0 );
    numberList.push_back( 4.0 );
    numberList.push_back( 2.0 );

    // el tamanyo del vector, es decir, el numero de
    // elementos del vector:
    int vectorElements = (int)numberList.size();

    // variable que controla el orden/sentido de ordenamiento:
    bool sortOrder = true; // true -> menor a mayor, false -> mayor a menor

    // variables para almacenar el numero menor y el numero mayor de
    // todo el vector:
    float minNumber = 0.0;
    float maxNumber = 100.0;

    //  preparar el apuntador a maxNumber
    float* pointerMaxNumber;       // declaramos el apuntador a float
    pointerMaxNumber = &maxNumber; // creamos la referencia a la variable maxNumber

    // llamada a la funcion de la libreria
    customLibrary::bubbleSort( numberList, sortOrder, minNumber, pointerMaxNumber );

    // imprimir el vector ya ordenado:
    for( int i = 0; i < vectorElements; i++ ){
        // buscar el elemento actual del vector  (actual en esa iteracion)
        float currentValue = numberList[ i ];
        // imprimir la info
        std::cout<<"i: "<<i<<" - "<<currentValue<<std::endl;
    }

    std::cout<<"Min number: "<<minNumber<<std::endl;
    std::cout<<"Max number: "<<maxNumber<<std::endl;

    // informacion de apuntador:
    std::cout<<"**********Info de mi apuntador/referencia:**********"<<std::endl;
    std::cout<<"Direccion del elemento mayor (max): "<<&maxNumber<<std::endl;
    std::cout<<"Direccion del apuntador al elemento mayor: "<<&pointerMaxNumber<<std::endl;
    std::cout<<"Contenido del apuntador al elemento mayor: "<<pointerMaxNumber<<std::endl;
    std::cout<<"[Direccionamiento Indirecto]Datos del contenido del apuntador: "<<*pointerMaxNumber<<std::endl;

    return 0;
}
