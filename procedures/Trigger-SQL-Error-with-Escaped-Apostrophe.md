---
id: p-trigger-sqli-error
tags:
  - sqli
  - entity-escape
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
updated_at: '2025-12-14T03:15:10.314Z'
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
# Trigger SQL Error with Escaped Apostrophe

## Summary

Bypass XML entity filtering by using &apos; to inject an apostrophe, triggering a SQL syntax error to confirm injection.

## Description

In <MainAccount>123456&apos;</MainAccount>, the escaped apostrophe broke the query, revealing SQLi.

## Requirements

1. XML endpoint with entity support
2. Knowledge of SQL syntax
3. Response analysis

## Defense

- Escape all user input properly
- Validate XML structure
- Monitor for injection errors

## Objectives

1. Confirm SQLi
2. Identify error-based feedback
3. Validate bypass

## Instructions

### Step 1: Inject Escaped Apostrophe

**Context**: Use XML entity to inject '.

**Command** ([[commands/curl-apos-escape]]):
```bash
curl -X POST -H "Content-Type: application/xml" -d '<xml><MainAccount>123456&apos;</MainAccount></xml>' http://target-subdomain.example.com/upload
```

> Expected output: SQL syntax error in response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-apos-escape]]

## Tools Used


## Tags

- sqli
- xml-escape
