class Rectangle(object):
  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur
  def aire(self):
    return self.longueur * self.largeur
  def perimetre(self):
    return 2 * (self.longueur + self.largeur)
