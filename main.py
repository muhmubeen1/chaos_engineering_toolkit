from chaos_toolkit import ChaosToolkit

def main():
    toolkit = ChaosToolkit()

    # Simulate network latency
    print("Simulating network latency...")
    toolkit.simulate_network_latency(delay_ms=100, duration_sec=10)

    # Kill and restart a service
    print("Killing and restarting service...")
    toolkit.kill_service(service_name="nginx")

    # Stress the CPU
    print("Stressing the CPU...")
    toolkit.stress_cpu(duration_sec=15)

    # Simulate Disk I/O Saturation
    print("Saturating Disk I/O...")
    toolkit.saturate_disk_io(duration_sec=30)

    # Simulate DNS failure
    print("Simulating DNS failure...")
    toolkit.simulate_dns_failure(domain="example.com", duration_sec=20)

    # Disconnect a database
    print("Disconnecting database service...")
    toolkit.disconnect_database(db_service_name="mysql", duration_sec=15)

    # Throttle API
    print("Simulating API throttling...")
    toolkit.throttle_api(endpoint="http://api.example.com", max_requests=10, duration_sec=60)

    print("Chaos engineering scenarios completed.")

if __name__ == "__main__":
    main()
