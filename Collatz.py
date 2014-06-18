#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r is a reader
    return a list of the two ints, otherwise a list of zeros
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

cache = [0 for x in range (1000000)]

def collatz_eval (i, j) :
    global cache

    assert i > 0
    assert j > 0

    if j < i :
        temp = i
        i = j
        j = temp
    
    cache[0] = 0
    cache[1] = 1

    max = 0
    count = 0
    for t in range (i, j+1) :
        count = 0
        if cache[t] != 0 :
            count = cache[t]

        else :  #t is not in the cache
            t2 = t;
            while t > 1:
                if t % 2 == 0 :
                    t //= 2
                    count += 1
                else :
                    t = t + (t >> 1) + 1
                    count += 2

                if t < 1000000 and cache[t] != 0 :
                    count += cache[t]
                    break
            t = t2
            cache[t] = count

        if count > max :
            max = count
    
    assert max > 0
    return max

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
