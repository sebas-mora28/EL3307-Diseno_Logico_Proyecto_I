import matplotlib.pyplot as plt

'''
Esta función recibe una señal de entrada y produce un gráfico
de matplotlib de la codificación NRZ-I de esa señal.

Requiere matplotlib para funcionar.

Ejemplo de uso:
>>> plot_NRZI("100110100101", 0b1)

TO DO:
     (1) poner labels en los ejes
     (2) poner alguna label de la señal original
     (3) poner alguna label de la codificación nrzi
     (4) graficar la señal original
     (5) nightmode

@param signal: Señal de entrada. Es una string que
               representa una señal. Por ejemplo: "100110100101"

@param initial_state: Estado inicial de la señal. Es un número en
                      representación binaria de python,
                      por ejemplo: 0b1

@return: None
'''
def plot_NRZI(signal: str, initial_state: bin) -> None:
    signal: list = [int(bit) for bit in signal]
    nrzi: list = []
    state: bin = initial_state
    
    for bit in signal:
        state ^= bit
        nrzi.append(state)
    
    print(f"signal: {signal}")
    print(f"nrzi:   {nrzi}")

    nrzi = [-1 if x == 0 else x for x in nrzi]

    nrzi.insert(0, nrzi[0]) # esto es un hack asquerosísimo pero ya sirve bien,
                            # luego veo cómo arreglarlo
    
    plt.plot(nrzi, drawstyle='steps-pre')
    x_axis = list((range(len(nrzi))))
    plt.xticks(x_axis)
    plt.yticks([-1,0,1])
    plt.show()
