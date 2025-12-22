---
id: cmd-run-script-gke-001
data: USE_GKE=1 ./run.sh
tags:
  - ssrf
  - reproduction
type: command
output: >-
  Deploys malicious pod, captures logs in output.txt showing requests with
  bearer tokens from control plane IPs like 34.122.28.173
executor: bash
platforms:
  - Linux
  - Kubernetes
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:08.944Z'
verified: false
validated: true
submitted: true
---
# run-reproduction-script-gke

## Command

```bash
USE_GKE=1 ./run.sh
```

## Description

Runs the reproduction script in GKE mode to hijack metrics-server, deploy the malicious pod, and capture SSRF redirects and logs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `USE_GKE=1` | Enables GKE-specific configuration for scaling and deployment | Yes |
| `./run.sh` | The script handling deployment and logging | Yes |

## Examples

### Basic Usage

```bash
USE_GKE=1 ./run.sh
```

### Advanced Usage

```bash
USE_GKE=1 VERBOSE=1 ./run.sh
```

## Expected Output

Deploys malicious pod, captures logs in output.txt showing requests with bearer tokens from control plane IPs like 34.122.28.173

## Related

- [[commands/cleanup-reproduction-environment-gke]]
- [[procedures/Run-Reproduction-Script-to-Observe-Redirects]]
