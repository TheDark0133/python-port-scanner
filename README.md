# Python Port Scanner (Multi-Thread)

A fast and lightweight port scanner written in Python. 
I developed this personal project to put networking concepts (TCP/IP suite) into practice and to learn how to handle concurrent execution (multithreading) in Python.

## Features
* TCP port scanning using the native `socket` library.
* Utilization of `ThreadPoolExecutor` to test multiple ports concurrently (avoiding the bottlenecks of synchronous loops).
* Clean Command-Line Interface (CLI) built with `argparse`.

## Usage
It requires no external libraries or special installations; it relies entirely on the Python 3 standard library.

```bash
# Default scan (first 1024 ports)
python3 scanner.py -t 192.168.1.1

# Custom scan (e.g., first 100 ports)
python3 scanner.py -t 192.168.1.1 -p 100

##  What I Learned
Writing this tool from scratch forced me to study what happens "under the hood" of a network connection:
* **Sockets & Protocols:** I worked with `AF_INET` (IPv4) and `SOCK_STREAM`, experiencing firsthand how the TCP protocol establishes a real connection (3-way handshake), unlike UDP.
* **Timeout Management:** I learned that networking is all about trade-offs. I set a 0.5s timeout on the sockets to prevent the script from hanging on dropped packets or firewalls silently discarding requests.
* **Multithreading:** Initially, I wrote a simple `for` loop, but network latency made it unusable. Implementing `concurrent.futures` taught me how to manage a worker pool, balancing CPU usage and speeding up the scan by 90%.

## Known Issues & TODOs
This project is a work in progress. Upcoming features I plan to work on:
- [ ] Add "Banner Grabbing" to identify the service version listening, not just port status.
- [ ] Implement DNS resolution error handling in case the user inputs a hostname instead of a direct IP.
- [ ] Exportable output (e.g., save the report to a .txt or .csv file).
