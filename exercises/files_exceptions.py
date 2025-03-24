exercises = [
    {
        "id": "fe_1",
        "title": "Écrire dans un fichier texte",
        "definition": "On ouvre un fichier avec open(nom, 'w') pour écrire. On doit le fermer ou utiliser with.",
        "example": "with open('test.txt', 'w') as f:\n    f.write('Hello')",
        "example_output": "",
        "instruction": "Écris la phrase 'Coucou' dans un fichier 'demo.txt'.",
        "expected_output": "",
        "level": 1,
        "theme": "files_exceptions"
    },
    {
        "id": "fe_2",
        "title": "Lire un fichier texte",
        "definition": "open(nom, 'r') ou juste open(nom) par défaut, puis f.read() pour lire tout le contenu.",
        "example": "with open('test.txt', 'r') as f:\n    contenu = f.read()\nprint(contenu)",
        "example_output": "Hello",
        "instruction": "Lis le fichier 'demo.txt' et affiche son contenu.",
        "expected_output": "Coucou",
        "level": 1,
        "theme": "files_exceptions"
    },
    {
        "id": "fe_3",
        "title": "Lire un fichier ligne par ligne",
        "definition": "On peut faire for line in f: pour itérer sur chaque ligne.",
        "example": "with open('test.txt') as f:\n    for line in f:\n        print(line.strip())",
        "example_output": "ligne1\nligne2",
        "instruction": "Crée un fichier 'lignes.txt' avec 2 lignes. Lis-les et affiche-les sans retour à la ligne supplémentaire.",
        "expected_output": "",
        "level": 2,
        "theme": "files_exceptions"
    },
    {
        "id": "fe_4",
        "title": "Ajouter du contenu à la fin d'un fichier (append)",
        "definition": "On ouvre avec open(nom, 'a') pour rajouter sans effacer l'existant.",
        "example": "with open('test.txt', 'a') as f:\n    f.write('\\nNouvelle ligne')",
        "example_output": "",
        "instruction": "Ouvre 'demo.txt' en mode append et ajoute '\\nHello' à la fin. Vérifie en relisant le fichier.",
        "expected_output": "",
        "level": 2,
        "theme": "files_exceptions"
    },
    {
        "id": "fe_5",
        "title": "try/except pour gérer un fichier inexistant",
        "definition": "On peut intercepter FileNotFoundError si on tente d'ouvrir un fichier qui n’existe pas.",
        "example": "try:\n    with open('inconnu.txt') as f:\n        print(f.read())\nexcept FileNotFoundError:\n    print('Fichier introuvable')",
        "example_output": "Fichier introuvable",
        "instruction": "Tente d'ouvrir 'pas_la.txt'. S’il n’existe pas, affiche 'Introuvable'.",
        "expected_output": "Introuvable",
        "level": 2,
        "theme": "files_exceptions"
    },
    {
        "id": "fe_6",
        "title": "Lever une exception personnalisée",
        "definition": "raise Exception('message') permet de lever une exception.",
        "example": "def check_age(age):\n    if age < 0:\n        raise ValueError('Age négatif impossible')\ncheck_age(-1)",
        "example_output": "ValueError: Age négatif impossible",
        "instruction": "Définis une fonction check_positive(n). Si n<0, lève ValueError('Nombre négatif interdit'). Teste avec n=-5.",
        "expected_output": "",
        "level": 3,
        "theme": "files_exceptions"
    },
    {
        "id": "fe_7",
        "title": "Multiple exceptions",
        "definition": "On peut intercepter plusieurs types d’exceptions dans plusieurs except.",
        "example": "try:\n    x = int('abc')\nexcept ValueError:\n    print('Valeur non convertible')\nexcept TypeError:\n    print('Type invalide')",
        "example_output": "Valeur non convertible",
        "instruction": "Fais un try où tu convertis 'abc' en entier. Si ValueError => affiche 'Conversion impossible', si autre => 'Erreur inconnue'.",
        "expected_output": "Conversion impossible",
        "level": 3,
        "theme": "files_exceptions"
    },
    {
        "id": "fe_8",
        "title": "finally",
        "definition": "Le bloc finally s’exécute toujours, qu’il y ait exception ou non.",
        "example": "try:\n    x = 10/0\nexcept ZeroDivisionError:\n    print('Division par zéro')\nfinally:\n    print('Fin du calcul')",
        "example_output": "Division par zéro\nFin du calcul",
        "instruction": "Fais un try avec 10/0, gère ZeroDivisionError et affiche 'Impossible'. Dans finally, affiche 'Terminé'.",
        "expected_output": "Impossible\nTerminé",
        "level": 3,
        "theme": "files_exceptions"
    }
]
