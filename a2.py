class person(object):
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)

class employee(person):
    def __init__(self, name, id, salary, post):
        self.salary=salary
        self.post=post
        person.__init__(self, name, id)

o=employee("RAHUL", 123, 200000, "INTERN")
o.display()
print(o.salary)
print(o.post)

o2=employee("ROHIT", 273, 450000, "MANAGER")
o2.display()
print(o2.salary)
print(o2.post)

