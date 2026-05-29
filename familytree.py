class Person:
  def __init__(self, name):
      self.name = name
      self.children = []
  def add_child(self, child):
      self.children.append(child)

grandparent = Person("Grandparent")
parent1 = Person("Parent1")
parent2 = Person("Parent2")
child1 = Person("Child1")
child2 = Person("Child2")

grandparent.add_child(parent1)
grandparent.add_child(parent2)
parent1.add_child(child1)
parent2.add_child(child2)

def print_family(person, level=0):
    print(" " * level * 2 + person.name)
    for child in person.children:
        print_family(child, level + 1)
print_family(grandparent)
