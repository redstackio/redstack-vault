---
data: USE_GKE=1 ./run.sh
tags:
  - gke
  - repro
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:38.937Z'
id: 5c42175e-7cb4-4cb6-a2b3-8c43cab18f48
verified: false
validated: true
submitted: true
---
# run-gke-reproduction-script

## Command

```bash
USE_GKE=1 ./run.sh
```

## Description

Runs the reproduction script configured for GKE, hijacking metrics-server and logging SSRF redirects with token leakage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| USE_GKE=1 | Enables GKE-specific handling | Yes |

## Examples

### Basic GKE Usage

```bash
USE_GKE=1 ./run.sh
```

### GKE with Cleanup

```bash
USE_GKE=1 CLEANUP=1 ./run.sh
```

## Expected Output

Deploys on GKE, captures traffic from control plane IP 34.122.28.173, including bearer tokens in output.txt.

## Related

- [[commands/run-reproduction-script]]
- [[procedures/Observe-Redirected-Traffic-and-Token-Leakage]]
