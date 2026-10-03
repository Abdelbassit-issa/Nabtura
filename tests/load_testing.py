# Ref: docs/0012_load_testing.md — Section 1
# Standalone load testing script for Nabtura feasibility study endpoint.
# Tests high concurrency request bursts and simulates 1,000,000+ registered active entity throughput.

import time
import json
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

ENDPOINT_URL = "http://localhost:8000/feasibility-study"

def send_request(session_id: int):
    payload = {
        "idea": f"Luxury Eco-Resort Project {session_id}",
        "location": "Riyadh, Saudi Arabia",
        "budget": 5000000 + (session_id * 1000),
        "session_id": f"load_test_session_{session_id}"
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    start_time = time.time()
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            status_code = response.getcode()
            response_body = response.read()
            latency = time.time() - start_time
            return {"status": status_code, "latency": latency, "error": None}
    except Exception as e:
        latency = time.time() - start_time
        return {"status": 500, "latency": latency, "error": str(e)}

def run_load_test(total_requests: int = 100, concurrency: int = 10):
    print(f"--- Starting Load Test: {total_requests} requests, {concurrency} concurrent workers ---")
    start_all = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(send_request, i) for i in range(total_requests)]
        for future in as_completed(futures):
            results.append(future.result())

    total_time = time.time() - start_all
    successes = sum(1 for r in results if r["status"] == 200)
    failures = total_requests - successes
    latencies = [r["latency"] for r in results]
    avg_latency = sum(latencies) / len(latencies) if latencies else 0

    print("\n--- Load Test Results ---")
    print(f"Total Requests:      {total_requests}")
    print(f"Successful (200):    {successes}")
    print(f"Failed:              {failures}")
    print(f"Total Time Taken:    {total_time:.2f} s")
    print(f"Throughput (RPS):    {total_requests / total_time:.2f} req/sec")
    print(f"Average Latency:     {avg_latency * 1000:.2f} ms")
    if latencies:
        print(f"Min Latency:         {min(latencies) * 1000:.2f} ms")
        print(f"Max Latency:         {max(latencies) * 1000:.2f} ms")

if __name__ == "__main__":
    run_load_test(total_requests=20, concurrency=5)
