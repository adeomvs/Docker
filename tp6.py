from csv import csv


class tp_csv(object):

    def __init__(self, fcsv):
        self.fcsv = fcsv

    def read_csv(self):
        lecsv = csv.reader(open("self.fcsv"), delimiter=";")
        for ligne in lecsv:
            print(ligne)
