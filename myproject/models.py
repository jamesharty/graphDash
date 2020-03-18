#MODELS.PY
# set up the db inside the __init__.py
from myproject import db

class Animal(db.Model):

    __tablename__ = 'animals'
    animalID = db.Column(db.Integer,primary_key = True)
    startWeight = db.Column(db.Float)
    w1 = db.Column(db.Float)
    w2 = db.Column(db.Float)
    w3 = db.Column(db.Float)
    w4 = db.Column(db.Float)
    finalWeight = db.Column(db.Float)
    motherID = db.Column(db.Integer)
    fatherID = db.Column(db.Integer)
    diet = db.Column(db.Text)
    ch4_daily_mean = db.Column(db.Float)
    feedEfficiency = db.Column(db.Float)
    waterEfficieny = db.Column(db.Float)

    def __init__(self,animalID,startWeight,w1,w2,w3,w4,finalWeight,
    motherID,fatherID,diet,ch4_daily_mean,feedEfficiency,waterEfficieny):
        self.animalID = animalID
        self.startWeight = startWeight
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = animalID
        self.finalWeight = finalWeight
        self.motherID = motherID
        self.fatherID = fatherID
        self.diet = diet
        self.ch4_daily_mean = ch4_daily_mean
        self.feedEfficiency = feedEfficiency
        self.waterEfficieny = waterEfficieny

    def __repr__(self):
        
        return self
        


