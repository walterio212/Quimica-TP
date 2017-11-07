from __future__ import division, print_function
from visual import *
from particula import Particula
from random import uniform
import wx

def crearParticulas(particulasLista, cantidadACrear, centroPared, velMaxAbsoluta):
    for x in xrange(cantidadACrear):
        esfera = sphere(pos = (uniform(-centroPared, centroPared), uniform(-centroPared, centroPared), uniform(-centroPared, centroPared)), radius = 0.2, color = color.cyan)
        vectorVelocidad = vector(uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta))
        esfera.velocity = vectorVelocidad
        nuevaParticula = Particula(vectorVelocidad, esfera)
        nuevaParticula.velocidadOriginal = vector(vectorVelocidad.x, vectorVelocidad.y, vectorVelocidad.z)
        particulasLista.append(nuevaParticula)

def particulasEnMismaPosicion(particula1, particula2):
    return particula1.pos.x == particula2.pos.x and particula1.pos.y == particula2.pos.y and particula1.pos.z == particula2.pos.z

def evaluarColisionParticulas(particula, listaParticulas):
    for elemento in listaParticulas:
        hayColision = particulasEnMismaPosicion(particula.sphereView, elemento.sphereView)
        if(hayColision):
            aux = elemento.sphereView.velocity
            elemento.sphereView.velocity = particula.sphereView.velocity
            particula.sphereView.velocity = aux

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
    #vector(uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta))
    for x in particulas:        
        x.sphereView.velocity = x.velocidadOriginal

def particulasDetenidas(particulas):
    estanDetenidas = True
    for x in particulas:
        esfera = x.sphereView
        if(estanDetenidas and esfera.velocity.x == 0 and esfera.velocity.y == 0 and esfera.velocity.z == 0):
            estanDetenidas = True
        else:
            estanDetenidas = False
            break

    return estanDetenidas        

def obtenerLambdaVelocidad(temperatura):
    factorConversion = ((temperatura * 45 / 1000))
    return factorConversion * 10/100

def variarValocidadPorTemperatura(particulas, temperatura):
    lambdaVelocidad = obtenerLambdaVelocidad(temperatura)
    for x in particulas:
        
        xsign = 1 if x.sphereView.velocity.x > 0 else -1
        ysign = 1 if x.sphereView.velocity.y > 0 else -1
        zsign = 1 if x.sphereView.velocity.z > 0 else -1
        
        x.sphereView.velocity = lambdaVelocidad * vector(xsign * x.velocidadOriginal.x, ysign * x.velocidadOriginal.y, zsign * x.velocidadOriginal.z)

def leave(evt): 
    exit()
    
L = 320

