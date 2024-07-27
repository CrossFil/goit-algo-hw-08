import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    
    total_cost = 0
    combination_order = []

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        combined = first + second
        total_cost += combined

        heapq.heappush(cables, combined)

        combination_order.append((first, second))
    
    return total_cost, combination_order

cables = [4, 3, 2, 6]
total_cost, combination_order = min_cost_to_connect_cables(cables)

print("The minimum cost to connect all cables is:", total_cost)
print("The order of combinations is:")
for pair in combination_order:
    print(f"Combine cables of length {pair[0]} and {pair[1]}")
