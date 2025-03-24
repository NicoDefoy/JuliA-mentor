from core.agent import run_exercise
from core.memory import is_done
from exercises import loops
from exercises import conditions

themes = {
    "1": {
        "name": "Boucles",
        "exercises": loops.exercises
    },
    "2": {
        "name": "Conditions",
        "exercises": conditions.exercises
    }
    # On ajoutera d’autres thèmes ici plus tard (ex: conditions, fonctions...)
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
