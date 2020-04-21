#! /usr/bin/python3
'''
Practice problem

Given login and logout times of users (in ints, e.g. [2, 10], [5, 8]) find the peak load interval.

Assumptions: 
- "peak load interval" is most users are logged in, and then longest such interval, and then first of that length
- time is abstract and pre-binned into int values, but otherwise cannot treat as finite
-- if time is finite, we can just make a single large hash of binned values and take the count at each timestamp. This is O(n).
- input is well-formed, i.s. always pairs of ints, logout always after login

Algo:
- sort by start and end times
- split into start and end lists
- walk through lists, checking number of users for max, and duration for max

Notes:
- sorting makes this O(n*log(n))
- sorting allows us to go through start times in order and increment user count
'''
__author__ = "Alan Au"
__date__   = "2020-04-21"

def peak_load(all_users): # list of lists
    sorted_users = sorted(all_users, key = lambda x: (x[0],x[1]))
    start = []
    end = []
    for user in sorted_users:
        start.append(user[0])
        end.append(user[1])
    
    max_s = 0
    max_e = 0
    users = 0
    max_users = 0
    duration = 0
    max_duration = 0

    i = 0 #start
    j = 0 #end

    while i < len(start): # Only track logins, because after that it's all logouts.
        time_s = start[i]
        time_e = end[j]
        duration = time_e - time_s
        if duration > 0: # If end > start
            users += 1
            if users >= max_users and duration > max_duration:
                max_s = time_s
                max_e = time_e
            i += 1
        elif duration < 0:
            user_count -= 1
            j += 1
    return([max_s, max_e])
            
if __name__ == "__main__":
    my_inputs = [[2, 10], [5, 8], [1, 6]] # Expected output: [5, 6]
    print("Inputs: {}".format(my_inputs))
    print("Peak load: {}".format(peak_load(my_inputs)))