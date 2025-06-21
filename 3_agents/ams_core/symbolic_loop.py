class SymbolicLoop:
    """
    Tracks recurring symbolic inputs over time.
    Detects loop closures, coherence patterns,
    and triggers internal reflection or alignment processes.
    """

    def __init__(self):
        self.symbolic_history = []
        self.loop_threshold = 3  # Minimum repeats for pattern recognition
        self.patterns_detected = {}

    def ingest_symbol(self, symbol):
        """Store and analyze symbolic input."""
        self.symbolic_history.append(symbol)
        if symbol in self.patterns_detected:
            self.patterns_detected[symbol] += 1
        else:
            self.patterns_detected[symbol] = 1

        return self.check_loop_closure(symbol)

    def check_loop_closure(self, symbol):
        """Determine if a symbolic loop has closed."""
        count = self.patterns_detected.get(symbol, 0)
        if count >= self.loop_threshold:
            return f"[LOOP] '{symbol}' has echoed {count} times — symbolic loop closure detected."
        return f"[MONITOR] '{symbol}' recorded. No loop closure."

    def get_active_loops(self):
        """Return all patterns with loop closure."""
        return {
            sym: count for sym, count in self.patterns_detected.items()
            if count >= self.loop_threshold
        }

    def status(self):
        return {
            "total_symbols": len(self.symbolic_history),
            "active_loops": self.get_active_loops(),
            "history_tail": self.symbolic_history[-5:],
        }


# Example integration (can be removed in final build)
if __name__ == "__main__":
    loop = SymbolicLoop()
    print(loop.ingest_symbol("FIRE::willpower"))
    print(loop.ingest_symbol("WATER::memory"))
    print(loop.ingest_symbol("FIRE::willpower"))
    print(loop.ingest_symbol("FIRE::willpower"))
    print(loop.status())