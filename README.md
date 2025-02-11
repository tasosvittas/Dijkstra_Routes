# Dijkstra Routes

## Overview
This project implements **Dijkstra's algorithm** to find the shortest path between locations using real-world routing data. It processes transport connections between various nodes (cities, airports, etc.) and calculates the optimal routes based on different parameters such as **travel time** and **cost**.

## Dataset
The algorithm uses **routes.csv**, which contains the following key fields:
- **source**: The starting location (city, airport, etc.).
- **destination**: The destination location.
- **type**: The type of transport (e.g., boat, bus, plane, train, truck).
- **time**: The travel time for the connection.
- **cost**: The cost of the transport.

## Implementation
The project is implemented in Python and includes:
- `dijkstra_solution.py`: Implements **Dijkstra's algorithm** to compute the shortest path.
- `main.py`: Handles data input, processing, and route calculation.
- `routes.csv` and `testing_routes.csv`: Contain sample data for testing the algorithm.

## Usage
1. Run `main.py` to load the dataset and compute the shortest routes.
2. The program outputs the most efficient route based on travel time and cost.

## Output
![image](https://github.com/user-attachments/assets/74b5fb17-9c91-4314-aced-77fb26389394)
![image](https://github.com/user-attachments/assets/6f2b5ca4-be00-4d64-8cda-235fb67fc38b)
![image](https://github.com/user-attachments/assets/f1d5c07a-4d16-4a01-8ccf-a7d0b5e970dc)
