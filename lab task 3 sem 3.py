class ReflexAgent:
    def __init__(self):
        self.state = 'neurolink'

    def perceive(self, environment):
        if environment == 'sad':
            self.state = 'sad'
        elif environment == 'tired':
            self.state = 'tired'
        elif environment == 'happy':
            self.state = 'happy'
        else:
            self.state = 'neutral'

    def act(self):
        if self.state == 'sad':
            return "Keep Patience"
        elif self.state == 'tired':
            return "Rest"
        elif self.state == 'happy':
            return "Enjoy"
        else:
            return "Do nothing"

if __name__ == "__main__":
    agent = ReflexAgent()
    environment = ['neutral', 'sad', 'tired', 'happy', 'neutral']
    for state in environment:
        print(f"Recognized state: {state}")
        agent.perceive(state)
        action = agent.act()
        print(f"Agent action: {action}")