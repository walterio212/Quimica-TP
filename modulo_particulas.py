#!/usr/bin/python
# -*- coding: utf-8 -*-
from visual import *
from random import uniform
from particula import Particula

def crearParticulas(
    particulasLista,
    cantidadACrear,
    centroPared,
    velMaxAbsoluta,
    ):
    for x in xrange(cantidadACrear):
        esfera = sphere(pos=(uniform(-centroPared, centroPared),
                        uniform(-centroPared, centroPared),
                        uniform(-centroPared, centroPared)),
                        radius=0.2, color=color.cyan)
        vectorVelocidad = vector(uniform(-velMaxAbsoluta,
                                 velMaxAbsoluta),
                                 uniform(-velMaxAbsoluta,
                                 velMaxAbsoluta),
                                 uniform(-velMaxAbsoluta,
                                 velMaxAbsoluta))
        esfera.velocity = vectorVelocidad
        nuevaParticula = Particula(vectorVelocidad, esfera)
        nuevaParticula.velocidadOriginal = vector(vectorVelocidad.x,
                vectorVelocidad.y, vectorVelocidad.z)
        particulasLista.append(nuevaParticula)

def particulasEnMismaPosicion(particula1, particula2):
    return particula1.pos.x == particula2.pos.x and particula1.pos.y \
        == particula2.pos.y and particula1.pos.z == particula2.pos.z


def evaluarColisionParticulas(particula, listaParticulas):
    for elemento in listaParticulas:
        hayColision = particulasEnMismaPosicion(particula.sphereView,
                elemento.sphereView)
        if hayColision:
            aux = elemento.sphereView.velocity
            elemento.sphereView.velocity = particula.sphereView.velocity
            particula.sphereView.velocity = aux


def evaluarColisionParedX(particula, pared1, pared2):
    if particula.pos.x >= pared1.pos.x or particula.pos.x \
        < pared2.pos.x:
        particula.velocity.x = -particula.velocity.x


def evaluarColisionParedY(particula, pared1, pared2):
    if particula.pos.y >= pared1.pos.y or particula.pos.y \
        < pared2.pos.y:
        particula.velocity.y = -particula.velocity.y


def evaluarColisionParedZ(particula, pared1, pared2):
    if particula.pos.z >= pared1.pos.z or particula.pos.z \
        < pared2.pos.z:
        particula.velocity.z = -particula.velocity.z


def regenerarVelocidades(particulas, velMaxAbsoluta):

    # vector(uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta), uniform(-velMaxAbsoluta, velMaxAbsoluta))

    for x in particulas:
        x.sphereView.velocity = x.velocidadOriginal


def particulasDetenidas(particulas):
    estanDetenidas = True
    for x in particulas:
        esfera = x.sphereView
        if estanDetenidas and esfera.velocity.x == 0 \
            and esfera.velocity.y == 0 and esfera.velocity.z == 0:
            estanDetenidas = True
        else:
            estanDetenidas = False
            break

    return estanDetenidas


def obtenerLambdaVelocidad(temperatura):
    factorConversion = temperatura * 45 / 1000
    return (factorConversion * 10 / 100)


def variarValocidadPorTemperatura(particulas, temperatura):
    lambdaVelocidad = obtenerLambdaVelocidad(temperatura)
    for x in particulas:

        xsign = (1 if x.sphereView.velocity.x > 0 else -1)
        ysign = (1 if x.sphereView.velocity.y > 0 else -1)
        zsign = (1 if x.sphereView.velocity.z > 0 else -1)

        x.sphereView.velocity = lambdaVelocidad * vector(xsign
                * x.velocidadOriginal.x, ysign * x.velocidadOriginal.y,
                zsign * x.velocidadOriginal.z)


