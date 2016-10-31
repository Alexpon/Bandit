import numpy as np


bandits = [0.1, 0.3, 0.6, 0.2, 0.5, 0.8, 0.7, 0.4, 0.2, 0.1, 0.05, 0.25]
bandit_size = len(bandits)
iter_num = 1000

def random():
	reward = 0
	for i in range(iter_num):
		if(np.random.rand() <= bandits[np.random.randint(bandit_size)]):
			reward += 1
	return reward


def naive_algorithm(sample_num):
    cumulate = np.zeros((bandit_size, 2))
    reward = 0
    for i in range(sample_num):
        choose = np.random.randint(bandit_size)
        prob = np.random.rand()
        if(prob <= bandits[choose]):
            cumulate[choose][0] += 1
            reward += 1
        else:
            cumulate[choose][1] += 1
    prob_list = np.zeros(bandit_size)
    for i in range(bandit_size):
        denominator = cumulate[i][0]+cumulate[i][1]
        if denominator==0:
            prob_list[i] = 0
        else:
            prob_list[i] = cumulate[i][0] / denominator

    idx = np.argmax(prob_list)
    for i in range(iter_num-sample_num):
    	prob = np.random.rand()
    	if(prob <= bandits[idx]):
            reward += 1
    print ("sample_num =", sample_num, " reward =", reward)

def epsilon_greedy(epsilon):
	cumulate = np.zeros((3, bandit_size))
	reward = 0
	now_bandit = np.random.randint(bandit_size)

	if(np.random.rand() <= bandits[now_bandit]):
		cumulate[0][now_bandit] += 1
		reward += 1
	else:
		cumulate[1][now_bandit] += 1
	cumulate[2][now_bandit] = cumulate[0][now_bandit] / (cumulate[0][now_bandit]+cumulate[1][now_bandit])

	for i in range(iter_num-1):
		eps_prob = np.random.rand()
		if(eps_prob <= epsilon):
			new = np.random.randint(bandit_size)
			while (new == now_bandit):
				new = np.random.randint(bandit_size)
			now_bandit = new
		else:
			now_bandit = np.argmax(cumulate[2])

		if(np.random.rand() <= bandits[now_bandit]):
			reward += 1
			cumulate[0][now_bandit] += 1
		else:
			cumulate[1][now_bandit] += 1
		cumulate[2][now_bandit] = cumulate[0][now_bandit] / (cumulate[0][now_bandit]+cumulate[1][now_bandit])
	return reward


def main():

	print ("Random Select: ")
	print ("reward=", random())

	print ("\nNaive Select: ")
	naive_algorithm(2)
	naive_algorithm(5)
	naive_algorithm(10)
	naive_algorithm(100)
	naive_algorithm(200)
    
	print ("Epsilon Greedy: ")
	print ("reward=", epsilon_greedy(0.1))

    
if __name__ == '__main__':
    main()
