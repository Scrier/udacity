import numpy as np
from collections import defaultdict


class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.Epsilon = .64
        self.Counter = 0
        self.Gamma = .6
        self.Alpha = .6

    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        policy_s = np.ones(self.nA) * self.Epsilon / self.nA
        policy_s[np.argmax(self.Q[state])] = 1 - self.Epsilon + (self.Epsilon / self.nA)

        return np.random.choice(np.arange(self.nA), p=policy_s)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        if not done:
            gamma = self.Gamma
            alpha = self.Alpha

            next_action = self.select_action(next_state)
            policy_s = np.ones(self.nA) * self.Epsilon / self.nA
            policy_s[np.argmax(self.Q[next_state])] = 1 - self.Epsilon + (self.Epsilon / self.nA)

            self.Counter += 1
            self.Epsilon = self.Alpha ** self.Counter

            Qsa_next = np.dot(self.Q[next_state], policy_s)

            self.Q[state][action] = self.Q[state][action] + (
                        alpha * (reward + (gamma * Qsa_next) - self.Q[state][action]))

