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
def kill_service(self, service_name):
    """Simulate a service crash by killing the process."""
    self.log(f"Killing service: {service_name}")
    
    # Stop the service
    command = f"sudo systemctl stop {service_name}"
    subprocess.call(command, shell=True)
    
    # Simulate downtime
    time.sleep(5)
    
    # Restart the service
    command = f"sudo systemctl start {service_name}"
    subprocess.call(command, shell=True)
    
    self.log(f"Service {service_name} restarted.")
    
def stress_cpu(self, duration_sec, load_percent=100):
        """Simulate CPU resource exhaustion by stressing the CPU."""
        self.log(f"Stressing CPU for {duration_sec} seconds with {load_percent}% load.")
        
        # Use stress-ng to stress the CPU
        command = f"stress-ng --cpu 1 --cpu-load {load_percent} --timeout {duration_sec}s"
        subprocess.call(command, shell=True)
        
        self.log("CPU stress simulation ended.")
def saturate_disk_io(self, duration_sec):
        """Simulate heavy disk I/O by repeatedly writing and deleting a file."""
        self.log(f"Saturating Disk I/O for {duration_sec} seconds.")
        end_time = time.time() + duration_sec
        while time.time() < end_time:
            with open('temp_io_test_file', 'wb') as f:
                f.write(os.urandom(10**6))  # Write 1MB of random data
            os.remove('temp_io_test_file')
        self.log("Disk I/O saturation simulation ended.")
def simulate_dns_failure(self, domain, duration_sec):
        """Simulate DNS failure by modifying the /etc/hosts file."""
        self.log(f"Simulating DNS failure for {domain} for {duration_sec} seconds.")
        with open('/etc/hosts', 'a') as f:
            f.write(f"127.0.0.1 {domain}\n")
        time.sleep(duration_sec)
        with open('/etc/hosts', 'r') as f:
            lines = f.readlines()
        with open('/etc/hosts', 'w') as f:
            for line in lines:
                if domain not in line:
                    f.write(line)
        self.log(f"DNS failure simulation for {domain} ended.")
        
def disconnect_database(self, db_service_name, duration_sec):
        """Temporarily disconnect a database service."""
        self.log(f"Disconnecting database service: {db_service_name} for {duration_sec} seconds.")
        os.system(f"sudo systemctl stop {db_service_name}")
        time.sleep(duration_sec)
        os.system(f"sudo systemctl start {db_service_name}")
        self.log(f"Database service {db_service_name} reconnected.")