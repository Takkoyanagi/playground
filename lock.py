from collections import deque


def open_lock(deadends, target):
    """ determine how many moves it will
    take to arrive to the target value
    """
    # define variables
    visited = {x for x in deadends}
    start = '0000'
    que = deque()
    lvl = 0
    # add edge cases
    if start in visited or not start:
        return -1

    que.appendleft((start, lvl))
    visited.add(start)

    # bfs to build states of the lock
    while que:
        current, lvl = que.pop()
        if current == target:
            return lvl
        else:
            for neighbor in find_neighbors(current):
                if neighbor not in visited:
                    que.appendleft((neighbor, lvl+1))
                    visited.add(neighbor)

    return -1


def find_neighbors(current):
    # create helper function to get 8 neighbors
    neighbors = []
    for ind, val in enumerate(current):
        temp_up = (int(val) + 1) % 10
        temp_down = (int(val) - 1) % 10
        neighbors.append(current[:ind] + str(temp_up) + current[ind+1:])
        neighbors.append(current[:ind] + str(temp_down) + current[ind+1:])
    return neighbors


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print(open_lock(deadends, target))
