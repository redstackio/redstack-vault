---
id: p-develop-time-sqli
tags:
  - blind-sqli
  - time-based
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.312Z'
skill_level: advanced
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Develop Time-Based Blind SQLi Payload

## Summary

Craft payloads using time delays for blind SQL injection where no data is directly returned, suitable for Microsoft SQL Server.

## Description

Manual payloads with WAITFOR DELAY '0:0:5' were developed to infer data via response timing in the XML endpoint.

## Requirements

1. Confirmed blind SQLi
2. SQL Server knowledge
3. Timing measurement tools

## Defense

- Implement query timeouts
- Use WAF with time-based detection
- Parameterize inputs

## Objectives

1. Enable data extraction
2. Confirm conditions blindly
3. Build exfil chain

## Instructions

### Step 1: Basic Time Delay Test

**Context**: Inject delay on true condition.

**Command** ([[commands/curl-time-delay]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123 AND 1=1; WAITFOR DELAY "0:0:5"--</MainAccount></xml>' http://target-subdomain.example.com/upload
```

> Expected output: 5-second delay on true, no delay on false.

### Step 2: Binary Search Payload

**Context**: Extract chars via conditional delays.

Adapt for ASCII extraction.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-time-delay]]

## Tools Used


## Tags

- blind-sqli
- mssql
