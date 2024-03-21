Luke Arnold, a02368233, Algorithms Under Uncertainty Midterm
============================================================

Processor Binning
----------------------------------------

Mineral Samples and Geological Surveys
----------------------------------------

   *   Part 1:

    -   The run the code to see the graphs for part 1, simply run

        `python MineralSamples.py part1`

        This will run the simulation and print out the graphs. 

        The simulation simply consists of a for loop incrementing from 1 to 24. At each loop the simulation 
        finds a value for each site dependent on the specified dsitributions given in the prompt, and appends these
        values to a list. There are 10 lists for each 10 sites. 

        After the 24 loops are calculated, the values are plotted and graphed.

   *   Part 2:

    -   The implementation of the epsilon greedy is slightly different in part 2 than it was in the multiarmed bandit assignment.\

        Because there are so many sites, and so many of them could potentially be profitable, I didn't want to isolate attention on soley the best performing sites, and as as result ignore
        other potentially profitable sites.

        Therefore, instead of isolating attention on the best performing site, I gave attention to the 5 best performing sites initially, and allowed the algorithm to slowly converge onto a smaller batch of sites. 

        Each month, the algorithm randomly determined a value of epsilon, if it was less than the specified value of epsilon, 5 random sites were chosen and they each performed two draws (with a total of 10 teams of work). 
        The average output was then calculated for all of these locations.

        If the value was greater than epsilon, the algoritm had the five preselected sites perform two draws each (once again a total of 10 teams work). These five preselected sites ware determined from an initital draw.

        Following each simulation, the algorithm would reapportion attention to each site, checking the five worst performing locations (based on average output), removing a team and giving these teams to the five best
        performing locations. Therefore, even though initially only 5 of the sites had teams, after the first month its possible that any number of sites could have work performed.

        As the algorithm continued, the attention placed on sites converges closer to a batch of well performing locations. The specific attention given to each sites varies, but usually a single site 
        is converged upon with either 4 - 7 teams focusing on it. 

    -   To run the simulation for part 2, simply run 

        `python MineralSamples.py part2`

        Once this code it run it will display two graphs, one will show to average performance of each site, the second shows the number of teams at each site per month.

   *   Part 3:

    -   Part 3 works in the same way as part 2, however of course the attention given to each site is locked in with one team per location up until month 6. 

    -   What I noticed is that following month 6, the sites converge to their respective number of teams almost immediately. Though, sometimes different sites get priority
        as opposed to part 2. It seems that allowing a larger group of averages to be determined before shifting teams provides a better metric as it allows a more 
        accurate average to be determined before certain sites are ignored

   *   Part 4:

    -   Sites should be opened a location 10, and location 6. With both simulations these most often converge as the best locatations for optimal profit when mining.
        This can be determined relatively quickly, with convergence being determined usually around month 8 of the 24 month study. From there other less optimal sites will vary, but the top
        performing ones are relatively stagnant. 

        On some simulations, other locations rather than 10 and 6 may perform better. But with most simulations I've ran sites 10 and 6 are the optimal choices. 



    
