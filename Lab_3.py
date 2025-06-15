from collections import deque
def min_steps(m, n, d):
    if d > max(m, n):
        return -1 

    q = deque([(0, 0, 0, [(0, 0)])])
    visited = [[False] * (n + 1) for _ in range(m + 1)]  
    visited[0][0] = True

    while q:
        jug1, jug2, steps, path = q.popleft()

        # Goal reached
        if jug1 == d or jug2 == d:
            for i, state in enumerate(path):
                print(f"({state[0]}, {state[1]})")
            return steps

        # Generate next possible states
        next_states = []

        # 1. Fill Jug1
        next_states.append((m, jug2))
        # 2. Fill Jug2
        next_states.append((jug1, n))
        # 3. Empty Jug1
        next_states.append((0, jug2))
        # 4. Empty Jug2
        next_states.append((jug1, 0))
        # 5. Pour Jug1 -> Jug2
        pour1to2 = min(jug1, n - jug2)
        next_states.append((jug1 - pour1to2, jug2 + pour1to2))
        # 6. Pour Jug2 -> Jug1
        pour2to1 = min(jug2, m - jug1)
        next_states.append((jug1 + pour2to1, jug2 - pour2to1))

        for new_jug1, new_jug2 in next_states:
            if not visited[new_jug1][new_jug2]:
                visited[new_jug1][new_jug2] = True
                q.append((new_jug1, new_jug2, steps + 1, path + [(new_jug1, new_jug2)]))

    print("No solution possible.")
    return -1

# jug1 = 4 litre, jug2 = 3 litre 
m, n, d = 4, 3, 2
print(min_steps(m, n, d))
