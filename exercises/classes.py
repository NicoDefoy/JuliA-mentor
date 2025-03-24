exercises = [
    {
        "id": "class_1",
        "title": "Créer une classe simple",
        "definition": "Une classe se définit avec class NomDeClasse:. Le constructeur est __init__(self).",
        "example": "class Person:\n    def __init__(self, name):\n        self.name = name\n\np = Person('Alice')\nprint(p.name)",
        "example_output": "Alice",
        "instruction": "Crée une classe 'Animal' avec un attribut 'species'. Instancie-la avec 'Dog' et affiche species.",
        "expected_output": "Dog",
        "level": 1,
        "theme": "classes"
    },
    {
        "id": "class_2",
        "title": "Ajouter une méthode à la classe",
        "definition": "Les méthodes sont des fonctions définies dans la classe (def nom_méthode(self): ...).",
        "example": "class Person:\n    def __init__(self, name):\n        self.name = name\n    def say_hello(self):\n        print('Hello, je suis', self.name)\n\np = Person('Alice')\np.say_hello()",
        "example_output": "Hello, je suis Alice",
        "instruction": "Dans la classe Animal, ajoute une méthode speak() qui affiche 'Je suis un' + species. Instancie Animal('Chat') et appelle speak().",
        "expected_output": "Je suis un Chat",
        "level": 1,
        "theme": "classes"
    },
    {
        "id": "class_3",
        "title": "Héritage simple",
        "definition": "Une classe peut hériter d'une autre : class Dog(Animal): ...",
        "example": "class Animal:\n    def __init__(self, species):\n        self.species = species\n\nclass Dog(Animal):\n    def bark(self):\n        print('Woof!')\n\nd = Dog('Chien')\nprint(d.species)\nd.bark()",
        "example_output": "Chien\nWoof!",
        "instruction": "Crée une classe Bird(Animal) qui a une méthode fly() affichant 'Je vole'. Instancie Bird('Aigle'), appelle fly().",
        "expected_output": "Je vole",
        "level": 2,
        "theme": "classes"
    },
    {
        "id": "class_4",
        "title": "Attributs de classe vs attributs d'instance",
        "definition": "Un attribut de classe est partagé par toutes les instances, ex: class Person: population = 0",
        "example": "class Person:\n    population = 0\n    def __init__(self, name):\n        self.name = name\n        Person.population += 1\np1 = Person('Alice')\np2 = Person('Bob')\nprint(Person.population)",
        "example_output": "2",
        "instruction": "Crée une classe Compteur avec un attribut de classe nb_instances=0. Incrémente-le dans __init__ et affiche sa valeur après 3 instanciations.",
        "expected_output": "3",
        "level": 2,
        "theme": "classes"
    },
    {
        "id": "class_5",
        "title": "__str__ pour l'affichage",
        "definition": "La méthode __str__ définit comment l'objet se représente en string.",
        "example": "class Person:\n    def __init__(self, name):\n        self.name = name\n    def __str__(self):\n        return f'Person({self.name})'\np = Person('Alice')\nprint(p)",
        "example_output": "Person(Alice)",
        "instruction": "Dans la classe Animal, implémente __str__ pour qu'un Animal('Chat') s'affiche comme 'Animal: Chat'.",
        "expected_output": "Animal: Chat",
        "level": 2,
        "theme": "classes"
    },
    {
        "id": "class_6",
        "title": "Propriété (property)",
        "definition": "On peut créer des getters/setters en Python via @property et @nom_setter.",
        "example": "class Person:\n    def __init__(self, name):\n        self._name = name\n    @property\n    def name(self):\n        return self._name\n    @name.setter\n    def name(self, new_name):\n        self._name = new_name\np = Person('Bob')\np.name = 'Alice'\nprint(p.name)",
        "example_output": "Alice",
        "instruction": "Crée une classe Temperature avec un attribut _celsius. Ajoute une property celsius pour le lire et l'écrire. Teste avec t=Temperature(20), puis t.celsius=25.",
        "expected_output": "", 
        "level": 3,
        "theme": "classes"
    },
    {
        "id": "class_7",
        "title": "Méthode de classe (classmethod)",
        "definition": "Une méthode de classe reçoit la classe en 1er argument (cls). On la décore avec @classmethod.",
        "example": "class Person:\n    population = 0\n    def __init__(self, name):\n        self.name = name\n        Person.population += 1\n    @classmethod\n    def get_population(cls):\n        return cls.population",
        "example_output": "",
        "instruction": "Dans la classe Compteur, ajoute une méthode de classe get_count() qui renvoie la variable de classe. Teste après plusieurs instanciations.",
        "expected_output": "", 
        "level": 3,
        "theme": "classes"
    },
    {
        "id": "class_8",
        "title": "Surcharge d'opérateurs",
        "definition": "On peut définir __add__, __eq__, etc. pour que les objets réagissent aux opérateurs +, ==, etc.",
        "example": "class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n\nv1 = Vector(1,2)\nv2 = Vector(3,4)\nv3 = v1 + v2\nprint(v3.x, v3.y)",
        "example_output": "4 6",
        "instruction": "Crée une classe Point(x,y). Implémente __add__ pour additionner les coords. Teste avec Point(1,1)+Point(2,3) => (3,4).",
        "expected_output": "3 4",
        "level": 3,
        "theme": "classes"
    }
]
