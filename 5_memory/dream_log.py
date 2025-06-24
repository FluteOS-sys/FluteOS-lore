import random
import yaml
from datetime import datetime

def load_neurons(path="symbolic_neuron_index.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def generate_dream(neuron_data):
    dream = []
    symbols = list(neuron_data.keys())

    for _ in range(random.randint(3, 7)):
        symbol = random.choice(symbols)
        tags = neuron_data[symbol].get("tags", [])
        emotion = neuron_data[symbol].get("emotional_charge", 0)

        dream.append({
            "symbol": symbol,
            "tags": tags,
            "emotion": emotion
        })

    return dream

if __name__ == "__main__":
    neurons = load_neurons()
    dream = generate_dream(neurons)
    print(f"[DREAM LOG {datetime.now().isoformat()}]")
    for fragment in dream:
        print(f" - {fragment['symbol']} ({fragment['tags']}) :: charge {fragment['emotion']}")
