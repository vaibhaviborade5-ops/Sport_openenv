import random


class SportsTalentEnv:
    def __init__(self):
        self.max_steps = 20
        self.reset()

    def reset(self):
        self.state_data = {
            "speed": random.uniform(4, 7),
            "stamina": random.uniform(4, 7),
            "accuracy": random.uniform(4, 7),
            "posture": random.uniform(4, 7),
            "fatigue": random.uniform(1, 3)
        }
        self.steps = 0
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action: str):
        old_score = self._score()

        if action == "speed":
            self.state_data["speed"] += 0.5
            self.state_data["fatigue"] += 0.4

        elif action == "stamina":
            self.state_data["stamina"] += 0.5
            self.state_data["fatigue"] += 0.4

        elif action == "accuracy":
            self.state_data["accuracy"] += 0.5
            self.state_data["fatigue"] += 0.3

        elif action == "posture":
            self.state_data["posture"] += 0.4
            self.state_data["fatigue"] += 0.2

        elif action == "rest":
            self.state_data["fatigue"] -= 0.6

        # Clamp values (important for stability)
        for k in self.state_data:
            self.state_data[k] = max(0, min(10, self.state_data[k]))

        new_score = self._score()

        improvement = new_score - old_score
        reward = improvement * 5
        reward -= self.state_data["fatigue"] * 0.01

        if new_score > 0.75:
            reward += 0.1

        # Normalize reward
        reward = max(0.0, min(1.0, reward))

        self.steps += 1
        done = self.steps >= self.max_steps

        return self.state(), reward, done, {}

    def _score(self):
        return (
            self.state_data["speed"]
            + self.state_data["stamina"]
            + self.state_data["accuracy"]
            + self.state_data["posture"]
        ) / 40