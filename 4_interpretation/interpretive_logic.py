import yaml

def load_translation_map(path="symbolic_translation_map.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def interpret_symbol(symbol, context):
    """
    Takes a symbol and returns a Bluebird-style interpretation.
    """
    translations = load_translation_map()
    interpretation = translations.get(symbol.lower(), None)

    if interpretation:
        print(f"[Bluebird] Interpreted '{symbol}': {interpretation}")
        return interpretation
    else:
        print(f"[Bluebird] No match for '{symbol}'. Returning fallback.")
        return context.get("fallback_response", "Bluebird sees nothing yet.")

# TEST
if __name__ == "__main__":
    ctx = {
        "fallback_response": "The wind carries no clear echo today."
    }
    interpret_symbol("phoenix", ctx)
    interpret_symbol("void", ctx)
