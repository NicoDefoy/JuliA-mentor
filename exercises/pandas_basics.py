exercises = [
    {
        "id": "pd_1",
        "title": "Créer un DataFrame à partir d'un dict",
        "definition": "Pandas manipule des données tabulaires via le type DataFrame.",
        "example": "import pandas as pd\ndata = {'name': ['Alice', 'Bob'], 'age': [25, 30]}\ndf = pd.DataFrame(data)\nprint(df)",
        "example_output": "    name  age\n0  Alice   25\n1    Bob   30",
        "instruction": "Crée un DataFrame avec {'fruit': ['pomme', 'banane'], 'prix': [1, 2]} et affiche-le.",
        "expected_output": "   fruit  prix\n0 pomme     1\n1 banane    2",
        "level": 1,
        "theme": "pandas_basics"
    },
    {
        "id": "pd_2",
        "title": "Lire un CSV (exercice simulé)",
        "definition": "df = pd.read_csv('fichier.csv') charge un CSV si le fichier existe.",
        "example": "import pandas as pd\ndf = pd.DataFrame({'col':[1,2]})\nprint(df.head())",
        "example_output": "   col\n0    1\n1    2",
        "instruction": "Simule la lecture d'un CSV en créant un DataFrame {'A': [1,2,3], 'B':[4,5,6]}. Affiche df.",
        "expected_output": "   A  B\n0  1  4\n1  2  5\n2  3  6",
        "level": 1,
        "theme": "pandas_basics"
    },
    {
        "id": "pd_3",
        "title": "Sélection par index/loc/iloc",
        "definition": "df.loc[0] sélectionne la ligne d'index 0, df.iloc[0] la première ligne peu importe l'index.",
        "example": "df = pd.DataFrame({'X':[10,20],'Y':[30,40]}, index=['a','b'])\nprint(df.loc['a'])\nprint(df.iloc[1])",
        "example_output": "X 10\nY 30\nName: a, dtype: int64\nX    20\nY    40\nName: b, dtype: int64",
        "instruction": "Crée un DataFrame df = {'score':[100,200],'temps':[10,20]} index=['p1','p2']. Affiche la ligne d’index 'p2'.",
        "expected_output": "score    200\ntemps     20\nName: p2, dtype: int64",
        "level": 2,
        "theme": "pandas_basics"
    },
    {
        "id": "pd_4",
        "title": "Filtrer un DataFrame",
        "definition": "df[df['col'] > valeur] renvoie les lignes où la colonne 'col' est > valeur.",
        "example": "df = pd.DataFrame({'age':[10,20,30], 'nom':['A','B','C']})\nprint(df[df['age']>15])",
        "example_output": "   age nom\n1   20   B\n2   30   C",
        "instruction": "Crée df={'note':[12,15,8],'nom':['A','B','C']}. Affiche les lignes où la note est >=10.",
        "expected_output": "   note nom\n0    12   A\n1    15   B",
        "level": 2,
        "theme": "pandas_basics"
    },
    {
        "id": "pd_5",
        "title": "Ajouter une colonne calculée",
        "definition": "df['nouvelle_col'] = df['colA'] + df['colB'] par exemple.",
        "example": "df = pd.DataFrame({'x':[1,2], 'y':[3,4]})\ndf['z'] = df['x']*df['y']\nprint(df)",
        "example_output": "   x  y  z\n0  1  3  3\n1  2  4  8",
        "instruction": "Crée df={'val1':[1,2],'val2':[10,20]}. Ajoute val3 = val1*val2. Affiche df.",
        "expected_output": "   val1  val2  val3\n0     1    10    10\n1     2    20    40",
        "level": 2,
        "theme": "pandas_basics"
    },
    {
        "id": "pd_6",
        "title": "Supprimer une ligne ou une colonne",
        "definition": "df.drop('nom_colonne', axis=1) supprime la colonne. axis=0 pour les lignes.",
        "example": "df = pd.DataFrame({'A':[1,2],'B':[3,4]})\ndf = df.drop('A', axis=1)\nprint(df)",
        "example_output": "   B\n0  3\n1  4",
        "instruction": "Crée df={'A':[10,20],'B':[30,40]}. Supprime la colonne 'A'. Affiche le résultat.",
        "expected_output": "   B\n0  30\n1  40",
        "level": 2,
        "theme": "pandas_basics"
    },
    {
        "id": "pd_7",
        "title": "Regrouper (groupby) et agrégation",
        "definition": "df.groupby('col').agg({'autre_col': 'sum'}) par exemple.",
        "example": "df = pd.DataFrame({'type':['fruit','fruit','legume'],'quantite':[3,5,2]})\nprint(df.groupby('type').agg({'quantite':'sum'}))",
        "example_output": "        quantite\ntype             \nfruit           8\nlegume          2",
        "instruction": "Crée df={'cat':['A','A','B'],'val':[10,20,5]}. Fais un groupby sur 'cat' pour sommer 'val'.",
        "expected_output": "     val\ncat     \nA     30\nB      5",
        "level": 3,
        "theme": "pandas_basics"
    },
    {
        "id": "pd_8",
        "title": "Joindre deux DataFrames (merge)",
        "definition": "pd.merge(df1, df2, on='col') fait une jointure sur la colonne 'col'.",
        "example": "df1 = pd.DataFrame({'id':[1,2],'nom':['A','B']})\ndf2 = pd.DataFrame({'id':[1,2],'score':[10,20]})\nres = pd.merge(df1, df2, on='id')\nprint(res)",
        "example_output": "   id nom  score\n0   1   A     10\n1   2   B     20",
        "instruction": "Crée df1={'id':[1,2],'valA':[100,200]} et df2={'id':[1,2],'valB':[300,400]}. Fais un merge sur 'id' et affiche le résultat.",
        "expected_output": "   id  valA  valB\n0   1   100   300\n1   2   200   400",
        "level": 3,
        "theme": "pandas_basics"
    }
]
