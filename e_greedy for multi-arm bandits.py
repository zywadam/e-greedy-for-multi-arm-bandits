# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:29:13 2017

@author: zywadam
"""

__filename__ = "bandits.py"

import numpy as np

Nexp = 1000
Nlands = 10000
    
    class Bandit:
   def __init__(self,keys,init,epsilon=0.1):
        self.epsilon = epsilon
        self.PlantOutput = {}
        for key in keys:
            self.PlantOutput[key] = init
        
    def get_profit(self,plant):
        if PlantOutput[plant][1]*(price-cost) > PlantOutput[plant][0]*(price-cost) 
            return 1
        else:
            return 0
    
    def choose_plant(self):
        """
        For 1-epsilon of the time, choose the action with the highest estimated value.
        For epsilon of the time, randomly choose an action
        """
        random_num = np.random.rand()
        if random_num<self.epsilon:
            return random.choice(self.PlantOutput.keys())
        else:
            return max(self.PlantOutput, key=lambda x:self.PlantOutput.get(x)[1])
    
   def update(self,plant,reward):
        """
        Update estimated value by keeping running average of rewards for each action
        """
        K = self.PlantOutput[plant][0]
        Value = self.PlantOutput[plant][1]
        K += 1
        alpha = 1./K
        Value += alpha * (reward - Value)
        self.PlantOutput[plant] = (K,Value)


        """
        Main function running experiments and calculate expected profit
        """
  def runtest(bandit,Nlands,epsilon):
    history = []
    for i in range(Nlands):
        plant = bandit.choose_plant(epsilon)
        R = bandit.get_profit(plant)
        bandit.update(plant,R)
        history.append(R)
    return np.array(history)


    exp_profit = np.zeros(Nlands)


    for i in range(Nexp):
        bandit = Bandit()
        exp_profite += runtest(bandit,Nlands,0.1)

    exp_profit /= np.float(Nexp)


