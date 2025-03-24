exercises = [
    {
        "id": "str_1",
        "title": "Mettre un texte en majuscules",
        "definition": "Les chaînes possèdent des méthodes comme upper(), lower().",
        "example": "mot = 'python'\nprint(mot.upper())",
        "example_output": "PYTHON",
        "instruction": "Déclare une variable 'texte' = 'bonjour' et affiche-la en majuscules.",
        "expected_output": "BONJOUR",
        "level": 1,
        "theme": "strings"
    },
    {
        "id": "str_2",
        "title": "Slicing d'une chaîne",
        "definition": "Le slicing permet de prendre une portion de string : texte[start:end].",
        "example": "mot = 'python'\nprint(mot[1:4])",
        "example_output": "yth",
        "instruction": "Déclare 'mot' = 'formation'. Affiche uniquement les 4 premières lettres (form).",
        "expected_output": "form",
        "level": 1,
        "theme": "strings"
    },
    {
        "id": "str_3",
        "title": "Vérifier la présence d'une sous-chaîne",
        "definition": "On peut utiliser l'opérateur 'in' pour vérifier si un sous-texte apparaît.",
        "example": "phrase = 'Je code en Python'\nif 'Python' in phrase:\n    print('Oui')\nelse:\n    print('Non')",
        "example_output": "Oui",
        "instruction": "Déclare phrase='Bonjour tout le monde'. Affiche 'Trouvé' si 'jour' est dedans, sinon 'Pas trouvé'.",
        "expected_output": "Trouvé",
        "level": 2,
        "theme": "strings"
    },
    {
        "id": "str_4",
        "title": "Concaténation de chaînes",
        "definition": "On peut concaténer avec l'opérateur + ou f-string.",
        "example": "prenom = 'Alice'\nnom = 'Dupont'\nprint(prenom + ' ' + nom)",
        "example_output": "Alice Dupont",
        "instruction": "Déclare nom='Doe', prenom='John'. Affiche 'John Doe' (concaténation).",
        "expected_output": "John Doe",
        "level": 1,
        "theme": "strings"
    },
    {
        "id": "str_5",
        "title": "Longueur d'une chaîne",
        "definition": "La fonction len() donne la longueur d'une chaîne.",
        "example": "mot = 'Python'\nprint(len(mot))",
        "example_output": "6",
        "instruction": "Déclare texte='Hello World'. Affiche la longueur de ce texte (11 caractères).",
        "expected_output": "11",
        "level": 1,
        "theme": "strings"
    },
    {
        "id": "str_6",
        "title": "Remplacement de sous-chaîne",
        "definition": "La méthode replace(old, new) permet de remplacer une sous-chaîne par une autre.",
        "example": "s = 'Bonjour tout le monde'\ns = s.replace('Bonjour', 'Salut')\nprint(s)",
        "example_output": "Salut tout le monde",
        "instruction": "Déclare s='Hello World'. Remplace 'Hello' par 'Salut' puis affiche la nouvelle chaîne.",
        "expected_output": "Salut World",
        "level": 2,
        "theme": "strings"
    },
    {
        "id": "str_7",
        "title": "Split et join",
        "definition": "split() découpe la chaîne en liste, join() reconstruit une chaîne à partir d'une liste.",
        "example": "s = 'un,deux,trois'\nparts = s.split(',')\nprint(parts)\nrejoin = '-'.join(parts)\nprint(rejoin)",
        "example_output": "['un', 'deux', 'trois']\nun-deux-trois",
        "instruction": "Déclare s='Python est génial'. Sépare la phrase sur les espaces (split), puis réassemble-la avec un tiret '-'.",
        "expected_output": "Python-est-génial",
        "level": 2,
        "theme": "strings"
    },
    {
        "id": "str_8",
        "title": "Formatage avec f-strings",
        "definition": "Les f-strings permettent d'insérer des variables dans une chaîne en écrivant f\"{variable}\".",
        "example": "nom = 'Alice'\nage = 30\nprint(f\"Je m'appelle {nom} et j'ai {age} ans\")",
        "example_output": "Je m'appelle Alice et j'ai 30 ans",
        "instruction": "Déclare nom='Bob', score=42. Affiche : \"Bob a obtenu 42 points\" (utilise une f-string).",
        "expected_output": "Bob a obtenu 42 points",
        "level": 3,
        "theme": "strings"
    }
]
