####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Exercice 1 - Interface graphique
###  Nom:Gabriel Charbonneau
###  No étudiant: 2037703
###  No Groupe: 00001
###  Description du fichier: Classe Cours
####################################################################################



class Cours:
    """
    Classe cours
    """

    def __init__(self, p_sigle_cours = "A0000", p_titre_cours = "", p_nombre_heures_cours = 0):

        """
        Méthode constructeur
        Définition des attributs de la classe Cours
        """

        self.__sigle_cours = p_sigle_cours
        self.__titre_cours = p_titre_cours
        self.__nombre_heures_cours = p_nombre_heures_cours


    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    # Propriété sigle_cours
    def _get_sigle_cours(self):
        """
           Accesseur de l'attribut privé  __sigle_cours
        """
        return self.__sigle_cours
    def _set_sigle_cours(self,p_sigle_cours):
        """
        Mutateur de l'attribur privé __sigle_cours
        """
        if p_sigle_cours[0].isalpha() and p_sigle_cours[1:].isnumeric():
            self.__sigle_cours = p_sigle_cours

    Sigle_cours = property(_get_sigle_cours,_set_sigle_cours)


    # Propriété titre_cours
    def _get_titre_cours(self)->str:
        """
           Accesseur de l'attribut privé  __titre_cours
        """
        return self.__titre_cours
    def _set_titre_cours(self,p_titre_cours):
        """
        Mutateur de l'attribur privé __titre_cours
        """
        if p_titre_cours <= 60:
            self.__titre_cours = p_titre_cours

    Titre_cours = property(_get_titre_cours, _set_titre_cours)

    
    #Propriété nombre_heures_cours

    def _get_nombre_heures_cours(self)->int:
        """
        Accesseur de l'attribut privé __nombre_heures_cours
        """

        return self.__nombre_heures_cours

    def _set_nombre_heures_cours(self,p_nombre_heures_cours):
        """
        Mutateur de l'attribut privé __titre_cours
        """

        if p_nombre_heures_cours >= 0:
            self.__nombre_heures_cours = p_nombre_heures_cours

    Nombre_heures_cours = property(_get_nombre_heures_cours, _set_nombre_heures_cours)



