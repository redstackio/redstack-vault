---
tags:
  - reconnaissance
  - kubernetes
  - scanning
type: procedure
tools:
  - '[[tools/BinaryEdge-Scanner]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:32:48.638Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 0f71e313-c4c5-451d-a1c5-cd04fd6b52df
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Scan-for-Exposed-Kubernetes-APIs

## Summary

This procedure uses online scanning tools to identify publicly exposed Kubernetes API servers worldwide, focusing on endpoints without proper authentication to enable initial reconnaissance for potential exploitation.

## Description

In the attack on Snapchat's infrastructure, a global scan via binaryedge.io revealed an exposed Kubernetes API endpoint accessible without authorization. This step involves querying vulnerability databases or scanners for Kubernetes signatures on public IPs, typically targeting port 6443. Prerequisites include access to a scanning service; expected outcomes are a list of vulnerable endpoints ready for probing.

## Requirements

1. Subscription or free access to a scanning platform like BinaryEdge
2. Basic knowledge of Kubernetes API signatures (e.g., /version endpoint)
3. Internet connectivity for worldwide queries

## Defense

Defensive measures and detection strategies:

- Restrict API server exposure using network policies or firewalls (e.g., only allow internal IPs)
- Enable RBAC and authentication on Kubernetes API (e.g., via cert-manager or OIDC)
- Monitor for anomalous scan traffic using tools like Falco or AWS GuardDuty

## Objectives

1. Discover publicly accessible Kubernetes clusters
2. Identify authorization weaknesses
3. Gather targets for further exploitation

## Instructions

### Step 1: Query Scanning Service

**Context**: Perform a targeted search for exposed Kubernetes APIs using BinaryEdge's search interface or API.

**Command** ([[BinaryEdge Query]]):

No direct command; use web UI or API:

```bash
# Example API call (requires API key)
curl "https://api.binaryedge.io/v2/query?query=port:6443%20%22kubernetes%22&key=YOUR_API_KEY"
```

> This returns JSON with IPs and ports matching Kubernetes exposure. Filter for recent results.

### Step 2: Validate Exposure

**Context**: Confirm the endpoint is live and Kubernetes-specific.

**Command** ([[commands/curl-kubernetes-api-probe]]):

```bash
curl -k -v https://<scanned-ip>:6443/version
```

> Expect JSON like {"major":"1","minor":"20"} if exposed; errors indicate protection.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning: Scanning IP Blocks

### Sub-Techniques

- None

## Commands Used

- None specific; relies on tool UI/API

## Tools Used

- [[tools/BinaryEdge-Scanner]]

## Tags

- [[Reconnaissance]]
- [[kubernetes]]
- [[scanning]]