w = window(width=2*(L+window.dwidth), height=L+window.dheight+window.menuheight+200,
           menus=True, title='Simulador Gases Ideales - Untref',
           style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

d = 20
disp = display(window=w, x=d, y=d+20, width=400, height=400, forward=-vector(0,1,2))

p = w.panel 

temperaturaMaxima = 1000

wx.StaticText(p, pos=(d+150,10), size=(L-2*d,d), label='Simulador Gases Ideales - Untref', style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

s1 = wx.Slider(p, pos=(0.4*L,0.95*500), size=(400,20), minValue=-0, maxValue=temperaturaMaxima)
s1.SetBackgroundColour((50,50,50))

lblTemperaturaK = wx.StaticText(p, pos=(0.1*L,0.95*500), label='Temperatura (K):', size=(100,40))
lblTemperaturaK.SetForegroundColour((255,0,0))

#Modificacion RV

#text(pos= (0,10,10),text='GASES IDEALES',
#   align='center',height = 0.5, depth= 0.8, color=color.green)


LblDatos = wx.StaticText(p, pos=(520, 40), label='DATOS:', size=(40,15))
LblDatos.SetForegroundColour((0,0,0))

LblPresion = wx.StaticText(p, pos=(450, 80), label='PRESIÓN:', size=(50,15))
LblPresion.SetBackgroundColour((255,255,0))
valorPresion = wx.StaticText(p, pos=(570, 80), size=(100,15))
valorPresion.SetForegroundColour((255,0,0))

cantidadParticulas = wx.StaticText(p, pos=(450, 120), label='PARTICULAS:', size=(70,15))
cantidadParticulas.SetBackgroundColour((255,255,0))
valorParticulas = wx.StaticText(p, pos=(570, 120), label='25', size=(100,15))
valorParticulas.SetForegroundColour((255,0,0))

LblTemperaturaC = wx.StaticText(p, pos=(450, 160), label='TEMPERATURA °C:', size=(100,15))
LblTemperaturaC.SetBackgroundColour((255,255,0))
valorTemperaturaC = wx.StaticText(p, pos=(570, 160), size=(200,15))
valorTemperaturaC.SetForegroundColour((255,0,0))

LblVolumen = wx.StaticText(p, pos=(450, 200), label='VOLUMEN:', size=(60,15))
LblVolumen.SetBackgroundColour((255,255,0))
valorVolumen = wx.StaticText(p, pos=(570, 200), label='1 L', size=(200,15))
valorVolumen.SetForegroundColour((255,0,0))

LblMoles = wx.StaticText(p, pos=(450, 240), label='MOLES:', size=(40,15))
LblMoles.SetBackgroundColour((255,255,0))
valorMoles = wx.StaticText(p, pos=(570, 240), label='10 M', size=(200,15))
valorMoles.SetForegroundColour((255,0,0))

# Inicializaciones
s1.SetValue(70)

lblTemperaturaValor = wx.StaticText(p, pos=(1.0*L,1.55*L), label=str(s1.GetValue()))

tamanio = 10
opacidad = 0.1
factorCorreccionPosicion = 90/100
centroPared = tamanio/2

paredDer = box(pos = (centroPared, 0, 0), size = (0.2, tamanio, tamanio), color = color.green, opacity = opacidad)
paredIzq = box(pos = (-centroPared, 0, 0), size = (0.2, tamanio, tamanio), color = color.green, opacity = opacidad)

paredSup = box(pos = (0, centroPared, 0), size = (tamanio, 0.2, tamanio), color = color.green, opacity = opacidad)
paredInf = box(pos = (0, -centroPared, 0), size = (tamanio, 0.2, tamanio), color = color.green, opacity = opacidad)

paredTrasera = box(pos = (0, 0, -centroPared), size = (tamanio, tamanio, 0.2), color = color.green, opacity = opacidad)
paredFrontal = box(pos = (0, 0, centroPared), size = (tamanio, tamanio, 0.2), color = color.green, opacity = opacidad)

cantidadParticulas = 15

particulas = []

velMaxAbsoluta = 10

crearParticulas(particulas, cantidadParticulas, centroPared * factorCorreccionPosicion, velMaxAbsoluta)

deltaT = 0.005
t = 0

escala = 0.1

temperaturaPrevia = s1.GetValue()

P1 = (0.082 * 10 * 70) / 10


while True:
    rate(100)
    temperatura = s1.GetValue()
    lblTemperaturaValor.SetLabel(str(temperatura))
    
#RV FALTA CALCULO DE PRESION...

    valorPresion.SetLabel(str((P1*temperatura)/70) + ' ATM')
    valorTemperaturaC.SetLabel(str(temperatura - 273.15))

#
    particulasEvaluadas = []

    if(particulasDetenidas(particulas) and temperatura != 0):
        regenerarVelocidades(particulas, temperatura)

    for particula in particulas:

        evaluarColisionParticulas(particula, particulasEvaluadas)
        particulasEvaluadas.append(particula)
        
        #movimiento en X limitado por  las paredes izquierda y derecha
        evaluarColisionParedX(particula.sphereView, paredDer, paredIzq)

        #movimiento en Y limitado por  las paredes inferior y superior
        evaluarColisionParedY(particula.sphereView, paredSup, paredInf)

        #movimiento en Z limitado por  las paredes frontal y trasera
        evaluarColisionParedZ(particula.sphereView, paredFrontal, paredTrasera)

        particula.sphereView.pos = particula.sphereView.pos + (particula.sphereView.velocity * deltaT)
        
    t = t + deltaT

    if(temperaturaPrevia != temperatura):
        temperaturaPrevia = temperatura
        variarValocidadPorTemperatura(particulas, temperatura)
