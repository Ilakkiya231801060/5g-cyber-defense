import csv
import random

random.seed(42)

rows = []

for _ in range(50):
    rows.append([
        random.randint(80, 300),
        random.randint(400, 900),
        random.randint(5, 25),
        random.randint(0, 2),
        random.randint(50, 100),
        "normal"
    ])

for _ in range(30):
    rows.append([
        random.randint(3000, 10000),
        random.randint(60, 200),
        random.randint(500, 2000),
        random.randint(300, 1500),
        random.randint(3, 15),
        "ddos"
    ])

for _ in range(30):
    rows.append([
        random.randint(250, 1000),
        random.randint(100, 500),
        random.randint(25, 150),
        random.randint(10, 80),
        random.randint(15, 60),
        "abnormal"
    ])

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
