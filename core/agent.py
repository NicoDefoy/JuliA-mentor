def run_exercise(exo):
    print(f"\n📘 Exercice : {exo['title']}")
    print(f"\n📖 Définition :\n{exo['definition']}")
    print(f"\n🧪 Exemple :\n{exo['example']}")
    print(f"\nCe code affiche :\n{exo['example_output']}")
    print(f"\n💪 À toi de jouer !\n{exo['instruction']}")
    print("\nTape ton code ci-dessous (tape END sur une ligne seule pour valider) :")

    user_code = ""
    while True:
        line = input()
        if line.strip().lower() == "end":
            break
        user_code += line + "\n"

    try:
        local_env = {}
        exec(user_code, {}, local_env)

        import io
        import contextlib

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            exec(user_code, {}, {})
        output = f.getvalue().strip()

        if output == exo['expected_output']:
            from core.memory import mark_exercise_done
            mark_exercise_done(exo["id"])
            print("\n✅ Bien joué, c’est exactement ça ! Cet exercice est désormais marqué comme terminé.")

        else:
            print("\n❌ Le résultat est incorrect.")
            print("Tu veux : [1] un indice ou [2] la correction ?")
            choice = input("> ")
            if choice == "1":
                print("\n💡 Indice : Utilise la fonction range(5) et print(i).")
            else:
                print("\n✅ Correction possible :")
                print(exo['example'])
    except Exception as e:
        print(f"\n⚠️ Erreur détectée : {type(e).__name__}")
        if isinstance(e, IndentationError):
            print("🔧 Astuce : Le code à l'intérieur d'une boucle doit être indenté (décalé avec des espaces).")
            print("Exemple :\nfor i in range(5):\n    print(i)")
        elif isinstance(e, SyntaxError):
            print("🔧 Astuce : Vérifie la syntaxe, il manque peut-être un deux-points, une parenthèse ou un guillemet.")
        else:
            print(f"🧨 Détail de l'erreur : {e}")
