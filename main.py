from visual import *
particula = sphere(pos = (-5, 0, 0), radius = 0.5, color = color.cyan)
paredDer = box(pos = (6, 0, 0), size = (0.2, 12, 12), color = color.green, opacity = 0.2)
paredIzq = box(pos = (-6, 0, 0), size = (0.2, 12, 12), color = color.green, opacity = 0.2)

paredSup = box(pos = (0, 6, 0), size = (12, 0.2, 12), color = color.green, opacity = 0.2)
paredInf = box(pos = (0, -6, 0), size = (12, 0.2, 12), color = color.green, opacity = 0.2)

paredTrasera = box(pos = (0, 0, -6), size = (12, 12, 0.2), color = color.green, opacity = 0.2)
paredFrontal = box(pos = (0, 0, 6), size = (12, 12, 0.2), color = color.green, opacity = 0.01)

particula.velocity = vector(25, 4, -6)

deltaT = 0.005
t = 0

escala = 0.1
vectorVelocidad = arrow(pos = particula.pos, axis = escala * particula.velocity, color = color.yellow)

#rastro de la particula
particula.trail = curve(color=particula.color, retain = 50, interval = 20)

while t < 100:
    rate(100)

    #movimiento en X limitado por  las paredes izquierda y derecha
    if particula.pos.x >= paredDer.pos.x or particula.pos.x < paredIzq.pos.x:
        particula.velocity.x = -particula.velocity.x
        vectorVelocidad.axis.x = -vectorVelocidad.axis.x

    #movimiento en Y limitado por  las paredes inferior y superior
    if particula.pos.y >= paredSup.pos.y or particula.pos.y < paredInf.pos.y:
        particula.velocity.y = -particula.velocity.y
        vectorVelocidad.axis.y = -vectorVelocidad.axis.y

    #movimiento en Z limitado por  las paredes frontal y trasera
    if particula.pos.z >= paredFrontal.pos.z or particula.pos.z < paredTrasera.pos.z:
        particula.velocity.z = -particula.velocity.z
        vectorVelocidad.axis.z = -vectorVelocidad.axis.z
        
    particula.pos = particula.pos + particula.velocity * deltaT
    particula.trail.append(pos = particula.pos)
    vectorVelocidad.pos = particula.pos
    t = t + deltaT
