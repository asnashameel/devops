import multiprocessing

def cpu_load():
    while True:
        pass  # Infinite loop to keep CPU busy

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Get the number of CPU cores
    print(f"Starting {num_cores} CPU-intensive processes...")
    
    processes = [multiprocessing.Process(target=cpu_load) for _ in range(num_cores)]
    
    for p in processes:
        p.start()

    for p in processes:
        p.join()  # Keep the processes running
