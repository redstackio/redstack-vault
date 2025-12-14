---
id: p-craft-xml-payloads
tags:
  - xml
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:10.322Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft XML Payloads for Backend Identification

## Summary

Construct valid XML payloads with domain-specific nodes to elicit errors that reveal the backend application, such as Microsoft Dynamics AX.

## Description

Using nodes like MainAccount, Credit, Debit, Invoice in XML submissions triggered errors confirming Dynamics AX processing, setting up for injection testing.

## Requirements

1. Knowledge of target app schema
2. XML editor or HTTP client
3. Endpoint URL

## Defense

- Parse XML safely with disabling external entities
- Log malformed XML
- Use WAF for anomaly detection

## Objectives

1. Identify backend
2. Confirm XML nodes in SQL
3. Prepare for injection

## Instructions

### Step 1: Build Basic XML

**Context**: Create payload with accounting nodes.

**Command** ([[commands/curl-xml-post]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123</MainAccount><Credit>100</Credit></xml>' http://target-subdomain.example.com/upload
```

> Expected output: Errors referencing Dynamics AX tables.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xml-post]]

## Tools Used


## Tags

- xml
- dynamics-ax
