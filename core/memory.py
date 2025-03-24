import json
from pathlib import Path

MEMORY_PATH = Path("memory.json")

def load_memory():
    if not MEMORY_PATH.exists():
        return {}
    with open(MEMORY_PATH, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_PATH, "w") as f:
        json.dump(memory, f, indent=4)

def mark_exercise_done(exo_id):
    memory = load_memory()
    memory[exo_id] = "done"
    save_memory(memory)

def is_done(exo_id):
    memory = load_memory()
    return memory.get(exo_id) == "done"
