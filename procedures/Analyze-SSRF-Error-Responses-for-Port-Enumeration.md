---
tags:
  - ssrf
  - enumeration
  - error-analysis
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:02.310Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9dc16dd1-f89d-40cd-b994-2f2273dd3fa0
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-SSRF-Error-Responses-for-Port-Enumeration

## Summary

This procedure details interpreting the error messages from SSRF submissions to determine open and closed ports on the localhost interface, enabling service enumeration.

## Description

Upon submitting localhost URLs, the server attempts to fetch them and returns errors that leak port status: successful connections for open ports (e.g., SSH on 22) versus failures for closed ones (e.g., Telnet on 21). This allows attackers to scan internal services like HTTP on 80 without direct access, potentially leading to further exploits on firewall-protected systems. The vendor rated it low risk due to mitigations, but it still enables reconnaissance.

## Requirements

1. Multiple SSRF submission responses collected
2. Knowledge of common ports and services (e.g., 22=SSH, 80=HTTP)
3. Manual log or screenshot of errors

## Defense

Defensive measures and detection strategies:

- Sanitize error messages to avoid leaking internal details
- Implement request filtering to deny localhost/internal requests
- Monitor for patterns of rapid, sequential port probes in logs

## Objectives

1. Identify open ports from response differences
2. Enumerate internal services for targeted attacks
3. Assess potential for deeper network compromise

## Instructions

### Step 1: Collect Responses

**Context**: Submit URLs for ports 21, 22, 80 and record the exact error messages.

Example submissions:
- https://127.0.0.1:22 → "Connection successful" or fetch-related success
- https://127.0.0.1:21 → "Connection refused" or timeout

### Step 2: Compare and Map

**Context**: Differentiate open vs. closed ports based on error types.

Open ports show partial success (e.g., HTTP response leak); closed show immediate failure.

**Expected Output**: Mapping like "Port 22 open (SSH), Port 80 open (HTTP), Port 21 closed."

### Step 3: Document Findings

**Context**: Log enumerated services for follow-up attacks.

Note services: SSH (22), HTTP (80) accessible internally.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- enumeration
- port-analysis
- ssrf
