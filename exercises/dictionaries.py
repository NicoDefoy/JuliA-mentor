exercises = [
    {
        "id": "dict_1",
        "title": "Créer un dictionnaire",
        "definition": "Un dictionnaire mappe des clés à des valeurs. Exemple : {'nom': 'Alice', 'age': 25}",
        "example": "perso = {'nom': 'Bob', 'score': 42}\nprint(perso)",
        "example_output": "{'nom': 'Bob', 'score': 42}",
        "instruction": "Crée {'pays': 'France', 'capitale': 'Paris'}, puis affiche-le.",
        "expected_output": "{'pays': 'France', 'capitale': 'Paris'}",
        "level": 1,
        "theme": "dictionaries"
    },
    {
        "id": "dict_2",
        "title": "Accéder et modifier une valeur",
        "definition": "On accède à une valeur en utilisant dict['clé']. On peut aussi l'assigner.",
        "example": "perso = {'nom': 'Bob', 'score': 42}\nperso['score'] = 100\nprint(perso['score'])",
        "example_output": "100",
        "instruction": "Crée {'produit': 'Livre', 'prix': 10}. Modifie 'prix' pour qu'il vaille 12, puis affiche la nouvelle valeur de 'prix'.",
        "expected_output": "12",
        "level": 1,
        "theme": "dictionaries"
    },
    {
        "id": "dict_3",
        "title": "Parcourir un dictionnaire",
        "definition": "On peut faire for clé, valeur in dict.items(): pour itérer sur les paires.",
        "example": "infos = {'lang': 'Python', 'version': 3.9}\nfor k, v in infos.items():\n    print(k, v)",
        "example_output": "lang Python\nversion 3.9",
        "instruction": "Crée {'a': 1, 'b': 2}. Parcours-le et affiche chaque paire sous la forme 'clé -> valeur'.",
        "expected_output": "a -> 1\nb -> 2",
        "level": 2,
        "theme": "dictionaries"
    },
    {
        "id": "dict_4",
        "title": "Ajouter et supprimer des clés",
        "definition": "On peut ajouter une clé dict['nouvelle_cle'] = val, et supprimer avec del dict['clé'].",
        "example": "d = {'x': 10}\nd['y'] = 20\ndel d['x']\nprint(d)",
        "example_output": "{'y': 20}",
        "instruction": "Crée un dict vide {}. Ajoute la clé 'nom'='Alice' puis supprime-la. Affiche le dict final (vide).",
        "expected_output": "{}",
        "level": 1,
        "theme": "dictionaries"
    },
    {
        "id": "dict_5",
        "title": "Vérifier la présence d'une clé",
        "definition": "L'opérateur 'in' vérifie la présence d'une clé dans un dictionnaire (ex: 'nom' in d).",
        "example": "d = {'age': 25}\nif 'age' in d:\n    print('Clé présente')",
        "example_output": "Clé présente",
        "instruction": "Crée {'ville': 'Paris'}. Vérifie si la clé 'pays' existe. Affiche 'existe' ou 'existe pas'.",
        "expected_output": "existe pas",
        "level": 2,
        "theme": "dictionaries"
    },
    {
        "id": "dict_6",
        "title": "Méthodes get() et keys()",
        "definition": "dict.get('clé', valeur_par_défaut) évite l'erreur si la clé n'existe pas; dict.keys() renvoie la liste des clés.",
        "example": "d = {'lang': 'Python'}\nprint(d.get('lang', 'rien'))\nprint(d.get('version', 0))",
        "example_output": "Python\n0",
        "instruction": "Crée d={'x':10}. Affiche d.get('x', 0) puis d.get('y', 0). Enfin, affiche la liste des clés.",
        "expected_output": "10\n0\ndict_keys(['x'])",
        "level": 2,
        "theme": "dictionaries"
    },
    {
        "id": "dict_7",
        "title": "Fusion de deux dictionnaires",
        "definition": "En Python 3.9+, on peut fusionner deux dicts avec l'opérateur | (ou update()).",
        "example": "d1 = {'a': 1}\nd2 = {'b': 2}\nmerged = d1 | d2\nprint(merged)",
        "example_output": "{'a': 1, 'b': 2}",
        "instruction": "Crée d1={'nom':'Bob'}, d2={'age':30}. Fusionne-les en d3 et affiche d3.",
        "expected_output": "{'nom': 'Bob', 'age': 30}",
        "level": 3,
        "theme": "dictionaries"
    },
    {
        "id": "dict_8",
        "title": "Dictionnaire de listes",
        "definition": "Les valeurs d'un dictionnaire peuvent être de tout type, y compris des listes.",
        "example": "notes = {'Alice': [12, 15], 'Bob': [10, 9]}\nprint(notes)",
        "example_output": "{'Alice': [12, 15], 'Bob': [10, 9]}",
        "instruction": "Crée un dict {'fruits': ['pomme','poire'], 'legumes': ['tomate','carotte']}. Affiche uniquement la liste de 'legumes'.",
        "expected_output": "['tomate', 'carotte']",
        "level": 3,
        "theme": "dictionaries"
    }
]
