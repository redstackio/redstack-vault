---
data: ./run.sh
tags:
  - kubernetes
  - repro
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.947Z'
id: 636d9af4-beab-47f8-8f97-75b960a59cf1
verified: false
validated: true
submitted: true
---
# run-reproduction-script

## Command

```bash
./run.sh
```

## Description

Executes the end-to-end reproduction script to build the malicious image, deploy the pod, scale down metrics-server, and capture output for SSRF demonstration on AKS/GKE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| USE_GKE=1 | Flag to adapt for Google Kubernetes Engine | No |
| CLEANUP=1 | Flag to remove resources after execution | No |

## Examples

### Basic Usage

```bash
./run.sh
```

### GKE-Specific Usage

```bash
USE_GKE=1 ./run.sh
```

### With Cleanup

```bash
USE_GKE=1 CLEANUP=1 ./run.sh
```

## Expected Output

Deploys malicious pod, scales deployment, and logs redirected traffic to output.txt, including bearer tokens from control plane IPs like 34.122.28.173.

## Related

- [[commands/run-gke-reproduction-script]]
- [[procedures/Scale-Down-Original-Metrics-Server]]
