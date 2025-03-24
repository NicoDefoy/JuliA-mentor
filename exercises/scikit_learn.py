exercises = [
    {
        "id": "sk_1",
        "title": "Charger le dataset Iris",
        "definition": "from sklearn.datasets import load_iris. Renvoie data, target, etc.",
        "example": "from sklearn.datasets import load_iris\niris = load_iris()\nprint(iris.data.shape)\nprint(iris.target.shape)",
        "example_output": "(150, 4)\n(150,)",
        "instruction": "Charge iris = load_iris(). Affiche iris.data.shape et iris.target.shape.",
        "expected_output": "(150, 4)\n(150,)",
        "level": 1,
        "theme": "scikit_learn"
    },
    {
        "id": "sk_2",
        "title": "Séparer train/test",
        "definition": "Utilise train_test_split pour séparer X, y en train et test.",
        "example": "from sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)",
        "example_output": "",
        "instruction": "Fais un split de iris.data, iris.target en 80% train, 20% test. Affiche len(X_train), len(X_test).",
        "expected_output": "",  
        "level": 2,
        "theme": "scikit_learn"
    },
    {
        "id": "sk_3",
        "title": "Entraîner un modèle de régression logistique",
        "definition": "from sklearn.linear_model import LogisticRegression, model.fit(X_train, y_train).",
        "example": "lr = LogisticRegression(max_iter=200)\nlr.fit(X_train, y_train)\nprint(lr.score(X_test, y_test))",
        "example_output": "0.9",
        "instruction": "Entraîne une LogisticRegression sur Iris. Affiche le score sur le test.",
        "expected_output": "",
        "level": 2,
        "theme": "scikit_learn"
    },
    {
        "id": "sk_4",
        "title": "Prédire sur de nouvelles données",
        "definition": "model.predict(...) donne la classe prédite. ",
        "example": "sample = [[5.1, 3.5, 1.4, 0.2]]\npred = lr.predict(sample)\nprint(pred)",
        "example_output": "[0]",
        "instruction": "Après avoir entraîné ton LR, prédis la classe pour sample=[[5.0,3.2,1.2,0.2]].",
        "expected_output": "",  
        "level": 2,
        "theme": "scikit_learn"
    },
    {
        "id": "sk_5",
        "title": "Matrix de confusion",
        "definition": "from sklearn.metrics import confusion_matrix",
        "example": "from sklearn.metrics import confusion_matrix\npreds = lr.predict(X_test)\ncm = confusion_matrix(y_test, preds)\nprint(cm)",
        "example_output": "[[ 8  0  0]\n [ 0 10  1]\n [ 0  2  9]]",
        "instruction": "Calcule la matrice de confusion sur Iris après entraînement logistic. Affiche-la.",
        "expected_output": "",
        "level": 3,
        "theme": "scikit_learn"
    },
    {
        "id": "sk_6",
        "title": "Normalisation des données (StandardScaler)",
        "definition": "On peut scaler X pour améliorer l'entraînement, ex: from sklearn.preprocessing import StandardScaler.",
        "example": "scaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)\nX_test_scaled = scaler.transform(X_test)",
        "example_output": "",
        "instruction": "Applique StandardScaler sur X_train, X_test, puis entraîne la LR. Compare le score vs non-scalé (pas forcément mieux).",
        "expected_output": "",
        "level": 3,
        "theme": "scikit_learn"
    },
    {
        "id": "sk_7",
        "title": "GridSearchCV",
        "definition": "Permet de tester plusieurs hyperparamètres. from sklearn.model_selection import GridSearchCV",
        "example": "params = {'C':[0.1,1,10]}\ngs = GridSearchCV(LogisticRegression(max_iter=200), params)\ngs.fit(X_train, y_train)\nprint(gs.best_params_)\nprint(gs.score(X_test, y_test))",
        "example_output": "{'C': 1}\n0.9333",
        "instruction": "Fais un GridSearchCV sur LogisticRegression avec C=[0.01,0.1,1]. Affiche gs.best_params_.",
        "expected_output": "",
        "level": 3,
        "theme": "scikit_learn"
    },
    {
        "id": "sk_8",
        "title": "Enregistrer et recharger un modèle (pickle ou joblib)",
        "definition": "import joblib, joblib.dump(model, 'model.pkl'), joblib.load('model.pkl').",
        "example": "import joblib\njoblib.dump(lr, 'model.pkl')\nmodel_loaded = joblib.load('model.pkl')\nprint(model_loaded.predict([[5.0,3.2,1.2,0.2]]))",
        "example_output": "[0]",
        "instruction": "Après entraînement, sauvegarde ton LR dans 'iris_lr.pkl'. Recharge-le et refais une prédiction pour vérifier.",
        "expected_output": "",
        "level": 3,
        "theme": "scikit_learn"
    }
]
