import csv
import random

random.seed(42)

rows = []

def add_rows(count, packet_rate, packet_size, connections, failed, duration, label):
    for _ in range(count):
        rows.append([
            random.randint(*packet_rate),
            random.randint(*packet_size),
            random.randint(*connections),
            random.randint(*failed),
            random.randint(*duration),
            label
        ])

add_rows(100, (80, 300), (400, 900), (5, 25), (0, 2), (50, 100), "normal")

add_rows(100, (3000, 10000), (60, 200), (500, 2000), (300, 1500), (3, 15), "ddos")

add_rows(100, (1500, 5000), (100, 400), (100, 600), (50, 300), (5, 30), "dos")

add_rows(100, (100, 500), (100, 500), (20, 100), (50, 200), (10, 60), "brute_force")

add_rows(100, (100, 800), (40, 200), (100, 1000), (10, 100), (5, 40), "port_scan")

add_rows(100, (500, 3000), (100, 700), (50, 500), (20, 200), (10, 50), "botnet")

add_rows(100, (200, 1500), (100, 600), (30, 300), (10, 100), (10, 60), "web_attack")

add_rows(100, (200, 2000), (100, 700), (40, 400), (20, 150), (10, 60), "infiltration")

random.shuffle(rows)

with open("data/network_traffic.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "packet_rate",
        "packet_size",
        "connection_count",
        "failed_connections",
        "traffic_duration",
        "label"
    ])

    writer.writerows(rows)

print("Dataset created successfully!")
print("Total records:", len(rows))
