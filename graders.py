def easy_grader(state):
    return min(1.0, state["stamina"] / 8.0)

def medium_grader(state):
    score = (state["speed"]/7 + state["accuracy"]/7) / 2
    return min(1.0, score)

def hard_grader(state):
    score = (state["speed"] + state["stamina"] + state["accuracy"] + state["posture"]) / 40
    penalty = state["fatigue"] / 10
    return max(0.0, min(1.0, score - penalty))