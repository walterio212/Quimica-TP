#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division, print_function
from visual import *
from particula import Particula
import modulo_const as const
import modulo_interfaz_grafica as interfaz
import modulo_particulas
from random import uniform
import wx

# Inicializaciones

cantidadParticulas = 15
particulas = []
velMaxAbsoluta = 10
deltaT = 0.005
t = 0
escala = 0.1
P1 = 0.082 * 10 * 70 / 10


interfaz.s1.SetValue(298.15)

lblTemperaturaValor = wx.StaticText(interfaz.p, pos=(1.0 * const.L, 1.55 * const.L),
                                    label=str(interfaz.s1.GetValue()))

modulo_particulas.crearParticulas(particulas,cantidadParticulas, const.centroPared
                * const.factorCorreccionPosicion, velMaxAbsoluta)

temperaturaPrevia = interfaz.s1.GetValue()

while True:
    rate(100)
    temperatura = interfaz.s1.GetValue()
    lblTemperaturaValor.SetLabel(str(temperatura))

    interfaz.valorPresion.SetLabel(str(P1 * temperatura / 70) + ' ATM')
    interfaz.valorTemperaturaC.SetLabel(str(temperatura - 273.15))

    particulasEvaluadas = []

    if modulo_particulas.particulasDetenidas(particulas) and temperatura \
        != 0:
        modulo_particulas.regenerarVelocidades(particulas, temperatura)

    for particula in particulas:

        modulo_particulas.evaluarColisionParticulas(particula,
                particulasEvaluadas)
        particulasEvaluadas.append(particula)

        # movimiento en X limitado por  las paredes izquierda y derecha

        modulo_particulas.evaluarColisionParedX(particula.sphereView,
                interfaz.paredDer, interfaz.paredIzq)

        # movimiento en Y limitado por  las paredes inferior y superior

        modulo_particulas.evaluarColisionParedY(particula.sphereView,
                interfaz.paredSup, interfaz.paredInf)

        # movimiento en Z limitado por  las paredes frontal y trasera

        modulo_particulas.evaluarColisionParedZ(particula.sphereView,
                interfaz.paredFrontal, interfaz.paredTrasera)

        particula.sphereView.pos = particula.sphereView.pos \
            + particula.sphereView.velocity * deltaT

    t = t + deltaT

    if temperaturaPrevia != temperatura:
        temperaturaPrevia = temperatura
        modulo_particulas.variarValocidadPorTemperatura(particulas,
                temperatura)

            