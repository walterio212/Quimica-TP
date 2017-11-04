from __future__ import division, print_function
from visual import *
from random import uniform
import wx

def crearParticulas(particulasLista, cantidadACrear, centroPared, velMaxAbsoluta):
    for x in xrange(cantidadACrear):
        nuevaParticula = sphere(pos = (uniform(-centroPared, centroPared), uniform(-centroPared, centroPared), uniform(-centroPared, centroPared)), radius = 0.2, color = color.cyan)
        nuevaParticula.velocity = vector(uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta))
        particulasLista.append(nuevaParticula)

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

def regenerarVelocidades(particulas, velMaxAbsoluta):
    for x in particulas:        
        x.velocity = vector(uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta))        

def particulasDetenidas(particulas):
    estanDetenidas = True
    for x in particulas:        
        if(estanDetenidas and x.velocity.x == 0 and x.velocity.y == 0 and x.velocity.z == 0):
            estanDetenidas = True
        else:
            estanDetenidas = False
            break

    return estanDetenidas        

def obtenerLambdaVelocidad(temperatura):
    factorConversion = ((temperatura * 150 / 1000))
    return factorConversion * 10/100

def variarValocidadPorTemperatura(particulas, temperatura):
    lambdaVelocidad = obtenerLambdaVelocidad(temperatura)
    for x in particulas:
        x.velocity = lambdaVelocidad * x.velocity

def leave(evt): # called on "Exit under program control" button event
    exit()
    
L = 320
# Create a window. Note that w.win is the wxPython "Frame" (the window).
# window.dwidth and window.dheight are the extra width and height of the window
# compared to the display region inside the window. If there is a menu bar,
# there is an additional height taken up, of amount window.menuheight.
# The default style is wx.DEFAULT_FRAME_STYLE; the style specified here
# does not enable resizing, minimizing, or full-sreening of the window.
w = window(width=2*(L+window.dwidth), height=L+window.dheight+window.menuheight+300,
           menus=True, title='Simulador Gases Ideales - Untref',
           style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

# Place a 3D display widget in the left half of the window.
d = 20
disp = display(window=w, x=d, y=d+20, width=400, height=400, forward=-vector(0,1,2))

# Place buttons, radio buttons, a scrolling text object, and a slider
# in the right half of the window. Positions and sizes are given in
# terms of pixels, and pos(0,0) is the upper left corner of the window.
p = w.panel # Refers to the full region of the window in which to place widgets

temperaturaMaxima = 1000

wx.StaticText(p, pos=(d,4), size=(L-2*d,d), label='Simulador Gases Ideales - Untref', style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

s1 = wx.Slider(p, pos=(d,500), size=(400,20), minValue=-0, maxValue=temperaturaMaxima)
s1.SetBackgroundColour((50,50,50))

lblTemperaturaK = wx.StaticText(p, pos=(0.2*L,0.95*500), label='Temperatura (K)', size=(100,40))
lblTemperaturaK.SetForegroundColour((255,0,0))

# Initializations
s1.SetValue(70)

lblTemperaturaValor = wx.StaticText(p, pos=(1.0*L,1.75*L), label=str(s1.GetValue()))

tamanio = 10
opacidad = 0.1
factorCorreccionPosicion = 99/100
centroPared = tamanio/2


paredDer = box(pos = (centroPared, 0, 0), size = (0.2, tamanio, tamanio), color = color.green, opacity = opacidad)
paredIzq = box(pos = (-centroPared, 0, 0), size = (0.2, tamanio, tamanio), color = color.green, opacity = opacidad)

paredSup = box(pos = (0, centroPared, 0), size = (tamanio, 0.2, tamanio), color = color.green, opacity = opacidad)
paredInf = box(pos = (0, -centroPared, 0), size = (tamanio, 0.2, tamanio), color = color.green, opacity = opacidad)

paredTrasera = box(pos = (0, 0, -centroPared), size = (tamanio, tamanio, 0.2), color = color.green, opacity = opacidad)
paredFrontal = box(pos = (0, 0, centroPared), size = (tamanio, tamanio, 0.2), color = color.green, opacity = opacidad)

cantidadParticulas = 25

particulas = []

velMaxAbsoluta = 10

crearParticulas(particulas, cantidadParticulas, centroPared * factorCorreccionPosicion, velMaxAbsoluta)

deltaT = 0.005
t = 0

escala = 0.1

temperaturaPrevia = s1.GetValue()

while True:
    rate(100)
    temperatura = s1.GetValue()
    lblTemperaturaValor.SetLabel(str(temperatura))
    particulasEvaluadas = []

    if(particulasDetenidas(particulas) and temperatura != 0):
        regenerarVelocidades(particulas, temperatura)

    #if(temperaturaPrevia != temperatura):
    #    temperaturaPrevia = temperatura
    #    variarValocidadPorTemperatura(particulas, temperatura)
    
    for particula in particulas:

        evaluarColisionParticulas(particula, particulasEvaluadas)
        particulasEvaluadas.append(particula)
        
        #movimiento en X limitado por  las paredes izquierda y derecha
        evaluarColisionParedX(particula, paredDer, paredIzq)

        #movimiento en Y limitado por  las paredes inferior y superior
        evaluarColisionParedY(particula, paredSup, paredInf)

        #movimiento en Z limitado por  las paredes frontal y trasera
        evaluarColisionParedZ(particula, paredFrontal, paredTrasera)

        particula.pos = particula.pos + (particula.velocity * deltaT)
        
    t = t + deltaT
       
