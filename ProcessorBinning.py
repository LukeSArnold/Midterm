import random
import sys
import matplotlib.pyplot as plt

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


    

if __name__ == '__main__':
    if 'part1' in sys.argv:
        part1(50)
