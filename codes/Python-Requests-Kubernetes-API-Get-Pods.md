---
id: 3328bd89-f2cb-48d5-80f0-3cafd9cec716
name: Python-Requests-Kubernetes-API-Get-Pods
type: code
language: python
verified: true
created_at: '2023-04-06T03:56:01.090475+00:00'
updated_at: '2023-10-10T20:34:03.473403+00:00'
platforms:
  - Kubernetes
  - Linux
tags:
  - kubernetes
  - api
  - enumeration
  - python
validated: true
---

# Python-Requests-Kubernetes-API-Get-Pods

## Code

```python
import requests

url = "https://<API_SERVER>/api/v1/namespaces/<NAMESPACE>/pods"
headers = {
    "Authorization": "Bearer <TOKEN>",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers, verify=False)
print(response.json())
```

## Description

This Python code snippet uses the requests library to send a GET request to the Kubernetes API server, fetching a list of pods in a specified namespace. It simulates kubectl get pods for environments without the tool, enabling enumeration of cluster resources via direct API interaction. The code disables SSL verification for self-signed certificates and prints the JSON response for parsing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <API_SERVER> | Kubernetes API server URL | kubernetes.default.svc |
| <NAMESPACE> | Target namespace | default |
| <TOKEN> | Bearer token for authentication | eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9... |

## Usage

Run this in a Python interpreter or script after installing requests (pip install requests). Substitute placeholders with actual values. Ideal for automated reconnaissance in compromised pods or scripts chaining API calls, such as extracting pod IPs for lateral movement. Deliver via initial access vectors like malicious container images.

## Detection

- Monitor for Python processes importing requests and making HTTPS calls to API server endpoints.
- API audit logs showing requests without kubectl user-agent or from unexpected pods.
- Network traffic to API server port 443 with bearer tokens from non-standard clients.
- Anomalous JSON parsing of pod lists in process memory dumps.

## Related

- [[procedures/Simulate-Kubectl-API-Requests-with-Curl-and-Python]]
- [[commands/curl-kubernetes-api-get-pods]]
