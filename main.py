from dijkstra_solution import read_csv, build_graph, dijkstra

def main():
    # CSV file
    data = read_csv('routes.csv')

    # xtizw grafo
    graph = build_graph(data)
    print('Enter the starting location and the destination you want to travel to.')
    print("From: (UPPERCASE ONLY)")
    start_city = input().strip().upper()
    print("To: (UPPERCASE ONLY)")
    end_city = input().strip().upper()

    # validate
    if start_city not in graph:
        print(f"The location '{start_city}', you want to start from, doesn't exist.")
        return
    if end_city not in graph:
        print(f"The location '{end_city}' doesn't exist.")
        return
    
    #by time
    shortest_time, path_time, travel_mode_path1 = dijkstra(graph, start_city, end_city, weight_type="time")
    if path_time:
        print(f"Shortest path by time: {path_time} with total time {shortest_time}")
        print(f"To travel from {start_city} to {end_city} you have to take: {travel_mode_path1} ")
    else:
        print(f"No path found between {start_city} and {end_city} by time.")

    #by cost (proairetika)
    shortest_cost, path_cost, travel_mode_path2= dijkstra(graph, start_city, end_city, weight_type="cost")
    if path_cost:
        print(f"Shortest path by cost: {path_cost} with total cost {shortest_cost}")
        print(f"To travel from {start_city} to {end_city} you have to take: {travel_mode_path2} ")
    else:
        print(f"No path found between {start_city} and {end_city} by cost.")


if __name__ == "__main__":
    main()
