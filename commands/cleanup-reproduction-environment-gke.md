---
id: cmd-cleanup-script-gke-001
data: USE_GKE=1 CLEANUP=1 ./run.sh
tags:
  - ssrf
  - cleanup
type: command
output: Removes the hijacker pod and restores original metrics-server
executor: bash
platforms:
  - Linux
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.942Z'
verified: false
validated: true
submitted: true
---
# cleanup-reproduction-environment-gke

## Command

```bash
USE_GKE=1 CLEANUP=1 ./run.sh
```

## Description

Cleans up the test environment by removing the hijacker pod and scaling up the original metrics-server in GKE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `USE_GKE=1` | GKE mode | Yes |
| `CLEANUP=1` | Triggers cleanup of pods and deployments | Yes |
| `./run.sh` | The script for teardown | Yes |

## Examples

### Basic Usage

```bash
USE_GKE=1 CLEANUP=1 ./run.sh
```

### Advanced Usage

```bash
USE_GKE=1 CLEANUP=1 FORCE=1 ./run.sh
```

## Expected Output

Removes the hijacker pod and restores original metrics-server

## Related

- [[commands/run-reproduction-script-gke]]
- [[procedures/Run-Reproduction-Script-to-Observe-Redirects]]
