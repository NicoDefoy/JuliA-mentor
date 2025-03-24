from core.agent import run_exercise
from core.memory import is_done
from exercises import loops, conditions, variables, strings, lists, dictionaries, functions, classes, sets_tuples, files_exceptions, env_imports, numpy_basics, pandas_basics, scikit_learn


themes = themes = themes = {
    "1": {"name": "Variables",     "exercises": variables.exercises},
    "2": {"name": "Strings",       "exercises": strings.exercises},
    "3": {"name": "Conditions",    "exercises": conditions.exercises},
    "4": {"name": "Boucles",       "exercises": loops.exercises},
    "5": {"name": "Listes",        "exercises": lists.exercises},
    "6": {"name": "Dictionnaires", "exercises": dictionaries.exercises},
    "7": {"name": "Fonctions",     "exercises": functions.exercises},
    "8": {"name": "Classes",       "exercises": classes.exercises},
    "9": {"name": "Sets et Tuples", "exercises": sets_tuples.exercises},
    "10": {"name": "Files et Exceptions", "exercises": files_exceptions.exercises},
    "11": {"name": "Environnement et Imports", "exercises": env_imports.exercises},
    "12": {"name": "NumPy", "exercises": numpy_basics.exercises},
    "13": {"name": "Pandas", "exercises": pandas_basics.exercises},
    "14": {"name": "Scikit-learn", "exercises": scikit_learn.exercises},
}


def show_menu():
    print("\n=== MENU PRINCIPAL ===")
    print("Choisis un thème à travailler :")
    for key, theme in themes.items():
        print(f"[{key}] {theme['name']}")
    print("[Q] Quitter")

def main():
    print("👋 Salut, moi c’est JuliA. Ravie de te revoir !")

    while True:
        show_menu()
        choice = input("\n> ").strip().upper()

        if choice == "Q":
            print("À bientôt !")
            break
        elif choice in themes:
            selected = themes[choice]
            print(f"\n📚 Thème sélectionné : {selected['name']}")

            for ex in selected["exercises"]:
                if not is_done(ex["id"]):
                    run_exercise(ex)
                    break
            else:
                print("🎉 Tu as terminé tous les exercices de ce thème !")
        else:
            print("❌ Choix invalide. Essaie à nouveau.")
if __name__ == "__main__":
    main()
