# Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input('Distância da viagem: '))
velocidade_media = float(input('Velocidade média: '))
tempo = distancia / velocidade_media

print(f'O tempo de duração da viagem será: {tempo:.2f}')
