from peewee import *

db = MySQLDatabase('herboriste', user='corentinB', password='E8af035aab', host="127.0.0.1")


class BaseModel(Model):
    """Base Model for current database"""

    class Meta:
        database = db


class Sub_class(BaseModel):
    name = CharField(max_length=50)
    name_fr = CharField(max_length=50)


class Familly(BaseModel):
    name = CharField(max_length=50)
    name_fr = CharField(max_length=50)
    sub_class = ForeignKeyField(Sub_class, backref='sous_classes')


class Plantes(BaseModel):
    name = CharField()
    indication = CharField(max_length=50)
    use_part = CharField(max_length=50)
    price = DecimalField(max_digits=10, decimal_places=2)
    familly = ForeignKeyField(Familly, backref='familles')

    def __str__(self):
        return self.name
