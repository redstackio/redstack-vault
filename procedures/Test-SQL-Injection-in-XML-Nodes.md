---
id: p-test-sqli-xml
tags:
  - sqli
  - xml
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
updated_at: '2025-12-14T03:15:10.316Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test SQL Injection in XML Nodes

## Summary

Probe XML nodes for SQL injection by targeting parameters likely inserted into queries, such as numerical IDs in MainAccount.

## Description

Initial tests on MainAccount ID suspected in WHERE clauses failed due to XML restrictions, but confirmed potential for injection.

## Requirements

1. Injectable XML endpoint
2. Basic SQL payloads
3. Error monitoring

## Defense

- Parameterize all SQL queries
- Sanitize XML inputs
- Use prepared statements

## Objectives

1. Identify injectable nodes
2. Confirm SQL context
3. Prepare for payload crafting

## Instructions

### Step 1: Basic Injection Test

**Context**: Inject simple SQL in numerical field.

**Command** ([[commands/curl-sqli-basic]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123 OR 1=1</MainAccount></xml>' http://target-subdomain.example.com/upload
```

> Expected output: No error, but behavior change indicates potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-basic]]

## Tools Used


## Tags

- sqli
- blind
