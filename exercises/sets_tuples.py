exercises = [
    {
        "id": "st_1",
        "title": "Créer et afficher un set",
        "definition": "Un set est un ensemble de valeurs uniques, défini par {val1, val2}.",
        "example": "fruits = {'pomme', 'banane', 'pomme'}\nprint(fruits)",
        "example_output": "{'banane', 'pomme'}",
        "instruction": "Crée un set contenant 'a', 'b', 'a', puis affiche-le (il ne doit contenir que 'a' et 'b').",
        "expected_output": "{'a', 'b'}",
        "level": 1,
        "theme": "sets_tuples"
    },
    {
        "id": "st_2",
        "title": "Opérations ensemblistes (union, intersection)",
        "definition": "Les sets supportent | pour l’union, & pour l’intersection.",
        "example": "s1 = {1, 2}\ns2 = {2, 3}\nprint(s1 | s2)\nprint(s1 & s2)",
        "example_output": "{1, 2, 3}\n{2}",
        "instruction": "Crée s1={1,2,3}, s2={2,3,4}. Affiche l’union et l’intersection.",
        "expected_output": "{1, 2, 3, 4}\n{2, 3}",
        "level": 2,
        "theme": "sets_tuples"
    },
    {
        "id": "st_3",
        "title": "Ajouter et retirer des éléments d'un set",
        "definition": "On peut faire s.add(val) pour ajouter, s.remove(val) pour retirer.",
        "example": "nombres = {1,2,3}\nnombres.add(4)\nnombres.remove(2)\nprint(nombres)",
        "example_output": "{1, 3, 4}",
        "instruction": "Crée un set {10,20}, ajoute 30, puis retire 20. Affiche le résultat.",
        "expected_output": "{10, 30}",
        "level": 1,
        "theme": "sets_tuples"
    },
    {
        "id": "st_4",
        "title": "Vérifier l’appartenance à un set",
        "definition": "L’opérateur 'in' permet de tester si une valeur est dans un set.",
        "example": "lettres = {'a','b'}\nif 'a' in lettres:\n    print('trouvé')",
        "example_output": "trouvé",
        "instruction": "Crée un set s={'x','y'}. Vérifie si 'z' est dedans. Affiche 'oui' ou 'non'.",
        "expected_output": "non",
        "level": 1,
        "theme": "sets_tuples"
    },
    {
        "id": "st_5",
        "title": "Créer et afficher un tuple",
        "definition": "Un tuple est une liste immutable, définie par (val1, val2).",
        "example": "coords = (10, 20)\nprint(coords[0])",
        "example_output": "10",
        "instruction": "Crée un tuple (1, 2, 3) et affiche son deuxième élément.",
        "expected_output": "2",
        "level": 1,
        "theme": "sets_tuples"
    },
    {
        "id": "st_6",
        "title": "Tuple packing/unpacking",
        "definition": "On peut affecter les valeurs d’un tuple à plusieurs variables : a, b = (1, 2).",
        "example": "point = (3, 4)\nx, y = point\nprint(x)\nprint(y)",
        "example_output": "3\n4",
        "instruction": "Crée un tuple (10,20). Assigne-le à x,y. Affiche x et y sur 2 lignes.",
        "expected_output": "10\n20",
        "level": 1,
        "theme": "sets_tuples"
    },
    {
        "id": "st_7",
        "title": "Immutabilité d’un tuple",
        "definition": "On ne peut pas modifier un tuple en place (tuple[0]=...).",
        "example": "t = (1,2,3)\n# t[0] = 10  => provoque une erreur",
        "example_output": "",
        "instruction": "Crée un tuple t=(5,6). Tente de modifier t[0]. Gère l'erreur dans un try/except et affiche 'impossible'.",
        "expected_output": "impossible",
        "level": 2,
        "theme": "sets_tuples"
    },
    {
        "id": "st_8",
        "title": "Compter et trouver l’index d’une valeur",
        "definition": "Un tuple a des méthodes count(val) et index(val).",
        "example": "t = (2,2,3)\nprint(t.count(2))\nprint(t.index(3))",
        "example_output": "2\n2",
        "instruction": "Crée un tuple (4,4,4,5). Affiche le count de 4 (3), puis l’index de 5 (3).",
        "expected_output": "3\n3",
        "level": 2,
        "theme": "sets_tuples"
    }
]
