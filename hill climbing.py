def hill_climbing(start):
    current = start

    while True:
        neighbors = [current - 1, current + 1]
        best = max(neighbors, key=lambda x: -(x - 5) ** 2)

        if -(best - 5) ** 2 <= -(current - 5) ** 2:
            break

        current = best
        print("Current State:", current)

    return current

start = int(input("Enter starting value: "))

result = hill_climbing(start)

print("Final Solution:", result)
