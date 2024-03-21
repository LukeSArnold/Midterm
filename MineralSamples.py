from numpy.random import beta, normal, uniform
import random
import matplotlib.pyplot as plt
import sys

def part1():
    # collect one data point per month, for two years
    # 24 total months

    area1 = []
    area2 = []
    area3 = []
    area4 = []
    area5 = []
    area6 = []
    area7 = []
    area8 = []
    area9 = []
    area10 = []
    
    months = [i for i in range(24)]

    for i in range(24):
        # get area distributions
        area1.append(beta(2, 2)+1)
        area2.append(beta(3, 7)*3)
        area3.append(normal(2.4, 1.8))
        area4.append(uniform(-1, 4))
        area5.append(normal(0, 9))
        area6.append(beta(7, 3)+2)
        area7.append(uniform(0, 4))
        area8.append(beta(3, 7)*2)        
        area9.append(normal(2, 1.4))
        area10.append(normal(1.3, 7))
        
    plt.plot(months, area1, label='area 1')
    plt.plot(months, area2, label='area 2')
    plt.plot(months, area3, label='area 3')
    plt.plot(months, area4, label='area 4')
    plt.plot(months, area5, label='area 5')
    plt.plot(months, area6, label='area 6')
    plt.plot(months, area7, label='area 7')
    plt.plot(months, area8, label='area 8')
    plt.plot(months, area9, label='area 9')
    plt.plot(months, area10, label='area 10')

    plt.title('Value generated from each mining site per day')
    plt.legend()
    plt.show()

def part2():
    
    def get_distributions():
        """ This function exists to ensure that distributions are always random, and don't default to an initial value"""
        return [beta(2, 2)+1, beta(3, 7)*3, normal(2.4, 1.8), uniform(-1, 4), normal(0, 9), beta(7, 3)+2, uniform(0, 4), beta(3, 7)*2, normal(2, 1.4), normal(1.3, 7)]
            
    epsilon = 0.3

    # initializing default for one sample per location per month
    monthly_sample = [1,1,1,1,1,1,1,1,1,1]
    all_monthly_samples = []
    draws = [[],[],[],[],[],[],[],[],[],[]] 
    all_averages = [[],[],[],[],[],[],[],[],[],[]]
    averages = []
    
    # perform initial draw
    for i in range(len(get_distributions())):
        draw = get_distributions()[i]
        draws[i].append(draw)
        averages.append(sum(draws[i])/ len(draws[i]))

    # This is a variation on the epsilon greedy for the "multi-armed bandits" problem. 
    # Instead of prioritizing a single location, we will prioritize 5 locations, and slowly reapportion
    # attention to the best performing locations. 
    # 
    # As the simulation continues, we will converge on a smaller number of higher performing locations 

    best_averages = []
    intermediary = averages.copy()
    intermediary.sort()
    for i in range(5, 0, -1):
        best_averages.append(averages.index(intermediary[i]))


    # increment the amount of time spent at each location, 
    # taking it from low performing locations and giving it to high performing ones
    for i in range(len(monthly_sample)):
        if i in best_averages:
            monthly_sample[i] += 1
        else:
            monthly_sample[i] -= 1

    # run through 24 months for pilot sample
    for i in range(24):
        all_monthly_samples.append(monthly_sample.copy())
        val = random.randint(0,1)
        if val <= epsilon:
            for x in range(5):
                site = random.randint(0,9)
                for attention in range(2):
                    draws[site].append(get_distributions()[site])

                averages[x] = (sum(draws[x]) / len(draws[x]))


        else:
            for x in range(len(get_distributions())):
                for attention in range(monthly_sample[x]):
                    draws.append(get_distributions()[x])

                averages[x] = (sum(draws[x]) / len(draws[x]))

        # update best averages and attention to each location
        best_averages = []
        intermediary = averages.copy()
        intermediary.sort()
        for x in range(9, 4, -1):
            best_averages.append(averages.index(intermediary[x])) 

        num_teams_available = 0
        for x in range(len(monthly_sample)):
            if ((monthly_sample[x] > 0) and (x not in best_averages)):
                monthly_sample[x] -= 1
                num_teams_available += 1

        for index in best_averages:
            if num_teams_available > 0:
                monthly_sample[index] += 1
                num_teams_available -= 1

        for x in range(len(averages)):
            all_averages[x].append(averages[x])

    plt.title('Average production from each site')
    plt.plot(all_averages[0], label='area1')
    plt.plot(all_averages[1], label='area2')
    plt.plot(all_averages[2], label='area3')
    plt.plot(all_averages[3], label='area4')
    plt.plot(all_averages[4], label='area5')
    plt.plot(all_averages[5], label='area6')
    plt.plot(all_averages[6], label='area7')
    plt.plot(all_averages[7], label='area8')
    plt.plot(all_averages[8], label='area9')
    plt.plot(all_averages[9], label='area10')
    plt.legend()

    plt.show()

    # get breakdown of all monthly samples to display how the attention
    # provided to each site moves 

    breakdown_sample = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(all_monthly_samples)):
        working_sample = all_monthly_samples[i]
        for x in range(len(working_sample)):
            breakdown_sample[x].append(working_sample[x])

    plt.figure()
    plt.title('Teams given to each site by month')
    plt.plot(breakdown_sample[0], label='area1')
    plt.plot(breakdown_sample[1], label='area2')
    plt.plot(breakdown_sample[2], label='area3')
    plt.plot(breakdown_sample[3], label='area4')
    plt.plot(breakdown_sample[4], label='area5')
    plt.plot(breakdown_sample[5], label='area6')
    plt.plot(breakdown_sample[6], label='area7')
    plt.plot(breakdown_sample[7], label='area8')
    plt.plot(breakdown_sample[8], label='area9')
    plt.plot(breakdown_sample[9], label='area10')
    plt.legend()
    plt.show()
    
