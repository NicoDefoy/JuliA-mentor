exercises = [
    {
        "id": "np_1",
        "title": "Créer un tableau NumPy",
        "definition": "NumPy est la base pour manipuler des tableaux multidimensionnels.",
        "example": "import numpy as np\narr = np.array([1, 2, 3])\nprint(arr.shape)\nprint(arr.dtype)",
        "example_output": "(3,)\nint64",
        "instruction": "Crée un tableau [10, 20, 30] et affiche sa forme (shape).",
        "expected_output": "(3,)",
        "level": 1,
        "theme": "numpy_basics"
    },
    {
        "id": "np_2",
        "title": "Accéder aux éléments et slicing",
        "definition": "arr[0], arr[1:]... etc.",
        "example": "import numpy as np\narr = np.array([1, 2, 3])\nprint(arr[1])\nprint(arr[:2])",
        "example_output": "2\n[1 2]",
        "instruction": "Crée un tableau [4,5,6,7]. Affiche arr[0] puis arr[2:].",
        "expected_output": "4\n[6 7]",
        "level": 1,
        "theme": "numpy_basics"
    },
    {
        "id": "np_3",
        "title": "Opérations vectorisées",
        "definition": "On peut faire arr * 2 pour multiplier chaque élément par 2, arr + arr2 pour additionner terme à terme, etc.",
        "example": "arr = np.array([1,2,3])\nprint(arr * 2)\nprint(arr + 10)",
        "example_output": "[2 4 6]\n[11 12 13]",
        "instruction": "Crée arr=[2,4,6], multiplie par 3 et affiche le résultat ([6,12,18]).",
        "expected_output": "[ 6 12 18]",
        "level": 1,
        "theme": "numpy_basics"
    },
    {
        "id": "np_4",
        "title": "Matrice 2D",
        "definition": "On peut créer un tableau 2D avec np.array([[1,2],[3,4]]).",
        "example": "mat = np.array([[1,2],[3,4]])\nprint(mat.shape)",
        "example_output": "(2, 2)",
        "instruction": "Crée une matrice 2x3 [[1,2,3],[4,5,6]] et affiche sa forme.",
        "expected_output": "(2, 3)",
        "level": 2,
        "theme": "numpy_basics"
    },
    {
        "id": "np_5",
        "title": "Sommation, moyenne, min, max",
        "definition": "np.sum(arr), np.mean(arr) etc. permettent des stats rapides.",
        "example": "arr = np.array([1,2,3])\nprint(np.sum(arr))\nprint(np.mean(arr))",
        "example_output": "6\n2.0",
        "instruction": "Crée arr=[10,20,30]. Affiche la somme (60), la moyenne (20) et le max (30).",
        "expected_output": "60\n20.0\n30",
        "level": 2,
        "theme": "numpy_basics"
    },
    {
        "id": "np_6",
        "title": "Reshape",
        "definition": "arr.reshape(new_shape) change la forme du tableau sans changer les données.",
        "example": "arr = np.array([1,2,3,4])\nmat = arr.reshape((2,2))\nprint(mat)",
        "example_output": "[[1 2]\n [3 4]]",
        "instruction": "Crée arr=[1,2,3,4,5,6]. Fais un reshape en (2,3) et affiche la matrice.",
        "expected_output": "[[1 2 3]\n [4 5 6]]",
        "level": 2,
        "theme": "numpy_basics"
    },
    {
        "id": "np_7",
        "title": "Indexation booléenne",
        "definition": "On peut filtrer un array avec arr[arr > 5] par ex.",
        "example": "arr = np.array([3,6,9])\nprint(arr[arr > 5])",
        "example_output": "[6 9]",
        "instruction": "Crée arr=[2,5,7,10]. Affiche uniquement les éléments >5 ([7,10]).",
        "expected_output": "[ 7 10]",
        "level": 3,
        "theme": "numpy_basics"
    },
    {
        "id": "np_8",
        "title": "Random & seed",
        "definition": "np.random.seed(x) fixe la graine. np.random.rand(n) génère n nombres aléatoires entre 0 et 1.",
        "example": "import numpy as np\nnp.random.seed(0)\nprint(np.random.rand(3))",
        "example_output": "[0.5488135  0.71518937 0.60276338]",
        "instruction": "Fixe la seed à 42, puis génère 3 nombres aléatoires. Affiche-les.",
        "expected_output": "",  
        "level": 3,
        "theme": "numpy_basics"
    }
]
