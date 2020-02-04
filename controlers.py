from models import *


test = Plantes.select(Plantes.name)
for plante in test:
    print(plante)


def fn_average_price():
    average_price = Plantes.select(Plantes.indication, fn.ROUND(fn.AVG(Plantes.price), 2).alias("ave")).order_by(Plantes.indication).group_by(Plantes.indication)
    for plante in average_price:
        print(plante.indication, plante.ave)

def fn_displayed_familly_identified():
    displayed_familly_identified = Plantes.select(Familly.name, fn.COUNT(Plantes.name).alias("dis")).join(Familly).order_by(Familly.name).group_by(Familly.name)
    for plante in displayed_familly_identified:
        print(plante.familly.name, plante.dis)




fn_average_price()
fn_displayed_familly_identified()