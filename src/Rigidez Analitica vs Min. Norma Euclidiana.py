from lib.UVATool import *

n1 = Node(0, 0)
n2 = Node(2, 0)
n3 = Node(6, 0)
n4 = Node(8, 0)

n1.setSupport(Apoio.terceiro_genero)
n4.setSupport(Apoio.terceiro_genero)

n2.setNodalForce(NodalForce(0, -10, 0))
n3.setNodalForce(NodalForce(0, -10, 0))

rec = Rectangle(0.012, 0.001)
area = rec.area()
inercia = rec.momentInertia()

e1 = Element(n1, n2, area, inercia, 1)
e12 = Element(n2, n3, area, inercia, 1)
e2 = Element(n3, n4, area, inercia, 1)

nodes = [n1, n2, n3, n4]
elements = [e1, e12, e2]

print("ANALISE ELASTICA VIA RIGIDEZ ANALITICA")
proc = Process(nodes, elements, Analise.elastica_via_rigidez_analitica)
plot = Print(proc)
plot.internalForces()

print("ANALISE RIGIDO PLASTICA VIA MINIMA NORMA EUCLIDIANA")
proc = Process(nodes, elements, Analise.rigido_plastica_via_minima_norma_euclidiana)
plot = Print(proc)
plot.internalForces()
