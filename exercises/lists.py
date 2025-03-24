exercises = [
    {
        "id": "list_1",
        "title": "Créer et afficher une liste",
        "definition": "Une liste se déclare avec des crochets : [val1, val2].",
        "example": "fruits = ['pomme', 'banane']\nprint(fruits)",
        "example_output": "['pomme', 'banane']",
        "instruction": "Crée une liste contenant 3 prénoms et affiche-la.",
        "expected_output": "['Alice', 'Bob', 'Charlie']",
        "level": 1,
        "theme": "lists"
    },
    {
        "id": "list_2",
        "title": "Ajouter un élément à la liste",
        "definition": "On peut utiliser la méthode append() pour ajouter un élément en fin de liste.",
        "example": "nombres = [1, 2, 3]\nnombres.append(4)\nprint(nombres)",
        "example_output": "[1, 2, 3, 4]",
        "instruction": "Crée une liste [10, 20] et ajoute 30 dedans, puis affiche la liste.",
        "expected_output": "[10, 20, 30]",
        "level": 1,
        "theme": "lists"
    },
    {
        "id": "list_3",
        "title": "Calculer la somme des éléments",
        "definition": "On peut itérer sur la liste ou utiliser la fonction sum().",
        "example": "nums = [1, 2, 3]\nprint(sum(nums))",
        "example_output": "6",
        "instruction": "Crée une liste [2, 4, 6] et affiche la somme totale (12).",
        "expected_output": "12",
        "level": 2,
        "theme": "lists"
    },
    {
        "id": "list_4",
        "title": "Accéder à un élément par index",
        "definition": "On peut accéder à un élément via son index : liste[0]. Attention aux index hors de range.",
        "example": "lettres = ['a', 'b', 'c']\nprint(lettres[1])",
        "example_output": "b",
        "instruction": "Crée une liste ['x','y','z']. Affiche le premier élément.",
        "expected_output": "x",
        "level": 1,
        "theme": "lists"
    },
    {
        "id": "list_5",
        "title": "Retirer un élément (remove ou pop)",
        "definition": "remove(val) enlève la première occurrence de val, pop(index) enlève l'élément à l'index donné.",
        "example": "fruits = ['pomme', 'banane', 'pomme']\nfruits.remove('pomme')\nprint(fruits)",
        "example_output": "['banane', 'pomme']",
        "instruction": "Crée une liste [1,2,3,2]. Retire la valeur 2 (la première occurrence) et affiche la liste.",
        "expected_output": "[1, 3, 2]",
        "level": 2,
        "theme": "lists"
    },
    {
        "id": "list_6",
        "title": "Compter les occurrences d'une valeur",
        "definition": "La méthode count(val) retourne le nombre de fois où val apparaît.",
        "example": "nums = [2,2,3]\nprint(nums.count(2))",
        "example_output": "2",
        "instruction": "Crée une liste ['a','b','a','c','a']. Affiche combien de fois 'a' apparaît (3).",
        "expected_output": "3",
        "level": 2,
        "theme": "lists"
    },
    {
        "id": "list_7",
        "title": "Trier une liste",
        "definition": "La méthode sort() trie la liste sur place, sorted(liste) renvoie une copie triée.",
        "example": "nums = [3,1,2]\nnums.sort()\nprint(nums)",
        "example_output": "[1, 2, 3]",
        "instruction": "Crée une liste [5,2,9,1]. Trie-la et affiche-la. (attendu: [1,2,5,9])",
        "expected_output": "[1, 2, 5, 9]",
        "level": 2,
        "theme": "lists"
    },
    {
        "id": "list_8",
        "title": "Liste en compréhension",
        "definition": "Une liste en compréhension permet de créer une liste via une boucle 'condensée'.",
        "example": "carrés = [x*x for x in range(3)]\nprint(carrés)",
        "example_output": "[0, 1, 4]",
        "instruction": "Crée une liste en compréhension qui contient le double de chaque nombre de 0 à 4. (attendu: [0,2,4,6,8])",
        "expected_output": "[0, 2, 4, 6, 8]",
        "level": 3,
        "theme": "lists"
    }
]
