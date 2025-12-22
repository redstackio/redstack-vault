---
id: proc-inspect-logs-leak-001
tags:
  - logs
  - exfiltration
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/retrieve-apiserver-logs]]'
verified: false
platforms:
  - Kubernetes
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T04:08:55.695Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Inspect-Apiserver-Logs-for-Leaked-Responses

## Summary

Retrieve kube-apiserver INFO logs via proxy to extract full SSRF response bodies, revealing leaked internal data like cloud credentials.

## Description

With v=10, logs include 'Response Body:' sections from redirected requests to metadata servers (e.g., AWS IMDS, GCP metadata). In cloud, logs may be accessible remotely.

## Requirements

1. Proxy running on 8001
2. Verbosity set to 10
3. Webhook triggered

## Defense

- Reduce log verbosity in production
- Scrub sensitive data from logs
- Use log shippers with filtering for metadata

## Objectives

1. Fetch and parse apiserver logs
2. Identify SSRF evidence
3. Exfiltrate leaked credentials

## Instructions

### Step 1: Retrieve Logs

**Context**: Use curl via proxy to get INFO logs.

**Command** ([[commands/retrieve-apiserver-logs]]):
```bash
curl http://localhost:8001/logs/kube-apiserver.INFO
```

> Downloads log file content. Expected: Text with timestamps, HTTP details.

### Step 2: Search for Leaks

**Context**: Grep for response bodies.

**Command** ([[commands/search-log-responses]]):
```bash
grep -i "response body" kube-apiserver.INFO
```

> Output: Full bodies from internal fetches, e.g., JSON with tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques


## Commands Used

- [[commands/retrieve-apiserver-logs]]
- [[commands/search-log-responses]]

## Tools Used

- [[tools/curl]]

## Tags

- logs
- leak
- metadata
