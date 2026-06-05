# analyzer/incident_classifier.py

class IncidentClassifier:

    def classify(self, incident_data):

        # Kubernetes incidents

        if incident_data.get("last_state") == "OOMKilled":
            return {
                "incident_type": "kubernetes_oomkilled",
                "confidence": 0.98,
                "reason": "Container exceeded memory limit"
            }

        if incident_data.get("pod_status") == "CrashLoopBackOff":
            return {
                "incident_type": "kubernetes_crashloopbackoff",
                "confidence": 0.95,
                "reason": "Container repeatedly crashed"
            }

        if incident_data.get("pod_status") == "ImagePullBackOff":
            return {
                "incident_type": "kubernetes_imagepullbackoff",
                "confidence": 0.99,
                "reason": "Container image could not be pulled"
            }

        # Linux incidents

        if incident_data.get("cpu_saturated"):
            return {
                "incident_type": "cpu_saturation",
                "confidence": 0.95,
                "reason": "CPU idle percentage below threshold"
            }

        if incident_data.get("memory_pressure"):
            return {
                "incident_type": "memory_pressure",
                "confidence": 0.95,
                "reason": "Available memory below threshold"
            }

        if incident_data.get("load_high"):
            return {
                "incident_type": "ambiguous_load",
                "confidence": 0.75,
                "reason": "System load exceeds CPU core count"
            }

        return {
            "incident_type": "healthy",
            "confidence": 1.00,
            "reason": "No incident indicators detected"
        }
