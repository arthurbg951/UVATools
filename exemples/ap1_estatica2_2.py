from uvatool import (
    Node,
    Apoio,
    NodalForce,
    Rectangle,
    Element,
    Structure,
    Process,
    Print,
)

n1 = Node(0, 0)
n2 = Node(8, 0)
n3 = Node(4, 3)

n1.setSupport(Apoio.segundo_genero)
n2.setSupport(Apoio.primeiro_genero)
n3.setNodalForce(NodalForce(1000, 0, 0))

rec = Rectangle(0.012, 0.001)
area = rec.area
inercia = rec.inertia
young = 100_000

e1 = Element(n1, n2, area, inercia, young)
e2 = Element(n2, n3, area, inercia, young)
e3 = Element(n1, n3, area, inercia, young)

nodes = [n1, n2, n3]
elements = [e1, e2, e3]

structure = Structure("AP1 ESTÁTICA II - 2ª QUESTÃO", nodes, elements)

if __name__ == "__main__":
    calc = Process(nodes, elements)
    deslocamentos = calc.getNodalDisplacement()

    plot = Print(calc)
    plot.internalForces()
