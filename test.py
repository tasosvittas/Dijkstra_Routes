import csv
import heapq
import sys
sys.stdout.reconfigure(encoding='utf-8')
class Graph:
    def __init__(self):
        # Αποθήκευση του γράφου ως dictionary of lists
        self.graph = {}

    def add_edge(self, from_city, to_city, time):
        # Προσθήκη ακμής με το χρόνο ως βάρος
        if from_city not in self.graph:
            self.graph[from_city] = []
        self.graph[from_city].append((to_city, time))

        # Αν ο γράφος είναι μη κατευθυνόμενος, προσθέτουμε και την αντίστροφη διαδρομή
        if to_city not in self.graph:
            self.graph[to_city] = []
        self.graph[to_city].append((from_city, time))

    def dijkstra(self, start, end):
        # Αρχικοποίηση των αποστάσεων
        distances = {city: float('inf') for city in self.graph}
        distances[start] = 0

        # Προτεραιότητα με heap queue
        priority_queue = [(0, start)]

        # Προηγούμενοι κόμβοι για ανίχνευση της διαδρομής
        previous_nodes = {city: None for city in self.graph}

        while priority_queue:
            current_distance, current_city = heapq.heappop(priority_queue)

            # Αν φτάσουμε στον στόχο, σταματάμε
            if current_city == end:
                break

            # Εξετάζουμε τους γείτονες
            for neighbor, travel_time in self.graph[current_city]:
                distance = current_distance + travel_time

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_city
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Ανίχνευση της διαδρομής
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path = path[::-1]  # Αναστροφή της διαδρομής

        return distances[end], path if distances[end] != float('inf') else None

# Φόρτωση δεδομένων από CSV και κατασκευή του γράφου
def load_graph_from_csv(filename):
    graph = Graph()
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            from_city = row[0]
            to_city = row[1]
            travel_mode = row[2]
            time = float(row[3])  # Μετατροπή του χρόνου σε δεκαδικό αριθμό
            # Προσθήκη ακμής στον γράφο μόνο για πτήσεις
            if travel_mode == "plane":
                graph.add_edge(from_city, to_city, time)
    return graph

# Παράδειγμα χρήσης
filename = 'routes.csv'  # Αντικατέστησε με το όνομα του αρχείου CSV
graph = load_graph_from_csv(filename)

start_city = 'India'
end_city = 'Guatemala'
distance, path = graph.dijkstra(start_city, end_city)

if path:
    print(f"Η συντομότερη απόσταση από την πόλη {start_city} στην πόλη {end_city} είναι {distance} ώρες και η διαδρομή είναι {' -> '.join(path)}.")
else:
    print(f"Δεν υπάρχει διαδρομή από την πόλη {start_city} στην πόλη {end_city}.")
