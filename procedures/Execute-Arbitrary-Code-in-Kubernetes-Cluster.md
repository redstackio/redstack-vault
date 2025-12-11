---
tags:
  - execution
  - rce
  - kubernetes
type: procedure
tools:
  - '[[tools/BinaryEdge]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-kubernetes-api-access]]'
  - '[[commands/curl-create-kubernetes-job]]'
  - '[[commands/curl-get-kubernetes-secrets]]'
  - '[[commands/curl-binaryedge-query]]'
platforms:
  - Kubernetes
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 97116839-d32e-446d-9c97-5c8a8fd041c7
created_at: '2025-12-11T06:10:10.576Z'
updated_at: '2025-12-11T06:10:10.576Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Execute Arbitrary Code in Kubernetes Cluster

## Summary

This procedure uses unauthorized API access to create and run arbitrary jobs or pods for remote code execution as cluster-admin.

## Description

With admin-level access, attackers can deploy privileged containers to execute code, potentially leading to full cluster compromise. This involves posting YAML definitions to the API.

## Requirements

1. Unauthorized API access
2. YAML file for malicious job/pod
3. Network access

## Defense

Defensive measures and detection strategies:

- Implement pod security policies
- Monitor API server logs for unauthorized creations

## Objectives

1. Deploy malicious workload
2. Achieve RCE
3. Maintain persistence

## Instructions

### Step 1: Prepare Malicious YAML

**Context**: Create a YAML file for a job running arbitrary code.

### Step 2: Deploy Job

**Command** ([[commands/curl-create-kubernetes-job]]):
```bash
curl -k -X POST -H "Content-Type: application/yaml" --data-binary @malicious-job.yaml https://TARGET_IP:6443/apis/batch/v1/namespaces/default/jobs
```

> This deploys the job, executing the specified command.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/curl-create-kubernetes-job]]

## Tools Used

- [[commands/curl-binaryedge-query]]

## Tags

- [[Execution]]
- [[rce]]
