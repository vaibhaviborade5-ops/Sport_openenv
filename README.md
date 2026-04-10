# Sports Talent RL Environment (OpenEnv)

## Key Innovation
This project models athlete training as a reinforcement learning problem where an AI agent learns optimal coaching strategies under performance-fatigue trade-offs.

## Run

```bash
docker build -t sports-env .
docker run -p 7860:7860 sports-env