def part3():

    def get_distributions():
        """ This function exists to ensure that distributions are always random, and don't default to an initial value"""
        return [beta(2, 2)+1, beta(3, 7)*3, normal(2.4, 1.8), uniform(-1, 4), normal(0, 9), beta(7, 3)+2, uniform(0, 4), beta(3, 7)*2, normal(2, 1.4), normal(1.3, 7)]

    epsilon = 0.3

    # initializing default for one sample per location per month
    monthly_sample = [1,1,1,1,1,1,1,1,1,1]
    all_monthly_samples = []
    draws = [[],[],[],[],[],[],[],[],[],[]]
    all_averages = [[],[],[],[],[],[],[],[],[],[]]
    averages = []

    # perform initial draw
    for i in range(len(get_distributions())):
        draw = get_distributions()[i]
        draws[i].append(draw)
        averages.append(sum(draws[i])/ len(draws[i]))


    # run through 24 months for pilot sample
    for i in range(24):
        all_monthly_samples.append(monthly_sample.copy())
        val = random.randint(0,1)

        if i > 5:
            if val <= epsilon:
                for x in range(5):
                    site = random.randint(0,9)
                    for attention in range(2):
                        draws[site].append(get_distributions()[site])

                    averages[x] = (sum(draws[x]) / len(draws[x]))


            else:
                for x in range(len(get_distributions())):
                    for attention in range(monthly_sample[x]):
                        draws.append(get_distributions()[x])

                    averages[x] = (sum(draws[x]) / len(draws[x]))

        else:
             for x in range(len(get_distributions())):
                    for attention in range(monthly_sample[x]):
                        draws.append(get_distributions()[x])


        # update best averages and attention to each location
        best_averages = []
        intermediary = averages.copy()
        intermediary.sort()
        for x in range(9, 4, -1):
            best_averages.append(averages.index(intermediary[x]))

        if i > 5:
            num_teams_available = 0
            for x in range(len(monthly_sample)):
                if ((monthly_sample[x] > 0) and (x not in best_averages)):
                    monthly_sample[x] -= 1
                    num_teams_available += 1

            for index in best_averages:
                if num_teams_available > 0:
                    monthly_sample[index] += 1
                    num_teams_available -= 1

        for x in range(len(averages)):
            all_averages[x].append(averages[x])

    plt.title('Average production from each site')
    plt.plot(all_averages[0], label='area1')
    plt.plot(all_averages[1], label='area2')
    plt.plot(all_averages[2], label='area3')
    plt.plot(all_averages[3], label='area4')
    plt.plot(all_averages[4], label='area5')
    plt.plot(all_averages[5], label='area6')
    plt.plot(all_averages[6], label='area7')
    plt.plot(all_averages[7], label='area8')
    plt.plot(all_averages[8], label='area9')
    plt.plot(all_averages[9], label='area10')
    plt.legend()

    plt.show()

    # get breakdown of all monthly samples to display how the attention
    # provided to each site moves

    breakdown_sample = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(all_monthly_samples)):
        working_sample = all_monthly_samples[i]
        for x in range(len(working_sample)):
            breakdown_sample[x].append(working_sample[x])

    plt.figure()
    plt.title('Teams given to each site by month')
    plt.plot(breakdown_sample[0], label='area1')
    plt.plot(breakdown_sample[1], label='area2')
    plt.plot(breakdown_sample[2], label='area3')
    plt.plot(breakdown_sample[3], label='area4')
    plt.plot(breakdown_sample[4], label='area5')
    plt.plot(breakdown_sample[5], label='area6')
    plt.plot(breakdown_sample[6], label='area7')
    plt.plot(breakdown_sample[7], label='area8')
    plt.plot(breakdown_sample[8], label='area9')
    plt.plot(breakdown_sample[9], label='area10')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    if 'part1' in sys.argv:
        part1()
    elif 'part2' in sys.argv:
        part2()
    elif 'part3' in sys.argv:
        part3()
