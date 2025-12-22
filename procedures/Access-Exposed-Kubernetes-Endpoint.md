---
tags:
  - initial-access
  - kubernetes
  - api-exploit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-kubernetes-api-probe]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:48.637Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: c97a2ae2-ecd8-4a67-bfe1-d39b9163da08
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Exposed-Kubernetes-Endpoint

## Summary

This procedure involves directly interacting with an exposed Kubernetes API endpoint to verify unauthorized access and enumerate cluster resources, setting the stage for privilege escalation.

## Description

Following reconnaissance, attackers probe the API (e.g., Snapchat's cluster) using simple HTTP requests to confirm no auth checks. This reveals cluster-admin level access due to misconfiguration, allowing reads/writes to resources like pods and secrets. Target environment is any public Kubernetes API; outcomes include full cluster visibility.

## Requirements

1. Exposed API URL from scanning
2. curl or similar HTTP client
3. Knowledge of Kubernetes API paths (e.g., /api/v1)

## Defense

Defensive measures and detection strategies:

- Implement API server authentication (e.g., client certificates, tokens)
- Use network ACLs to block external access to port 6443
- Log and alert on unauthorized API calls via audit logs in Kubernetes

## Objectives

1. Confirm unauthenticated access
2. Enumerate cluster components
3. Prepare for code execution

## Instructions

### Step 1: Probe API Version

**Context**: Test basic accessibility without credentials.

**Command** ([[commands/curl-kubernetes-api-probe]]):

```bash
curl -k https://<target-ip>:6443/version
```

> Successful output: JSON with Kubernetes version details.

### Step 2: Enumerate Resources

**Context**: List namespaces or nodes to assess scope.

**Command** ([[commands/curl-kubernetes-api-probe]]):

```bash
curl -k https://<target-ip>:6443/api/v1/namespaces
```

> Output: Array of namespaces, indicating read access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-kubernetes-api-probe]]

## Tools Used

- None

## Tags

- [[initial-access]]
- [[kubernetes]]
- [[api-exploit]]
