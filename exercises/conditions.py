exercises = [
    {
        "id": "cond_1",
        "title": "Vérifier si un nombre est positif",
        "definition": "Les conditions if/else permettent d'exécuter du code en fonction d'un test logique.",
        "example": "x = 5\nif x > 0:\n    print('x est positif')\nelse:\n    print('x est négatif ou nul')",
        "example_output": "x est positif",
        "instruction": "Écris un code qui vérifie si la variable x est positive. Affiche 'positif' ou 'négatif ou nul'.",
        "expected_output": "positif",
        "level": 1,
        "theme": "conditions"
    },
    {
        "id": "cond_2",
        "title": "Pair ou impair",
        "definition": "Pour savoir si un nombre est pair, on vérifie si son reste modulo 2 vaut 0.",
        "example": "n = 4\nif n % 2 == 0:\n    print('pair')\nelse:\n    print('impair')",
        "example_output": "pair",
        "instruction": "Écris un code qui teste la variable n. Affiche 'pair' ou 'impair' selon le cas.",
        "expected_output": "pair",
        "level": 1,
        "theme": "conditions"
    },
    {
        "id": "cond_3",
        "title": "Signe d'un nombre (positif, négatif, nul)",
        "definition": "On peut utiliser if/elif/else pour distinguer plusieurs cas.",
        "example": "x = 0\nif x > 0:\n    print('positif')\nelif x < 0:\n    print('négatif')\nelse:\n    print('nul')",
        "example_output": "nul",
        "instruction": "Déclare une variable x= -5. Affiche 'positif' si x>0, 'négatif' si x<0, sinon 'nul'.",
        "expected_output": "négatif",
        "level": 1,
        "theme": "conditions"
    },
    {
        "id": "cond_4",
        "title": "Trier deux nombres",
        "definition": "On peut comparer deux valeurs et les afficher dans l'ordre croissant.",
        "example": "a, b = 7, 3\nif a < b:\n    print(a, b)\nelse:\n    print(b, a)",
        "example_output": "3 7",
        "instruction": "Déclare a=10 et b=4. Affiche d'abord la plus petite valeur, puis la plus grande.",
        "expected_output": "4 10",
        "level": 1,
        "theme": "conditions"
    },
    {
        "id": "cond_5",
        "title": "Trouver le maximum de trois nombres",
        "definition": "On peut imbriquer les conditions ou utiliser max() pour comparer trois valeurs.",
        "example": "x, y, z = 2, 5, 3\nif x >= y and x >= z:\n    print(x)\nelif y >= x and y >= z:\n    print(y)\nelse:\n    print(z)",
        "example_output": "5",
        "instruction": "Déclare x=7, y=1, z=7. Affiche le maximum des trois.",
        "expected_output": "7",
        "level": 2,
        "theme": "conditions"
    },
    {
        "id": "cond_6",
        "title": "Deviner un nombre",
        "definition": "Utilise if/elif/else pour indiquer si la proposition est trop grande, trop petite ou correcte.",
        "example": "secret = 7\nguess = 5\nif guess < secret:\n    print('Trop petit')\nelif guess > secret:\n    print('Trop grand')\nelse:\n    print('Bravo')",
        "example_output": "Trop petit",
        "instruction": "Déclare secret=3 et guess=5. Dis si guess est trop petit, trop grand ou correct.",
        "expected_output": "Trop grand",
        "level": 2,
        "theme": "conditions"
    },
    {
        "id": "cond_7",
        "title": "Voyelle ou consonne",
        "definition": "On peut tester si une lettre est dans un ensemble ('a', 'e', 'i', 'o', 'u', 'y').",
        "example": "lettre = 'e'\nif lettre in ['a','e','i','o','u','y']:\n    print('voyelle')\nelse:\n    print('consonne')",
        "example_output": "voyelle",
        "instruction": "Déclare lettre='x'. Affiche 'voyelle' si c'est dans [a,e,i,o,u,y], sinon 'consonne'.",
        "expected_output": "consonne",
        "level": 2,
        "theme": "conditions"
    },
    {
        "id": "cond_8",
        "title": "Système de notation (grading)",
        "definition": "On peut affecter un message en fonction d'un score sur 100 (ex: >=80 = Excellent).",
        "example": "score = 75\nif score >= 80:\n    print('Excellent')\nelif score >= 60:\n    print('Assez bien')\nelse:\n    print('Peut mieux faire')",
        "example_output": "Assez bien",
        "instruction": "Déclare score=85. Affiche 'Excellent' si >=80, 'Assez bien' si >=60, sinon 'Peut mieux faire'.",
        "expected_output": "Excellent",
        "level": 3,
        "theme": "conditions"
    }
]
