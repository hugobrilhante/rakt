import multiprocessing

# Bind to 0.0.0.0:8000 (accept connections from outside the container)
bind = "0.0.0.0:8000"

# Number of workers based on available CPUs in the container
workers = multiprocessing.cpu_count() * 2 + 1

# Worker class selection based on application type (asynchronous or not)
worker_class = "gthread"  # Or 'gevent' for asynchronous applications

# Threads per worker for I/O intensive operations
threads = 4

# Timeout for requests
timeout = 30

# Log file directed to standard output (stdout)
log_file = "-"

# Worker temporary directory for better performance
worker_tmp_dir = "/dev/shm"
