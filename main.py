from dijkstra_solution import read_csv, build_graph, dijkstra

# Execution
def main():
    # Read data from the CSV file
    data = read_csv('routes.csv')

    # Build the graph
    graph = build_graph(data)
    print('Enter the starting location and the destination you want to travel to.')
    # Get start and end cities from user input
    print("From: (UPPERCASE ONLY)")
    start_city = input().strip().upper()
    print("To: (UPPERCASE ONLY)")
    end_city = input().strip().upper()

    # Validate input
    if start_city not in graph:
        print(f"The location '{start_city}', you want to start from, doesn't exist.")
        return
    if end_city not in graph:
        print(f"The location '{end_city}' doesn't exist.")
        return
    
    # Find shortest path by time
    shortest_time, path_time = dijkstra(graph, start_city, end_city, weight_type="time")
    if path_time:
        print(f"Shortest path by time: {path_time} with total time {shortest_time}")
    else:
        print(f"No path found between {start_city} and {end_city} by time.")

    # Find shortest path by cost
    shortest_cost, path_cost = dijkstra(graph, start_city, end_city, weight_type="cost")
    if path_cost:
        print(f"Shortest path by cost: {path_cost} with total cost {shortest_cost}")
    else:
        print(f"No path found between {start_city} and {end_city} by cost.")


if __name__ == "__main__":
    main()
