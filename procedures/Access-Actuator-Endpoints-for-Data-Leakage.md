---
id: proc-838635-002
tags:
  - information-leakage
  - heapdump
  - env-variables
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Spring Boot
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Information Repositories]]'
  - '[[Credential Dumping]]'
updated_at: '2025-12-14T17:31:52.906Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
  - '[[Credential Dumping]]'
---
# Access-Actuator-Endpoints-for-Data-Leakage

## Summary

This procedure exploits exposed Spring Boot Actuator endpoints to extract sensitive data, including environment variables and heap dumps, from misconfigured applications, leading to potential credential theft and system insight.

## Description

Once endpoints are confirmed exposed, direct access allows retrieval of critical information: /env exposes configuration like database URLs and secrets, while /heapdump provides in-memory data such as active sessions or tokens. This targets sensitive web applications using Spring Boot. Prerequisites are confirmed endpoint exposure. Outcomes include downloadable data for offline analysis, highlighting risks in production environments.

## Requirements

1. Confirmed accessible endpoints from prior discovery
2. HTTP client capable of handling JSON and binary downloads
3. Sufficient bandwidth for large heap dumps (potentially GBs)

## Defense

Defensive measures and detection strategies:

- Disable sensitive Actuator endpoints (e.g., via application.properties: management.endpoint.heapdump.enabled=false)
- Implement logging and SIEM rules to detect large file downloads or /env accesses
- Use network segmentation to restrict management endpoints to internal networks

## Objectives

1. Download environment variables revealing configs and secrets
2. Obtain heap dump for memory forensics and token extraction
3. Evaluate impact on application security posture

## Instructions

### Step 1: Fetch Environment Variables

**Context**: Access /env to retrieve all active environment properties, which may include sensitive keys.

**Command** (using curl to get JSON data):
```bash
curl https://target-app.com/actuator/env > env.json
```

> The response is a JSON object with properties like activeProfiles, systemEnvironment, and propertySources. Parse for secrets (e.g., grep for 'password' or 'key').

### Step 2: Download Heap Dump

**Context**: Retrieve the in-memory heap snapshot, which can contain loaded classes, objects, and potentially secrets.

**Command** (download binary heap dump):
```bash
curl -o heapdump.hprof https://target-app.com/actuator/heapdump
```

> This downloads a HPROF file. Use tools like Eclipse MAT or jhat to analyze for sensitive strings. Success if file size indicates full dump (e.g., >100MB).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Information Repositories]] Data from Information Repositories
- [[Credential Dumping]] OS Credential Dumping

### Sub-Techniques

- None

## Commands Used

- None (uses standard HTTP requests)

## Tools Used

- None

## Tags

- [[data-exfiltration]]
- [[memory-dump]]
- [[configuration-leak]]
