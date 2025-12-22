---
id: 6d6bd590-eea3-41e8-95be-19cb4b04f6d0
name: Kubelet-API-Enumeration-PowerShell-Script
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:01.510910+00:00'
updated_at: '2023-04-10T20:34:01.315533+00:00'
platforms:
  - Linux
  - Kubernetes
  - Windows
tags:
  - discovery
  - kubernetes
  - kubelet
  - script
validated: true
---

# Kubelet-API-Enumeration-PowerShell-Script

## Code

```powershell
curl -k https://<IP address>:10250
curl -k https://<IP address>:10250/metrics
curl -k https://<IP address>:10250/pods
```

## Description

This PowerShell script sequentially queries the Kubelet API's root, metrics, and pods endpoints to enumerate node and cluster information. It performs basic discovery without authentication, assuming network access to the worker node.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <IP address> | IP address of the Kubernetes worker node | 192.168.1.100 |

## Usage

Save the script as a .ps1 file and execute it in PowerShell on a machine with network access to the cluster. Replace <IP address> with the target node's IP. Pipe outputs to files for analysis, e.g., `./script.ps1 > output.txt`. Use in reconnaissance phases of Kubernetes pentests to quickly map node details.

## Detection

- Network monitoring for repeated HTTPS requests to port 10250 from unauthorized sources.
- Kubelet logs showing unauthenticated API calls.
- PowerShell execution logs (if run on Windows attacker machine) via Event ID 4104.
- Anomalous traffic patterns to worker nodes.

## Related

- [[procedures/Kubelet-API-Enumeration-via-Curl]]
- [[commands/curl-kubelet-root-endpoint]]
