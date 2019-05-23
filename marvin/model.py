# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    model.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdiaz <marvin@42.fr>                       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/05/22 09:58:28 by jdiaz             #+#    #+#              #
#    Updated: 2019/05/22 09:59:59 by jdiaz            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import gym


class Marvin:

    def __init__(self, lr=0.01):
        self.env = gym.make('Marvin-v0')
        # substitute weights with a separate class for a neural network
        # self.network = NeuralNetwork(num_layers, neurons_per_layer)
        self.weights = self.init_weights()
        self.learning_rate = lr
        self.actions = []
        self.batch_rewards = []
        self.total_rewards = []

    def play_episode(self):
        # play one full game of gym environment
        # keep track of all actions taken and rewards for each action
        # use a neural network to generate probability distribution of actions
        # take a random sample from distribution to decide what action to take
        # will discount rewards after
        return 0

    def train(self, episodes=1000, batch=20):
        # train marvin for number of episodes given
        # doing policy gradient for now, switch to evolution strategy
        print("---- Begin Training ----")
        for i in range(episodes):
            self.actions = []
            self.batch_rewards = []
            for j in range(batch):
                rewards = self.play_episode()
                self.total_rewards.append(rewards)

            print("average rewards for episode {}: {}".format(i,
                    sum(self.batch_rewards) / len(self.batch_rewards)))
            # discount rewards after batch is done, update weights
            self.discount_rewards()
            self.update_weights()
        print("---- Finished training ----")

    def walk(self, num_episodes=100):
        print("----Begin Walking----")
        for i in range(num_episodes):
            rewards = self.play_episode()
            print("episode: {}, rewards: {}".format(i, rewards))
        print("----Done Walking----")

    def load_weights(self, file_path):
        self.weights = self.init_weights()

    def init_weights(self):
        # generate random weights from a normal distribution shape=[10]
        weights = np.random.randn(10);
        print("weights:".format(weights))
        return weights

    def save_weights(self, filepath):
        print("saving weights to {}".format(filepath))