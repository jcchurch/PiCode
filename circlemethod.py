import random

def main():
    TOTAL_PECKS = 100000
    hits = 0
    i = 0
    while i < TOTAL_PECKS:
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1
        
        if x * x + y * y <= 1:
            hits += 1

        i += 1
    
    pi = 4.0 * float(hits) / TOTAL_PECKS
    print "Estimate Pi:", pi

main()
