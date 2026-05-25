from math import sin,cos,pi

D = 81.21       # distancia em mm do alvo optico
alfa = 0.5        # angulo de rotacao
alfa = alfa*pi/180 

deltaY = 2*sin(alfa/2)*D
deltaZ = (1-cos(alfa/2))*D

print(deltaY), print(deltaZ)