import os
import time
import psutil
import subprocess
from datetime import datetime

class ChaosToolkit:
    def __init__(self, log_file="chaos.log"):
        self.log_file = log_file

    def log(self, message):
        with open(self.log_file, "a") as f:
            f.write(f"{datetime.now()} - {message}\n")
            

def simulate_network_latency(self, delay_ms, duration_sec):
    """Simulate network latency by using the 'tc' command."""
    self.log(f"Simulating {delay_ms}ms network latency for {duration_sec} seconds.")
    
    # Add network latency
    command = f"sudo tc qdisc add dev eth0 root netem delay {delay_ms}ms"
    subprocess.call(command, shell=True)
    
    # Wait for the specified duration
    time.sleep(duration_sec)
    
    # Remove the added latency
    command = "sudo tc qdisc del dev eth0 root netem"
    subprocess.call(command, shell=True)
    
    self.log("Network latency simulation ended.")
