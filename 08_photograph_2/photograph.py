from collections import Counter, deque


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int, v: bool = False) -> int:

    total_photograph = 0
    # from left to right
    counter_a = getCounterA(N, C, X, Y)
    total_photograph += getCounterB(counter_a, N, C, X, Y)

    # from right to left
    counter_a_reverse = getCounterA(N, C, X, Y, reverse=True)
    total_photograph += getCounterB(counter_a_reverse, N, C, X, Y, reverse=True)

    return total_photograph


def getCounterA(N, C, X, Y, reverse=False):

    if X > 1:
        q_p_waiting = deque(maxlen=X-1)

    if Y > X:
        q_p = deque(maxlen=Y-X+1)
    
    counter_a = Counter()
    n_current_p = 0
    
    _range = range(N) if not reverse else range(N-1, -1, -1)

    for idx in _range:

        c = C[idx]

        idx_p = None
        if c == "P":
            idx_p = idx
        
        if c == "A":
            counter_a[idx] = n_current_p
        
        # waiting Q
        if X > 1:
            
            idx_p_pop_waiting = None

            if len(q_p_waiting) == q_p_waiting.maxlen:
                idx_p_pop_waiting = q_p_waiting.pop()
                if not idx_p_pop_waiting is None:
                    n_current_p += 1
            q_p_waiting.appendleft(idx_p)
            
            # Q
            if Y > X:

                if len(q_p) == q_p.maxlen:
                    idx_p_pop = q_p.pop()
                    if not idx_p_pop is None:
                        n_current_p -= 1
                q_p.appendleft(idx_p_pop_waiting)
            
            # X = Y
            # No Q
            else:
                if idx_p_pop_waiting is None:
                    n_current_p = 0

        # X = 1
        # no waiting Q
        else:
            
            if not idx_p is None:
                n_current_p += 1

            # Q
            if Y > X:

                if len(q_p) == q_p.maxlen:
                    idx_p_pop = q_p.pop()
                    if not idx_p_pop is None:
                        n_current_p -= 1
                q_p.appendleft(idx_p)
            
            # X = Y = 1
            # No Q
            else:
                if idx_p is None:
                    n_current_p = 0

    return counter_a


def getCounterB(counter_a, N, C, X, Y, reverse=False):
    
    if X > 1:
        q_a_waiting = deque(maxlen=X-1)

    if Y > X:
        q_a = deque(maxlen=Y-X+1)

    total_photograph = 0
    n_current_a = 0

    _range = range(N) if not reverse else range(N-1, -1, -1)

    for idx in _range:

        c = C[idx]

        idx_a = None

        if c == "A":
            idx_a = idx

        if c == "B":
            total_photograph += n_current_a

        # waiting Q
        if X > 1:

            idx_a_pop_waiting = None
            if len(q_a_waiting) == q_a_waiting.maxlen:
                idx_a_pop_waiting = q_a_waiting.pop()
                if not idx_a_pop_waiting is None:
                    n_current_a += counter_a[idx_a_pop_waiting]
            q_a_waiting.appendleft(idx_a)
            
            # Q
            if Y > X:
                if len(q_a) == q_a.maxlen:
                    idx_a_pop = q_a.pop()
                    if not idx_a_pop is None:
                        n_current_a -= counter_a[idx_a_pop]
                q_a.appendleft(idx_a_pop_waiting)
            
            # X = Y
            # No Q
            else:
                if idx_a_pop_waiting is None:
                    n_current_a = 0

        # X = 1
        # no waiting Q
        else:
            
            if not idx_a is None:
                n_current_a += counter_a[idx_a]

            # Q
            if Y > X:
                if len(q_a) == q_a.maxlen:
                    idx_a_pop = q_a.pop()
                    if not idx_a_pop is None:
                        n_current_a -= counter_a[idx_a_pop]
                q_a.appendleft(idx_a)
            
            # X = Y = 1
            # No Q
            else:
                if idx_a is None:
                    n_current_a = 0

    return total_photograph
