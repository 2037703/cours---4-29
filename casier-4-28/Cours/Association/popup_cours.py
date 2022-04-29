# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la classe casier
from cours import *

# Importer la boite de dialogue

import interfacecours

# Import ls_Etudiants

from logique import ls_Etudiants


# Importer le main

from main import *
#Fonctions cacher labels erreur

#Instanciation de la liste cours

ls_cours = []




#instanciation de cours

Prog1 = Cours("A1111", "Prog", 20)
Res1 = Cours("A2222", "Réseaux", 10)
Out1 = Cours("A3333", "Outils", 15)

ls_cours.append(Prog1)

ls_cours.append(Res1)

ls_cours.append(Out1)


def cacher_labels_erreur(objet):
    objet.label_cours_erreur_numero.setVisible(False)


######################################################
###### DÉFINITIONS DE LA CLASSE popup_casier ######
######################################################

class PopUpCours(QtWidgets.QDialog, interfacecours.Ui_popup_cours):
    def __init__(self, parent=None):
        super(PopUpCours, self).__init__(parent)
        self.setupUi(self)
        cacher_labels_erreur(self)
        for c in ls_cours:
            self.comboBox_cours.addItem(c.Titre_cours)



    @pyqtSlot()
    def on_pushButton_cours_ajouter_clicked(self):
        """
        Méthode du button ajouter cours
        """

        # Instanciation d'un étudiants
        etud2 = Etudiant()

        #Entrée de données
        titre_cours = self.comboBox_cours.currentText()

        etud2.NumEtud = self.lineEdit.text()

        trouve = False
        for e in ls_Etudiants:
            if etud2.NumEtud == e.NumEtud:
                trouve = True
                for c in ls_cours:

                    if titre_cours == c.Titre_cours:
                        () = c


        if trouve is False:

            self.lineEdit.clear()



