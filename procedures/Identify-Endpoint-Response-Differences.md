---
id: proc-hackerone-response-identify-001
tags:
  - information-disclosure
  - api-enumeration
  - reconnaissance
type: procedure
tools:
  - '[[tools/python-requests]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/python-requests-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:29:28.120Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify Endpoint Response Differences

## Summary

This procedure identifies the core vulnerability in HackerOne's /reports/[report_id].json endpoint by comparing response lengths for submitted private reports (empty JSON, length 0) versus non-existent reports (404 error JSON, length 36), enabling distinction without authentication.

## Description

In the context of HackerOne's bug bounty platform, the endpoint returns inconsistent formats that leak the existence of private reports. This is exploited for reconnaissance by measuring response sizes, revealing whether a report ID has been submitted. Prerequisites include public access to the endpoint and basic HTTP client tools. Expected outcomes: Confirmation of the discrepancy, setting the stage for automated polling.

## Requirements

1. Internet access to hackerone.com
2. Python with requests library installed
3. Knowledge of a sample valid private report ID (e.g., from public disclosures)

## Defense

Defensive measures and detection strategies:

- Standardize API responses to uniform formats (e.g., always empty or always 404 with same length)
- Implement rate limiting on the endpoint to detect polling patterns
- Monitor for sequential ID requests from single IPs

## Objectives

1. Verify the response length vulnerability
2. Understand distinction mechanism for report existence
3. Prepare for automated detection of new submissions

## Instructions

### Step 1: Query Known Valid Report

**Context**: Test a known submitted private report to observe the empty response.

**Command** ([[commands/python-requests-get]]):
```python
import requests
response = requests.get('https://hackerone.com/reports/159874.json')
print(len(response.text))
```

> This sends a GET request and prints the response length, expecting 0 for empty JSON.

### Step 2: Query Non-Existent Report

**Context**: Test a high, unused ID to observe the 404 response.

**Command** ([[commands/python-requests-get]]):
```python
import requests
response = requests.get('https://hackerone.com/reports/999999.json')
print(len(response.text))
```

> This should output 36, confirming the {"status":"404","error":"Not Found"} object.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/python-requests-get]]

## Tools Used

- [[tools/python-requests]]

## Tags

- information-disclosure
- api-enumeration
