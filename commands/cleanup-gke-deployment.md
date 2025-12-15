---
data: USE_GKE=1 CLEANUP=1 ./run.sh
tags:
  - cleanup
  - gke
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.931Z'
id: 9fe4b318-bc45-4510-9508-182858b7b80c
verified: false
validated: true
submitted: true
---
# cleanup-gke-deployment

## Command

```bash
USE_GKE=1 CLEANUP=1 ./run.sh
```

## Description

Cleans up the malicious deployment after SSRF testing on GKE, removing pods and restoring the original metrics-server state.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| USE_GKE=1 | GKE configuration | Yes |
| CLEANUP=1 | Triggers cleanup mode | Yes |

## Examples

### GKE Cleanup

```bash
USE_GKE=1 CLEANUP=1 ./run.sh
```

## Expected Output

Removes malicious pod, scales up original deployment, and confirms clean state.

## Related

- [[commands/run-gke-reproduction-script]]
- [[procedures/Scale-Down-Original-Metrics-Server]]
