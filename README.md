# Chaos Engineering Toolkit

## Overview

The Chaos Engineering Toolkit is a Python-based tool designed to help engineers simulate various failure scenarios in a live system. The primary goal of this toolkit is to test the resilience of systems, verify the effectiveness of fallback mechanisms, and identify potential weaknesses before they manifest in a production environment.

This toolkit allows you to simulate different failure conditions such as network latency, service crashes, CPU and memory exhaustion, disk I/O overload, DNS failures, database disconnections, and API throttling. By using this toolkit, you can better understand how your system behaves under stress and improve its robustness.

## Features

- **Network Latency Simulation**: Introduce artificial delays in network communication.
- **Service Crashes**: Randomly stop and restart services to simulate crashes.
- **Resource Exhaustion**: Max out CPU or memory usage to simulate resource exhaustion.
- **Disk I/O Saturation**: Overload disk I/O operations to test performance under heavy load.
- **DNS Failures**: Simulate DNS failures by modifying the `/etc/hosts` file.
- **Database Disconnections**: Temporarily disconnect a database service to test how the system handles database unavailability.
- **API Throttling**: Limit the number of API requests to simulate throttling scenarios.

## Project Structure

```plaintext
chaos_engineering_toolkit/
│
├── chaos_toolkit.py           # Main script containing the ChaosToolkit class and scenarios
├── README.md                  # Project documentation and usage instructions
├── requirements.txt           # List of required Python libraries
├── chaos.log                  # Log file where all actions are recorded
└── tests/
    └── test_chaos_toolkit.py  # Unit tests for the toolkit
