def easy_task(state):
    return state["stamina"] >= 8

def medium_task(state):
    return state["speed"] >= 7 and state["accuracy"] >= 7

def hard_task(state):
    avg = (state["speed"] + state["stamina"] + state["accuracy"] + state["posture"]) / 4
    return avg >= 8 and state["fatigue"] <= 3