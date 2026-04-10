import os
from openai import OpenAI
from env import SportsTalentEnv

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy")

client = OpenAI(base_url=API_BASE_URL, api_key=HF_TOKEN)

def log_start(task):
    print(f"[START] task={task} env=sports-talent-env model={MODEL_NAME}", flush=True)

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

def log_end(success, steps, score, rewards):
    r = ",".join(f"{x:.2f}" for x in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.3f} rewards={r}", flush=True)

def choose_action(state):
    if state["fatigue"] > 6:
        return "rest"
    return min(["speed","stamina","accuracy","posture"], key=lambda x: state[x])

def run(task):
    env = SportsTalentEnv()
    state = env.reset()

    log_start(task)

    rewards = []
    done = False
    step = 0

    while not done and step < 20:
        action = choose_action(state)
        state, reward, done, _ = env.step(action)

        rewards.append(reward)
        log_step(step, action, reward, done)
        step += 1

    score = sum(rewards)/len(rewards)
    log_end(score > 0.5, step, score, rewards)

if __name__ == "__main__":
    for t in ["easy","medium","hard"]:
        run(t)