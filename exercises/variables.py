exercises = [
    {
        "id": "var_1",
        "title": "Déclarer et afficher une variable",
        "definition": "En Python, on déclare une variable en lui affectant une valeur par simple assignation (ex: x = 5).",
        "example": "x = 3\nprint(x)",
        "example_output": "3",
        "instruction": "Crée une variable 'age' valant 25, puis affiche-la.",
        "expected_output": "25",
        "level": 1,
        "theme": "variables"
    },
    {
        "id": "var_2",
        "title": "Types de base (int, float, str, bool)",
        "definition": "Les types fondamentaux sont int, float, str et bool. On peut vérifier un type avec type().",
        "example": "x = 3.14\nprint(type(x))",
        "example_output": "<class 'float'>",
        "instruction": "Crée une variable 'nom' valant 'Alice' (str) et une variable 'score' valant 99 (int). Affiche-les sur deux lignes.",
        "expected_output": "Alice\n99",
        "level": 1,
        "theme": "variables"
    },
    {
        "id": "var_3",
        "title": "Conversion de types",
        "definition": "On peut convertir un type avec int(), float(), str(), etc. pour changer la représentation.",
        "example": "x = '42'\nx_int = int(x)\nprint(x_int + 1)",
        "example_output": "43",
        "instruction": "Crée une variable texte '10', convertis-la en entier et affiche le double de cette valeur (20).",
        "expected_output": "20",
        "level": 2,
        "theme": "variables"
    },
    {
        "id": "var_4",
        "title": "Opérations sur deux variables",
        "definition": "On peut additionner, multiplier, etc. des variables entières ou flottantes.",
        "example": "a = 10\nb = 3\nsomme = a + b\nprint(somme)",
        "example_output": "13",
        "instruction": "Déclare a=10, b=3. Affiche successivement leur somme, leur différence et leur produit.",
        "expected_output": "13\n7\n30",
        "level": 1,
        "theme": "variables"
    },
    {
        "id": "var_5",
        "title": "Incrémenter une variable",
        "definition": "Incrémenter signifie augmenter la valeur d'une variable, ex: x += 1.",
        "example": "x = 5\nx += 1\nprint(x)",
        "example_output": "6",
        "instruction": "Déclare x=10 puis incrémente-le 2 fois de 1. Affiche le résultat final (12).",
        "expected_output": "12",
        "level": 1,
        "theme": "variables"
    },
    {
        "id": "var_6",
        "title": "Échanger deux variables (swap)",
        "definition": "Pour échanger a et b, on peut faire: a, b = b, a.",
        "example": "a, b = 1, 2\na, b = b, a\nprint(a, b)",
        "example_output": "2 1",
        "instruction": "Déclare a=100, b=200. Échange leurs valeurs et affiche a et b.",
        "expected_output": "200 100",
        "level": 2,
        "theme": "variables"
    },
    {
        "id": "var_7",
        "title": "Saisie utilisateur",
        "definition": "input() permet de récupérer une chaîne. On peut ensuite la convertir si besoin.",
        "example": "nom = input()\nprint('Salut', nom)",
        "example_output": "Salut Bob",
        "instruction": "Demande à l'utilisateur son prénom et stocke-le dans une variable. Affiche ensuite 'Bonjour' suivi de ce prénom.",
        "expected_output": "",  
        "level": 2,
        "theme": "variables"
    },
    {
        "id": "var_8",
        "title": "Assignation multiple",
        "definition": "On peut déclarer plusieurs variables sur une même ligne: x, y = 1, 2.",
        "example": "a, b = 10, 20\nprint(a, b)",
        "example_output": "10 20",
        "instruction": "En une seule ligne, déclare x=3, y=5, puis affiche-les séparés par un espace.",
        "expected_output": "3 5",
        "level": 3,
        "theme": "variables"
    }
]
