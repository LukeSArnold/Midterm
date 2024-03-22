import random
import sys
import matplotlib.pyplot as plt
import seaborn as sns

def part1(days):

    # breaking down percentage values relative to entire processor batch

    # 0.3886 are type 3
    # 0.1392 are type 5
    # 0.05104 are type 7
    # 0.00116 are eHP


    total = []
    for day in range(days):

        type3 = 0
        type5 = 0
        type7 = 0
        ehp = 0

        
        for i in range(1000):
            random_val = random.uniform(1,1000)
            if 1 <= random_val <= 2.16:
                ehp += 1
            elif 2.16 < random_val <= 53.2:
                type7 += 1
            elif 52.3 < random_val <= 192.4:
                type5 += 1
            elif 192.4 < random_val <= 581:
                type3 += 1
        total.append(ehp)

    total_days = [i for i in range(days)]
    plt.title('Number of EHP processors created per day')
    plt.plot(total_days, total)
    plt.show()

    sns.displot(total, kde=True).set(title='Distribution of Processors Created Daily')
    plt.show()

def part2(days):

    # assuming 50 days, create 1000 units per day for at least 50 days.
    # for the first 37% of days, check which day produces the most number of EHP processors
    # per day.
    # For the first day that produces more EHP in a single day than the previous days
    # stop production. 

    total = []



    thirty_seven_per = int(days * 0.37)
    for day in range(thirty_seven_per):

        type3 = 0
        type5 = 0
        type7 = 0
        ehp = 0
        for i in range(1000):
            random_val = random.uniform(1,1000)
            if 1 <= random_val <= 2.16:
                ehp += 1
            elif 2.16 < random_val <= 53.2:
                type7 += 1
            elif 52.3 < random_val <= 192.4:
                type5 += 1
            elif 192.4 < random_val <= 581:
                type3 += 1
        total.append(ehp)

    max_val = max(total)

    for day in range(thirty_seven_per, days, 1):
        type3 = 0
        type5 = 0
        type7 = 0
        ehp = 0
        for i in range(1000):
            random_val = random.uniform(1,1000)
            if 1 <= random_val <= 2.16:
                ehp += 1
            elif 2.16 < random_val <= 53.2:
                type7 += 1
            elif 52.3 < random_val <= 192.4:
                type5 += 1
            elif 192.4 < random_val <= 581:
                type3 += 1

        total.append(ehp)
        if ehp > max_val:
            break

    total_days = [i for i in range(len(total))]
    plt.title('Number of EHP processors created daily with stopping')
    plt.plot(total_days, total)
    plt.show()
        
    sns.displot(total, kde=True).set(title='Distribution of Processors Created Daily with Early Stopping')
    plt.show()

def part3(days):

    # once again assuming 50 days and 37% rule for stopping
    total = []
    rewards = []

    thirty_seven_per = int(days * 0.37)
    for day in range(thirty_seven_per):

        type3 = 0
        type5 = 0
        type7 = 0
        ehp = 0
        for i in range(1000):
            random_val = random.uniform(1,1000)

            if 1 <= random_val <= 2.16:
                ehp += 1
            elif 2.16 < random_val <= 53.2:
                type7 += 1
            elif 52.3 < random_val <= 192.4:
                type5 += 1
            elif 192.4 < random_val <= 581:
                type3 += 1

            if random_val < 998:
                rewards.append(0)
            else:
                rewards.append(5000 * (random_val-997)**2)

        total.append(ehp)

    max_val = max(rewards)

    for day in range(thirty_seven_per, days, 1):
        type3 = 0
        type5 = 0
        type7 = 0
        ehp = 0
        for i in range(1000):
            random_val = random.uniform(1,1000)
            if 1 <= random_val <= 2.16:
                ehp += 1
            elif 2.16 < random_val <= 53.2:
                type7 += 1
            elif 52.3 < random_val <= 192.4:
                type5 += 1
            elif 192.4 < random_val <= 581:
                type3 += 1

            if random_val < 998:
                rewards.append(0)
            else:
                rewards.append(5000 * (random_val-997)**2)

            if rewards[-1] > max_val:
                break

        total.append(ehp)

    plt.plot(total)
    plt.title('Number of EHP chips produced by day with stopping based on reward')
    plt.show()

    plt.plot(rewards)
    plt.title('Rewards')
    plt.show()

    sns.displot(total, kde=True).set(title='Distribution of Processors Created Daily with Early Stopping')
    plt.show()

    sns.displot(rewards, kde=True).set(title='Distribution of Rewards with Early Stopping')
    plt.show()


if __name__ == '__main__':
    if 'part1' in sys.argv:
        part1(50)
    elif 'part2' in sys.argv:
        part2(50)
    elif 'part3' in sys.argv:
        part3(50)
