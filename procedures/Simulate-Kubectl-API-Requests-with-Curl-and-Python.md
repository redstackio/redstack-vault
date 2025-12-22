---
id: a483c910-3db7-4b12-a979-6f4bd3da82af
name: Simulate-Kubectl-API-Requests-with-Curl-and-Python
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:01.095742+00:00'
updated_at: '2023-10-10T20:34:03.455806+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
techniques:
  - '[[techniques/Account Manipulation|T1098 - Account Manipulation]]'
  - '[[techniques/Native API|T1106 - Native API]]'
sub_techniques: []
tags:
  - '[[tags/Container Environment]]'
  - '[[tags/Kubernetes]]'
  - '[[tags/Simulating kubectl API Requests]]'
commands:
  - '[[commands/curl-kubernetes-api-get-pods]]'
platforms:
  - Kubernetes
  - Linux
tools: []
validated: true
---

# Simulate-Kubectl-API-Requests-with-Curl-and-Python

## Summary

This procedure demonstrates how to manually simulate kubectl API requests to interact with a Kubernetes cluster using tools like curl or Python's requests library. It is particularly useful in environments where kubectl is unavailable, such as restricted containers, allowing attackers to enumerate resources, access sensitive data, execute code, or establish persistence by crafting direct HTTP requests to the Kubernetes API server.

## Description

In a Kubernetes environment, the API server handles all cluster operations. When kubectl is not accessible, direct API calls can mimic its functionality to perform actions like listing pods, creating resources, or modifying configurations. This technique leverages bearer token authentication to bypass the need for the kubectl binary, enabling unauthorized access to cluster resources. It targets scenarios where an attacker has obtained a service account token or user credentials, allowing operations that could lead to data exfiltration, lateral movement, or backdoor creation. The approach uses insecure SSL (via -k or verify=False) to handle self-signed certificates common in internal clusters.

## Requirements

1. Valid Kubernetes API bearer token (e.g., from a service account or user)
2. Network access to the Kubernetes API server (typically port 443)
3. Knowledge of the API server URL and target namespace
4. Tools: curl (for bash) or Python with requests library (for scripted access)
5. Optional: Proxy or VPN for internal cluster access

## Defense

- Implement strict RBAC policies to limit API access to least privilege, revoking unnecessary service account tokens.
- Enable Kubernetes audit logging on the API server to monitor anomalous requests, such as direct HTTP calls without kubectl user-agent.
- Use network policies to restrict pod-to-API-server traffic and enforce mTLS for API communications.
- Regularly rotate tokens and monitor for token exposure in pod mounts or environment variables.
- Deploy tools like Falco or auditd to detect unusual API patterns, such as mass resource enumeration.

## Objectives

1. Simulate kubectl commands to enumerate Kubernetes resources like pods without the kubectl tool.
2. Access sensitive cluster information, such as pod details, secrets, or configurations.
3. Enable execution of arbitrary code or resource creation for persistence in the cluster.
4. Validate API access and token validity for further exploitation.

## Instructions

### Step 1: Fetch Pods List Using Curl

**Context**: This step uses curl to send a GET request to the Kubernetes API, simulating `kubectl get pods` in a specific namespace. It authenticates with a bearer token and skips SSL verification for internal self-signed certs, retrieving a JSON list of pods to identify running workloads and potential targets.

**Command** ([[commands/curl-kubernetes-api-get-pods]]):
```bash
curl -k -H "Authorization: Bearer $_TOKEN" https://$_API_SERVER/api/v1/namespaces/$_NAMESPACE/pods
```

> This command authenticates to the API server and fetches pod details. Replace $_TOKEN with your bearer token, $_API_SERVER with the API endpoint (e.g., kubernetes.default.svc), and $_NAMESPACE with the target namespace (e.g., default). The -k flag ignores SSL errors. Success is indicated by a 200 OK response with JSON containing pod metadata; errors like 401 suggest invalid tokens.

### Step 2: Fetch Pods List Using Python Requests

**Context**: For scripted or automated access, this Python snippet uses the requests library to perform the same API call as Step 1. It provides programmatic control for chaining requests, parsing JSON responses, or integrating into larger exploits, such as looping over namespaces or extracting secrets.

**Code** ([[codes/Python-Requests-Kubernetes-API-Get-Pods]]):
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

> Execute this code in a Python environment with requests installed (pip install requests). Substitute <API_SERVER>, <NAMESPACE>, and <TOKEN> with actual values. The verify=False disables SSL checks. Expected output is a JSON dictionary with pod items; check response.status_code == 200 for success. Use this for dynamic token handling or response parsing in automated attacks.
