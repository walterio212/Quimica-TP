from visual import vector

class Particula:
    def __init__(self, vectorVelocidad, sphereView):
        self.velocidadOriginal = vector(vectorVelocidad.x, vectorVelocidad.y, vectorVelocidad.z)
        self.sphereView = sphereView
