exercises = [
    {
        "id": "func_1",
        "title": "Définir une fonction sans paramètre",
        "definition": "On définit une fonction en Python avec def nom_de_fonction():.",
        "example": "def hello():\n    print('Hello!')\n\nhello()",
        "example_output": "Hello!",
        "instruction": "Définis une fonction bonjour() qui affiche 'Salut !'. Appelle-la ensuite.",
        "expected_output": "Salut !",
        "level": 1,
        "theme": "functions"
    },
    {
        "id": "func_2",
        "title": "Fonction avec paramètre et retour",
        "definition": "Une fonction peut recevoir des arguments et retourner une valeur avec return.",
        "example": "def carre(x):\n    return x*x\n\nprint(carre(3))",
        "example_output": "9",
        "instruction": "Définis une fonction add(a, b) qui renvoie la somme des deux. Affiche le résultat pour add(5, 7) (12).",
        "expected_output": "12",
        "level": 1,
        "theme": "functions"
    },
    {
        "id": "func_3",
        "title": "Fonction avec boucle",
        "definition": "On peut combiner boucle et fonction, ex: calculer la somme d'une liste.",
        "example": "def sum_list(liste):\n    total = 0\n    for val in liste:\n        total += val\n    return total\n\nprint(sum_list([1,2,3]))",
        "example_output": "6",
        "instruction": "Définis product_list(liste) qui multiplie tous les éléments de la liste. Teste-la sur [2,3,4] (résultat 24).",
        "expected_output": "24",
        "level": 2,
        "theme": "functions"
    },
    {
        "id": "func_4",
        "title": "Paramètre par défaut",
        "definition": "On peut donner une valeur par défaut à un paramètre, ex: def ma_fonction(x=10): ...",
        "example": "def salut(nom='inconnu'):\n    print(f'Bonjour {nom}')\nsalut()\nsalut('Alice')",
        "example_output": "Bonjour inconnu\nBonjour Alice",
        "instruction": "Définis une fonction greet(name='ami') qui affiche 'Salut name'. Appelle-la sans argument, puis avec 'Bob'.",
        "expected_output": "Salut ami\nSalut Bob",
        "level": 2,
        "theme": "functions"
    },
    {
        "id": "func_5",
        "title": "Fonction avec plusieurs retours",
        "definition": "On peut return plusieurs valeurs sous forme de tuple.",
        "example": "def stats(a, b):\n    return (a+b, a*b)\nsomme, produit = stats(3,4)\nprint(somme, produit)",
        "example_output": "7 12",
        "instruction": "Définis get_min_max(liste) qui renvoie (min, max). Teste sur [2,5,1]. Affiche la paire retournée (1,5).",
        "expected_output": "(1, 5)",
        "level": 2,
        "theme": "functions"
    },
    {
        "id": "func_6",
        "title": "Fonction récursive",
        "definition": "Une fonction récursive s'appelle elle-même. Attention à la condition d'arrêt !",
        "example": "def fact(n):\n    if n <= 1:\n        return 1\n    else:\n        return n * fact(n-1)\n\nprint(fact(3))",
        "example_output": "6",
        "instruction": "Définis factorial(n). Teste avec n=4, résultat attendu 24.",
        "expected_output": "24",
        "level": 3,
        "theme": "functions"
    },
    {
        "id": "func_7",
        "title": "Fonction lambda",
        "definition": "Une lambda est une fonction anonyme. ex: carre = lambda x: x*x.",
        "example": "carre = lambda x: x*x\nprint(carre(5))",
        "example_output": "25",
        "instruction": "Déclare une variable double = lambda x: x*2. Affiche double(10) (20).",
        "expected_output": "20",
        "level": 2,
        "theme": "functions"
    },
    {
        "id": "func_8",
        "title": "Docstring",
        "definition": "Les docstrings décrivent la fonction, exemple:\n\"\"\"Cette fonction calcule...\"\"\"",
        "example": "def addition(a, b):\n    \"\"\"Retourne la somme de a et b\"\"\"\n    return a + b\n\nprint(addition(2,3))",
        "example_output": "5",
        "instruction": "Définis une fonction multiply(a, b) avec une docstring décrivant son rôle. Retourne a*b et affiche le résultat pour 4*5 (20).",
        "expected_output": "20",
        "level": 3,
        "theme": "functions"
    }
]
