---
tags:
  - sql-injection
  - xml
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-tamper-htmlencode]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3eed8ca6-0ded-44bd-a00e-78b3fd6608f7
created_at: '2025-12-11T06:10:30.833Z'
updated_at: '2025-12-11T06:10:30.833Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Test SQL Injection in XML MainAccount Node

## Summary

This procedure injects escaped SQL payloads into XML nodes to test for injection vulnerabilities.

## Description

By escaping special characters in XML (e.g., &apos; for '), inputs can bypass XML restrictions and reach the SQL query unsanitized.

## Requirements

1. XML upload endpoint with known structure
2. Ability to craft and upload XML files
3. HTTP client

## Defense

Defensive measures and detection strategies:

- Sanitize inputs before SQL execution
- Use prepared statements

## Objectives

1. Trigger database errors
2. Confirm injection point
3. Validate payload decoding

## Instructions

### Step 1: Craft Injected XML

**Context**: Inject into MainAccount node.

Create XML with: <MainAccount>123456&apos;</MainAccount>

### Step 2: Upload and Observe

**Context**: Upload the XML and check responses.

Use curl or similar to submit and look for SQL errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[sql-injection]]
- [[xml]]
