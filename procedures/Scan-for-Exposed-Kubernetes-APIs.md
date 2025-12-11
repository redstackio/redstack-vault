---
tags:
  - reconnaissance
  - scanning
  - kubernetes
type: procedure
tools:
  - '[[tools/BinaryEdge]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-kubernetes-api-access]]'
  - '[[commands/curl-create-kubernetes-job]]'
  - '[[commands/curl-get-kubernetes-secrets]]'
  - '[[commands/curl-binaryedge-query]]'
platforms:
  - Kubernetes
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 32575c0e-a388-4364-80b8-fdcab0609279
created_at: '2025-12-11T06:10:10.570Z'
updated_at: '2025-12-11T06:10:10.570Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1595]]'
---
# Scan for Exposed Kubernetes APIs

## Summary

This procedure uses BinaryEdge to perform a worldwide scan for publicly exposed Kubernetes API endpoints, identifying potential targets for further exploitation.

## Description

BinaryEdge is a cybersecurity search engine that indexes internet-connected devices. By querying for Kubernetes services on common ports like 6443, attackers can discover misconfigured clusters exposed without authentication. This is a reconnaissance step to build a list of vulnerable APIs.

## Requirements

1. Access to BinaryEdge (free tier or API key)
2. Internet connection
3. Basic knowledge of query syntax

## Defense

Defensive measures and detection strategies:

- Restrict Kubernetes API to internal networks or use authentication
- Monitor for unusual scans on port 6443 using firewall logs

## Objectives

1. Identify exposed Kubernetes APIs
2. Collect IP addresses for targeting
3. Assess global exposure of similar misconfigurations

## Instructions

### Step 1: Query BinaryEdge for Kubernetes Services

**Context**: Use the BinaryEdge API or dashboard to search for exposed Kubernetes instances.

**Command** ([[commands/curl-binaryedge-query]]):
```bash
curl -H "X-Key: YOUR_API_KEY" "https://api.binaryedge.io/v2/query/search?query=product:kubernetes port:6443"
```

> This command queries BinaryEdge for devices running Kubernetes on port 6443, returning a list of IPs and details.

### Step 2: Analyze Results

**Context**: Review the scan output to select viable targets.

Filter results for APIs responding without authentication by testing connectivity.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques



## Commands Used

- [[commands/curl-binaryedge-query]]

## Tools Used

- [[tools/BinaryEdge]]

## Tags

- [[Reconnaissance]]
- [[commands/curl-kubernetes-api-access]]
