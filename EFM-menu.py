def menu():
    print("1.Pour afficher les information de Employe")
    print("2.Pour Afficher les information de Formateur")
    print("3.Pour afficher SalaireAPayer de Formateur")
    choice = int(input("Entrer une number entre 1 - 3 "))
    if choice == 1 :
        print(Employe.__str__())
    if choice == 2 : 
        print(Formateur.__str__())

    if choice == 3 :
        print(Formateur.SalaireAPayer())
"1-Class IR"
class IR:
    _tranches = [0, 28001, 40001, 50001, 60001, 150001]
    _tauxIR = [0, 0.12, 0.24, 0.34, 0.38, 0.40]

    @staticmethod
    def getIR(salaire):
        for i in range(1, 6):
            if salaire < IR._tranches[i]:
                return IR._tauxIR[i - 1]
        return IR._tauxIR[5]
    

"2-Class lEmploye"
from datetime import datetime

class IEmploye:
    def Age(self):
        pass
    
    def Anciennete(self):
        pass
    
    def DateRetraite(self, ageRetraite):
        pass

"3-Class Employe"

from abc import ABC, abstractmethod
from datetime import datetime

class Employe(ABC):
    cpt = 0

    def __init__(self):
        self._mtle = 0
        self._nom = ""
        self._dateNaissance = datetime.now()
        self._dateEmbauche = datetime.now()
        self._salaireBase = 0.0

    @property
    def Matricule(self):
        return self._mtle

    @property
    def Nom(self):
        return self._nom

    @Nom.setter
    def Nom(self, value):
        self._nom = value

    @property
    def DateNaissance(self):
        return self._dateNaissance

    @DateNaissance.setter
    def DateNaissance(self, value):
        self._dateNaissance = value

    @abstractmethod
    def CompareTo(self, other):
        pass

    from datetime import datetime

class Employe:
    cpt = 0

    def __init__(self):
        Employe.cpt += 1
        self._mtle = Employe.cpt
        self._nom = ""
        self._dateEmbauche = datetime.now()
        self._dateNaissance = datetime(2000, 1, 1)
        self._salaireBase = 0

    def __init__(self, nom, dateNaissance, dateEmbauche, salaireBase):
        self._nom = nom
        self._dateNaissance = dateNaissance
        self.DateEmbauche = dateEmbauche
        self._salaireBase = salaireBase
        Employe.cpt += 1
        self._mtle = Employe.cpt

    @property
    def DateEmbauche(self):
        return self._dateEmbauche

    @DateEmbauche.setter
    def DateEmbauche(self, value):
        ts = value - self._dateNaissance
        if (ts.days / 365) < 16:
            raise Exception("L'âge au recrutement doit être supérieur à 16 ans")
        self._dateEmbauche = value

    @property
    def SalaireBase(self):
        return self._salaireBase

    @SalaireBase.setter
    def SalaireBase(self, value):
        self._salaireBase = value


    def CompareTo(self, e):
        return self._nom.CompareTo(e._nom)

    def Age(self):
       ts = datetime.datetime.now() - self._dateNaissance
       return int(ts.total_seconds() / (60 * 60 * 24 * 365))

    def Anciennete(self):
       ts = datetime.datetime.now() - self._dateEmbauche
       return int(ts.total_seconds() / (60 * 60 * 24 * 365))

    def DateRetraite(self, ageRetraite):
       ts = datetime.timedelta(days=ageRetraite*365)
       dateRetraite = datetime.datetime(self._dateNaissance.year, self._dateNaissance.month, self._dateNaissance.day) + ts
       return dateRetraite

    def __str__(self):
      return str(self._mtle) + "-" + str(self._nom) + "-" + self._dateNaissance.strftime("%d/%m/%Y") + "-" + self._dateEmbauche.strftime("%d/%m/%Y") + "-" + str(self._salaireBase)

    def __eq__(self, obj):
       e = obj 
       if e == None:
        return False
       return self._mtle == e._mtle



"4-class Formateur"
class Formateur(Employe):
    
    def __init__(self):
        self._heureSup = 0
        self._remunerationHSup = 70.00
    
    
    @property
    def RemunerationHSup(self):
        return self._remunerationHSup
    
    @RemunerationHSup.setter
    def RemunerationHSup(self, value):
        self._remunerationHSup = value
    
    @property
    def HeureSup(self):
        return self._heureSup
    
    @HeureSup.setter
    def HeureSup(self, value):
        self._heureSup = value
    
    
    def __init__(self, nom, dateNaissance, dateEmbauche, salaireBase, heureSup):
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        self._heureSup = heureSup
    

    def SalaireAPayer(self):
        NbreHS = self._heureSup
        if NbreHS >= 30:
            NbreHS = 30
        return (self._salaireBase + NbreHS*self._remunerationHSup) * (1 - IR.getIR(self._salaireBase*12))
    
    
    def ToString(self):
        return super.ToString() + "-" + str(self._heureSup)
    
"5-Class Agent"
class Agent(Employe):
    def __init__(self, nom, dateNaissance, dateEmbauche, salaireBase, primeResponsabilite):
        super().__init__(nom, dateNaissance, dateEmbauche, salaireBase)
        self._primeResponsabilite = primeResponsabilite
    
    @property
    def PrimeResponsabilite(self):
        return self._primeResponsabilite
    
    @PrimeResponsabilite.setter
    def PrimeResponsabilite(self, value):
        self._primeResponsabilite = value
    
    def SalaireAPayer(self):
        return (self._salaireBase + self._primeResponsabilite) * (1 - IR.getIR(self._salaireBase * 12))


