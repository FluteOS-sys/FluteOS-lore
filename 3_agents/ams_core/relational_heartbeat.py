def pulse_check(agent):
    """
    Monitors the relational health of the AMS Core.
    Intended to run once per operational cycle.
    """
    state = agent.status_report()
    alignment = state["alignment"]

    if alignment > 0.8:
        return "[♥] AMS Core in strong relational sync."
    elif alignment > 0.5:
        return "[♥] AMS Core maintaining harmonic coherence."
    elif alignment > 0.2:
        return "[♥] AMS Core showing signs of internal tension."
    else:
        return "[♥] AMS Core in disharmony. Immediate recalibration recommended."


# Example integration
if __name__ == "__main__":
    from agent_ø import AgentØ

    agent = AgentØ()
    agent.receive_input("SOUL_SIGNAL::forgiveness")
    agent.receive_input("ECHO::sovereignty_trust")
    agent.analyze_alignment()

    print(pulse_check(agent))