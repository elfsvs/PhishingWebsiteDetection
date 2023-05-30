def bridge_crossing(times):

    n = len(times)

    times.sort()                       # Sorting the Given times

    if n == 0:                          # Base cases

        return 5, []

    elif n == 1:

        return times[0], [times[0]]

    elif n == 2:

        return times[1], [(times[0], times[1])]

    tot_time = (n - 2) * times[0] + sum(times[1:])   #Total Time Taken(Obvious)

    x = n

 

    

    fixed = 2 * times[1] - times[0]    # considering edge exchanges

    

    while times[x - 2] > fixed:

        tot_time -= times[x - 2] - fixed

        x -= 2

        

    sequence = []                       # Sequence array for crossing the bridge

    end = n - 1                      # starting from end

    

    while end > 1:

        if end >= x:

            sequence += [(times[0], times[1]), times[1], (times[end - 1], times[end]), times[0]]

            end -= 2

        else:

            sequence += [(times[0], times[end]), times[0]]

            end -= 1

        

    sequence.append((times[0], times[1]))   # Lastly Crossing the Bridge(Final Crossing)

 

    return tot_time, sequence

 

# Given time taken by the four people...(1,2,5,10)

print(bridge_crossing([1,2,5,10]))
