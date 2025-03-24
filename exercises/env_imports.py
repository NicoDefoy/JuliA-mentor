exercises = [
    {
        "id": "env_1",
        "title": "Importer un module standard",
        "definition": "On peut importer math, random, os... ex: import math",
        "example": "import math\nprint(math.sqrt(16))",
        "example_output": "4.0",
        "instruction": "Fais un import math, puis affiche math.pi",
        "expected_output": "3.141592653589793",
        "level": 1,
        "theme": "env_imports"
    },
    {
        "id": "env_2",
        "title": "Importer seulement une fonction",
        "definition": "from math import sqrt permet d’importer une fonction précise.",
        "example": "from math import factorial\nprint(factorial(5))",
        "example_output": "120",
        "instruction": "Importe seulement sqrt depuis math. Calcule sqrt(25).",
        "expected_output": "5.0",
        "level": 1,
        "theme": "env_imports"
    },
    {
        "id": "env_3",
        "title": "Installer un package externe (theorique)",
        "definition": "On utilise pip install nom_du_package. Depuis la console, pas dans le code.",
        "example": "pip install requests\nimport requests",
        "example_output": "",
        "instruction": "Écris la commande pip pour installer 'requests' en local. (Indice: pip install requests)",
        "expected_output": "",
        "level": 1,
        "theme": "env_imports"
    },
    {
        "id": "env_4",
        "title": "Utiliser un module externe (requests)",
        "definition": "Après installation, on peut import requests et l’utiliser.",
        "example": "import requests\nr = requests.get('https://httpbin.org/get')\nprint(r.status_code)",
        "example_output": "200",
        "instruction": "Fais un import requests, puis fais une requête GET sur 'https://httpbin.org/get'. Affiche r.status_code.",
        "expected_output": "200",
        "level": 2,
        "theme": "env_imports"
    },
    {
        "id": "env_5",
        "title": "Créer un virtualenv (théorique)",
        "definition": "python -m venv env crée un environnement virtuel nommé env. On l’active avec source env/bin/activate (Linux/Mac).",
        "example": "",
        "example_output": "",
        "instruction": "Donne la commande pour créer et activer un virtualenv nommé 'mon_env'.",
        "expected_output": "",
        "level": 2,
        "theme": "env_imports"
    },
    {
        "id": "env_6",
        "title": "Lister les packages installés (théorique)",
        "definition": "pip list montre les packages installés dans l’environnement courant.",
        "example": "pip list",
        "example_output": "",
        "instruction": "Quelle commande pip affiche la liste des packages installés ?",
        "expected_output": "",
        "level": 1,
        "theme": "env_imports"
    },
    {
        "id": "env_7",
        "title": "freeze et requirements.txt (théorique)",
        "definition": "pip freeze > requirements.txt sauvegarde la liste des deps. pip install -r requirements.txt les réinstalle.",
        "example": "",
        "example_output": "",
        "instruction": "Explique comment créer un fichier requirements.txt à partir de l’environnement actuel.",
        "expected_output": "",
        "level": 2,
        "theme": "env_imports"
    },
    {
        "id": "env_8",
        "title": "Créer son propre module local",
        "definition": "On peut créer un fichier monmodule.py et l’importer depuis un autre script (import monmodule).",
        "example": "# monmodule.py\ndef salut():\n    print('Salut')\n\n# main.py\nimport monmodule\nmonmodule.salut()",
        "example_output": "Salut",
        "instruction": "Crée un fichier 'utils.py' avec une fonction bonjour(). Importe-la dans main.py et exécute bonjour().",
        "expected_output": "Salut",
        "level": 3,
        "theme": "env_imports"
    }
]
