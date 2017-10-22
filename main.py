from visual import *

def particulasEnMismaPosicion(particula1, particula2):
    return particula1.pos.x == particula2.pos.x and particula1.pos.y == particula2.pos.y and particula1.pos.z == particula2.pos.z

def evaluarColisionParticulas(particula, listaParticulas):
    for elemento in listaParticulas:
        hayColision = particulasEnMismaPosicion(particula, elemento)
        if(hayColision):
            aux = elemento.velocity
            elemento.velocity = particula.velocity
            particula.velocity = aux

def evaluarColisionParedX(particula, pared1, pared2):
    if particula.pos.x >= pared1.pos.x or particula.pos.x < pared2.pos.x:
        particula.velocity.x = -particula.velocity.x
    
def evaluarColisionParedY(particula, pared1, pared2):
    if particula.pos.y >= pared1.pos.y or particula.pos.y < pared2.pos.y:
        particula.velocity.y = -particula.velocity.y

def evaluarColisionParedZ(particula, pared1, pared2):
    if particula.pos.z >= pared1.pos.z or particula.pos.z < pared2.pos.z:
        particula.velocity.z = -particula.velocity.z
        
tamanio = 10
centroPared = tamanio/2
paredDer = box(pos = (centroPared, 0, 0), size = (0.2, tamanio, tamanio), color = color.green, opacity = 0.2)
paredIzq = box(pos = (-centroPared, 0, 0), size = (0.2, tamanio, tamanio), color = color.green, opacity = 0.2)

paredSup = box(pos = (0, centroPared, 0), size = (tamanio, 0.2, tamanio), color = color.green, opacity = 0.2)
paredInf = box(pos = (0, -centroPared, 0), size = (tamanio, 0.2, tamanio), color = color.green, opacity = 0.2)

paredTrasera = box(pos = (0, 0, -centroPared), size = (tamanio, tamanio, 0.2), color = color.green, opacity = 0.2)
paredFrontal = box(pos = (0, 0, centroPared), size = (tamanio, tamanio, 0.2), color = color.green, opacity = 0.01)

particula1 = sphere(pos = (-5, 0, 0), radius = 0.2, color = color.cyan)
particula2 = sphere(pos = (-2, 0, 0), radius = 0.2, color = color.cyan)
particula3 = sphere(pos = (1, 0, 0), radius = 0.2, color = color.cyan)
particula4 = sphere(pos = (4, 0, 0), radius = 0.2, color = color.red)
particula5 = sphere(pos = (-4, 0, 0), radius = 0.2, color = color.red)

particulas = [particula1, particula2, particula3, particula4, particula5]

particula1.velocity = vector(25, 4, -6)
particula2.velocity = vector(2, 14, -6)
particula3.velocity = vector(5, -4, 3)
particula4.velocity = vector(15, -24, 1)
particula5.velocity = vector(-15, 24, -1)

deltaT = 0.005
t = 0

escala = 0.1

while true:
    rate(100)
    particulasEvaluadas = []

    for particula in particulas:

        evaluarColisionParticulas(particula, particulasEvaluadas)
        particulasEvaluadas.append(particula)
        
        #movimiento en X limitado por  las paredes izquierda y derecha
        evaluarColisionParedX(particula, paredDer, paredIzq)

        #movimiento en Y limitado por  las paredes inferior y superior
        evaluarColisionParedY(particula, paredSup, paredInf)

        #movimiento en Z limitado por  las paredes frontal y trasera
        evaluarColisionParedZ(particula, paredFrontal, paredTrasera)

        particula.pos = particula.pos + particula.velocity * deltaT
        
    t = t + deltaT
