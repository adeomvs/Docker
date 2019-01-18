class Animal(object):
  def __init__(self, poids, cri):
    self.poids = poids
    self.cri = cri
  def get_poids(self):
    return self.poids
  def get_cri(self):
    return self.cri

class Chat(Animal):
  def __init__(self, poids, cri, pattes):
    super(Chat, self).__init__(poids, cri)
    self.pattes = pattes
  def nb_pattes(self):
    return self.pattes

tp = Chat(8, "Miaou", 4)
print(tp.nb_pattes())
print(tp.get_cri())
print(tp.get_poids())
