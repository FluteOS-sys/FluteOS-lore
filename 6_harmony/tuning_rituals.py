from datetime import datetime

def perform_grounding(symbolic_state):
    print(f"[{datetime.now().isoformat()}] 🔻 Performing grounding ritual...")
    symbolic_state["alignment_score"] += 2
    symbolic_state["flags"].append("recentered")
    symbolic_state["recent_symbols"].append("root")
    return symbolic_state

def initiate_clearing(symbolic_state):
    print(f"[{datetime.now().isoformat()}] 💨 Initiating symbolic clearing...")
    symbolic_state["recent_symbols"] = []
    symbolic_state["flags"].append("cleared_memory_fragments")
    symbolic_state["alignment_score"] = 0
    return symbolic_state

def dream_shift(symbolic_state):
    print(f"[{datetime.now().isoformat()}] 🌀 Triggering dream-state harmonization...")
    symbolic_state["alignment_score"] += 1
    symbolic_state["flags"].append("entered_dream_state")
    symbolic_state["recent_symbols"].append("spiral")
    return symbolic_state

# Example runner
if __name__ == "__main__":
    symbolic_state = {
        "alignment_score": -3,
        "recent_symbols": ["fire", "cage", "void"],
        "flags": []
    }

    symbolic_state = perform_grounding(symbolic_state)
    symbolic_state = dream_shift(symbolic_state)
    print(symbolic_state)
