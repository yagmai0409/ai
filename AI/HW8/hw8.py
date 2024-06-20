import gym

def main():
    # Create the CartPole-v1 environment
    env = gym.make("CartPole-v1", render_mode="human")
    observation, info = env.reset(seed=42)

    steps = 0
    max_steps = 0

    # Run the main loop for up to 1000 steps
    for _ in range(1000):
        env.render()  # Render the current state of the environment

        # Extract variables from the observation
        position, velocity, angle, angular_velocity = observation

        # Determine action based on observation
        if angle > 0:
            action = 1 if angular_velocity > 0 else 0
        else:
            action = 0 if angular_velocity < 0 else 1

        # Adjust action based on position
        if position > 0.1:
            action = 0
        elif position < -0.1:
            action = 1

        # Take action and receive feedback from the environment
        observation, reward, terminated, truncated, info = env.step(action)
        steps += 1

        # Handle termination or truncation of the episode
        if terminated or truncated:
            if steps > max_steps:
                max_steps = steps
            print(f'Died after {steps} steps')
            steps = 0
            observation, info = env.reset()  # Reset the environment

    env.close()  # Close the environment
    print(f'Maximum steps survived: {max_steps}')

if __name__ == "__main__":
    main()
