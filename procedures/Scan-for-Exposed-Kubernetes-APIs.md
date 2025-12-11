---
tags:
  - reconnaissance
  - kubernetes
  - scanning
type: procedure
tools:
  - '[[tools/binaryedge.io]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Kubernetes
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 51b4378b-f2c8-4693-ac9b-5d1214cdcd5c
created_at: '2025-12-10T05:44:16.324Z'
updated_at: '2025-12-10T05:44:16.324Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Scan for Exposed Kubernetes APIs

## Summary

This procedure involves using scanning tools to perform a worldwide search for exposed Kubernetes API endpoints, identifying potential misconfigurations that allow public access without authorization.

## Description

In this attack scenario, attackers leverage public scanning platforms to detect Kubernetes APIs exposed to the internet. The target environment is any Kubernetes cluster with misconfigured network exposure. Expected outcomes include a list of vulnerable endpoints that can be further exploited for unauthorized access.

## Requirements

1. Access to a scanning platform like binaryedge.io
2. Internet connectivity for global scanning
3. Basic knowledge of Kubernetes API signatures (e.g., ports 6443, 443)

## Defense

Defensive measures and detection strategies:

- Implement network segmentation and firewalls to restrict API exposure
- Monitor for unusual scanning traffic targeting Kubernetes ports

## Objectives

1. Identify exposed Kubernetes APIs globally
2. Filter for targets without authorization
3. Prepare for further exploitation

## Instructions

### Step 1: Initiate Global Scan

**Context**: Use a scanning tool to query for exposed Kubernetes instances.

Access [[tools/binaryedge.io]] and perform a search for Kubernetes APIs:

```bash
# Use binaryedge.io web interface or API to query:
# Example query: port:6443 and "kubernetes"
```

> This will return a list of IP addresses and hosts with exposed APIs.

### Step 2: Validate Exposure

**Context**: Confirm the APIs are publicly accessible.

Test connectivity with a basic curl command:

```bash
curl https://identified-ip:6443/version
```

> Expect a response with Kubernetes version info if exposed without auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/binaryedge.io]]

## Tags

- [[Reconnaissance]]
- #kubernetes
