// aqui se define el prototipo/interfaz de las funciones
// el tipo de dato que regresa la funcion, los tipos de datos de sus argumentos

#ifndef CUSTOMLIBRARY_H
#define CUSTOMLIBRARY_H

// inlcuimos a vector
#include <vector>

    // definimos nuestro namespace
namespace customLibrary {

    void bubbleSort( std::vector<float>& inputVector, const bool& inputSortOrder,
                     float& inputMinNumber, float* inputPointerMaxNumber );

}


#endif // CUSTOMLIBRARY_H
