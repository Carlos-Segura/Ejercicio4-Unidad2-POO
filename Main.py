from ClaseVentana import Ventana

if __name__ == '__main__':
    
    print("====VENTANA INICIO====")
    ventanaInicio = Ventana("Inicio")
    #ventanaInicio.mostrar()
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(), ventanaInicio.getAlto(), ventanaInicio.getAncho()))
    
    print('====VENTANA CARGAR====')
    ventanaCargar = Ventana('Cargar',10,20)
    #ventanaCargar.mostrar()
    print('***Mueve a la derecha***')
    ventanaCargar.moverDerecha(10)
    #ventanaCargar.mostrar()
    print('***Mueve a la izquierda***')
    ventanaCargar.moverIzquierda(10)
    #ventanaCargar.mostrar()
    print('***Bajar***')
    ventanaCargar.Bajar(10)
    #ventanaCargar.mostrar()
    
    print('====VENTANA BORRAR====')
    ventanaBorrar = Ventana('Borrar',10,20,100,200)
    #ventanaBorrar.mostrar()
    print('***Subir***')
    ventanaBorrar.Subir(5)
    #ventanaBorrar.mostrar()
    print('***Bajar***')
    ventanaBorrar.Bajar()
    #ventanaBorrar.mostrar()