'''
Project Name: Human Pyramid
Author Name: Nolen Shubin
Due Date: 09/26/2021
Course: CS1410-003

Using the user input from the command line (ex. python3 pyramid.py 8 (the 8 is the extra 
parameter passed before the file is executed)), the propgram takes the number passed as 
the size of the pyramid then creates a file to outputthe weight each person in the 
pyramid has to bear. 

This program uses recursive functions and dictionaries to execute its objective, later 
saved in a .txt file. The program's performance was exceeded by 25% in time, 48% in 
function calls, and 22% in calls to the cache with the addition of 3 lines of code. 
Instead of saving the weight for one oerson at a time, I save the same weight that 2
people share in the pyramid.
'''
import math, sys
from time import perf_counter

def main():
    # Declare counter and global pyramid variables
    row = sys.argv[1]
    cache = {}
    cacheHits = 0
    funcHits = 0
    w = 200

    # Find weight-bearing of that specific person (part2.txt)
    def weight_on(r, c, f=0, ch=0):
        key = (r, c)
        mirror = (r, r-c)
        s = 0
        print(key, mirror)
        if cache.get(key, False):
            ch += 1
            return [cache[key], f, ch]
        else:
            f += 1
            # If it is the first person on top of the pyramid
            if r == 0:
                cache[key] = s
                return [s, f, ch]
            #If the person is on the very left of the row
            elif c == 0 and c < r:
                r1 = weight_on(r-1, c, f, ch)
                n1 = r1[0] + w
                s = round(n1 / 2, 2)
                #Save in cache that person and the very right person as well
                cache[key] = s
                cache[mirror] = s
                f += r1[1]
                ch += r1[2]
                return [s, f, ch]
            elif c == r and r != 0:
                r1 = weight_on(r-1, c-1, f, ch)
                n1 = r1[0] + w
                s = round(n1 / 2, 2)
                #Save in cache that person and the right person as well
                cache[key] = s
                cache[mirror] = s
                f += r1[1]
                ch += r1[2]
                return [s, f, ch]
            else:
                r1 = weight_on(r-1, c-1, f, ch)
                r2 = weight_on(r-1, c, f, ch)
                n1 = r1[0] + w
                n2 = r2[0] + w
                s = round((n1 + n2) / 2, 2)
                #Save in cache that person and the right person as well
                cache[key] = s
                cache[mirror] = s
                f += r1[1] + r2[1]
                ch += r1[2] + r2[2]
                return [s, f, ch]

    # Start the timer, count the function/cache recursions, and print pyramid
    file1 = open("part2.txt", "w")

    #Part 2
    start = perf_counter()
    for r in range(int(row) + 1):
        line = ''
        for c in range(int(r) + 1):
            results = weight_on(r, c)
            line += str(results[0]) + ' '
            funcHits += results[1]
            cacheHits += results[2]
        file1.write(line + '\n')
    # Stop the timer and print results
    stop = perf_counter()
    timeStamp = "Time Elapsed: " + str(stop - start)
    
    # Write the times to part2.txt file
    file1.write(timeStamp + "\nNumber of function calls: " + str(funcHits) + "\nNumber of cache hits: " + str(cacheHits))
    file1.close()
            



if __name__ == "__main__":
    main()