# analyzer/k8s_incident_classifier.py


class KubernetesIncidentClassifier:

    def classify(self, incident):

        current_reason = incident.get("current_reason", "")
        last_reason = incident.get("last_reason", "")
        exit_code = incident.get("exit_code", "")

        # Root causes first

        if last_reason == "OOMKilled":
            return {
                "incident_type": "kubernetes_oomkilled",
                "confidence": 0.99,
                "reason": "Previous container termination was OOMKilled"
            }

        if current_reason == "ImagePullBackOff":
            return {
                "incident_type": "kubernetes_imagepullbackoff",
                "confidence": 0.99,
                "reason": "Container image pull failure"
            }

        if current_reason == "CrashLoopBackOff":
            return {
                "incident_type": "kubernetes_crashloopbackoff",
                "confidence": 0.95,
                "reason": "Container repeatedly restarting"
            }

        if exit_code == "137":
            return {
                "incident_type": "kubernetes_oomkilled",
                "confidence": 0.90,
                "reason": "Exit code 137 typically indicates OOM kill"
            }

        return {
            "incident_type": "unknown",
            "confidence": 0.50,
            "reason": "Unable to determine incident type"
        }
