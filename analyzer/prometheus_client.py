def analyze_metrics(metrics):
    cpu_idle = metrics["cpu_idle_pct"]
    load = metrics["load_1m"]
    memory = metrics["memory_available_mb"]
    disk = metrics["disk_io_time"]
    node_up = metrics["node_up"]

    result = {}

    result["cpu_saturated"] = min(cpu_idle) < 5
    result["load_high"] = max(load) > metrics["cpu_cores"]
    result["memory_pressure"] = min(memory) < 500
    result["disk_pressure"] = max(disk) > 0.1
    result["monitoring_available"] = node_up

    return result


