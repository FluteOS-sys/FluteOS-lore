# outbound_adapter.py
# FluteOS Output Gateway Adapter

from typing import Dict, Any

class OutboundAdapter:
    """
    Translates symbolic output into formats
    compatible with external modules or systems.
    """

    def __init__(self):
        self.channels = {
            "narrative_response": self._send_narrative,
            "ui_trigger": self._trigger_interface,
            "memory_push": self._archive_memory
        }

    def handle_output(self, channel_id: str, data: Dict[str, Any]) -> str:
        if channel_id not in self.channels:
            raise ValueError(f"Unknown outbound channel: {channel_id}")
        return self.channels[channel_id](data)

    def _send_narrative(self, data: Dict[str, str]) -> str:
        return f"[Narrative Output] {data.get('text', 'No text provided')}"

    def _trigger_interface(self, signal: Dict[str, Any]) -> str:
        return f"[UI Event] Trigger: {signal.get('symbol', 'unspecified')}"

    def _archive_memory(self, memory_blob: Dict[str, Any]) -> str:
        return f"[Archive Push] Memory unit sent to backup node {memory_blob.get('target', 'unspecified')}"

# Example usage
if __name__ == "__main__":
    out = OutboundAdapter()
    test = out.handle_output("narrative_response", {"text": "You’ve reconnected a symbolic thread."})
    print(test)
