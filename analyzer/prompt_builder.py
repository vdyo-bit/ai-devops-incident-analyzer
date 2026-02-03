def build_report(analysis):
    lines = []

    if analysis["cpu_saturated"]:
        lines.append("CPU saturation detected (CPU idle dropped below 5%).")
    else:
        lines.append("No CPU saturation detected.")

    if analysis["load_high"]:
        lines.append("Load average exceeded available CPU cores.")
    else:
        lines.append("Load average remained within CPU capacity.")

    if analysis["memory_pressure"]:
        lines.append("Memory pressure observed (low available memory).")
    else:
        lines.append("Memory pressure not observed.")

    if analysis["disk_pressure"]:
        lines.append("Disk I/O pressure observed.")
    else:
        lines.append("Disk I/O was not a bottleneck.")

    if analysis["monitoring_available"]:
        lines.append("Monitoring remained available throughout the incident.")
    else:
        lines.append("Monitoring availability was impacted.")

    return "\n".join(lines)
