import csv
import heapq

def read_csv(filename):
    csv_data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            from_city = row[0]
            # .strip().upper()  # Normalize city names
            to_city = row[1]
            # .strip().upper()   # Normalize city names
            travel_mode = row[2]
            time = float(row[3])
            cost = float(row[4])  # Convert cost to float
            csv_data.append((from_city, to_city, travel_mode, time, cost))
    return csv_data

# Build the graph
def build_graph(data):
    graph = {}
    for from_city, to_city, travel_mode, time, cost in data:
        if from_city not in graph:
            graph[from_city] = []
        if to_city not in graph:
            graph[to_city] = []
        graph[from_city].append((to_city, travel_mode, time, cost))
        graph[to_city].append((from_city, travel_mode, time, cost))  # Assuming undirected graph
    #print("Graph:", graph) 
    return graph
    
# Dijkstra's Algorithm
def dijkstra(graph, start, end, weight_type="time"):
    pq = [(0, start, [])]
    visited = set()
    
    while pq:
        accumulated_weight, current_city, path = heapq.heappop(pq)
        
        if current_city in visited:
            continue
        
        visited.add(current_city)
        path = path + [current_city]
        
        if current_city == end:
            return accumulated_weight, path
        
        for neighbor, travel_mode, time, cost in graph[current_city]:
            if neighbor not in visited:
                weight = time if weight_type == "time" else cost
                heapq.heappush(pq, (accumulated_weight + weight, neighbor, path))
    
    return float("inf"), []

# Execution
data = read_csv('testing_routes.csv')
graph = build_graph(data)

# start_city = "ATHENS"
# end_city = "LONDON"
print("From: ")
start_city = input()
print("To: ")
end_city = input()
if start_city not in graph:
    print(f"The location '{start_city}', you want to start from, doesnt exist.")
    exit()
if end_city not in graph:
    print(f"The location '{end_city}' doesnt exist")
    exit()

shortest_time, path_time = dijkstra(graph, start_city, end_city, weight_type="time")
print(f"Shortest path by time: {path_time} with total time {shortest_time}")

shortest_cost, path_cost = dijkstra(graph, start_city, end_city, weight_type="cost")
print(f"Shortest path by cost: {path_cost} with total cost {shortest_cost}")
