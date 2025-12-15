---
id: proc-k8s-scale-up
tags:
  - kubernetes
  - scaling
  - json
type: procedure
tools:
  - '[[tools/bash]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.586Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Prepare Kubernetes Scale Up JSON

## Summary

This procedure generates a JSON file specifying a high replica count (999) for scaling a deployment, used in rapid cycles to exhaust API processing.

## Description

The scale subresource in Kubernetes deployments allows updating replicas via JSON payloads. This file sets replicas to 999, forcing the API server to process large pod scheduling queues and etcd updates, especially when repeated. Assumes deployment 'nginx' in default namespace exists.

## Requirements

1. Text editor or shell access
2. Existing deployment to scale
3. Basic JSON knowledge

## Defense

Defensive measures and detection strategies:

- Set HorizontalPodAutoscaler or manual limits on max replicas per deployment (<100)
- Rate-limit API calls to scale endpoints via API server flags (e.g., --max-requests-inflight)
- Audit logs for frequent scale updates from single users

## Objectives

1. Define payload for high-scale operation
2. Ensure compatibility with API PUT requests
3. Enable automation in scripts

## Instructions

### Step 1: Create Scale JSON

**Context**: Use echo or editor to produce minimal JSON for the scale spec.

**Command** (bash echo):

```bash
echo '{"spec":{"replicas":999}}' > scale.json
```

> Creates file; verify with cat scale.json. Expected: Valid JSON object.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/bash]]

## Tags

- kubernetes
- scaling
- json
