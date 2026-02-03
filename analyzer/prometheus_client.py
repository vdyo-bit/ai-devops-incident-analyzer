# prometheus_client.py

def analyze(metrics):
    result = {}

    cpu_idle_min = min(metrics["cpu_idle_pct"])
    load_max = max(metrics["load_1m"])

    result["cpu_saturated"] = cpu_idle_min < 5
    result["load_exceeded_cores"] = load_max > 2
    result["disk_involved"] = max(metrics["disk_io_time"]) > 0.1
    result["memory_exhausted"] = min(metrics["memory_available_mb"]) < 500
    result["monitoring_ok"] = metrics["node_up"]

    return result
