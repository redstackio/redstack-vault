---
tags:
  - information-disclosure
  - data-analysis
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-send-incomplete-post]]'
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 3b23d910-b043-4299-a6d1-61283d1bc949
created_at: '2025-12-13T09:01:22.515Z'
updated_at: '2025-12-13T09:01:22.515Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Analyze Response for Leaked Data

## Summary

This procedure involves capturing and examining the server response from a desynchronized request to identify leaked sensitive information such as credentials.

## Description

After triggering the vulnerability, the error response may include data from previous user requests due to improper handling of POST Content-Length.

## Requirements

1. Response from exploitation step
2. Tool to capture and view output
3. Text editor or analysis tool

## Defense

Defensive measures and detection strategies:

- Enable strict request validation in Tomcat
- Log and alert on error responses with unexpected data

## Objectives

1. Identify leaked sensitive data
2. Confirm exploitation success
3. Document findings

## Instructions

### Step 1: Capture Response

**Context**: Save the server response to a file.

**Command** ([[commands/curl-send-incomplete-post]]):
```bash
curl -X POST http://target.com/ -H 'Content-Length: 6' --data 'incomp' > response.txt
```

> This captures the full response for analysis.

### Step 2: Inspect for Leaks

**Context**: Review the response file for anomalies.

> Open response.txt and search for clear-text credentials or other sensitive data from prior requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-incomplete-post]]

## Tools Used

- [[tools/curl]]

## Tags

- [[information-disclosure]]
- [[data-analysis]]
