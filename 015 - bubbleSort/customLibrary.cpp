// aqui se implementan los detalles (operaciones) de las funciones

#include <vector>
#include <iostream>

namespace customLibrary{

/*
     Bubble Sort: Esta funcion ordena un vector de entrada
     Argumentos: std::vector<float>& inputVector - la referencia al vector a ordenar
                 const bool& inputSortOrder - la referencia a la bandera del sentido de ordenamiento
                 float& inputMinNumber - la referenica a la variable que va a almacenar el elemento menor
                 float* inputPointerMaxNumber - apuntador a la variable que almacena el elemento mayor

*/
    void bubbleSort( std::vector<float>& inputVector, const bool& inputSortOrder,
                     float& inputMinNumber, float* inputPointerMaxNumber ){

        int vectorElements = (int)inputVector.size();

        // bandera para decidir cuando terminamos de iterar
        // el vector
        // utilizamos esta bandera pasa saber cuando el vector
        // esta ordenado
        bool swap = true;

        // bucle que corre mientras la bandera de intercambio
        // esta activada
        while ( swap ){

            // el valor de inicio de la bandera de swap
            swap = false;

            // bucle (for) que examina parejas de numeros
            for( int i = 0; i < vectorElements - 1; i++ ){
                // extraer los dos elementos dee parejas de numeros
                float a = inputVector[ i ];   // elemento de la izquierda
                float b = inputVector[ i+1 ]; // elemento de la derecha

                // determinar el sentido de ordenamiento
                if ( inputSortOrder ){

                    // ordenamiento de menor a mayor
                    // determinar si a > b -> se debe efectuar un swap
                    if ( a > b ){
                        // cambiar el valor de la bandera de swap
                        swap = true;
                        // intercambiar los elementos del vector
                        inputVector[ i ] = b; // el elemento de la izquierda (despues del swap)
                        inputVector[ i+1 ] = a; // el elemento de la derecha (despues del swap)
                    }

                }else{

                    // ordenamiento de mayor a menor
                    // determinar si a > b -> se debe efectuar un swap
                    if ( a < b ){
                        // cambiar el valor de la bandera de swap
                        swap = true;
                        // intercambiar los elementos del vector
                        inputVector[ i ] = b; // el elemento de la izquierda (despues del swap)
                        inputVector[ i+1 ] = a; // el elemento de la derecha (despues del swap)
                    }

                }



            }

        }

        // desde aqui el vector ya esta ordenado

        int minIndex; // va a adquirir el indice del menor elemento
        int maxIndex; // va a adquirir el indice del mayor elemento

        // esos valores de indices dependen de la bandera de
        // ordenamiento
        if ( inputSortOrder ){
            // el ordenamiento es de menor a mayor:
            minIndex = 0; // el primer elemento del vector ordenado
            maxIndex = vectorElements - 1; // el ultimo elemento del vector ordenado
        }else{
            // el ordenamiento es de mayor a menor:
            minIndex = vectorElements - 1; // el ultimo elemento del vector ordenado
            maxIndex = 0;
        }

        // parametros de salida
        inputMinNumber = inputVector[minIndex]; // se lo devolvemos por referencia
        // modificando el valor de un apuntador
        // ya estoy afectando el valor de la direccion almacenada
        *inputPointerMaxNumber = inputVector[maxIndex]; // modificacion por apuntador


    }

}
