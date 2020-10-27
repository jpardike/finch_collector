from django.db import models

# Create your models here.

class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

finches = [
    Finch('Chuck', 'Brambling', 'black head in summer, and an orange breast with white belly', 2),
    Finch('Stubbs', 'Greenfinch', 'wheezing song', 4),
    Finch('James', 'Scottish crossbill', 'chunky, thick-set finch with a large head and substantial bill', 0)
]