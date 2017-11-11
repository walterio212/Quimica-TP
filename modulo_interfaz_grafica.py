import modulo_const as const
from visual import *
import wx

def leave(evt):
    exit()

w = window(width=2 * (const.L + window.dwidth), height=const.L + window.dheight
           + window.menuheight + 200, menus=True,
           title='Simulador Gases Ideales - Untref',
           style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

disp = display(
    window=w,
    x=const.d,
    y=const.d + 20,
    width=400,
    height=400,
    forward=-vector(0, 1, 2),
    )

p = w.panel

wx.StaticText(p, pos=(const.d + 150, 10), size=(const.L - 2 * const.d, const.d),
              label='Simulador Gases Ideales - Untref',
              style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

s1 = wx.Slider(p, pos=(0.4 * const.L, 0.95 * 500), size=(400, 20),
               minValue=0, maxValue=const.temperaturaMaxima)
s1.SetBackgroundColour((50, 50, 50))

lblTemperaturaK = wx.StaticText(p, pos=(0.1 * const.L, 0.95 * 500),
                                label='Temperatura (K):', size=(100,
                                40))
lblTemperaturaK.SetForegroundColour((255, 0, 0))

# Modificacion RV

# text(pos= (0,10,10),text='GASES IDEALES',
#   align='center',height = 0.5, depth= 0.8, color=color.green)

LblDatos = wx.StaticText(p, pos=(520, 40), label='DATOS:', size=(40,
                         15))
LblDatos.SetForegroundColour((0, 0, 0))

LblPresion = wx.StaticText(p, pos=(450, 80), label='PRESION:', size=(50,
                           15))
LblPresion.SetBackgroundColour((255, 255, 0))
valorPresion = wx.StaticText(p, pos=(570, 80), size=(100, 15))
valorPresion.SetForegroundColour((255, 0, 0))

cantidadParticulas = wx.StaticText(p, pos=(450, 120),
                                   label='PARTICULAS:', size=(70, 15))
cantidadParticulas.SetBackgroundColour((255, 255, 0))
valorParticulas = wx.StaticText(p, pos=(570, 120), label='25',
                                size=(100, 15))
valorParticulas.SetForegroundColour((255, 0, 0))

LblTemperaturaC = wx.StaticText(p, pos=(450, 160),
                                label='TEMPERATURA C:', size=(100, 15))
LblTemperaturaC.SetBackgroundColour((255, 255, 0))
valorTemperaturaC = wx.StaticText(p, pos=(570, 160), size=(200, 15))
valorTemperaturaC.SetForegroundColour((255, 0, 0))

LblVolumen = wx.StaticText(p, pos=(450, 200), label='VOLUMEN:',
                           size=(60, 15))
LblVolumen.SetBackgroundColour((255, 255, 0))
valorVolumen = wx.StaticText(p, pos=(570, 200), label='1 L', size=(200,
                             15))
valorVolumen.SetForegroundColour((255, 0, 0))

LblMoles = wx.StaticText(p, pos=(450, 240), label='MOLES:', size=(40,
                         15))
LblMoles.SetBackgroundColour((255, 255, 0))
valorMoles = wx.StaticText(p, pos=(570, 240), label='10 M', size=(200,
                           15))
valorMoles.SetForegroundColour((255, 0, 0))

paredDer = box(pos=(const.centroPared, 0, 0), size=(0.2, const.tamanio, const.tamanio),
               color=color.green, opacity=const.opacidad)
paredIzq = box(pos=(-const.centroPared, 0, 0), size=(0.2, const.tamanio, const.tamanio),
               color=color.green, opacity=const.opacidad)

paredSup = box(pos=(0, const.centroPared, 0), size=(const.tamanio, 0.2, const.tamanio),
               color=color.green, opacity=const.opacidad)
paredInf = box(pos=(0, -const.centroPared, 0), size=(const.tamanio, 0.2, const.tamanio),
               color=color.green, opacity=const.opacidad)

paredTrasera = box(pos=(0, 0, -const.centroPared), size=(const.tamanio, const.tamanio,
                   0.2), color=color.green, opacity=const.opacidad)
paredFrontal = box(pos=(0, 0, const.centroPared), size=(const.tamanio, const.tamanio,
                   0.2), color=color.green, opacity=const.opacidad)