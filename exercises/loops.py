exercises = [
    {
        "id": "loop_1",
        "title": "Boucle simple de 0 à 4",
        "definition": "Une boucle for permet de répéter une instruction pour chaque valeur d'une séquence.",
        "example": "for i in range(5):\n    print(i)",
        "example_output": "0\n1\n2\n3\n4",
        "instruction": "Écris une boucle for qui affiche les nombres de 0 à 4 inclus.",
        "expected_output": "0\n1\n2\n3\n4",
        "level": 1,
        "theme": "boucles"
    },
    {
        "id": "loop_2",
        "title": "Boucle pour afficher les nombres de 2 à 6",
        "definition": "Toujours la même syntaxe, mais on précise la plage de départ et de fin avec range().",
        "example": "for i in range(3, 6):\n    print(i)",
        "example_output": "3\n4\n5",
        "instruction": "Écris une boucle for qui affiche les nombres de 2 à 6 inclus.",
        "expected_output": "2\n3\n4\n5\n6",
        "level": 1,
        "theme": "boucles"
    },
    {
        "id": "loop_3",
        "title": "Carrés des nombres de 0 à 4",
        "definition": "On peut aussi effectuer un calcul dans la boucle avant d'afficher.",
        "example": "for i in range(3):\n    print(i * i)",
        "example_output": "0\n1\n4",
        "instruction": "Écris une boucle for qui affiche les carrés des nombres de 0 à 4 (0, 1, 4, 9, 16).",
        "expected_output": "0\n1\n4\n9\n16",
        "level": 2,
        "theme": "boucles"
    },
    {
        "id": "loop_4",
        "title": "Somme des nombres de 1 à 5",
        "definition": "On peut additionner des valeurs dans une boucle. Initialise un total à 0 et ajoute chaque nombre.",
        "example": "total = 0\nfor i in range(1, 4):\n    total += i\nprint(total)",
        "example_output": "6",
        "instruction": "Calcule la somme des nombres de 1 à 5 inclus et affiche-la (attendu: 15).",
        "expected_output": "15",
        "level": 2,
        "theme": "boucles"
    },
    {
        "id": "loop_5",
        "title": "Boucle while simple (0 à 4)",
        "definition": "La boucle while s'exécute tant qu'une condition est vraie. Attention aux conditions pour éviter les boucles infinies.",
        "example": "i = 0\nwhile i < 3:\n    print(i)\n    i += 1",
        "example_output": "0\n1\n2",
        "instruction": "Écris une boucle while qui affiche les nombres de 0 à 4 inclus.",
        "expected_output": "0\n1\n2\n3\n4",
        "level": 2,
        "theme": "boucles"
    },
    {
        "id": "loop_6",
        "title": "Boucle while avec saisie utilisateur",
        "definition": "On peut demander à l'utilisateur un input() et continuer tant qu'il ne tape pas 'quit'.",
        "example": "command = ''\nwhile command != 'stop':\n    command = input()\n    print('Tu as tapé:', command)",
        "example_output": "Tu as tapé: ...",
        "instruction": "Écris une boucle while qui demande une saisie à l'utilisateur, et s'arrête si la saisie est 'quit'. Affiche chaque saisie avant de redemander.",
        "expected_output": "",  
        "level": 3,
        "theme": "boucles"
    },
    {
        "id": "loop_7",
        "title": "Parcourir une liste de fruits",
        "definition": "Une boucle for peut aussi itérer sur une liste. Par exemple: for elem in ma_liste: print(elem).",
        "example": "fruits = ['pomme', 'banane']\nfor f in fruits:\n    print(f)",
        "example_output": "pomme\nbanane",
        "instruction": "Crée une liste ['pomme', 'poire', 'fraise'] et affiche chaque fruit dans la console, un par ligne.",
        "expected_output": "pomme\npoire\nfraise",
        "level": 2,
        "theme": "boucles"
    },
    {
        "id": "loop_8",
        "title": "Trouver le plus grand nombre dans une liste",
        "definition": "On peut utiliser une variable max pour stocker le plus grand élément trouvé en parcourant la liste.",
        "example": "nums = [10, 5, 8]\nmax_val = nums[0]\nfor n in nums:\n    if n > max_val:\n        max_val = n\nprint(max_val)",
        "example_output": "10",
        "instruction": "Crée une liste [3, 7, 2, 9, 5]. Parcours-la pour trouver la valeur max, puis affiche-la (9).",
        "expected_output": "9",
        "level": 3,
        "theme": "boucles"
    }
]
