import pandas as pd
import heapq
import sys
sys.stdout.reconfigure(encoding='utf-8')
# Load the CSV file, specifying only the first five columns
df = pd.read_csv('routes.csv', usecols=[0, 1, 2, 3, 4], header=None)

# Display the result
print(df)



class Graph:
    def __init__(self):
        # Αποθηκεύουμε τον γράφο ως dictionary of lists, όπου κάθε κόμβος έχει λίστα από γειτονικούς κόμβους και βάρη.
        self.graph = {}

    def add_edge(self, from_node, to_node, weight):
        # Προσθέτουμε το βάρος για το μονοπάτι από τον from_node στον to_node
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append((to_node, weight))

        # Αν ο γράφος είναι μη κατευθυνόμενος, προσθέτουμε και την αντίστροφη διαδρομή
        if to_node not in self.graph:
            self.graph[to_node] = []
        self.graph[to_node].append((from_node, weight))

    def dijkstra(self, start, end):
        # Αρχικοποιούμε τις αποστάσεις με το άπειρο
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        # Προτεραιότητα με χρήση heapq
        priority_queue = [(0, start)]

        # Προηγούμενοι κόμβοι για την ανίχνευση της διαδρομής
        previous_nodes = {node: None for node in self.graph}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Αν φτάσουμε στον στόχο, σταματάμε
            if current_node == end:
                break

            # Επεξεργαζόμαστε τους γείτονες του τρέχοντος κόμβου
            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight

                # Εάν βρούμε μια πιο σύντομη διαδρομή προς τον γείτονα
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Εύρεση της συντομότερης διαδρομής αναδρομικά μέσω των προηγούμενων κόμβων
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path = path[::-1]  # Αναστρέφουμε τη διαδρομή

        return distances[end], path if distances[end] != float('inf') else None

# Παράδειγμα χρήσης
graph = Graph()
graph.add_edge('A', 'B', 4)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'C', 5)
graph.add_edge('B', 'D', 10)
graph.add_edge('C', 'D', 3)

start_node = 'A'
end_node = 'D'
distance, path = graph.dijkstra(start_node, end_node)

if path:
    print(f"Η συντομότερη απόσταση από τον κόμβο {start_node} στον κόμβο {end_node} είναι {distance} και η διαδρομή είναι {' -> '.join(path)}.")
else:
    print(f"Δεν υπάρχει διαδρομή από τον κόμβο {start_node} στον κόμβο {end_node}.")
