
# Basic Knowledge

- pipeline
At timestep t, agent observe (state_t, reward_t), then execute action_t --> env change to state_{t+1}, give reward_{t+1}   
- value function
If we only care about the reward, we will fall inito a local optimum  
The better way is: total income of state_t = immediate rewards and future gains (reward_t + \gamma * V_{t+1}):  
$$
V_t = R_t + \gamma V_{t+1}
$$





# Algorithms


RLHF + PPO

DPO

KTO

IPO

SimPO

TDPO (Token-level Direct Preference Optimization)



# Framework


[OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)



[InternLM/xtuner](https://github.com/InternLM/xtuner)



# paper


[Policy Optimization in RLHF: The Impact of Out-of-preference Data](https://arxiv.org/abs/2312.10584): 讲了DPO不如RLHF

CVPR2024 best paper: [Rich Human Feedback for Text-to-Image Generation](https://github.com/google-research/google-research/tree/master/richhf_18k)
