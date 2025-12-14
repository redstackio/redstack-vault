---
id: proc-enable-proxy-debug-001
tags:
  - debug
  - proxy
type: procedure
tools:
  - '[[tools/kubectl]]'
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/start-kubectl-proxy]]'
  - '[[commands/set-klog-verbosity]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Disable or Modify Tools]]'
updated_at: '2025-12-14T04:08:55.700Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Enable-Kubectl-Proxy-and-Debug-Flags

## Summary

Start kubectl proxy and set klog verbosity to 10 to expose debug endpoints and enable full response logging for SSRF evidence.

## Description

The proxy provides access to /debug/flags/v for runtime changes. Verbosity 10 logs complete HTTP bodies from client-go during webhook calls, crucial for leak observation.

## Requirements

1. Running Kubernetes cluster
2. Port 8001 free
3. Cluster-admin for debug access

## Defense

- Disable debug endpoints in production
- Monitor for proxy startups and flag changes
- Limit verbosity via PodSecurityPolicies

## Objectives

1. Expose apiserver debug interface
2. Increase logging detail for responses
3. Prepare log retrieval

## Instructions

### Step 1: Start Proxy

**Context**: Run proxy to localhost:8001 for debug access.

**Command** ([[commands/start-kubectl-proxy]]):
```bash
kubectl proxy &
```

> Background process. Expected: Proxy started.

### Step 2: Set Verbosity

**Context**: Update klog v flag to 10 via HTTP PUT.

**Command** ([[commands/set-klog-verbosity]]):
```bash
curl -XPUT --data "10" http://localhost:8001/debug/flags/v
```

> Sets level; without this, only errors logged. Expected: 200 OK response.

### Step 3: Verify

**Context**: Check flags.

**Command** ([[commands/verify-debug-flags]]):
```bash
curl http://localhost:8001/debug/flags/v
```

> Output: 10.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Disable or Modify Tools]] Disable or Modify Tools

### Sub-Techniques


## Commands Used

- [[commands/start-kubectl-proxy]]
- [[commands/set-klog-verbosity]]
- [[commands/verify-debug-flags]]

## Tools Used

- [[tools/kubectl]]
- [[tools/curl]]

## Tags

- proxy
- debug
- klog
