import csv
import heapq

#read data from a CSV file
def read_csv(filename):
    csv_data = []
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 5:  # Skip rows i dont want (mikroteres tou epithimitou mikous)
                print(f"Skipping row: {row}") 
                continue
            #gia kanonikopoihsh twn from_city kai to_city row[0].strip().upper()
            from_city = row[0].strip().upper()
            to_city = row[1].strip().upper()
            travel_mode = row[2].strip()
            time = float(row[3])
            cost = float(row[4])
            csv_data.append((from_city, to_city, travel_mode, time, cost))
    return csv_data


# xtizw ton grafo
def build_graph(data):
    graph = {}
    for from_city, to_city, travel_mode, time, cost in data:
        if from_city not in graph:
            graph[from_city] = []
        if to_city not in graph:
            graph[to_city] = []
        graph[from_city].append((to_city, travel_mode, time, cost))
        graph[to_city].append((from_city, travel_mode, time, cost))  #undirected graph
    # print(graph)
    return graph


# Dijkstra's Algorithm
def dijkstra(graph, start, end, weight_type="time"):
    pq = [(0, start, [], [])]  # Pqueue: (accumulated_weight, current_city, path, travel_path)
    visited = set()
    
    while pq:
        accumulated_weight, current_city, path, travel_mode_path = heapq.heappop(pq)
        
        # elegxw an exw episkefthei
        if current_city in visited:
            continue

        visited.add(current_city)
        path = path + [current_city]
        if current_city == end:
            return accumulated_weight, path, travel_mode_path
            
        for neighbor, travel_mode, time, cost in graph[current_city]:
            if neighbor not in visited:
                weight = time if weight_type == "time" else cost
                heapq.heappush(pq, (accumulated_weight + weight, neighbor, path, travel_mode_path + [travel_mode]))
    
    return float("inf"), []  #an den vrw path epistrefw inf & empty path
