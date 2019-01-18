from tp1 import Rectangle

class Rectangle3D(Rectangle):
  def __init__(self, longueur, largeur, hauteur):
    #Rectangle.__init__(self,longueur,largeur)
    super(Rectangle3D, self).__init__(largeur, longueur)
    self.hauteur = hauteur
  def aire3D(self):
    return 2 * ((self.longueur * self.largeur) + (self.longueur * self.hauteur) + (self.largeur * self.hauteur))
  def volume(self):
    return self.aire() * self.hauteur

tp = Rectangle3D(2,3,4)
print(tp.aire3D())
print(tp.volume())
print(tp.aire())
print(tp.perimetre())
